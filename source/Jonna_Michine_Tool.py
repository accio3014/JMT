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
# pip3.8 install lxml

from urllib.parse import quote_plus
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time
import ssl
import random

# Setting SSL
ssl._create_default_https_context = ssl._create_unverified_context

# 지금 동작 보면 특정 위치에 result.md 파일이 있어야 그 파일에 결과를 추가하거든?
# 이걸 내가 특정 경로에 파일 저장 되게 변경해 주세요!
# -> 절대 경로로 지정되어 있으면 다른 OS에서 경로를 변경해야하므로 비율적임
# -> 상대 경로로 바꾸기

# 그리고 저장 파일이 result.md 말고 report_현재날짜및시간.md
# -> report_20230517151245

def exploitGHDB(query, search_url, result_time):
    
    # readCategory(categoryPath)

    # Save report md file
    result = open("./report_" + result_time + ".md", "a") 

    # 한글을 대비해서 quote_plus() 함수를 사용
    baseUrl = 'https://www.google.com/search?q='
    exploit_url = "site:" + search_url + " "
    url = baseUrl + quote_plus(exploit_url) + quote_plus(query)

    # Setting safari
    caps = DesiredCapabilities.SAFARI.copy()
    caps["browserstack.safari.enablePopups"] = "true"
    caps['safari.private'] = True

    # Start web crawling
    driver = webdriver.Safari()
    driver.get(url)

    # Read Web html file.
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')

    searchResult = soup.select('.tF2Cxc')           # Result of search
    result.write('## %s \n</br>' % query)           # Write heading of report file

    time.sleep(random.randint(1, 2))                # Avoid bot detection

    # print(url)  # Checking

    for i in searchResult :
        try :  
            # .LC20lb.MBeuO.DKV0Md is heading
            print(i.select_one('.LC20lb.MBeuO.DKV0Md').text)            
            result.write(i.select_one('.LC20lb.MBeuO.DKV0Md').text)
            result.write('</br>')
            
            # i.a.attrs['href'] is sub heading
            print(i.a.attrs['href'])
            result.write(i.a.attrs['href'])
            print()
            result.write('</br>\n</br>\n')

            return "Exploit"
        except :
            
            result.write('</br>\n</br>\n')
            return "Fail"

    result.write('</br>\n</br>\n')
    result.close()  # file close

    return "Fail"