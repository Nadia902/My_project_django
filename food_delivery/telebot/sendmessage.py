import requests
from .models import TeleSettings

# функция для отправки сообщения в телеграмм


def send_telegram(tg_name, tg_phone):  # принимаем переменные из функции thanks_page
    if TeleSettings.objects.get(pk=1):
        settings = TeleSettings.objects.get(pk=1)
        token = settings.tg_token  # присваиваем токен
        chat_id = settings.tg_chat
        text = settings.tg_message  # присваиваем текст сообщения для телеграмма из модели
        api = 'https://api.telegram.org/bot'
        method = api + token + '/sendMessage'  # собираем путь для отправки сообщения

        if text.find('{') and text.find('}') and text.rfind('{') and text.rfind('}'):
            part_1 = text[:text.find('{')] # делаем срез для вставки наших данных
            part_2 = text[text.find('}') + 1:text.rfind('{')]

            text_slice = part_1 + tg_name + part_2 + tg_phone  # собираем новый текст уведомления
        else:
            text_slice = text

        req = None
        try:  # проверяем уведомление на ошибки
            req = requests.post(method, data={
                'chat_id': chat_id,
                'text': text_slice
            })
        finally:
            if req.status_code != 200:
                print('Ошибка отправки!')
            elif req.status_code == 500:
                print('Ошибка сервера')
            else:
                print('Все OK. Сообщение отправлено!')