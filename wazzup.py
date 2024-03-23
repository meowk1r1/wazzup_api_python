import requests
import json



class WazzupAPI:
    def __init__(self, token):
        self.base_url = 'https://api.wazzup24.com/v3' #базовый url который я потом изменять буду в кажой функции, просто оно однажды меня выбесило
        self.token = token# токен что логично
        self.headers = {
            'Authorization': f'Bearer {self.token}',#токен мы передаем в headers всегда
            'Content-Type': 'application/json'
        }


    def get_user_data(self, user_id, name=None, phone=None):# получаем данные и регаем пользователя если его нет, для чего это и создавалось
        print("get_user_data")
        endpoint = f'{self.base_url}/users/{user_id}'
        response = requests.get(endpoint, headers=self.headers)
        print(response.text)
        if response.status_code != 200:
            # Если пользователя нет, регистрируем его
            if name is not None and phone is not None:
                print(1)
                return self.register_user(user_id, name, phone)
            else:
                print(2)
                return self.register_user(user_id, name, phone)
        else:
            return response.json()

    # def create_single_user(self, user_id, name, phone): # опять же создание челика, просто формировка json массива
    #     user_data = [{
    #         "id": str(user_id),
    #         "name": str(name)
    #         # "phone": phone # мы можем тут телеф сразу по апи передавать, но в моем случае это не нужно
    #     }]
    #     return self.create_user(user_data)
    

    def register_user(self, user_id, name, phone):
        # Здесь можно вызвать метод create_user или выполнить другие действия
        user_data = [{
            "id": str(user_id),
            "name": str(name)
            # "phone": phone
        }]
        print(user_data)
        return self.create_user(user_data)
    

    def create_user(self, user_data): #создаем юзера, почему нет
        self.base_url = "https://api.wazzup24.com/v3"
        endpoint = f'{self.base_url}/users'

        try:
            print(f"url: {endpoint}\ndata: {user_data}, headers:{self.headers}")
            # Преобразование данных в JSON перед отправкой запроса
            response = requests.post(endpoint, headers=self.headers, json=user_data)
            print(response.status_code)
            print(response.text)
            response.raise_for_status()
            return "Done"
        except requests.exceptions.HTTPError as err:
            print(err)
            return None  # Обработайте ошибку соответствующим образом
        
    

    def create_iframe(self, user_id, username, numbers): # то ради чего я это все однажды затеял - iframe
        filter_list = [{"chatType": "whatsapp", "chatId": num.replace("+", "")} for num in numbers]
        
        endpoint = f'{self.base_url}/iframe'
        payload = {
        "user": {
            "id": str(user_id),
            "name": str(username)
        },
        "scope": "card",
        "filter": filter_list,
        "activeChat": filter_list[0] if numbers else {}
        }
        response = requests.post(endpoint, headers=self.headers, json=payload)
        return response.json()['url'] if "url" in response.json() else None
    
    def create_global_iframe(self, user_id, username): #создание глобальной версии, тоесть будут все чаты
        print("class")
        endpoint = f'{self.base_url}/iframe'
        payload = {
            "user": {
                "id": user_id,
                "name": username
            },
            "scope": "global"
        }
        response = requests.post(endpoint, headers=self.headers, json=payload)
        return response.json()['url'] if "url" in response.json() else None


    def get_users_paginated(self, offset=0): #тож какая то апи хуйня, я не помню уже
        endpoint = f'{self.base_url}/users'
        params = {
            'offset': offset,
            'sort': 'name'  # Сортировка по имени
        }
        response = requests.get(endpoint, headers=self.headers, params=params)
        return response.json()
    

    def bulk_delete_users(self, user_ids): # удаление юзеров, ибо можно их случайно размножить почкованием. храни id челов по братски
        endpoint = f'{self.base_url}/users/bulk_delete'
        payload = user_ids  # Список ID пользователей для удаления
        response = requests.patch(endpoint, headers=self.headers, json=payload)
        return response.status_code
    
    def add_update_contact_whatsapp(self, user_id, contacts): # создание контакта, чтобы у нас не было голого номера. тут как обновление так и создание, wazzup тут умные
        endpoint = "https://api.wazzup24.com/v3/contacts"
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.token}",
        }
        body = []
        for contact in contacts:
            contact_info = {
                "id": contact['id'],  # Уникальный ID контакта в вашей CRM системе
                "responsibleUserId": user_id,  # ID ответственного пользователя
                "name": contact['name'],  # Имя контакта
                "contactData": []  # Подготавливаем пустой массив для данных о контакте
            }
        
            # Перебираем все номера телефона для текущего контакта
            for phone_number in contact['phone']:
                phone_number = phone_number.replace("+", "")  # Удаляем знак '+', если он есть
                contact_info["contactData"].append({
                    "chatType": "whatsapp",  # Тип чата
                    "chatId": phone_number,  # ID чата
                })

        body.append(contact_info)

        esponse = requests.post(endpoint, headers=headers, data=json.dumps(body))
        print(esponse.status_code)
        return esponse.status_code
    

    def return_contacts(self): # вернет все контакты, точнее 100 штук, для этого тут и есть оффсет
        url = "https://api.wazzup24.com/v3/contacts?offset=0"
        esponse = requests.get(url, headers=self.headers)
        return esponse.json()
    
    def delete_contact_whatsapp(self, contact_ids): # удалит чела если он вам не нужен
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.token}",
        }
        data_json = json.dumps(contact_ids) 
        endpoint = "https://api.wazzup24.com/v3/contacts/bulk_delete"
        req = requests.patch(url=endpoint, headers=headers, data=data_json)
        return req.status_code
    
    def get_channels(self): # канал - то что используется для отправки соо
        endpoint = "https://api.wazzup24.com/v3/channels"
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.token}",
        }
        req = requests.get(url=endpoint, headers=headers)
        try:
            return req.status_code, req.json()
        except Exception as e:
            return req.status_code, None
        
    def send_message(self, text, id, channel_id, user_id): # отправка соо, лимит 10к символов для whatsapp
        endpoint = "https://api.wazzup24.com/v3/message"
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.token}",
        }
        chatType = "whatsapp"
        chatId = id
        data = {
            "channelId":channel_id,
            "chatId":chatId,
            "chatType":chatType,
            "text":text,
            "crmUserId":user_id

        }
        req = requests.post(url=endpoint, headers=headers, data=json.dumps(data))
        return req.json()