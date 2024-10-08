from bs4 import BeautifulSoup
from urllib.parse import urlparse, quote
from faker import Faker
from fake_useragent import UserAgent  
from phonenumbers import geocoder, timezone, carrier, PhoneNumberFormat
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from pystyle import Write, Colors, System
from colorama import init
import requests
import os  
import sys 
import subprocess
import whois
import time
import platform
import phonenumbers
import csv
import smtplib

System.Title('Dark Legion')

init(autoreset=True)

faker = Faker('ru_RU')
fake_agent = UserAgent().random

requirements = [
    'bs4',
    'urllib3',
    'faker',
    'fake_useragent',
    'phonenumbers',
    'pystyle',
    'colorama',
    'requests',
    'python-whois',
    'selenium',
    'webdriver_manager'
]

senders = {
    'korlithiobtennick@mail.ru': 'feDLSiueGT89APb81v74',
    'terbgebuoviror@mail.ru': 'gaqaKs06xg22kkXXW2LU',
    'avyavya.vyaavy@mail.ru': 'zmARvx1MRvXppZV6xkXj',
    'gdfds98@mail.ru': '1CtFuHTaQxNda8X06CaQ',
    'dfsdfdsfdf51@mail.ru': 'SXxrCndCR59s5G9sGc6L',
'aria.therese.svensson@mail.com': 'Zorro1ab',
'taterbug@verizon.net': 'Holly1!',
'ejbrickner@comcast.net': 'Pass1178',
'teressapeart@cox.net': 'Quinton2329!',
'liznees@verizon.net': 'Dancer008',
'olajakubovich@mail.com': 'OlaKub2106OlaKub2106',
'kcdg@charter.net': 'Jennifer3*',
'bean_118@hotmail.com': 'Liverpool118!',
'dsdhjas@mail.com': 'LONGHACH123',
'robitwins@comcast.net': 'May241996',
'wasina@live.com': 'Marlas21',
'aruzhan.01@mail.com': '1234567!',
'rob.tackett@live.com': 'metallic',
'lindahallenbeck@verizon.net': 'Anakin@2014',
'hlaw82@mail.com': 'Snoopy37$$',
'paintmadman@comcast.net': 'mycat2200*',
'prideandjoy@verizon.net': 'Ihatejen12',
'sdgdfg56@mail.com': 'kenwood4201',
'garrett.danelz@comcast.net': 'N11golfer!',
'gillian_1211@hotmail.com': 'Gilloveu1211',
'sunpit16@hotmail.com': 'Putter34!',
'fdshelor@verizon.net': 'Masco123*',
'yeags1@cox.net': 'Zoomom1965!',
'amine002@usa.com': 'iScrRoXAei123',
'bbarcelo16@cox.net': 'Bsb161089$$',
'laliebert@hotmail.com': 'pirates2',
'vallen285@comcast.net': 'Delft285!1!',
'sierra12@email.com': 'tegen1111',
'luanne.zapevalova@mail.com': 'FqWtJdZ5iN@',
'kmay@windstream.net': 'Nascar98',
'redbrick1@mail.com': 'Redbrick11',
'ivv9ah7f@mail.com': 'K226nw8duwg',
'erkobir@live.com': 'floydLAWTON019',
'Misscarter@mail.com': 'ashtray19',
'carlieruby10@cox.net': 'Lollypop789$',
'blackops2013@mail.com': 'amason123566',
'caroline_cullum@comcast.net': 'carter14',
'dpb13@live.com': 'Ic&ynum13',
'heirhunter@usa.com': 'Noguys@714',
'sherri.edwards@verizon.net': 'Dreaming123#',
'rami.rami1980@hotmail.com': 'ramirami1980',
'jmsingleton2@comcast.net': '151728Jn$$',
'aberancho@aol.com': '10diegguuss10',
'dgidel@iowatelecom.net': 'Buster48',
'gpopandopul@mail.com': 'GEORG62A',
'bolgodonsk@mail.com': '012345678!',
'colbycolb@cox.net': 'Signals@1',
'nicrey4@comcast.net': 'Dabears54',
'mordechai@mail.com': 'Mordechai',
'inemrzoya@mail.com': 'rLS1elaUrLS1elaU',
'tarabedford@comcast.net': 'Money4me',
'mycockneedsit@mail.com': 'benjamin3',
'saralaine@mail.com': 'sarlaine12!1',
'jonb2006@verizon.net': '1969Camaro',
'rjhssa1@verizon.net': 'Donna613*',
'cameron.doug@charter.net': 'Jake2122$',
'bridget.shappell@comcast.net': 'Brennan1',
'rugs8@comcast.net': 'baseball46',
'averyjacobs3@mail.com': '1960682644!',
'lstefanick@hotmail.com': 'Luv2dance2',
'bchavez123@mail.com': 'aadrianachavez',
'lukejamesjones@mail.com': 'tinkerbell1',
'emahoney123@comcast.net': 'Shieknmme3#',
'mandy10.mcevoy@btinternet.com': 'Tr1plets3',
'jet747@cox.net': 'Sadie@1234',
'landsgascareservices@mail.com': 'Alisha25@',
'samantha224@mail.com': 'Madden098!@',
'kbhamil@wowway.com': 'Carol1940',
'email@bjasper.com': 'Lhsnh4us123!',
'biggsbrian@cox.net': 'Trains@2247Trains@2247',
'dzzeblnd@aol.com': 'Geosgal@1',
'jtrego@indy.rr.com': 'Jackwill14!',
'chrisphonte.rj@comcast.net': 'Junior@3311',
'tvwifiguy@comcast.net': 'Bill#0101',
'defenestrador@mail.com': 'm0rb1d8ss',
'glangley@gmx.com': 'ironhide',
'charlotte2850@hotmail.com': 'kelalu2850'
}

receivers = ['sms@telegram.org', 'dmca@telegram.org', 'abuse@telegram.org',
             'sticker@telegram.org', 'support@telegram.org']


def clear_screen():
    os.system('cls' if platform.system() == 'Windows' else 'clear')

def install_requirements():
    Write.Print('Установка зависимостей...\n', Colors.cyan, interval=0.00005)
    for module in requirements:
        try:
            __import__(module)
            Write.Print(f'{module} уже установлен\n', Colors.cyan, interval=0.00005)
        except ImportError:
            Write.Print(f'Установка {module}...\n', Colors.cyan, interval=0.00005)
            subprocess.check_call([sys.executable, '-m', 'pip', 'install', module, '--quiet'])

def return_menu():
    print()
    Write.Input('Нажмите Enter чтобы вернуться назад...', Colors.cyan, interval=0.00005)

def main_menu():
    banner = """
        ██████╗  █████╗ ██████╗ ██╗  ██╗    ██╗     ███████╗ ██████╗ ██╗ ██████╗ ███╗   ██╗
        ██╔══██╗██╔══██╗██╔══██╗██║ ██╔╝    ██║     ██╔════╝██╔════╝ ██║██╔═══██╗████╗  ██║
        ██║  ██║███████║██████╔╝█████╔╝     ██║     █████╗  ██║  ███╗██║██║   ██║██╔██╗ ██║
        ██║  ██║██╔══██║██╔══██╗██╔═██╗     ██║     ██╔══╝  ██║   ██║██║██║   ██║██║╚██╗██║
        ██████╔╝██║  ██║██║  ██║██║  ██╗    ███████╗███████╗╚██████╔╝██║╚██████╔╝██║ ╚████║
        ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝    ╚══════╝╚══════╝ ╚═════╝ ╚═╝ ╚═════╝ ╚═╝  ╚═══╝

        Made By: Crypton
        ═════════════════════════════════════════════════════════════════════════════════════
        [1] Поиск по номеру         [7] Генераторы   [10] DDOS Атака
        [2] Поиск по сайту          [8] Мануалы    
        [3] Поиск по нику           [9] Сносеры
        [4] Поиск по IP             [0] Выход
        [5] Поиск по ID тг
        [6] Поиск по @ тг

    """
    Write.Print(banner, Colors.cyan, interval=0.00005)

