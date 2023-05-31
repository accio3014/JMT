# JMT - Jonna Michine Tool

from urllib.parse import quote_plus
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time
import ssl
import random

# Setting SSL
ssl._create_default_https_context = ssl._create_unverified_context

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

    searchResult = soup.select('.tF2Cxc')       # Result of search
    result.write('## %s \n</br>\n' % query)     # Write heading of report file (Query)

    time.sleep(random.randint(1, 2))            # Avoid bot detection

    # print(url)  # Checking

    for i in searchResult :
        try :  
            # .LC20lb.MBeuO.DKV0Md is heading
            print(i.select_one('.LC20lb.MBeuO.DKV0Md').text)            
            result.write("\n### %s \n" % i.select_one('.LC20lb.MBeuO.DKV0Md').text)
            if(len(i.select_one('.LC20lb.MBeuO.DKV0Md').text) == 0):
                return "Fail"
            
            # i.a.attrs['href'] is sub heading
            print(i.a.attrs['href'])
            result.write(i.a.attrs['href'])
            print()
            result.write('\n</br>\n')

            # return "Exploit"
        except :
            result.write('</br>\n\n')
            return "Fail"

    result.write('</br>\n\n')
    result.close()  # file close

    return "Exploit"