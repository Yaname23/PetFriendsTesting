import json
import os

from api import PetFriends
from settings import *

pf = PetFriends()

def test_get_api_key_for_valid_user(email = valid_email, password = valid_password):
    status, result = pf.get_api_key(email, password)

    assert status == 200
    assert 'key' in result

def test_get_all_pets_with_valid_key(filter=''):#если нужно найти ID-шник, в фильтр добавить 'my_pets'
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.get_list_of_pats(auth_key, filter)
    #код  для поиска ID питомца по имени
    # for pet in result['pets']:
    #     if pet['name'] == 'Мурзик':
    #         print(f'\nID -->> {pet['id']}')
    #         break
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
    print(f"\nОтвет сервера: {animal_type} {name} добавлен!!!")
    assert status == 200
    assert os.path.exists(pet_photo), f"Файл не найден по пути: {pet_photo}"
    assert result['name'] == name

def test_post_add_photo(pet_id=new_cat_id, pet_photo=new_cat_photo ):
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pats(auth_key, "my_pets")
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    status, result = pf.post_add_photo(auth_key, pet_id, pet_photo)
    print(f"\nОтвет сервера: Фото добавлено!!!")
    assert status == 200
    assert os.path.exists(pet_photo), f"Файл не найден по пути: {pet_photo}"

def test_delete_pet_from_database(pet_id='206f9acc-8086-4c2e-b1bc-73a29e11ede1'):
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pats(auth_key, "my_pets")
    status, result = pf.delete_pet_from_database(auth_key, pet_id)
    print(f"\nОтвет сервера: запись удалена!!!")
    assert status == 200

def test_update_information_about_pet(pet_id='206f9acc-8086-4c2e-b1bc-73a29e11ede1', name = 'Тикки', animal_type = 'кошка', age = new_cat_age):
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.update_information_about_pet(auth_key, pet_id, name, animal_type, age)
    print(f"\nОтвет сервера: запись обновлена!!!")
    assert status == 200
    assert result['name'] == name