def search_phone_number():
    try:
        phone_number = Write.Input('[?] Введите номер телефона >>> ', Colors.cyan, interval=0.00005)
        phone_number_split = phone_number.replace(' ','').replace('+','')
        phone_number_parse = phonenumbers.parse(phone_number, 'RU')

        international_format = phonenumbers.format_number(phone_number_parse, PhoneNumberFormat.INTERNATIONAL)
        national_format = phonenumbers.format_number(phone_number_parse, PhoneNumberFormat.NATIONAL)
        E164_format = phonenumbers.format_number(phone_number_parse, PhoneNumberFormat.E164)
        RFC3966_format = phonenumbers.format_number(phone_number_parse, PhoneNumberFormat.RFC3966)

        is_possible = phonenumbers.is_possible_number(phone_number_parse)
        is_valid = phonenumbers.is_valid_number(phone_number_parse)

        region_code = phonenumbers.region_code_for_number(phone_number_parse)
        carrier_name = carrier.name_for_number(phone_number_parse, 'ru')
        location = geocoder.description_for_number(phone_number_parse, 'ru')
        timezone_info = timezone.time_zones_for_number(phone_number_parse)

        number_results = f"""
Результат обычного сканирования: 

[+] Форматы номера (Пригодится в поисковике для различных результатов)
├ Международный: {international_format}
├ Национальный: {national_format}
├ Формат E164: {E164_format}
└ Формат RFC3966: {RFC3966_format}

[+] Проверка номера
├ Верный: {'да' if is_possible else 'нет'}
└ Валидный: {'да' if is_valid else 'нет'}

[+] Информация по номеру
├ Телефонный номер: {phone_number}
├ Код номера: {region_code}
├ Оператор: {carrier_name}
├ Страна: {location}
└ Часовой пояс: {timezone_info}

[+] Социальные сети (Проверьте существование номера в перечисленных соц сетях)
├ Whatsapp: https://wa.me/{phone_number_split}
├ Telegram: https://t.me/{phone_number_split}
├ Viber: viber://add?number={phone_number_split}
├ Skype звонок: skype:{phone_number_split}?call
├ Google: https://www.google.com/search?q={phone_number}
├ Yandex: https://yandex.ru/search/?text={phone_number}
├ Vk: https://vk.com/restore
├ Facebook: https://www.facebook.com/login/identify/?ctx=recover&ars=facebook_login&from_login_screen=0
├ Instagram: https://www.instagram.com/accounts/password/reset/
├ Twitter: https://x.com/i/flow/password_reset
├ Linkedin: https://www.linkedin.com/checkpoint/rp/request-password-reset?trk=guest_homepage-basic_nav-header-signin
└ Ok: https://ok.ru/dk?st.cmd=anonymRecoveryStartPhoneLink
        """

        Write.Print(number_results, Colors.cyan, interval=0.00005)
        print()
        Write.Print('Результаты Fincalculator сканирования: ', Colors.cyan, interval=0.00005)
        # Сканирование на сервисе Fincalculator 
        url = f'https://fincalculator.ru/api/tel/{phone_number}'

        response = requests.get(url)

        if response.status_code == 200:
            try:
                list_d = {}
                data = response.json()
                if data:
                    for key, value in data.items():
                        Write.Print(f"{key}: {value}\n", Colors.cyan, interval=0.00005)

                else:
                    Write.Print(f'[!] Не найден', Colors.red, interval=0.00005)

                region = data.get('region')
                try:
                    url2 = f'https://nominatim.openstreetmap.org/search?q={region}&format=json&limit=1'
                    response = requests.get(url2)
                    if response.status_code == 200:
                        data = response.json()
                        if data:
                            location = data[0]
                            latitude = location['lat']
                            longitude = location['lon']
                            print()
                            Write.Print(f'├ Широта: {latitude}', Colors.cyan, interval=0.00005)
                            print()
                            Write.Print(f'├ Долгота: {longitude}', Colors.cyan, interval=0.00005)

                        else:
                            Write.Print('[!] Не найден', Colors.red, interval=0.00005)

                except requests.exceptions.RequestException as e:
                    print(f'[!] Ошибка запроса: {e}')

                print()
                if region:
                    google_maps_url = f'https://www.google.com/maps/place/{region}'
                    wikipedia = f'ru.wikipedia.org/wiki/{region}'
                    Write.Print(f'Регион по карте 1: {google_maps_url}', Colors.cyan, interval=0.00005)
                else:
                    Write.Print(f'[!] Не найден', Colors.red, interval=0.00005)

            except Exception as e:
                Write.Print(f'[!] Ошибка: {str(e)}\n', Colors.red, interval=0.00005)
        else:
            Write.Print(f"[!] Ошибка: {response.status_code}", Colors.red, interval=0.00005)

        Write.Print('\n\n[+] Результаты PhoneRadar сканирования: ', Colors.cyan, interval=0.00005)
        print()
        # Сервис Phoneradar
        url = f'https://phoneradar.ru/phone/{phone_number}'
        response = requests.get(url)

        if response.status_code == 200:
            try:
                html_content = response.text
                soup = BeautifulSoup(html_content, 'html.parser')
                table = soup.find_all('table', class_='table')
                if not table:
                    Write.Print(f'[!] Не найден', Colors.red, interval=0.00005)
                for tab in table:
                    text = tab.get_text(strip=True, separator='\n')
                    Write.Print(text, Colors.cyan, interval=0.00005)
            except Exception as e:
                Write.Print(f'[!] Ошибка: {str(e)}\n', Colors.red, interval=0.00005)
        else:
            Write.Print(f"[!] Ошибка: {response.status_code}", Colors.red, interval=0.00005)
    

        url = f'https://fincalculator.ru/api/tel/{phone_number}'
        response = requests.get(url)
        html_content = response.text  

        soup = BeautifulSoup(html_content, 'html.parser')
        find_region = soup.find_all('div', class_='col-xs-9 col-sm-8 tel-info_result-value')
        for div in find_region:
            print(div.get_text(strip=True))

        Write.Print('\n\n[+] Результаты HtmlWeb сканирования (20 попыток): ', Colors.cyan, interval=0.00005)
        print()
        url = 'https://htmlweb.ru/geo/api.php?'
        encoded_url = quote(phone_number)
        full_url = url + 'json&telcod=' + encoded_url

        response = requests.get(full_url)
        if response.status_code == 200:
            data = response.json()
            Write.Print(f"\n[+] Страна \n", Colors.cyan, interval=0.00005)
            country = data.get('country\n', {})
            Write.Print(f"├ Название: {data.get('name', 'Неизвестно')} \n", Colors.cyan, interval=0.00005)
            Write.Print(f"├ Полное название: {country.get('fullname', 'Неизвестно')} \n", Colors.cyan, interval=0.00005)
            Write.Print(f"├ Английское название: {country.get('english', 'Неизвестно')} \n", Colors.cyan, interval=0.00005)
            Write.Print(f"├ Код страны: {country.get('id', 'Неизвестно')} \n", Colors.cyan, interval=0.00005)
            Write.Print(f"├ Код страны (3 символа): {country.get('country_code3', 'Неизвестно')} \n", Colors.cyan, interval=0.00005)
            Write.Print(f"├ ISO код: {country.get('iso', 'Неизвестно')} \n", Colors.cyan, interval=0.00005)
            Write.Print(f"├ Телефонный код: {country.get('telcod', 'Неизвестно')} \n", Colors.cyan, interval=0.00005)
            Write.Print(f"├ Длина телефонного кода: {country.get('telcod_len', 'Неизвестно')} \n", Colors.cyan, interval=0.00005)
            Write.Print(f"├ Расположение: {country.get('location', 'Неизвестно')} \n", Colors.cyan, interval=0.00005)
            Write.Print(f"├ Столичный код: {country.get('capital', 'Неизвестно')} \n", Colors.cyan, interval=0.00005)
            Write.Print(f"├ MCC код: {country.get('mcc', 'Неизвестно')} \n", Colors.cyan, interval=0.00005)
            Write.Print(f"├ Язык: {country.get('lang', 'Неизвестно')} \n", Colors.cyan, interval=0.00005)
            Write.Print(f"└ Языковой код: {country.get('langcod', 'Неизвестно')} \n", Colors.cyan, interval=0.00005)
            Write.Print("-" * 40, Colors.cyan, interval=0.00005)

            region = data.get('region', {})
            Write.Print("\n[+] Регион: \n", Colors.cyan, interval=0.00005)
            Write.Print(f"├ ID: {region.get('id', 'Неизвестно')} \n", Colors.cyan, interval=0.00005)
            Write.Print(f"├ Название: {region.get('name', 'Неизвестно')} \n", Colors.cyan, interval=0.00005)
            Write.Print(f"├ Округ: {region.get('okrug', 'Неизвестно')} \n", Colors.cyan, interval=0.00005)
            Write.Print(f"├ Автокод: {region.get('autocod', 'Неизвестно')} \n", Colors.cyan, interval=0.00005)
            Write.Print(f"├ Столичный код: {region.get('capital', 'Неизвестно')} \n", Colors.cyan, interval=0.00005)
            Write.Print(f"├ Английское название: {region.get('english', 'Неизвестно')} \n", Colors.cyan, interval=0.00005)
            Write.Print(f"├ ISO код: {region.get('iso', 'Неизвестно')} \n", Colors.cyan, interval=0.00005)
            Write.Print(f"└ Страна: {region.get('country', 'Неизвестно')} \n", Colors.cyan, interval=0.00005)
            Write.Print("-" * 40, Colors.cyan, interval=0.00005)

            # Вывод данных о столице
            capital = data.get('capital', {})
            Write.Print("\n[+] Столица: \n", Colors.cyan, interval=0.00005)
            Write.Print(f"├ ID: {capital.get('id', 'Неизвестно')} \n", Colors.cyan, interval=0.00005)
            Write.Print(f"├ Название: {capital.get('name', 'Неизвестно')} \n", Colors.cyan, interval=0.00005)
            Write.Print(f"├ Площадь: {capital.get('area', 'Неизвестно')} \n", Colors.cyan, interval=0.00005)
            Write.Print(f"├ Телефонный код: {capital.get('telcod', 'Неизвестно')} \n", Colors.cyan, interval=0.00005)
            Write.Print(f"├ Широта: {capital.get('latitude', 'Неизвестно')} \n", Colors.cyan, interval=0.00005)
            Write.Print(f"├ Долгота: {capital.get('longitude', 'Неизвестно')} \n", Colors.cyan, interval=0.00005)
            Write.Print(f"├ Часовой пояс: {capital.get('time_zone', 'Неизвестно')} \n", Colors.cyan, interval=0.00005)
            Write.Print(f"├ Часовая зона: {capital.get('tz', 'Неизвестно')} \n", Colors.cyan, interval=0.00005)
            Write.Print(f"├ Английское название: {capital.get('english', 'Неизвестно')} \n", Colors.cyan, interval=0.00005)
            Write.Print(f"├ Район: {capital.get('rajon', 'Неизвестно')} \n", Colors.cyan, interval=0.00005)
            Write.Print(f"├ Страна: {capital.get('country', 'Неизвестно')} \n", Colors.cyan, interval=0.00005)
            Write.Print(f"├ Звуковое обозначение: {capital.get('sound', 'Неизвестно')} \n", Colors.cyan, interval=0.00005)
            Write.Print(f"├ Уровень: {capital.get('level', 'Неизвестно')} \n", Colors.cyan, interval=0.00005)
            Write.Print(f"├ ISO код: {capital.get('iso', 'Неизвестно')} \n", Colors.cyan, interval=0.00005)
            Write.Print(f"├ Вид: {capital.get('vid', 'Неизвестно')} \n", Colors.cyan, interval=0.00005)
            Write.Print(f"├ Почтовый индекс: {capital.get('post', 'Неизвестно')} \n", Colors.cyan, interval=0.00005)
            Write.Print(f"└ Wikipedia ссылка: {capital.get('wiki', 'Неизвестно')}  \n", Colors.cyan, interval=0.00005)
            Write.Print("-" * 40, Colors.cyan, interval=0.00005)

            # Вывод данных о населённом пункте
            city = data.get('0', {})
            Write.Print("\n[+] Населённый пункт: \n", Colors.cyan, interval=0.00005)
            Write.Print(f"├ ID: {city.get('id', 'Неизвестно')} \n", Colors.cyan, interval=0.00005)
            Write.Print(f"├ Название: {city.get('name', 'Неизвестно')} \n", Colors.cyan, interval=0.00005)
            Write.Print(f"├ Площадь: {city.get('area', 'Неизвестно')} \n", Colors.cyan, interval=0.00005)
            Write.Print(f"├ Телефонный код: {city.get('telcod', 'Неизвестно')} \n", Colors.cyan, interval=0.00005)
            Write.Print(f"├ Широта: {city.get('latitude', 'Неизвестно')} \n", Colors.cyan, interval=0.00005)
            Write.Print(f"├ Долгота: {city.get('longitude', 'Неизвестно')} \n", Colors.cyan, interval=0.00005)
            Write.Print(f"├ Часовой пояс: {city.get('time_zone', 'Неизвестно')} \n", Colors.cyan, interval=0.00005)
            Write.Print(f"├ Часовая зона: {city.get('tz', 'Неизвестно')} \n", Colors.cyan, interval=0.00005)
            Write.Print(f"├ Английское название: {city.get('english', 'Неизвестно')} \n", Colors.cyan, interval=0.00005)
            Write.Print(f"├ Район: {city.get('rajon', 'Неизвестно')} \n", Colors.cyan, interval=0.00005)
            Write.Print(f"├ Подрайон: {city.get('sub_rajon', 'Неизвестно')} \n", Colors.cyan, interval=0.00005)
            Write.Print(f"├ Страна: {city.get('country', 'Неизвестно')} \n", Colors.cyan, interval=0.00005)
            Write.Print(f"├ Звуковое обозначение: {city.get('sound', 'Неизвестно')} \n", Colors.cyan, interval=0.00005)
            Write.Print(f"├ Уровень: {city.get('level', 'Неизвестно')} \n", Colors.cyan, interval=0.00005)
            Write.Print(f"├ ISO код: {city.get('iso', 'Неизвестно')} \n", Colors.cyan, interval=0.00005)
            Write.Print(f"├ Вид: {city.get('vid', 'Неизвестно')} \n", Colors.cyan, interval=0.00005)
            Write.Print(f"├ Почтовый индекс: {city.get('post', 'Неизвестно')} \n", Colors.cyan, interval=0.00005)
            Write.Print(f"├ Wikipedia ссылка: {city.get('wiki', 'Неизвестно')} \n", Colors.cyan, interval=0.00005)
            Write.Print(f"├ Оператор: {city.get('oper', 'Неизвестно')} \n", Colors.cyan, interval=0.00005)
            Write.Print(f"├ Диапазон: {city.get('def', 'Неизвестно')} \n", Colors.cyan, interval=0.00005)
            Write.Print(f"├ Мобильный телефон: {city.get('mobile', 'Неизвестно')} \n", Colors.cyan, interval=0.00005)
            Write.Print(f"└ Бренд оператора: {city.get('oper_brand', 'Неизвестно')} \n", Colors.cyan, interval=0.00005)
            if capital.get('longitude') and capital.get('latitude'):
                longitude = capital.get('longitude')
                latitude = capital.get('latitude')
                region_maps = f'https://www.google.com/maps/place/{longitude}+{latitude}'
                Write.Print(f"├ Регион по карте 2: {region_maps}", Colors.cyan, interval=0.00005)
            else:
                Write.Print("[!] Неизвестно", Colors.cyan, interval=0.00005)

        else:
            Write.Print(f"[!] Ошибка: {response.status_code} \n", Colors.red, interval=0.00005)

        Write.Print("\n[+] Результаты поиска по Google: \n", Colors.cyan, interval=0.00005)
        url = f'https://www.google.com/search?q={phone_number}'
        region_code = phone_number_parse.country_code
        response = requests.get(url)

        soup = BeautifulSoup(response.text, 'lxml')
        all_href = soup.find_all('a')

        found = False

        for href in all_href:
            href_text = href.text.lower()  
            href_item = href.get('href')   
            if str(region_code) in href_text:
                Write.Print(f'├ Номер найден на сайте: {href_item}\n', Colors.cyan, interval=0.00005)
                found = True
                break 

        if not found:
            Write.Print(f'[!] Сайты по данному номеру не найдены', Colors.cyan, interval=0.00005)

    except phonenumbers.NumberParseException as e:
        Write.Print(f'[!] Ошибка {str(e)}\n', Colors.red, interval=0.00005)
    except Exception as e:
        Write.Print(f'[!] Ошибка {str(e)}\n', Colors.red, interval=0.00005)  

