import random
import gzip
import zlib

import datetime
import winsound
import time
import requests
from bs4 import BeautifulSoup
# from cookie import get_cookies
# from noah_sign import get_signature

# cookies = get_cookies()
# print(f'cookies >> {cookies}')

headers = {
    'Host': 'ticket.yes24.com',
    "Cookie": 'PCID=17267122635700594879780; _gcl_au=1.1.706538121.1726712264; __utmz=186092716.1726712264.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); _fwb=2142pE5DUkgol5kDTRdOLUw.1726712264130; _fbp=fb.1.1726712271637.110577346751333377; AT_LOGIN=AT_MID=&AT_SID=57E1DA0965892C22CC20EBB6395118A6&AT_PID=&AT_LDTS=202409191118; ServiceCookies=MTUyMDE3NjVgamFzaWMwNjI3YL72wOe9xGAwYDAxYGphc2ljMDYyN2BgMTUyMDE3NjVgMjhgMWNMZmpvSkdSeFZyVDljZVdEMFJ4V1pYbVpNazBZVFhkZFJhRGwxN3h1akUrQUF0OVJCNUYvZnFaQ3pVeXVWSDMzeXJ1Nlc0Z1hlSGgzNVB1N1VEbUE9PWBjaC90dlN1OXdSWGdHTEMvOWorM0liK0p3YzRvVytKQUt1Q01ZVU1nM0ZTSDAxZHo4VC91UXVDZjhCcGpNSEF2M0w5dEhiblFqS3hERkEwVnVQZkNmSFNQMEhadkg3ZjBpSnJmeHlwUDBKajFlRHlxWXJ2V3VtUXE5N3Z6SUd4Nm1ESnZMcVNqVzlJQ0FXeFNqR1N4dkE9PWBwYVd1STFjcGZ6VlpKY1cvdzNVMG1BPT0=; AdultAuthYN=; _fwb=178zYqeGKsKvQBaL99Y5PMa.1726712277877; _ga=GA1.1.902805687.1726712265; _abx__ioBYurVi4UKyZbh859fByw=G7WSqK33vh92996VAZmPPcenQ0m+gNxc6qQstTY6TW33xSBsl0TVzIH2TRSX5XiMPBRzI50vx0b3RIwHcmhvQUaEvwKkYrmAyWNixck0itit4pnVGnD0xUPs/xaLr0PXEt4ElTU001isA16ibRRfcC9vwAk57QMJaoj/FUU4E8/m0OjmwGPIreYTI5HsyeVuKx6IEyEPJzmGicTy+j5b8blTULOhg+1n/p7+IzgnggeVHmp8DCf7PVe+CuaJt0r5awvRPrbVuV+sbVKbxumlIDB1qP9qsYgSuflB1SvRjAykdiI9O4jNYJRbl/eHwH5ujsspt4PmNbmNeVOxQd4haSMeNOE9pGUhH7Af5R/ao2nX3kg0VL3ernZ9ADVEKavDIv9lfH5u9PyfDgNwZtGR2DKo/X65RLnzKQ95FxX/OhlsgloX7N4KZZlg7wSAz7N/WUZwMRodEoCuPTocQAgteGuFzCJ1WN4LSHMN5l7rlhrlVIYVswn4TdzwM0H/ifZq7WJoDWWmQsTELqFsWeT7qCzjXZVJuVwo6bcA7CtoQYwf8OXiU26981Lmc9GY3pn/mrZnF8pPWlCqE7A9OQnPL9MCZ8VpEr40j3eKPJLE2+WuyexFlh5Uh8lRbGQuNb9n0wYdcMukuZjafqOs6vRX0P/L6iLQohgW1kBjkhvwTBqOFFwMIUSBEbI2DwyRH5i+dmcKcOiIydlkhmO5LRg2E+R443X2CFIHrvGCVvBiNpT9dkIE0BoowxZX1NmhPp7hrag5Ya4Ce58KYMdE9py0L/Jqfaz6MTyeXpLSB6mIRDM=; _ga_FJT6RQ6VPQ=GS1.1.1726717021.2.0.1726717021.60.0.0; ASP.NET_SessionId=fhg3bwykpiqo2fhk2xdblodq; wcCookieV2=218.233.5.253_T_33367_WC; YesTicket=UserNO=52,86,153,5,174,254,255,78,29,134,27,173,165,156,94,37&UserID=232,180,207,205,217,72,167,56,52,118,65,180,41,53,140,131&UserName=228,133,21,81,148,36,238,66,246,66,181,12,202,15,3,197&UserNickName=232,180,207,205,217,72,167,56,52,118,65,180,41,53,140,131&Email=232,180,207,205,217,72,167,56,188,246,225,222,17,127,64,146,187,241,132,192,61,116,158,24&ManiaLevel=185,175,224,130,94,14,207,79&MemberStatus=245,54,43,158,39,91,228,116&UserIdentiNumber=6,251,93,8,20,214,139,146,183,197,72,94,110,17,227,184&StarLevel=245,54,43,158,39,91,228,116&PromotionCode=245,54,43,158,39,91,228,116&MemberGB=185,175,224,130,94,14,207,79&UserAge=226,223,210,38,100,34,217,39&ORD_PATH_GB=195,31,27,161,165,198,213,175&ZipCode=195,48,244,147,96,131,103,143&Address=17,176,240,144,29,209,230,3,72,178,0,14,69,200,245,101,252,81,221,40,134,227,254,220,208,200,205,121,55,176,192,255,119,75,192,99,71,120,46,33,162,211,156,246,250,119,246,142,5,241,135,172,31,111,102,223,36,193,238,52,189,198,41,25,77,35,203,158,116,33,253,170&Addr1=17,176,240,144,29,209,230,3,72,178,0,14,69,200,245,101,252,81,221,40,134,227,254,220,208,200,205,121,55,176,192,255,119,75,192,99,71,120,46,33,102,20,12,38,10,140,180,25&Addr2=23,139,204,160,0,246,119,240,167,177,156,154,88,55,117,74,69,235,144,243,132,114,15,89&Addr3=17,176,240,144,29,209,230,3,72,178,0,14,69,200,245,101,252,81,221,40,134,227,254,220,182,39,197,202,127,85,138,37,251,178,219,243,64,5,122,210,17,101,71,84,163,34,162,48,144,251,1,47,226,140,148,7&Addr4=16,9,167,116,173,202,194,130,184,176,165,245,104,33,43,251&Phone=41,76,75,211,249,101,108,243,0,13,13,11,60,173,212,184&Mobile=41,76,75,211,249,101,108,243,0,13,13,11,60,173,212,184&OrgID=13,101,187,16,10,24,135,131&Channel=13,101,187,16,10,24,135,131; RecentItems=6RrnjbUVjn849e0QBPGlXg2FhviAfX4xsTLjv63z9ItZzlBFMvCGOVWe7rwWVGEwXajIJDyf+UmMpN1H+AZEF4UA95D8IF9yrT9Gou+Er0aMgJ8yBqeIWB5cIfnVkC0j; __utmc=186092716; YesTicket=UserNO=52,86,153,5,174,254,255,78,29,134,27,173,165,156,94,37&UserID=232,180,207,205,217,72,167,56,52,118,65,180,41,53,140,131&UserName=228,133,21,81,148,36,238,66,246,66,181,12,202,15,3,197&UserNickName=232,180,207,205,217,72,167,56,52,118,65,180,41,53,140,131&Email=232,180,207,205,217,72,167,56,188,246,225,222,17,127,64,146,187,241,132,192,61,116,158,24&ManiaLevel=185,175,224,130,94,14,207,79&MemberStatus=245,54,43,158,39,91,228,116&UserIdentiNumber=6,251,93,8,20,214,139,146,183,197,72,94,110,17,227,184&StarLevel=245,54,43,158,39,91,228,116&PromotionCode=245,54,43,158,39,91,228,116&MemberGB=185,175,224,130,94,14,207,79&UserAge=226,223,210,38,100,34,217,39&ORD_PATH_GB=195,31,27,161,165,198,213,175&ZipCode=195,48,244,147,96,131,103,143&Address=17,176,240,144,29,209,230,3,72,178,0,14,69,200,245,101,252,81,221,40,134,227,254,220,208,200,205,121,55,176,192,255,119,75,192,99,71,120,46,33,162,211,156,246,250,119,246,142,5,241,135,172,31,111,102,223,36,193,238,52,189,198,41,25,77,35,203,158,116,33,253,170&Addr1=17,176,240,144,29,209,230,3,72,178,0,14,69,200,245,101,252,81,221,40,134,227,254,220,208,200,205,121,55,176,192,255,119,75,192,99,71,120,46,33,102,20,12,38,10,140,180,25&Addr2=23,139,204,160,0,246,119,240,167,177,156,154,88,55,117,74,69,235,144,243,132,114,15,89&Addr3=17,176,240,144,29,209,230,3,72,178,0,14,69,200,245,101,252,81,221,40,134,227,254,220,182,39,197,202,127,85,138,37,251,178,219,243,64,5,122,210,17,101,71,84,163,34,162,48,144,251,1,47,226,140,148,7&Addr4=16,9,167,116,173,202,194,130,184,176,165,245,104,33,43,251&Phone=41,76,75,211,249,101,108,243,0,13,13,11,60,173,212,184&Mobile=41,76,75,211,249,101,108,243,0,13,13,11,60,173,212,184&OrgID=13,101,187,16,10,24,135,131&Channel=13,101,187,16,10,24,135,131; NA_SAC=dT1odHRwJTNBJTJGJTJGdGlja2V0LnllczI0LmNvbSUyRlBhZ2VzJTJGUGVyZiUyRlNhbGUlMkZQZXJmU2FsZVByb2Nlc3MuYXNweCUzRklkUGVyZiUzRDUwNjg3JTI2SWRUaW1lJTNEMTMwNjk4NHxyPWh0dHAlM0ElMkYlMkZ0aWNrZXQueWVzMjQuY29tJTJGUGVyZiUyRjUwNjg3; __utma=186092716.1947507418.1726712264.1727852893.1727854976.3; __utmt=1; wcs_bt=s_1b6883469aa6:1727855095; __utmb=186092716.2.10.1727854976; _ga_719LSSZFC3=GS1.1.1727852892.5.1.1727855106.3.0.0',
    'Connection': 'keep-alive',
    'Content-Length': '63',
    'X-Requested-With': 'XMLHttpRequest',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36',
    'Accept': 'text/html, */*; q=0.01',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Origin': 'http://ticket.yes24.com',
    'Referer': 'http://ticket.yes24.com/Pages/Perf/Sale/PerfSaleProcess.aspx?IdPerf=50687',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7'
}

