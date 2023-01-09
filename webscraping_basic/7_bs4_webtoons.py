import requests
from bs4 import BeautifulSoup

res = requests.get("https://comic.naver.com/webtoon/weekday")
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")

# 네이버 웹툰 전체 목록 가져오기
cartoons = soup.find_all("a", attrs={"class": "title"}) # list 반환

# class 속성이 title인 모든 a element 출
for cartoon in cartoons:
    print(cartoon.get_text())