def search_by_domain():
    try:

        domain = Write.Input('[+] Введите домен сайта (example.com) >>> ', Colors.cyan, interval=0.00005)
        if not domain:
            Write.Print('[!] Поле не может быть пустым\n', Colors.red, interval=0.00005)
            return
        site = whois.whois(domain)
        site_results = f"""
[+] Инфа о сайте
├ Домен: {site.domain_name}
├ Регистрация: {site.registrar if site.registrar else 'не найдено'}
├ WHOIS Сервер: {site.whois_server if site.whois_server else 'не найдено'}
├ Реферальная ссылка: {site.referral_url if site.referral_url else 'не найдено'}
├ Дата создание: {site.creation_date if site.creation_date else 'не найдено'}
├ Дата обновлении: {site.updated_date if site.updated_date else 'не найдено'}
├ Дата истечение: {site.expiration_date if site.expiration_date else 'не найдено'}
├ Сервера: {site.name_servers if site.name_servers else 'не найдено'}
├ Почты: {site.emails if site.emails else 'не найдено'}
├ DNSSEC: {site.dnssec if site.dnssec else 'не найдено'}
├ Организация: {site.organisation if site.organisation else 'не найдено'}        
├ Адрес: {site.address if site.address else 'не найдено'}
├ Город: {site.city if site.city else 'не найдено'}
├ Штат: {site.state if site.referral_url else 'не найдено'}
├ Zip код: {site.zipcode if site.zipcode else 'не найдено'}
├ Страна: {site.country if site.country else 'не найдено'}
└ Статус: {site.status if site.status else 'не найдено'}
    """

        Write.Print(site_results, Colors.cyan, interval=0.00005)

    except Exception as e:
        Write.Print(f'[!] Ошибка {str(e)}\n', Colors.red, interval=0.00005)    

