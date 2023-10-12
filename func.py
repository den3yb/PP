import os
import time
from bs4 import BeautifulSoup

def create_data() -> None:
    if not os.path.isdir(f"dataset"):
        os.mkdir(f"dataset")


def create_score(_score: int) -> None:
    path = os.path.join("dataset", str(_score))
    if not os.path.isdir(str(path)):
        os.mkdir(str(path))


def create_text(_score: int, _count: int, _rev_main: str) -> None:
    path = os.path.join("dataset", str(_score), str(_count).zfill(3) + ".txt")
    with open(str(path), "w", encoding="utf-8") as file:
        file.write(_rev_main)
        print("Записан отзыв с оценкой " + str(_score) + " под номером " + str(_count))


def chek(_src: int) -> None:
    soupchek = BeautifulSoup(_src, "lxml")
    if "С Вашего IP-адреса было много обращений к сайту Отзовик." in str(soupchek):
        print("Waiting...")
        time.sleep(18000)
    else:
        time.sleep(45)
