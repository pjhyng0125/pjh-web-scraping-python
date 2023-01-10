import requests
import re
from bs4 import BeautifulSoup

headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36", "Accept-Language": "ko-KR,ko;q=0.8,en-US;q=0.5,en;q=0.3"}

# 1~6 페이지 웹 스크래핑
for i in range(1, 6):
    # print("페이지 : ", i)
    url = "https://www.coupang.com/np/search?q=%EB%85%B8%ED%8A%B8%EB%B6%81&channel=user&component=&eventCategory=SRP&trcid=&traid=&sorter=scoreDesc&minPrice=&maxPrice=&priceRange=&filterType=&listSize=36&filter=&isPriceRange=false&brand=&offerCondition=&rating=0&page={}&rocketAll=false&searchIndexingToken=&backgroundColor=".format(i)


    def emptyCheck(value, emptyStr):
        if value:
            return value.get_text()
        else:
            emptyStr

    # url = "https://www.coupang.com/np/search?component=&q=%EB%85%B8%ED%8A%B8%EB%B6%81&channel=user"
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
            # print("  <광고 상품 제외합니다>")
            continue

        name = item.find("div", attrs={"class":"name"}).get_text() # 제품명

        # Apple 상품 제외
        # if "Apple" in name:
            # print("  <Apple 상품 제외합니다>")

        # 한정 상품 제외
        # if "한정" in name:
            # print("  <한정 상품 제외합니다>")
        
        price = item.find("strong", attrs={"class":"price-value"}) # 가격
        priceTxt = emptyCheck(price, "가격 없음") # 가격 예외처리

        rate = item.find("em", attrs={"class":"rating"}) # 평점
        rateTxt = emptyCheck(rate, "평점 없음") # 평점 예외처리

        rateCnt = item.find("span", attrs={"class":"rating-total-count"}) # 평점수
        rateCntTxt = emptyCheck(rateCnt, "평점수 없음") # 평점수 예외처리

        link = item.find("a", attrs={"class":"search-product-link"})["href"]

        # if float(rate) >= 4.5 and int(rateCnt) >= 100:
        print(f"제품명 : {name}")
        print(f"가격 : {priceTxt}")
        print(f"평점 : {rateTxt}점 {rateCntTxt}개")
        print("바로가기 : {}".format("https://www.coupang.com" + link))
        print("-"*100)