def search_by_nick():
    try:
        nickname = Write.Input('[+] Введите ник >>> ', Colors.cyan, interval=0.00005)

        if not nickname:
            Write.Print(f'[!] Поле не может быть пустым\n', Colors.red, interval=0.00005)
            return

        urls = [
                    f"https://t.me/{nickname}",
                    f"https://www.instagram.com/{nickname}",
                    f"https://www.tiktok.com/@{nickname}",
                    f"https://twitter.com/{nickname}",
                    f"https://www.facebook.com/{nickname}",
                    f"https://www.youtube.com/@{nickname}",
                    f"https://t.me/{nickname}",
                    f"https://www.roblox.com/user.aspx?username={nickname}",
                    f"https://www.twitch.tv/{nickname}",
                    f"https://www.reddit.com/{nickname}",
                    f"https://pinterest.com/{nickname}",
                    f"https://linkedin.com/in/{nickname}",
                    f"https://snapchat.com/add/{nickname}"
                ]

        for url in urls:
            try:
                response = requests.get(url)
                if response.status_code == 200:
                    Write.Print(f"\n├ {url} - аккаунт найден", Colors.cyan, interval=0.005)
                elif response.status_code == 404:
                    Write.Print(f"\n[!] {url} - аккаунт не найден", Colors.red, interval=0.005)
                else:
                    Write.Print(f"\n[!] {url} - ошибка {response.status_code}", Colors.red, interval=0.005)

            except Exception as e:
                Write.Print(f'[!] Ошибка {str(e)}\n', Colors.red, interval=0.00005)

    except Exception as e:
            Write.Print(f'[!] Ошибка {str(e)}\n', Colors.red, interval=0.00005)

def search_by_ip():
    try:
        ip_address = Write.Input('[+] Введите Ip адрес >>> ', Colors.cyan, interval=0.00005).strip()
        if not ip_address:
            Write.Print('[!] Поле не может быть пустым\n', Colors.red, interval=0.00005)
            return

        url = f'http://ip-api.com/json/{ip_address}'

        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            info = ""
            for key,value in data.items():
                info += f"├ {key}: {value}\n"

            Write.Print(info, Colors.cyan, interval=0.00005)
        else:
            Write.Print(f'[!] Ошибка {response.status_code}\n', Colors.red, interval=0.00005)

        print()
        
    except Exception as e:
        Write.Print(f'[!] Ошибка {str(e)}\n', Colors.red, interval=0.00005)

