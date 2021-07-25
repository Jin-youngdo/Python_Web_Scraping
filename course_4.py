"""
# python module
from math import ceil, fsum

print(ceil(1.2)) # 올림
print(fsum([1, 2, 3, 4, 5, 6, 7])) # 총합 
"""

"""
# 외부 모듈 불러오기
from calculator import plus as pl
from calculator import minus as mi

print(pl(2,5))
print(mi(2, 10))
"""

"""
# Assignment Weeks_4
import os
import requests

url_list = [x for x in input("Please write a URL or URLS you want to check. (separated by comma)\n").split(sep=',')]
url_list = [i.strip() for i in url_list]
http_list = ["http://"]
http_url_list = ["", "", "", ""]
index = 0
sum = 0

# http:// 붙이기
for i in url_list:
    if "http://" in i:
        http_url_list[index] = url_list[sum]
        index+=1
    elif "http://" not in i:
        http_url_list[index] = http_list[0] + url_list[sum]
        index+=1
    sum+=1

# 소문자 변환
for i in range(0, len(http_url_list)):
    http_url_list[i] = http_url_list[i].lower()

# 리스트 내 빈 원소 제거
http_url_list = ' '.join(http_url_list).split()

print("http_url_list: ", http_url_list)


# url 유효성 검사
respone = ["","","",""]

for i in range(0, len(respone)):
    respone[i]=requests.get(http_url_list[i])
    print(respone[i].status_code)
    try:
        print(f"{http_url_list[i]} is up!")
    except:
        print(f"{http_url_list[i]} is down!")
"""