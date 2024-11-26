import random
import gzip
import zlib

import datetime
import winsound
import time
import requests
from bs4 import BeautifulSoup
import noah_sign

def n_url(url):
    org= 'http://ticket.yes24.com'
    n_url = org+url
    return n_url


def beep_sound():
    for _ in range(5):
        winsound.Beep(1500, 600) # Hz, duration
        time.sleep(0.2)

## no_used
# 241002
def mint(url):
    # 토요일 :1306984
    # 일요일 :1306986
    data = {
        "pIdTime": 1306984,
        "pIdCode": '',
        "pMax":10,
        "pTimeLimitChk":'ok',
        "pIdPerf": 50687,
    }
    response = requests.post(url, headers=headers, data=data)
    res = response.content
    result = res.decode('utf-8')
    return result

# 241125
def daysix(data):
    u = '/Pages/Perf/Sale/Ajax/Perf/TimeSeatRemain.aspx'
    url = n_url(u)
    # "pIdTime": 1325885, # 금요일
    # "pIdTime": 1326314, # 토요일
    response = requests.post(url, headers=headers, data=data)
    res = response.content
    result = res.decode('utf-8')
    return result


def filter_html(html):
    soup = BeautifulSoup(html, 'html.parser')
    # soup = '<li><strong>SR석</strong>154,000원 (잔여:<span class="red">2석</span>)</li><li><strong>R석</strong>143,000원 (잔여:<span class="red">1석</span>)</li><li><strong>S석</strong>132,000원 (잔여:<span class="red">0석</span>)</li>'
    result = []
    # print('soup>> \n',soup)
    for seat in soup:
        seat_type = seat.find('strong').text
        seat_count_text = seat.find('span', class_='red').text
        seat_count = int(seat_count_text.replace('석', '').strip())

        if seat_count > 0:
            result.append(f"{seat_type} {seat_count}석")
    return result


if __name__ == '__main__':

    headers = noah_sign.get_header()
    noah_sign.wirte_sign()
    print('program is up and running.')

    # 금, 토
    time_lst = ['1325885', '1326314']

    attempt, cnt = 0, 0
    while cnt < 10:
        try:
            for i in range(len(time_lst)):
                data = {
                    "pIdTime": time_lst[i],
                    "pIdCode": '',
                    "pDisplayRemainSeat": 0,
                }
                result = []
                html = daysix(data)
                # todo >> pIdTime에 따른 요일 표시를 위해 time_lst key,value로 전환 필요
                print(f'@@@@ {time_lst[i]} @@@@\n{html}')
                result = filter_html(html)

                if result:
                    print(f'좌석을 찾았습니다.\n {result}')
                    cnt += 1
                    beep_sound()
            attempt +=1
            if attempt % 100 == 0: time.sleep(10)
            print(f'{attempt}회 탐색 중')
            time.sleep(random.uniform(1.0,3.0))

        except Exception as e:
            print(f'[Error] 알 수 없는 에러 > {e}')