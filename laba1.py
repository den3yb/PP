import os
import requests 
from bs4 import BeautifulSoup;

url = "https://otzovik.com/reviews/sberbank_rossii/"

header = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.5845.967 YaBrowser/23.9.1.967 Yowser/2.5 Safari/537.36"
}

#src = requests.get(url, headers=header).text
#with open("site.html", "w", encoding='utf-8') as file:
     #file.write(src)
with open ("site.html", "r", encoding='utf-8') as file:
    site = file.read()


soup1 = BeautifulSoup(site, "lxml")

all_rev = soup1.find_all(class_="review-btn review-read-link")
for rev in all_rev:
    rev_href = "https://otzovik.com" + rev.get("href")
    print (rev_href)
    rev_req = requests.get("https://otzovik.com/review_13327608.html", headers=header).text
    soup2 = BeautifulSoup(rev_req, "lxml")
    rev_main = soup2.find(class_="review-body description")
    rev_rat = soup2.find(class_="rating")
    print(rev_main)
    print(rev_rat)
    
    




    

