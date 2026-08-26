import json
import os

from api import PetFriends
from settings import *

pf = PetFriends()

def test_get_api_key_for_valid_user(email = valid_email, password = valid_password):
    status, result = pf.get_api_key(email, password)

    assert status == 200
    assert 'key' in result

def test_get_all_pets_with_valid_key(filter=''):
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.get_list_of_pats(auth_key, filter)

    assert status == 200
    assert len(result['pets']) > 0

def test_post_add_information_about_new_pet_without_photo(name = new_cat_name, animal_type = new_cat_animal_type, age = new_cat_age):
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.post_add_information_about_new_pet_without_photo(auth_key, name, animal_type, age)
    assert status == 200
    assert result['name'] == name

def test_post_add_information_about_new_pet_with_photo(name = new_kitten_name, animal_type = new_kitten_animal_type, age= new_kitten_age, pet_photo = new_kitten_photo):
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    # print(f"\nИщем файл тут: {pet_photo} -> Найдено? {os.path.exists(pet_photo)}")
    status, result = pf.post_add_information_about_new_pet_with_photo(auth_key, name, animal_type, age, pet_photo)
    print(f"\n{animal_type} {name} добавлен!!!")
    assert status == 200
    assert os.path.exists(pet_photo), f"Файл не найден по пути: {pet_photo}"
    assert result['name'] == name

def test_post_add_photo(pet_id=new_cat_id, pet_photo=new_cat_photo ):
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pats(auth_key, "my_pets")
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    status, result = pf.post_add_photo(auth_key, pet_id, pet_photo)
    print(f"\nФото добавлено!!!")
    assert status == 200
    assert os.path.exists(pet_photo), f"Файл с фото не найден : {pet_photo}"

def test_delete_pet_from_database(pet_id='729b086b-6f43-4620-8812-e2564fe8fd71'):
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pats(auth_key, "my_pets")
    status, result = pf.delete_pet_from_database(auth_key, pet_id)
    if os.path.exists(pet_id) != True:
        raise Exception('Введен неверный ID')
    else:
        assert status == 200
        print('Запрос на удаление выполнен успешно!')

def test_update_information_about_pet(pet_id='c3b66b94-1d0e-43d9-bd9f-66c77e720dcd', name = 'Смайлик', animal_type = 'ящерка', age = new_cat_age):
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.update_information_about_pet(auth_key, pet_id, name, animal_type, age)
    print(f"\nзапись обновлена!!!")
    assert status == 200
    assert result['name'] == name

#Тест обновит информацию о последнем питомце, если список пуст выведет сообщение
def test_successful_update_self_pet_info(name='Фанни',
                                         animal_type='кот', age=1):
   _, auth_key = pf.get_api_key(valid_email, valid_password)
   _, my_pets = pf.get_list_of_pats(auth_key, "my_pets")

   if len(my_pets['pets']) > 0:
       status, result = pf.update_information_about_pet(auth_key, my_pets['pets'][0]['id'],
                                                name, animal_type, age)
       assert status == 200
       assert result['name'] == name
   else:
       raise Exception("Список пуст!")


def test_get_ID(filter='my_pets'):
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.get_list_of_pats(auth_key, filter)
    # код для поиска ID питомца по имени
    for pet in result['pets']:
        firstname = 'Фанни'
        if pet['name'] == {firstname}:
            print(f'\nID {firstname}-->> {pet['id']}')
            break
    assert status == 200