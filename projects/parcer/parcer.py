import requests
from bs4 import BeautifulSoup
import pandas as pd
c_books = []
for i in range(1, 51): # перебор всех 50 страниц с сайта

    url=f'https://books.toscrape.com/catalogue/page-{i}.html'

    response = requests.get(url).text # получение html страниц
    soup = BeautifulSoup(response, 'html.parser')

    books = soup.find_all('article', class_='product_pod') # Получение данных о книгах со страниц

    rating_map = { Словарь для преобразования данных о рейтинеге книги
        "One" : 1,
        "Two" : 2,
        "Three" : 3,
        "Four" : 4,
        "Five" : 5,
    }
    for book in books: # добавление информации в виде словаря о каждой книге в массив.
        title = book.h3.a['title']
        price = book.find('p', class_='price_color').text[2:]
        rating = book.p["class"][-1]
        rating = rating_map.get(rating, 0)  
        c_books.append({
            "title" : title,
            'price in Pounds' : price,
            "rating" : rating
        })


df = pd.DataFrame(c_books) # Преобразование массива в датафрейм и сохранение

df.to_csv('test_parcer.csv', index=False)
