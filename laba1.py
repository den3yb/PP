import os
import requests 
from bs4 import BeautifulSoup
from time import sleep

url = "https://otzovik.com/reviews/sberbank_rossii/"


header = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.5845.967 YaBrowser/23.9.1.967 Yowser/2.5 Safari/537.36"
}

print('hello world')
if not os.path.isdir(f"dataset"):
    os.mkdir(f"dataset")


for score in range(1,6):
    if not os.path.isdir(f"dataset/{str(score)}"):
        os.mkdir(f"dataset/{str(score)}")
    for ratio in range(1,31):
        count=1
        src = requests.get(url + str(ratio) + "/?ratio=" + str(score), headers=header).text
        soup_main = BeautifulSoup(src, "lxml")
        if "С вашего IP-адреса было много обращений к сайту Отзовик" in str(soup_main):
            print("Waiting...")
            time.sleep(3600)
        else:
            time.sleep(45)
        all_rev = soup_main.find_all(class_="review-btn review-read-link")
        for rev in all_rev:
            rev_href = "https://otzovik.com" + rev.get("href")
            print (rev_href)
            rev_req = requests.get(rev_href, headers=header).text
            soup_rev = BeautifulSoup(rev_req, "lxml")
            if "С вашего IP-адреса было много обращений к сайту Отзовик" in str(soup_rev):
                print("Waiting...")
                time.sleep(3600)
            else:
                time.sleep(45)
            rev_main = soup_rev.find(class_="review-body description").text
            print(rev_main)
            with open(f"dataset/{score}/{str(count).zfill(4)}.txt", "w", encoding="utf-8") as file:
                file.write(rev_main)
            count+=1


        
    
    




    

