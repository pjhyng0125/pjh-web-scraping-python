import requests
# res = requests.get("http://naver.com")
# url = "http://nadocoding.tistory.com"
# url = "https://velog.io/@pjhyng0125"
url = "http://google.com"
res = requests.get(url)

print("url : ", url)
print("result : ", res.status_code) # 200 일 경우 정상!

if res.status_code == requests.codes.ok:
    print("정상입니다")
else:
    print("문제가 생겼습니다. [에러코드 ", res.status_code, "]")

res.raise_for_status() # 응답 비정상 시 Exception throw -> 종료!
print("웹 스크래핑을 진행합니다")

print(len(res.text))
# print(res.text)

with open("myGoogle.html", "w", encoding="utf8") as f:
    f.write(res.text)