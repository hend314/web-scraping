import requests
import csv
from bs4 import BeautifulSoup
from itertools import zip_longest

job_title = []
company = []
date = []
link =[]

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"
}

url = "https://remoteok.com/remote-engineer-jobs"
response = requests.get(url, headers=headers)

soup = BeautifulSoup(response.content, "lxml")

job_titles = soup.find_all("h2", {"itemprop" : "title"})
company_name = soup.find_all('h3' , {"itemprop" : "name"})
dates = soup.find_all("td",{"class" : "time"})
links = soup.find_all("a", itemprop="url", class_= "preventLink")

for i in range(len(job_titles)):

    job_title.append(job_titles[i].text.strip())

    company.append(company_name[i].text.strip())

    date.append(dates[i+1].text.strip())

    job_url = "https://remoteok.com"+links[i].get('href')
    link.append(job_url)

file_list = [job_title, company , date, link]

file_values = zip_longest(*file_list)

with open(r"F:\web-scraping-project\jobs.csv" , "w" , newline='') as file:
    wr = csv.writer(file)
    wr.writerow(['job_title', 'company', 'date', 'link' ])
    wr.writerows(file_values)
