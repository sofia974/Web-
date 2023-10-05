from bs4 import BeautifulSoup
import requests
import pandas as pd

def scrapper(page_num):
    url = f"https://www.linkedin.com/jobs"
    headers = {'User-Agent': }
    r = requests.get(url, headers)
    soup = BeautifulSoup(r.content, 'lxml')
    return soup

def extract(soup):
    jobs = soup.find_all('div', class_='base-card relative w-full hover:no-underline focus:no-underline base-card--link base-search-card base-search-card--link job-search-card')
    for item in jobs:
        title = item.find('a').text.strip()
        company = item.find('h4').text.strip()
        link = item.a['href']
        location = item.find('span', class_='job-search-card__location').text
        job_posted = item.find('time', class_='job-search-card__listdate')

        if job_posted is not None:
            time = job_posted.text.strip()

            job = {
                'Titulo': title,
                'Link': link,
                'Compania': company,
                'Localizacion': location,
                'Fecha_publicacion_trabajo': time
            }

joblist = []

page = int(input(f'Enter the number of pages you want to scrape: '))

for i in range(page):
    print(f'Getting page, {i+1}')
    s = scrapper(i)
    extract(s)

#print(joblist)
df = pd.DataFrame(joblist)
print(df.head())
df.to_csv('Linkedin.csv')
