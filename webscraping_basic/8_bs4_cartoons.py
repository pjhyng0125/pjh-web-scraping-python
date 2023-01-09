import requests
from bs4 import BeautifulSoup

res = requests.get("https://comic.naver.com/webtoon/list?titleId=641253&weekday=fri")
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")

# 웹툰 회차 제목 목록 가져오기
# cartoons = soup.find_all("td", attrs={"class": "title"}) # list 반환
# title = cartoons[0].a.get_text()
# link = cartoons[0].a["href"]

# print(title)
# print("https://comic.naver.com" + link)

# 만화 정보 가져오기
# for cartoon in cartoons:
#     title = cartoon.a.get_text()
#     link = "https://comic.naver.com" + cartoon.a["href"]
#     print(title, link)

# 평점 정보 가져오기
total_rates = 0
cartoons = soup.find_all("div", attrs={"class": "rating_type"}) # list 반환

for cartoon in cartoons:
    rate = cartoon.find("strong").get_text()
    print(rate)
    total_rates += float(rate)

print("전체 점수 : ", total_rates)
print("평균 점수 : ", total_rates / len(cartoons))