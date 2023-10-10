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


soup_main = BeautifulSoup(site, "lxml")

all_rev = soup_main.find_all(class_="review-btn review-read-link")
for rev in all_rev:
    rev_href = "https://otzovik.com" + rev.get("href")
    print (rev_href)
    rev_req = requests.get(rev_href, headers=header).text
    soup_rev = BeautifulSoup(rev_req, "lxml")
    rev_main = soup_rev.find(class_="review-body description").text
    rev_rat = soup_rev.find(class_="rating").text
    print(rev_main)
    print(rev_rat)
    
    




    