def search_by_telegram_id():
    found1 = found2 = False
    phone = username = first_name = last_name = None
    try:
        user_id = Write.Input('[?] Введите ID >>> ', Colors.cyan, interval=0.00005)

        with open('useridbase/EYEOFGOD_1.csv', mode='r', encoding='utf-8') as file:
            reader = csv.reader(file, delimiter=',')
            for row in reader:
                if row[0] == user_id:
                    phone = row[1]
                    username = row[2]
                    first_name = row[3]
                    last_name = row[4]
                    found1 = True
                    break

        if found1:
            id_results = f"""
[+] База 1
├ Номер телефона: {phone if phone else 'не найден'}
├ Никнейм: {username if username else 'не найден'}
├ Имя: {first_name if first_name else 'не найден'}
└ Фамилия: {last_name if last_name else 'не найден'}
                """

            Write.Print(id_results, Colors.cyan, interval=0.00005)

        else:
            Write.Print('\n[!] Пользователя в базе 1 нету\n', Colors.red, interval=0.00005)

        with open('useridbase/EYEOFGOD_2.csv', mode='r', encoding='utf-8') as file:
            reader = csv.reader(file, delimiter=',')
            for row in reader:
                if row[0] == user_id:
                    phone = row[1]
                    username = row[2]
                    first_name = row[3]
                    last_name = row[4]
                    found1 = True
                    break

        if found1:
            id_results = f"""
[+] База 2
├ Номер телефона: {phone if phone else 'не найден'}
├ Никнейм: {username if username else 'не найден'}
├ Имя: {first_name if first_name else 'не найден'}
└ Фамилия: {last_name if last_name else 'не найден'}
                """

            Write.Print(id_results, Colors.cyan, interval=0.00005)

        else:
            Write.Print('[!] Пользователя в базе 2 нету\n', Colors.red, interval=0.00005)

        with open('useridbase/EYEOFGOD_3.csv', mode='r', encoding='utf-8') as file:
            reader = csv.reader(file, delimiter=',')
            for row in reader:
                if row[0] == user_id:
                    phone = row[1]
                    username = row[2]
                    first_name = row[3]
                    last_name = row[4]
                    found1 = True
                    break

        if found1:
            id_results = f"""
[+] База 3
├ Номер телефона: {phone if phone else 'не найден'}
├ Никнейм: {username if username else 'не найден'}
├ Имя: {first_name if first_name else 'не найден'}
└ Фамилия: {last_name if last_name else 'не найден'}
                """

            Write.Print(id_results, Colors.cyan, interval=0.00005)

        else:
            Write.Print('[!] Пользователя в базе 3 нету\n', Colors.red, interval=0.00005)

        with open('useridbase/EYEOFGOD_4.csv', mode='r', encoding='utf-8') as file:
            reader = csv.reader(file, delimiter=',')
            for row in reader:
                if row[0] == user_id:
                    phone = row[1]
                    username = row[2]
                    first_name = row[3]
                    last_name = row[4]
                    found1 = True
                    break

        if found1:
            id_results = f"""
[+] База 4
├ Номер телефона: {phone if phone else 'не найден'}
├ Никнейм: {username if username else 'не найден'}
├ Имя: {first_name if first_name else 'не найден'}
└ Фамилия: {last_name if last_name else 'не найден'}
                """

            Write.Print(id_results, Colors.cyan, interval=0.00005)

        else:
            Write.Print('[!] Пользователя в базе 4 нету\n', Colors.red, interval=0.00005)

        with open('useridbase/EYEOFGOD_5.csv', mode='r', encoding='utf-8') as file:
            reader = csv.reader(file, delimiter=',')
            for row in reader:
                if row[0] == user_id:
                    phone = row[1]
                    username = row[2]
                    first_name = row[3]
                    last_name = row[4]
                    found1 = True
                    break

        if found1:
            id_results = f"""
[+] База 5
├ Номер телефона: {phone if phone else 'не найден'}
├ Никнейм: {username if username else 'не найден'}
├ Имя: {first_name if first_name else 'не найден'}
└ Фамилия: {last_name if last_name else 'не найден'}
                """

            Write.Print(id_results, Colors.cyan, interval=0.00005)

        else:
            Write.Print('[!] Пользователя в базе 5 нету\n', Colors.red, interval=0.00005)

        with open('useridbase/EYEOFGOD_6.csv', mode='r', encoding='utf-8') as file:
            reader = csv.reader(file, delimiter=',')
            for row in reader:
                if row[0] == user_id:
                    phone = row[1]
                    username = row[2]
                    first_name = row[3]
                    last_name = row[4]
                    found1 = True
                    break

        if found1:
            id_results = f"""
[+] База 6
├ Номер телефона: {phone if phone else 'не найден'}
├ Никнейм: {username if username else 'не найден'}
├ Имя: {first_name if first_name else 'не найден'}
└ Фамилия: {last_name if last_name else 'не найден'}
                """

            Write.Print(id_results, Colors.cyan, interval=0.00005)

        else:
            Write.Print('[!] Пользователя в базе 6 нету\n', Colors.red, interval=0.00005)

        with open('useridbase/EYEOFGOD_7.csv', mode='r', encoding='utf-8') as file:
            reader = csv.reader(file, delimiter=',')
            for row in reader:
                if row[0] == user_id:
                    phone = row[1]
                    username = row[2]
                    first_name = row[3]
                    last_name = row[4]
                    found1 = True
                    break

        if found1:
            id_results = f"""
[+] База 7
├ Номер телефона: {phone if phone else 'не найден'}
├ Никнейм: {username if username else 'не найден'}
├ Имя: {first_name if first_name else 'не найден'}
└ Фамилия: {last_name if last_name else 'не найден'}
                """

            Write.Print(id_results, Colors.cyan, interval=0.00005)

        else:
            Write.Print('[!] Пользователя в базе 7 нету\n', Colors.red, interval=0.00005)

        with open('useridbase/EYEOFGOD_8.csv', mode='r', encoding='utf-8') as file:
            reader = csv.reader(file, delimiter=',')
            for row in reader:
                if row[0] == user_id:
                    phone = row[1]
                    username = row[2]
                    first_name = row[3]
                    last_name = row[4]
                    found1 = True
                    break

        if found1:
            id_results = f"""
[+] База 8
├ Номер телефона: {phone if phone else 'не найден'}
├ Никнейм: {username if username else 'не найден'}
├ Имя: {first_name if first_name else 'не найден'}
└ Фамилия: {last_name if last_name else 'не найден'}
                """

            Write.Print(id_results, Colors.cyan, interval=0.00005)

        else:
            Write.Print('[!] Пользователя в базе 8 нету\n', Colors.red, interval=0.00005)

        with open('useridbase/EYEOFGOD_9.csv', mode='r', encoding='utf-8') as file:
            reader = csv.reader(file, delimiter=',')
            for row in reader:
                if row[0] == user_id:
                    phone = row[1]
                    username = row[2]
                    first_name = row[3]
                    last_name = row[4]
                    found1 = True
                    break

        if found1:
            id_results = f"""
[+] База 9
├ Номер телефона: {phone if phone else 'не найден'}
├ Никнейм: {username if username else 'не найден'}
├ Имя: {first_name if first_name else 'не найден'}
└ Фамилия: {last_name if last_name else 'не найден'}
                """

            Write.Print(id_results, Colors.cyan, interval=0.00005)

        else:
            Write.Print('[!] Пользователя в базе 9 нету\n', Colors.red, interval=0.00005)

        with open('useridbase/EYEOFGOD_10.csv', mode='r', encoding='utf-8') as file:
            reader = csv.reader(file, delimiter=',')
            for row in reader:
                if row[0] == user_id:
                    phone = row[1]
                    username = row[2]
                    first_name = row[3]
                    last_name = row[4]
                    found1 = True
                    break

        if found1:
            id_results = f"""
[+] База 10
├ Номер телефона: {phone if phone else 'не найден'}
├ Никнейм: {username if username else 'не найден'}
├ Имя: {first_name if first_name else 'не найден'}
└ Фамилия: {last_name if last_name else 'не найден'}
                """

            Write.Print(id_results, Colors.cyan, interval=0.00005)

        else:
            Write.Print('[!] Пользователя в базе 10 нету\n', Colors.red, interval=0.00005)

        with open('useridbase/EYEOFGOD_11.csv', mode='r', encoding='utf-8') as file:
            reader = csv.reader(file, delimiter=',')
            for row in reader:
                if row[0] == user_id:
                    phone = row[1]
                    username = row[2]
                    first_name = row[3]
                    last_name = row[4]
                    found1 = True
                    break

        if found1:
            id_results = f"""
[+] База 11
├ Номер телефона: {phone if phone else 'не найден'}
├ Никнейм: {username if username else 'не найден'}
├ Имя: {first_name if first_name else 'не найден'}
└ Фамилия: {last_name if last_name else 'не найден'}
                """

            Write.Print(id_results, Colors.cyan, interval=0.00005)

        else:
            Write.Print('[!] Пользователя в базе 11 нету\n', Colors.red, interval=0.00005)

        with open('useridbase/EYEOFGOD_12.csv', mode='r', encoding='utf-8') as file:
            reader = csv.reader(file, delimiter=',')
            for row in reader:
                if row[0] == user_id:
                    phone = row[1]
                    username = row[2]
                    first_name = row[3]
                    last_name = row[4]
                    found1 = True
                    break

        if found1:
            id_results = f"""
[+] База 12
├ Номер телефона: {phone if phone else 'не найден'}
├ Никнейм: {username if username else 'не найден'}
├ Имя: {first_name if first_name else 'не найден'}
└ Фамилия: {last_name if last_name else 'не найден'}
                """

            Write.Print(id_results, Colors.cyan, interval=0.00005)

        else:
            Write.Print('[!] Пользователя в базе 12 нету\n', Colors.red, interval=0.00005)

        with open('useridbase/EYEOFGOD_13.csv', mode='r', encoding='utf-8') as file:
            reader = csv.reader(file, delimiter=',')
            for row in reader:
                if row[0] == user_id:
                    phone = row[1]
                    username = row[2]
                    first_name = row[3]
                    last_name = row[4]
                    found1 = True
                    break

        if found1:
            id_results = f"""
[+] База 13
├ Номер телефона: {phone if phone else 'не найден'}
├ Никнейм: {username if username else 'не найден'}
├ Имя: {first_name if first_name else 'не найден'}
└ Фамилия: {last_name if last_name else 'не найден'}
                """

            Write.Print(id_results, Colors.cyan, interval=0.00005)

        else:
            Write.Print('[!] Пользователя в базе 13 нету\n', Colors.red, interval=0.00005)

        with open('useridbase/EYEOFGOD_14.csv', mode='r', encoding='utf-8') as file:
            reader = csv.reader(file, delimiter=',')
            for row in reader:
                if row[0] == user_id:
                    phone = row[1]
                    username = row[2]
                    first_name = row[3]
                    last_name = row[4]
                    found1 = True
                    break

        if found1:
            id_results = f"""
[+] База 14
├ Номер телефона: {phone if phone else 'не найден'}
├ Никнейм: {username if username else 'не найден'}
├ Имя: {first_name if first_name else 'не найден'}
└ Фамилия: {last_name if last_name else 'не найден'}
                """

            Write.Print(id_results, Colors.cyan, interval=0.00005)

        else:
            Write.Print('[!] Пользователя в базе 14 нету\n', Colors.red, interval=0.00005)

        with open('useridbase/EYEOFGOD_15.csv', mode='r', encoding='utf-8') as file:
            reader = csv.reader(file, delimiter=',')
            for row in reader:
                if row[0] == user_id:
                    phone = row[1]
                    username = row[2]
                    first_name = row[3]
                    last_name = row[4]
                    found1 = True
                    break

        if found1:
            id_results = f"""
[+] База 15
├ Номер телефона: {phone if phone else 'не найден'}
├ Никнейм: {username if username else 'не найден'}
├ Имя: {first_name if first_name else 'не найден'}
└ Фамилия: {last_name if last_name else 'не найден'}
                """

            Write.Print(id_results, Colors.cyan, interval=0.00005)

        else:
            Write.Print('[!] Пользователя в базе 15 нету\n', Colors.red, interval=0.00005)

        with open('useridbase/EYEOFGOD_16.csv', mode='r', encoding='utf-8') as file:
            reader = csv.reader(file, delimiter=',')
            for row in reader:
                if row[0] == user_id:
                    phone = row[1]
                    username = row[2]
                    first_name = row[3]
                    last_name = row[4]
                    found1 = True
                    break

        if found1:
            id_results = f"""
[+] База 16
├ Номер телефона: {phone if phone else 'не найден'}
├ Никнейм: {username if username else 'не найден'}
├ Имя: {first_name if first_name else 'не найден'}
└ Фамилия: {last_name if last_name else 'не найден'}
                """

            Write.Print(id_results, Colors.cyan, interval=0.00005)

        else:
            Write.Print('[!] Пользователя в базе 16 нету\n', Colors.red, interval=0.00005)

        with open('useridbase/EYEOFGOD_17.csv', mode='r', encoding='utf-8') as file:
            reader = csv.reader(file, delimiter=',')
            for row in reader:
                if row[0] == user_id:
                    phone = row[1]
                    username = row[2]
                    first_name = row[3]
                    last_name = row[4]
                    found1 = True
                    break

        if found1:
            id_results = f"""
[+] База 17
├ Номер телефона: {phone if phone else 'не найден'}
├ Никнейм: {username if username else 'не найден'}
├ Имя: {first_name if first_name else 'не найден'}
└ Фамилия: {last_name if last_name else 'не найден'}
                """

            Write.Print(id_results, Colors.cyan, interval=0.00005)

        else:
            Write.Print('[!] Пользователя в базе 18 нету\n', Colors.red, interval=0.00005)

        with open('useridbase/EYEOFGOD_18.csv', mode='r', encoding='utf-8') as file:
            reader = csv.reader(file, delimiter=',')
            for row in reader:
                if row[0] == user_id:
                    phone = row[1]
                    username = row[2]
                    first_name = row[3]
                    last_name = row[4]
                    found1 = True
                    break

        if found1:
            id_results = f"""
[+] База 18
├ Номер телефона: {phone if phone else 'не найден'}
├ Никнейм: {username if username else 'не найден'}
├ Имя: {first_name if first_name else 'не найден'}
└ Фамилия: {last_name if last_name else 'не найден'}
                """

            Write.Print(id_results, Colors.cyan, interval=0.00005)

        else:
            Write.Print('[!] Пользователя в базе 18 нету\n', Colors.red, interval=0.00005)

        with open('useridbase/EYEOFGOD_19.csv', mode='r', encoding='utf-8') as file:
            reader = csv.reader(file, delimiter=',')
            for row in reader:
                if row[0] == user_id:
                    phone = row[1]
                    username = row[2]
                    first_name = row[3]
                    last_name = row[4]
                    found1 = True
                    break

        if found1:
            id_results = f"""
[+] База 19
├ Номер телефона: {phone if phone else 'не найден'}
├ Никнейм: {username if username else 'не найден'}
├ Имя: {first_name if first_name else 'не найден'}
└ Фамилия: {last_name if last_name else 'не найден'}
                """

            Write.Print(id_results, Colors.cyan, interval=0.00005)

        else:
            Write.Print('[!] Пользователя в базе 19 нету\n', Colors.red, interval=0.00005)

        with open('useridbase/EYEOFGOD_20.csv', mode='r', encoding='utf-8') as file:
            reader = csv.reader(file, delimiter=',')
            for row in reader:
                if row[0] == user_id:
                    phone = row[1]
                    username = row[2]
                    first_name = row[3]
                    last_name = row[4]
                    found1 = True
                    break

        if found1:
            id_results = f"""
[+] База 20
├ Номер телефона: {phone if phone else 'не найден'}
├ Никнейм: {username if username else 'не найден'}
├ Имя: {first_name if first_name else 'не найден'}
└ Фамилия: {last_name if last_name else 'не найден'}
                """

            Write.Print(id_results, Colors.cyan, interval=0.00005)

        else:
            Write.Print('[!] Пользователя в базе 20 нету\n', Colors.red, interval=0.00005)

        with open('useridbase/EYEOFGOD_21.csv', mode='r', encoding='utf-8') as file:
            reader = csv.reader(file, delimiter=',')
            for row in reader:
                if row[0] == user_id:
                    phone = row[1]
                    username = row[2]
                    first_name = row[3]
                    last_name = row[4]
                    found1 = True
                    break

        if found1:
            id_results = f"""
[+] База 21
├ Номер телефона: {phone if phone else 'не найден'}
├ Никнейм: {username if username else 'не найден'}
├ Имя: {first_name if first_name else 'не найден'}
└ Фамилия: {last_name if last_name else 'не найден'}
                """

            Write.Print(id_results, Colors.cyan, interval=0.00005)

        else:
            Write.Print('[!] Пользователя в базе 21 нету\n', Colors.red, interval=0.00005)

        with open('useridbase/EYEOFGOD_22.csv', mode='r', encoding='utf-8') as file:
            reader = csv.reader(file, delimiter=',')
            for row in reader:
                if row[0] == user_id:
                    phone = row[1]
                    username = row[2]
                    first_name = row[3]
                    last_name = row[4]
                    found1 = True
                    break

        if found1:
            id_results = f"""
[+] База 22
├ Номер телефона: {phone if phone else 'не найден'}
├ Никнейм: {username if username else 'не найден'}
├ Имя: {first_name if first_name else 'не найден'}
└ Фамилия: {last_name if last_name else 'не найден'}
                """

            Write.Print(id_results, Colors.cyan, interval=0.00005)

        else:
            Write.Print('[!] Пользователя в базе 22 нету\n', Colors.red, interval=0.00005)

        with open('useridbase/EYEOFGOD_23.csv', mode='r', encoding='utf-8') as file:
            reader = csv.reader(file, delimiter=',')
            for row in reader:
                if row[0] == user_id:
                    phone = row[1]
                    username = row[2]
                    first_name = row[3]
                    last_name = row[4]
                    found1 = True
                    break

        if found1:
            id_results = f"""
[+] База 23
├ Номер телефона: {phone if phone else 'не найден'}
├ Никнейм: {username if username else 'не найден'}
├ Имя: {first_name if first_name else 'не найден'}
└ Фамилия: {last_name if last_name else 'не найден'}
                """

            Write.Print(id_results, Colors.cyan, interval=0.00005)

        else:
            Write.Print('[!] Пользователя в базе 23 нету\n', Colors.red, interval=0.00005)

        with open('useridbase/EYEOFGOD_24.csv', mode='r', encoding='utf-8') as file:
            reader = csv.reader(file, delimiter=',')
            for row in reader:
                if row[0] == user_id:
                    phone = row[1]
                    username = row[2]
                    first_name = row[3]
                    last_name = row[4]
                    found1 = True
                    break

        if found1:
            id_results = f"""
[+] База 24
├ Номер телефона: {phone if phone else 'не найден'}
├ Никнейм: {username if username else 'не найден'}
├ Имя: {first_name if first_name else 'не найден'}
└ Фамилия: {last_name if last_name else 'не найден'}
                """

            Write.Print(id_results, Colors.cyan, interval=0.00005)

        else:
            Write.Print('[!] Пользователя в базе 24 нету\n', Colors.red, interval=0.00005)

        with open('useridbase/EYEOFGOD_25.csv', mode='r', encoding='utf-8') as file:
            reader = csv.reader(file, delimiter=',')
            for row in reader:
                if row[0] == user_id:
                    phone = row[1]
                    username = row[2]
                    first_name = row[3]
                    last_name = row[4]
                    found1 = True
                    break

        if found1:
            id_results = f"""
[+] База 25
├ Номер телефона: {phone if phone else 'не найден'}
├ Никнейм: {username if username else 'не найден'}
├ Имя: {first_name if first_name else 'не найден'}
└ Фамилия: {last_name if last_name else 'не найден'}
                """

            Write.Print(id_results, Colors.cyan, interval=0.00005)

        else:
            Write.Print('[!] Пользователя в базе 25 нету\n', Colors.red, interval=0.00005)

        with open('useridbase/EYEOFGOD_26.csv', mode='r', encoding='utf-8') as file:
            reader = csv.reader(file, delimiter=',')
            for row in reader:
                if row[0] == user_id:
                    phone = row[1]
                    username = row[2]
                    first_name = row[3]
                    last_name = row[4]
                    found1 = True
                    break

        if found1:
            id_results = f"""
[+] База 26
├ Номер телефона: {phone if phone else 'не найден'}
├ Никнейм: {username if username else 'не найден'}
├ Имя: {first_name if first_name else 'не найден'}
└ Фамилия: {last_name if last_name else 'не найден'}
                """

            Write.Print(id_results, Colors.cyan, interval=0.00005)

        else:
            Write.Print('[!] Пользователя в базе 26 нету\n', Colors.red, interval=0.00005)

        with open('useridbase/EYEOFGOD_27.csv', mode='r', encoding='utf-8') as file:
            reader = csv.reader(file, delimiter=',')
            for row in reader:
                if row[0] == user_id:
                    phone = row[1]
                    username = row[2]
                    first_name = row[3]
                    last_name = row[4]
                    found1 = True
                    break

        if found1:
            id_results = f"""
[+] База 27
├ Номер телефона: {phone if phone else 'не найден'}
├ Никнейм: {username if username else 'не найден'}
├ Имя: {first_name if first_name else 'не найден'}
└ Фамилия: {last_name if last_name else 'не найден'}
                """

            Write.Print(id_results, Colors.cyan, interval=0.00005)

        else:
            Write.Print('[!] Пользователя в базе 27 нету\n', Colors.red, interval=0.00005)

        with open('useridbase/EYEOFGOD_28.csv', mode='r', encoding='utf-8') as file:
            reader = csv.reader(file, delimiter=',')
            for row in reader:
                if row[0] == user_id:
                    phone = row[1]
                    username = row[2]
                    first_name = row[3]
                    last_name = row[4]
                    found1 = True
                    break

        if found1:
            id_results = f"""
[+] База 28
├ Номер телефона: {phone if phone else 'не найден'}
├ Никнейм: {username if username else 'не найден'}
├ Имя: {first_name if first_name else 'не найден'}
└ Фамилия: {last_name if last_name else 'не найден'}
                """

            Write.Print(id_results, Colors.cyan, interval=0.00005)

        else:
            Write.Print('[!] Пользователя в базе 28 нету\n', Colors.red, interval=0.00005)

        with open('useridbase/EYEOFGOD_29.csv', mode='r', encoding='utf-8') as file:
            reader = csv.reader(file, delimiter=',')
            for row in reader:
                if row[0] == user_id:
                    phone = row[1]
                    username = row[2]
                    first_name = row[3]
                    last_name = row[4]
                    found1 = True
                    break

        if found1:
            id_results = f"""
[+] База 29
├ Номер телефона: {phone if phone else 'не найден'}
├ Никнейм: {username if username else 'не найден'}
├ Имя: {first_name if first_name else 'не найден'}
└ Фамилия: {last_name if last_name else 'не найден'}
                """

            Write.Print(id_results, Colors.cyan, interval=0.00005)

        else:
            Write.Print('[!] Пользователя в базе 29 нету\n', Colors.red, interval=0.00005)

        with open('useridbase/EYEOFGOD_30.csv', mode='r', encoding='utf-8') as file:
            reader = csv.reader(file, delimiter=',')
            for row in reader:
                if row[0] == user_id:
                    phone = row[1]
                    username = row[2]
                    first_name = row[3]
                    last_name = row[4]
                    found1 = True
                    break

        if found1:
            id_results = f"""
[+] База 30
├ Номер телефона: {phone if phone else 'не найден'}
├ Никнейм: {username if username else 'не найден'}
├ Имя: {first_name if first_name else 'не найден'}
└ Фамилия: {last_name if last_name else 'не найден'}
                """

            Write.Print(id_results, Colors.cyan, interval=0.00005)

        else:
            Write.Print('[!] Пользователя в базе 30 нету\n', Colors.red, interval=0.00005)

        with open('useridbase/EYEOFGOD_31.csv', mode='r', encoding='utf-8') as file:
            reader = csv.reader(file, delimiter=',')
            for row in reader:
                if row[0] == user_id:
                    phone = row[1]
                    username = row[2]
                    first_name = row[3]
                    last_name = row[4]
                    found1 = True
                    break

        if found1:
            id_results = f"""
[+] База 31
├ Номер телефона: {phone if phone else 'не найден'}
├ Никнейм: {username if username else 'не найден'}
├ Имя: {first_name if first_name else 'не найден'}
└ Фамилия: {last_name if last_name else 'не найден'}
                """

            Write.Print(id_results, Colors.cyan, interval=0.00005)

        else:
            Write.Print('[!] Пользователя в базе 31 нету\n', Colors.red, interval=0.00005)

        with open('useridbase/EYEOFGOD_32.csv', mode='r', encoding='utf-8') as file:
            reader = csv.reader(file, delimiter=',')
            for row in reader:
                if row[0] == user_id:
                    phone = row[1]
                    username = row[2]
                    first_name = row[3]
                    last_name = row[4]
                    found1 = True
                    break

        if found1:
            id_results = f"""
[+] База 32
├ Номер телефона: {phone if phone else 'не найден'}
├ Никнейм: {username if username else 'не найден'}
├ Имя: {first_name if first_name else 'не найден'}
└ Фамилия: {last_name if last_name else 'не найден'}
                """

            Write.Print(id_results, Colors.cyan, interval=0.00005)

        else:
            Write.Print('[!] Пользователя в базе 32 нету\n', Colors.red, interval=0.00005)


    except Exception as e:
        Write.Print(f'[!] Ошибка {str(e)}', Colors.red, interval=0.00005)


    except Exception as e:
        Write.Print(f'[!] Ошибка {str(e)}', Colors.red, interval=0.00005)


