from bs4 import BeautifulSoup
import requests

from func import *

url = "https://otzovik.com/reviews/sberbank_rossii/"

header = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.5845.967 YaBrowser/23.9.1.967 Yowser/2.5 Safari/537.36",
}



def main() -> None:
    for score in range(2, 6):
        count = 1
        create_score(score)
        for ratio in range(1, 32):
                url_temp = url + str(ratio) + "/?ratio=" + str(score)
                src = requests.get(url_temp, headers=header).text
                chek(src)
                soup_main = BeautifulSoup(src, "lxml")
                all_rev = soup_main.find_all(class_="review-btn review-read-link")
                for rev in all_rev:
                    rev_href = "https://otzovik.com" + rev.get("href")
                    rev_req = requests.get(rev_href, headers=header).text
                    chek(rev_req)
                    soup_rev = BeautifulSoup(rev_req, "lxml")
                    rev_main = soup_rev.find(class_="review-body description").text
                    create_text(score, count, rev_main)
                    count += 1

