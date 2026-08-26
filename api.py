import os

import requests
# from requests_toolbelt.multipart.encoder import MultipartEncoder


class PetFriends:
    def __init__(self):
        self.base_url = 'https://petfriends.skillfactory.ru/'

    def get_api_key(self, email, password):
        headers = {
            'email': email,
            'password': password,
        }
        res = requests.get(self.base_url+'api/key', headers=headers)
        status = res.status_code
        result = ""
        try:
            result = res.json()
        except:
            result = res.text
        return status, result

    def get_list_of_pats(self, auth_key, filter):
        headers = {'auth_key' : auth_key['key']}
        filter = {'filter': filter}

        res = requests.get(self.base_url+'api/pets', headers=headers, params=filter)
        status = res.status_code
        result = ""
        try:
            result = res.json()
        except:
            result = res.text
        return status, result

    def post_add_information_about_new_pet_without_photo(self, auth_key, name, animal_type, age ):
        headers = {'auth_key': auth_key['key']}
        data = {'name': name,
                'animal_type': animal_type,
                'age': age,
                }

        res = requests.post(self.base_url + 'api/create_pet_simple', headers=headers, data=data)
        status = res.status_code
        result = ""
        try:
            result = res.json()
        except:
            result = res.text
        print(result)
        return status, result


    def post_add_information_about_new_pet_with_photo(self, auth_key, name, animal_type, age, pet_photo ):
        headers = {'auth_key': auth_key['key']}
        data = {
                'name': str(name),
                'animal_type': str(animal_type),
                'age': str(age),
                # 'pet_photo': (pet_photo, open(pet_photo, 'rb'), 'image/jpeg')
            }

        file_name = os.path.basename(pet_photo)
        files = {
            'pet_photo': (file_name, open(pet_photo, 'rb'), 'image/jpeg')
        }
        res = requests.post(self.base_url + 'api/pets', headers=headers, data=data, files=files)
        status = res.status_code
        # result = ""
        try:
            result = res.json()
        except:
            result = res.text

        return status, result


    def post_add_photo(self, auth_key, pet_id, pet_photo ):

        headers = {'auth_key': auth_key['key']}
        data = {
                'pet_id': pet_id
            }

        file_name = os.path.basename(pet_photo)
        files = {
            'pet_photo': (file_name, open(pet_photo, 'rb'), 'image/jpeg')
        }
        res = requests.post(self.base_url + 'api/pets/set_photo/'+pet_id, headers=headers, data=data, files=files)
        status = res.status_code
        # result = ""
        try:
            result = res.json()
        except:
            result = res.text

        return status, result

    def delete_pet_from_database(self, auth_key, pet_id ):

        headers = {'auth_key': auth_key['key']}
        data = { 'pet_id': pet_id }

        res = requests.delete(self.base_url + 'api/pets/'+pet_id, headers=headers, data=data)
        status = res.status_code
        # result = ""
        try:
            result = res.json()
        except:
            result = res.text

        return status, result

    def update_information_about_pet (self, auth_key, pet_id, name, animal_type, age ):
        headers = {'auth_key': auth_key['key']}
        data = {
                'pet_id': pet_id,
                'name': name,
                'animal_type': animal_type,
                'age': age,
                }

        res = requests.put(self.base_url + 'api/pets/'+pet_id, headers=headers, data=data)
        status = res.status_code
        result = ""
        try:
            result = res.json()
        except:
            result = res.text
        print(result)
        return status, result




