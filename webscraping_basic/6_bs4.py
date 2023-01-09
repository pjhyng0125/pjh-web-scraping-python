import requests
from bs4 import BeautifulSoup

res = requests.get("https://comic.naver.com/webtoon/weekday")
res.raise_for_status()

# print(res.text)

soup = BeautifulSoup(res.text, "lxml")
# print(soup.title)
# print(soup.title.get_text())
# print(soup.a) # html에서 첫 a element 가져오기
# print(soup.a.attrs) # a element의 속성 정보 반환
# print(soup.a["onclick"]) # a element의 속성 정보 반환

# print(soup.find("a", attrs={"class":"Nbtn_upload"})) # 어떤 a element를 가져올지 조건 설정 가능
# print(soup.find(attrs={"class":"Nbtn_upload"})) # element 명시 없이도 조회 가능!

# print(soup.find("li", attrs={"class":"rank01"}))
rank1 = soup.find("li", attrs={"class":"rank01"})
# print(rank1.a) # 조회한 rank1 element 내 a element 뽑아내기
# print("rank1 (before) : " + rank1.a.get_text())
# rank2 = rank1.next_sibling.next_sibling # html br 개행이 있을 경우 2번 호출 필요!
# print("rank2 : " + rank2.a.get_text())
# rank1 = rank2.previous_sibling.previous_sibling
# print("rank1 (after) : " + rank1.a.get_text())

# print(rank1.parent) # 부모 element ol 출력 확인

# rank2 = rank1.find_next_sibling("li") # 자식 element 중 li 태그 찾기
# print("rank2 : " + rank2.a.get_text())

# 자식 element "들" 한번에 찾기
# rankList = rank1.find_next_siblings("li")
# print(rankList)

webtoon = soup.find("a", text="약한영웅")
print(webtoon)