from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup

options = Options()
options.add_argument('--headless')  


driver = webdriver.Firefox()
for i in range(2,20): 
    url = f'https://www.cian.ru/cat.php?currency=2&deal_type=sale&engine_version=2&maxprice=30000000&offer_type=flat&region=1&room1=1&room2=1&room3=1&room4=1&room5=1&p={i}'

    driver.get(url)
    html = driver.page_source
    driver.quit()

    soup = BeautifulSoup(html, 'html.parser')

    elements = soup.find_all('div', class_="_93444fe79c--container--kZeLu _93444fe79c--link--DqDOy")











rec = []
import re

def parse_apartment_info(text):
    rooms_match = re.search(r'(\d+)-комн\.', text)
    rooms = int(rooms_match.group(1)) if rooms_match else None

    area_match = re.search(r'(\d+(?:[.,]\d+)?)\s*м[²2]', text)
    if area_match:
        area_str = area_match.group(1).replace(',', '.')
        area = float(area_str)
    else:
        area = None

    floor_match = re.search(r'(\d+)/(\d+)\s*этаж', text)
    if floor_match:
        current_floor = int(floor_match.group(1))
        total_floors = int(floor_match.group(2))
    else:
        current_floor = None
        total_floors = None

    return {
        'rooms': rooms,
        'area': area,
        'current_floor': current_floor,
        'total_floors': total_floors
    }


def price_str_to_int(price_str):
    clean_str = price_str.replace(' ', '').replace('₽', '').replace('\xa0', '').strip()
    return int(clean_str)


import re

def parse_metro_time(text):
    match = re.match(r'^(.*?)(\d+)\s*минут', text)
    if match:
        station_name = match.group(1).strip()
        minutes = int(match.group(2))
        return station_name, minutes
    else:
        return None, None




for element in elements:
    
    price_spans = element.find_all('div', class_='_93444fe79c--row--kEHOK')
    spans = price_spans[0].find_all(
        'span')
    spans = price_spans[0].find_all('span')

    texts = []
    for span in spans:
        text = span.text.strip()
        if text and text not in texts:
            texts.append(text)

    info = ' '.join(texts)

    info = parse_apartment_info(info)
    
    price = price_spans[3].find('span', 
        class_='_93444fe79c--color_text-primary-default--vSRPB ' \
        '_93444fe79c--lineHeight_28px--KFXmc _93444fe79c--fontWeight_bold--BbhnX _93444fe79c-'
        '-fontSize_22px--sFuaL _93444fe79c--display_block--KYb25 _93444fe79c--text--b2YS3 _93444fe79c--text_letterSpacing__normal--yhcXb')
    if price is not None:
        price = price_str_to_int(price.text)
    else:
        price = None


    subway = price_spans[2].find('div', class_='_93444fe79c--container--w7txv')

    if subway is None:
        sub_inf = ''   
    else:
        subs = subway.find_all('div')
        sub_inf = ''
        for sub in subs:
            sub_inf += sub.text   

    subway, remote = parse_metro_time(sub_inf)


    apartment_data = {
    'rooms': info['rooms'],
    'area': info['area'],
    'current_floor': info['current_floor'],
    'total_floors': info['total_floors'],
    'price': price,
    'subway': subway,
    'remote_minutes': remote
    }
    
    rec.append(apartment_data)

import pandas as pd
import os

filename = r'C:\Users\HONOR\Desktop\t-edu\Apartment_info.csv'

new_records = rec
print(f'Новых записей получено: {len(new_records)}')
df_new = pd.DataFrame(new_records)
df_new.columns = df_new.columns.str.lower()

for col in ['rooms', 'area', 'price', 'current_floor', 'total_floors', 'remote_minutes']:
    if col in df_new.columns:
        df_new[col] = pd.to_numeric(df_new[col], errors='coerce')

if os.path.exists(filename):
    df_existing = pd.read_csv(filename)
    if 'unnamed: 0' in df_existing.columns:
        df_existing = df_existing.drop(columns=['unnamed: 0'])
    df_existing.columns = df_existing.columns.str.lower()
    for col in ['rooms', 'area', 'price', 'current_floor', 'total_floors', 'remote_minutes']:
        if col in df_existing.columns:
            df_existing[col] = pd.to_numeric(df_existing[col], errors='coerce')
else:
    df_existing = pd.DataFrame(columns=df_new.columns)


df_combined = pd.concat([df_existing, df_new], ignore_index=True)

key_columns = ['rooms', 'area', 'price', 'subway', 'current_floor', 'total_floors', 'remote_minutes']
key_columns = [col for col in key_columns if col in df_combined.columns]

df_combined = df_combined.drop_duplicates(subset=key_columns, keep='first')
print(f'Всего записей после удаления дубликатов: {len(df_combined)}')

df_combined.to_csv(filename, index=False)
print(f'Данные сохранены в файл: {filename}')

