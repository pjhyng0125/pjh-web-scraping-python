# 네이버> 날씨 정보 웹 스크래핑 해보기
import requests
from bs4 import BeautifulSoup

res = requests.get("https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&query=%EB%82%A0%EC%94%A8&oquery=%EA%B8%B0%EC%83%81%EC%B2%AD&tqi=hJwAzdp0YidssRp5NhRssssst%2FK-152991")
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")

# 전국 날씨 목록 find
weathers = soup.find_all("div", attrs={"class": "cell_temperature"}) # list 반환

print(len(weathers))

# class 속성이 title인 모든 a element 출
for weather in weathers:
    print(weather.span.get_text())