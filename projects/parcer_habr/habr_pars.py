import requests
from bs4 import BeautifulSoup
import pandas as pd

w = []
for i in range(1,40):
    url = 'https://career.habr.com/vacancies?page=1&type=all'

    re = requests.get(url).text

    soup =BeautifulSoup(re, 'html.parser')


    elements = soup.find_all('div', class_="vacancy-card__inner")

    for element in elements:
        date = element.find('time', class_='basic-date').text
        title =  element.find('a', class_='vacancy-card__title-link').text
        salary = element.find('div', class_='basic-salary').text
        comp = element.find('div', class_='vacancy-card__company-title').text
        comp_rating = element.find('span').text
        span_tag = element.find('div', class_='vacancy-card__skills')
        exp_req = span_tag.find_all('a', class_='link-comp link-comp--appearance-dark')[1].text

        span_tag = element.find('div', class_='vacancy-card__meta')
        remote = span_tag.find_all('span')[-1].text

        span_tag = element.find('div', class_='vacancy-card__meta')
        loc = span_tag.find('a', class_='link-comp link-comp--appearance-dark')
        if loc:
            loc = loc.text
        else:
            loc=loc
    
        w.append({
            "Дата" : date,
            "Вакансия" : title,
            "ЗП": salary,
            "Компания": comp,
            "Рейтинг компании": comp_rating,
            "Необходимый уровень": exp_req,
            "Место работы": loc,
            "Возможность удаленки": remote,
        })
    

df = pd.DataFrame(w)

df.to_csv('habr_jobs.csv', index=False)
    
    
