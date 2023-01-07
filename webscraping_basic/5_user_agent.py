# web browser 가 접속 기기에 따른 user agent 정보로 모바일, PC 판단
# 나의 user agent 정보 확인 : https://www.whatismybrowser.com/detect/what-is-my-user-agent/
# User-Agent 는 브라우저 종류, 기기에 따라 다 다름!

import requests
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"}
url = "http://nadocoding.tistory.com"
res = requests.get(url, headers=headers)
res.raise_for_status() # 응답 비정상 시 Exception throw -> 종료!

with open("nadocoding.html", "w", encoding="utf8") as f:
    f.write(res.text)