def generator():
    generator = {
        'Имя': faker.first_name(),
        'Фамилия': faker.last_name(),
        'Никнейм': faker.user_name(),
        'Дата рождении': faker.date_of_birth(),
        'Почта': faker.email(),
        'Работа': faker.job(),
        'Компания': faker.company(),
        'Банковская карта': faker.credit_card_number(),
        'Номер телефона': faker.phone_number(),
        'Адрес': faker.address(),
        'Ipv4': faker.ipv4(),
        'Ipv6': faker.ipv6(),
        'Mac адрес': faker.mac_address(),
        'SSN': faker.ssn(),
        'Номер паспорта': faker.passport_number(),
        'url': faker.url(),
    }

    for key,value in generator.items():
        Write.Print(f'├ {key}: {value}\n', Colors.cyan, interval=0.00005)

def telegram_killer_menu():
    killer_menu = """
[1] Сносер 1
    """

    Write.Print(f'{killer_menu}\n', Colors.cyan, interval=0.00005)
    user_choice = Write.Input('[?] Выбор >>> ', Colors.cyan, interval=0.00005)

    if user_choice == '1':
        clear_screen()
        Write.Print("[1] Снос аккаунтов\n", Colors.cyan, interval=0.00005)
        Write.Print("[2] Снос каналов\n", Colors.cyan, interval=0.00005)
        Write.Print("[3] Снос ботов\n", Colors.cyan, interval=0.00005)
        user_choice = Write.Input('[?] Выбор >>> ', Colors.cyan, interval=0.00005)
        return user_choice

