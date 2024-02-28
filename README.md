# wazzup_api_python
## Wazzup24.com api python
Данный файлик возможно позже станет либой, я об этом еще не думал.
Все началось с того, что у https://wazzup24.ru/ есть апишка, но нет либы под питон, а crm систему с интеграцией писать как то надо было.. В общем я набросал примерную структуру. У wazzup классная поддержка, но все равно использование готовой базы - быстрее и удобнее, чем выяснение всех аспектов

# Документация / Docs

## https://wazzup24.ru/help/api-ru/ - Russian
## https://wazzup24.com/help/api-en/ - English


# Установка / install
Просто скачай файл с гита и закинь его в папку своего проекта, дальше уже больше

# Использование / use
```python
#connect
import wazzup
#init
wa = WazzupAPI(token="YOUR_API_TOKEN")


#поиск пользователя или его создание(автоматически) / create_user
wa.get_user_data(user_id="id", name="name", phone="phone") # чтобы юзать телефон надо разкомментить строки / to use phone decomment need points
#Использовать лучше как создание, просто храните id в БД, повторно создать не дает


#Создание iframe. Номеров можно совать несколько, автоматом все подставится/ create iframe
iframe_url = wa.create_iframe(user_id="id", username="name", numbers="numbers whatsapp")
#Аналогично с global_iframe, ток номера указывать не нужно / analogy to global_iframe


#Удаление юзеров, передаем массив id / delete users
wz.bulk_delete_users(user_ids)

#Создание контактов / create contact
contacts = [{"id" : contragent_id, "name" : contragent_update['name'], "phone" : contragent_update['phones']}, {...}]
wz.add_update_contact_whatsapp(user_id, contacts)

#Получение контактов / get contacts
all_contacts = wz.return_contacts()

#Удаление контактов / delete contacts
wz.delete_contact_whatsapp(contact_ids)

#Получение контактов для отправки сообщений / get channels to send messages
channels = wz.get_channels()

#отправка сообщений / send messages
wz.send_message(text = "text", id="Chat_id", channel_id="channel_id", user_id="user_id - you")
```

# P.S
Надеюсь оно тебе поможет! С любовью от meowk1r1

I hope it helps you! With love from meowk1r1
