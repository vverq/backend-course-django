import requests
import os
from telegram import ReplyKeyboardMarkup, KeyboardButton

API_KEY = os.environ['API_KEY']
api_telegram_url = 'https://api.telegram.org'
api_app_url = 'http://127.0.0.1:8000/api'


def start(update, cb):
    user = update.effective_user
    response_get_user_info = requests.get(f'{api_telegram_url}/bot{API_KEY}/getChat?chat_id={user.id}').json()
    response_result = response_get_user_info['result']
    if 'photo' in response_result:
        file_id = response_result['photo']['small_file_id']
        response_get_photo = requests.get(f'{api_telegram_url}/bot{API_KEY}/getFile?file_id={file_id}').json()
        file_path = response_get_photo['result']['file_path']
        file = requests.get(f'{api_telegram_url}/file/bot{API_KEY}/{file_path}').content
    else:
        file = None

    user_info = {
        'id': response_result['id'],
        'username': response_result['username'],
        'first_name': response_result['first_name'],
        'last_name': response_result['last_name'] if 'last_name' in response_get_user_info['result'] else '',
        'bio': response_result['bio'] if 'bio' in response_get_user_info['result'] else '',
    }

    if file:
        user_info['profile_photo'] = 'profile_photo'
        files = {'profile_photo': (f'{file_id}.jpg', file)}
        requests.post(f'{api_app_url}/users/create/', data=user_info, files=files)
    else:
        requests.post(f'{api_app_url}/users/create/', data=user_info)


def share_phone(update):
    contact_keyboard = KeyboardButton(text="share", request_contact=True)
    reply_markup = ReplyKeyboardMarkup([[contact_keyboard]], one_time_keyboard=True)
    update.message.reply_text("share you contact", reply_markup=reply_markup)


def update_phone(update):
    contact = update.effective_message.contact
    phone = {'phone_number': contact.phone_number}
    requests.put(f'{api_app_url}/users/update/{contact.user_id}/', data=phone)


def me(update):
    user_id = update.effective_user.id
    response = requests.get(f'{api_app_url}/users/{user_id}/')
    if response.status_code == 404:
        update.message.reply_text("send me /start command")
    elif response.status_code == 200:
        if not response.json()['phone_number']:
            update.message.reply_text('send me /set_phone command')
        else:
            message_text = response.text.strip('{}').replace(',', '\n')
            update.message.reply_text(message_text)