def send_email(receiver, sender_email , sender_password, subject, body):
    try:
        msg = MIMEMultipart()
        msg['From'] = send_email
        msg['To'] = receiver
        msg.attach(MIMEText(body, 'plain'))
        server = smtplib.SMTP('smtp.mail.ru', 587)
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, receiver, msg.as_string())
        time.sleep(3)
        server.quit()
        return True
    except Exception as e:
        return False

def telegram_killer():
    sent_emails = 0  
    user_choice = telegram_killer_menu()
    if user_choice == '1':
        clear_screen()
        Write.Print("[1] Спам\n", Colors.cyan, interval=0.00005)
        Write.Print("[2] Доксинг\n", Colors.cyan, interval=0.00005)
        Write.Print("[3] Троллинг\n", Colors.cyan, interval=0.00005)
        Write.Print("[4] Снос сессии\n", Colors.cyan, interval=0.00005)
        Write.Print("[5] С премкой\n", Colors.cyan, interval=0.00005)
        Write.Print("[6] С вирт номером\n", Colors.cyan, interval=0.00005)
        comp_choice = Write.Input('[?] Выбор >>> ', Colors.cyan, interval=0.00005)
        if comp_choice in ["1", "2", "3"]:
            clear_screen()
            Write.Print("[?] Введите данные для сноса\n", Colors.cyan, interval=0.00005)
            username = Write.Input('[?] Введите @username >>> ', Colors.cyan, interval=0.00005)
            user_id = Write.Input('[?] Введите ID >>> ', Colors.cyan, interval=0.00005)
            chat_link = Write.Input('[?] Введите ссылку чата >>> ', Colors.cyan, interval=0.00005)
            violation_link = Write.Input('[?] Введите ссылку на нарушение >>> ', Colors.cyan, interval=0.00005)
            comp_texts = {
                "1": f"Здравствуйте, уважаемая поддержка. На вашей платформе я нашел пользователя который отправляет много ненужных сообщений - СПАМ. Его юзернейм - {username}, его айди - {user_id}, ссылка на чат - {chat_link}, ссылка на нарушения - {violation_link}. Пожалуйста примите меры по отношению к данному пользователю.",
                "2": f"Здравствуйте, уважаемая поддержка, на вашей платформе я нашел пользователя, который распространяет чужие данные без их согласия. его юзернейм - {username}, его айди - {user_id}, ссылка на чат - {chat_link}, ссылка на нарушение/нарушения - {violation_link}. Пожалуйста примите меры по отношению к данному пользователю путем блокировки его акккаунта.",
                "3": f"Здравствуйте, уважаемая поддержка телеграм. Я нашел пользователя который открыто выражается нецензурной лексикой и спамит в чатах. его юзернейм - {username}, его айди - {user_id}, ссылка на чат - {chat_link}, ссылка на нарушение/нарушения - {violation_link}. Пожалуйста примите меры по отношению к данному пользователю путем блокировки его акккаунта."
            }
            for sender_email, sender_password in senders.items():
                for receiver in receivers:
                    comp_text = comp_texts[comp_choice]
                    comp_body = comp_text.format(username=username.strip(), user_id=user_id.strip(), chat_link=chat_link.strip(),
                                                     violation_link=violation_link.strip())
                    send_email(receiver, sender_email, sender_password, 'Жалоба на аккаунт телеграм', comp_body)
                    Write.Print(f"Отправлено на {receiver} от {sender_email}!\n", Colors.cyan, interval=0.00005)
                    sent_emails += 14888
                    time.sleep(5)

        elif comp_choice == "4":
            Write.Print("[?] Введите данные для сноса\n", Colors.cyan, interval=0.00005)
            username = Write.Input('[?] Введите @username >>> ', Colors.cyan, interval=0.00005)
            user_id = Write.Input('[?] Введите ID >>> ', Colors.cyan, interval=0.00005)
            comp_texts = {
                "4": f"Здравствуйте, уважаемая поддержка. Я случайно перешел по фишинговой ссылке и утерял доступ к своему аккаунту. Его юзернейм - {username}, его айди - {id}. Пожалуйста удалите аккаунт или обнулите сессии"
            }
            for sender_email, sender_password in senders.items():
                for receiver in receivers:
                    comp_text = comp_texts[comp_choice]
                    comp_body = comp_text.format(username=username.strip(), user_id=user_id.strip())
                    send_email(receiver, sender_email, sender_password, 'Я утерял свой аккаунт в телеграм', comp_body)
                    Write.Print(f"Отправлено на {receiver} от {sender_email}!\n", Colors.cyan, interval=0.00005)
                    sent_emails += 14888
                    time.sleep(5)

        elif comp_choice in ["5", "6"]:
            Write.Print("[?] Введите данные для сноса\n", Colors.cyan, interval=0.00005)
            username = Write.Input('[?] Введите @username >>> ', Colors.cyan, interval=0.00005)
            user_id = Write.Input('[?] Введите ID >>> ', Colors.cyan, interval=0.00005)
            comp_texts = {
                "5": f"Добрый день поддержка Telegram!Аккаунт {username} , {user_id} использует виртуальный номер купленный на сайте по активации номеров. Отношения к номеру он не имеет, номер никак к нему не относиться.Прошу разберитесь с этим. Заранее спасибо!",
                "6": f"Добрый день поддержка Telegram! Аккаунт {username} {user_id} приобрёл премиум в вашем мессенджере чтобы рассылать спам-сообщения и обходить ограничения Telegram.Прошу проверить данную жалобу и принять меры!"
            }

            for sender_email, sender_password in senders.items():
                for receiver in receivers:
                    comp_text = comp_texts[comp_choice]
                    comp_body = comp_text.format(username=username.strip(), user_id=user_id.strip())
                    send_email(receiver, sender_email, sender_password, 'Жалоба на пользователя телеграм', comp_body)
                    Write.Print(f"Отправлено на {receiver} от {sender_email}!\n", Colors.cyan, interval=0.00005)
                    sent_emails += 9999
                    time.sleep(5)

    elif choice == "2":
        
        Write.Print("[1] C личными данными \n", Colors.cyan, interval=0.00005)
        Write.Print("[2] C живодерством \n", Colors.cyan, interval=0.00005)
        Write.Print("[3] C детским порно\n", Colors.cyan, interval=0.00005)
        Write.Print("[4] Для каналов типо прайсов \n", Colors.cyan, interval=0.00005)
        ch_choice = Write.Input("[?] Выбор >>> ", Colors.cyan, interval=0.00005)

        if ch_choice in ["1", "2", "3", "4"]:
            channel_link = Write.Input('[?] Введите ссылку канала >>> ', Colors.cyan, interval=0.00005)
            channel_violation = Write.Input('[?] Введите ссылку на нарушение >>> ', Colors.cyan, interval=0.00005)
            print("погоди чуть чуть.")
            comp_texts = {
                "1": f"Здравствуйте, уважаемая поддержка телеграм. На вашей платформе я нашел канал, который распространяет личные данные невинных людей. Ссылка на канал - {channel_link}, сслыки на нарушения - {channel_violation}. Пожалуйста заблокируйте данный канал.",
                "2": f"Здравствуйте, уважаемая поддержка телеграма. На вашей платформе я нашел канал который распространяет жестокое обращение с животными. Ссылка на канал - {channel_link}, сслыки на нарушения - {channel_violation}. Пожалуйста заблокируйте данный канал.",
                "3": f"Здравствуйте, уважаемая поддержка телеграма. На вашей платформе я нашел канал который распространяет порнографию с участием несовершеннолетних. Ссылка на канал - {channel_link}, сслыки на нарушения - {channel_violation}. Пожалуйста заблокируйте данный канал.",
                "4": f"Здравствуйте,уважаемый модератор телеграмм,хочу пожаловаться вам на канал,который продает услуги доксинга, сваттинга. Ссылка на телеграмм канал:{channel_link} Ссылка на нарушение:{channel_violation} Просьба заблокировать данный канал."
            }

            for sender_email, sender_password in senders.items():
                for receiver in receivers:
                    comp_text = comp_texts[ch_choice]
                    comp_body = comp_text.format(channel_link=channel_link.strip(), channel_violation=channel_violation.strip)
                    send_email(receiver, sender_email, sender_password, 'Жалоба на телеграм канал', comp_body)
                    Write.Print(f"Отправлено на {receiver} от {sender_email}!", Colors.cyan, interval=0.00005)
                    sent_emails += 100000
                    time.sleep(5)

    elif choice == "3":
        print("1. Глаз бога (пробив бот) \n")
        bot_ch = Write.Input('[?] Выбор >>> ', Colors.cyan, interval=0.00005)

        if bot_ch == "1":
            bot_user = Write.Input('[?] Введите @username бота >>> ', Colors.cyan, interval=0.00005)
            comp_texts = {
                "1": f"Здравствуйте, уважаемая поддержка телеграм. На вашей платформе я нашел бота, который осуществляет поиск по личным данным ваших пользователей. Ссылка на бота - {bot_user}. Пожалуйста разберитесь и заблокируйте данного бота."
                       }
            for sender_email, sender_password in senders.items():
                for receiver in receivers:
                    comp_text = comp_texts[bot_ch]
                    comp_body = comp_text.format(bot_user=bot_user.strip())
                    send_email(receiver, sender_email, sender_password, 'Жалоба на бота телеграм', comp_body)
                    Write.Print(f"Отправлено на {receiver} от {sender_email}!", Colors.cyan, interval=0.00005)
                    sent_emails += 1
                    time.sleep(5)

if __name__ == '__main__':
    passw = input('Введи пароль: ')
    if passw == '57452':
        install_requirements()
        while True:
            clear_screen()
            main_menu()
            print()
            user_choice = Write.Input('[+] Выбор >>> ', Colors.cyan, interval=0.00005)
            if user_choice == '1':
                clear_screen()
                search_phone_number()
                print()
                return_menu()

            elif user_choice == '2':
                clear_screen()
                search_by_domain()
                print()
                return_menu()

            elif user_choice == '3':
                clear_screen()
                search_by_nick()
                print()
                return_menu()

            elif user_choice == '4':
                clear_screen()
                search_by_ip()
                print()
                return_menu()

            elif user_choice == '5':
                clear_screen()
                search_by_telegram_id()
                print()
                return_menu()

            elif user_choice == '7':
                clear_screen()
                generator()
                print()
                return_menu()

            elif user_choice == '9':
                clear_screen()
                telegram_killer()
                print()
                return_menu()

            elif user_choice == '0':
                Write.Print("Выход из программы...", Colors.cyan, interval=0.00005)
                break

            else:
                Write.Print("Неверный выбор. Пожалуйста, попробуйте снова.", Colors.red, interval=0.00005)

            input()