def n_url(url):
    org= 'http://ticket.yes24.com'
    n_url = org+url
    return n_url


def beep_sound():
    for _ in range(5):
        winsound.Beep(1500, 600) # Hz, duration
        time.sleep(0.2)


def find_seat(text):
    soup = BeautifulSoup(text, 'lxml-xml')
    section_tag = soup.find('Section')
    ntext = section_tag.text if section_tag else None
    # print(ntext)
    seats = ntext.split('^')
    for seat in seats:
        if '@' in seat and seat[-1] != '0':
            print(seat)
            return seat
    return None

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


# idHall	12205
# idTime	1309168
def get_url5(url, data):
    global ans
    d = {
        "idHall" : "12205",
        "idTime" : "1309168"
    }
    for i in range(len(data)):
        # print(f'data >> {i}')
        response = requests.get(url, data[i])
        # print(f'get_url5 >>\n{response.text}')
        try:
            result = find_seat(response.text)
            if result:
                tmp = f'{20+i}일-{result}'
                if tmp not in ans:
                    print(f'좌석을 찾았습니다.\n{i}번째날({20+i}일) - {result}')
                    beep_sound()
                    ans.append(tmp)
                time.sleep(2)

        except Exception as e:
            print(f'[FindSeatError] {e}')


        time.sleep(random.uniform(0.0,2.0))

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
    '''
    data5 = [
        ## 20일
        {
            "idHall": "12205",
            "idTime": "1309168"
        },
        ## 21일
        {
            "idHall": "12205",
            "idTime": "1309432"
        },
        ## 22일
        {
            "idHall": "12205",
            "idTime": "1309433"
        },
    ]
    url5 = '/OSIF/Book.asmx/GetHallMapRemain'
    cnt = 0
    ans = []
    while True:
        get_url5(n_url(url5), data5)
        time.sleep(10)
        # time.sleep(random.randint(1, 3))
        cnt +=1
        if len(ans) == 10:
            print('10회 이상 좌석을 찾았습니다.\n프로그램을 종료합니다.')
            print(ans)
            time.sleep(5)
            break
        else:
            print(f'{cnt}회 탐색 중')
    '''



    '''
        url3,4는 예매 팝업 첫 단계 - 달력 누르는 곳이다.
        한번에 파악할 수 있으면 좋겠으나,
        응답 값이 따로 없어서 post요청으로 어떻게 잔여석을 받는지 모르겟음.
        급한대로 일단패스
    '''

    signature = """
                          _      _                                            
                         | |    ( )                                           
     _ __    ___    __ _ | |__  |/  ___          _ __ ___    __ _   ___  _ __   ___  
    |  _ \  / _ \  / _  ||  _ \    / __|        |  _   _ \  / _  | / __||  __| / _ \ 
    | | | || (_) || (_| || | | |   \__ \        | | | | | || (_| || (__ | |   | (_) |
    |_| |_| \___/  \__,_||_| |_|   |___/        |_| |_| |_| \__,_| \___||_|    \___/ 

    """


    print(signature)
    print('program is up and running.')
    # mint_url = '/Pages/Perf/Sale/Ajax/Perf/TimeNoSeatClass.aspx'
    # result = mint(n_url(url))

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
                    print(f'좌석을 찾았습니다.\n{result}')
                    cnt += 1
                    beep_sound()
            attempt +=1
            if attempt % 100 == 0: time.sleep(10)
            print(f'{attempt}회 탐색 중')
            time.sleep(random.uniform(1.0,3.0))

        except Exception as e:
            print(f'[Error] 알 수 없는 에러 > {e}')




    # attempt, cnt = 0, 0
    # msg ='<li class=\'grade\'></li>'
    # # print(result)
    # while cnt < 10:
    #     try:
    #         if msg == result:
    #             pass
    #         else:
    #             print('좌석을 찾았습니다.')
    #             print(result)
    #             cnt +=1
    #             beep_sound()
    #
        #     attempt +=1
        #     if attempt % 100 == 0: time.sleep(10)
        #     print(f'{attempt}회 탐색 중')
        #     time.sleep(random.uniform(1.0,3.0))
        #
        # except Exception as e:
        #     print(f'[Error] 알 수 없는 에러 > {e}')