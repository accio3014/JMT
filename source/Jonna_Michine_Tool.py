# JMT - Jonna Michine Tool

# 구글 해킹 툴 제작
# 사용자가 특정 웹 사이트 주소를 입력
# 해당 주소를 기반으로 구글 검색엔진 해킹 공격 시도
# 해당 결과를 리턴

# [진행 순서]
# 1. https://www.exploit-db.com/google-hacking-database 사이트에서 구문 자동으로 가져오기
# 2. 해킹하고자 하는 웹 사이트 입력
# 3. 해당 사이트에 대한 검색 엔진 구문을 전부 실행
# 4. 실행된 결과를 크롤링하여 가지고 옴
# 5. 깔끔하게 정리

# pip3 install selenium
# pip3 install beautifulsoup
# pip3 install bs4
# pip3 install fake_useragent
# pip3 install undetected_chromedriver
# pip3 install 2captcha-python 
# pip3.8 install lxml

# https://wikidocs.net/book/4614
# 위 도서의 셀레늄을 이용하여 개발
# from urllib.parse import quote_plus
# from bs4 import BeautifulSoup
# from selenium import webdriver

from urllib.parse import quote_plus
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time
import ssl
import random
ssl._create_default_https_context = ssl._create_unverified_context

query = []


# read exploit file and setting query
def readCategory(path):
    global query

    f = open(path, 'r')

    while(True):
        line = f.readline()
        if(not(line)):
            break
        
        line = line[:-1]
        query.append(line)
        
    f.close()



def exploitGHDB(categoryPath, idx):
    
    # f = open("/Users/seokcheon/OneDrive/College/2023-1/senior-project/JMT/File-Containing-Usernames.txt", 'r')

    readCategory(categoryPath)    
    result = open("/Users/seokcheon/OneDrive/College/2023-1/senior-project/JMT-test/result.md", "a")

    baseUrl = 'https://www.google.com/search?q='

    # for plusUrl in query :
    
    # plusUrl = input('무엇을 검색할까요? :')
    url = baseUrl + quote_plus(query[idx])
    # 한글은 인터넷에서 바로 사용하는 방식이 아니라, quote_plus가 변환해줌
    # URL에 막 %CE%GD%EC 이런 거 만들어주는 친구

    caps = DesiredCapabilities.SAFARI.copy()
    caps["browserstack.safari.enablePopups"] = "true"
    caps['safari.private'] = True

    driver = webdriver.Safari()
    driver.get(url)

    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')

    r = soup.select('.tF2Cxc')

    result.write('# %s \n</br>' % query[idx])

    time.sleep(random.randint(1, 2))

    for i in r :

        try :  
            # print(i.select_one('.LC20lb.MBeuO.DKV0Md').text) #제목 #select one을 사용하면 텍스트를 가져올 수 있다. #클래스에 빈칸은 점으로 바꿔준다.
            result.write(i.select_one('.LC20lb.MBeuO.DKV0Md').text)
            result.write('</br>')
            # print(i.a.attrs['href'])
            result.write(i.a.attrs['href'])
            # print()
            result.write('</br>\n</br>\n')
            # driver.close() #크롬 드라이버 닫아주기
        except :
            # driver.close() #크롬 드라이버 닫아주기
            return query[idx], 0

        # time.sleep(random.randint(1, 5))

    result.close()

    return query[idx], 1


# exploitGHDB("/Users/seokcheon/OneDrive/College/2023-1/senior-project/JMT/File-Containing-Usernames.txt")