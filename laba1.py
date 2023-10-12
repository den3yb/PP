import os
import requests 
from bs4 import BeautifulSoup
import time 
from time import sleep

url = "https://otzovik.com/reviews/sberbank_rossii/"


header = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.5845.967 YaBrowser/23.9.1.967 Yowser/2.5 Safari/537.36"
}


if not os.path.isdir(f"dataset"):
    os.mkdir(f"dataset")




for score in range(1,2):

    count=392
    if not os.path.isdir(f"dataset/{str(score)}"):
        os.mkdir(f"dataset/{str(score)}")

    for ratio in range(20,32):

        url_temp = url + str(ratio) + "/?ratio=" + str(score)
        src = requests.get( url_temp, headers=header).text
        soup_main = BeautifulSoup(src, "lxml")
        
        soup = BeautifulSoup(src, "html.parser")
        if "С Вашего IP-адреса было много обращений к сайту Отзовик." in str(soup):
            print("Waiting...")
            time.sleep(21600)
        else:
            time.sleep(45)

        all_rev = soup_main.find_all(class_="review-btn review-read-link")

        for rev in all_rev:
            rev_href = "https://otzovik.com" + rev.get("href")
            rev_req = requests.get(rev_href, headers=header).text
            soup_rev = BeautifulSoup(rev_req, "lxml")
            

            soup = BeautifulSoup(rev_req, "html.parser")
            if "С Вашего IP-адреса было много обращений к сайту Отзовик." in str(soup):
                print("Waiting...")
                time.sleep(21600)
            else:
                time.sleep(45)

            rev_main = soup_rev.find(class_="review-body description").text

            with open(f"dataset/{score}/{str(count).zfill(3)}.txt", "w", encoding="utf-8") as file:
                file.write(rev_main)
                print("Записан отзыв с оценкой " + str(score) + " под номером "  + str(count))
            count+=1


        
    
    




    

