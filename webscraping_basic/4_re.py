# 정규식
# 주민등록번호
# 940125-1111111

# 이메일주소
# jinbro@gmail.com

# 차량 번호
# 11가 1234
# 123가 1234

# IP 주소
# 192.0.0.1

# . : 하나의 문자
# ^ : 문자열의 시작 ex) ^de : de 로 시작하는 것!
# $ : 문자열의 끝 ex) se$ : se로 끝나는 것!

import re
p = re.compile("ca.e") # 원하는 형태로 컴파일

def print_match(m):
    if m :
        print("m.group() : ", m.group()) # 일치하는 문자열 반환
        print("m.string : ", m.string) # 입력받은 문자열
        print("m.start() : ", m.start()) # 일치하는 문자열의 시작 index
        print("m.end() : ", m.end()) # 일치하는 문자열의 끝 index
        print("m.span() : ", m.span()) # 일치하는 문자열의 시작 / 끝 index
    else: # 정규식 부적합 시 Error 발생!
        print("매칭실패")

# m = p.match("careless") # match : 주어진 문자열의 처음부터 일치하는지 확인
# m = p.search("good care") # search : 주어진 문자열 중 일치하는게 있는지 확인
# print_match(m)

lst = p.findall("good care cafe cade") # findall : 일치하는 모든 것을 리스트 형태로 반환
print(lst)

# 참고 레퍼런스
# 1. w3schools> Python RegEx
# 2. pytyon re