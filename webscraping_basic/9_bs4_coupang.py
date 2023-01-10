import requests
import re
from bs4 import BeautifulSoup

def emptyCheck(value, emptyStr):
    if value:
        return value.get_text()
    else:
        emptyStr

url = "https://www.coupang.com/np/search?q=%EB%85%B8%ED%8A%B8%EB%B6%81&channel=user&component=&eventCategory=SRP&trcid=&traid=&sorter=scoreDesc&minPrice=&maxPrice=&priceRange=&filterType=&listSize=36&filter=&isPriceRange=false&brand=&offerCondition=&rating=0&page=1&rocketAll=false&searchIndexingToken=&backgroundColor="
# url = "https://www.coupang.com/np/search?component=&q=%EB%85%B8%ED%8A%B8%EB%B6%81&channel=user"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36", "Accept-Language": "ko-KR,ko;q=0.8,en-US;q=0.5,en;q=0.3"}
# 쿠팡의 경우 headers Accept-Language 값 추가 필수!
res = requests.get(url, headers=headers) # 여기서 pending 됨...header User-Agent 추가해도 pending 됨... Accept-Language 추가로 해결!
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")

items = soup.find_all("li", attrs={"class":re.compile("^search-product")})
print(items[0].find("div", attrs={"class":"name"}).get_text())

for item in items:
    # 광고 제품은 제외
    ad_badge = item.find("span", attr={"class":"ad-badge-text"})
    if ad_badge:
        print("  <광고 상품 제외합니다>")
        continue

    name = item.find("div", attrs={"class":"name"}).get_text() # 제품명

    # Apple 상품 제외
    if "Apple" in name:
        print("  <Apple 상품 제외합니다>")

    # 한정 상품 제외
    if "한정" in name:
        print("  <한정 상품 제외합니다>")
    
    price = item.find("strong", attrs={"class":"price-value"}) # 가격
    priceTxt = emptyCheck(price, "가격 없음") # 가격 예외처리

    rate = item.find("em", attrs={"class":"rating"}) # 평점
    rateTxt = emptyCheck(rate, "평점 없음") # 평점 예외처리

    rateCnt = item.find("span", attrs={"class":"rating-total-count"}) # 평점수
    rateCntTxt = emptyCheck(rateCnt, "평점수 없음") # 평점수 예외처리

    print(name, priceTxt, rateTxt, rateCntTxt)


