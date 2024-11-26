import time
import random
import requests
from bs4 import BeautifulSoup
import winsound
import datetime
# import remain_seat
'''
  1. 일자별 좌석 조회
    - 비지정 좌석 시 유용
      data = {
        "pIdTime": time_lst[i],
        "pIdCode": '',
        "pDisplayRemainSeat": 0,
      }
  
  2. 블록별 잔여좌석 조회
    - 지정 좌석 시 유용
      data = {
        "idHall":	12487,
        "idTime":	1326314
      }
  
  isDate와 isSection 으로 분기
'''

def __n_url(url):
  org = 'http://ticket.yes24.com'
  n_url = org + url
  return n_url

def __beep_sound():
  for _ in range(5):
    winsound.Beep(1500, 600)  # Hz, duration
    time.sleep(0.2)


def __filter_seat_str(text):
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


def _find_seat(url, data):
  global ans
  for i in range(len(data)):
    # print(f'data >> {i}')
    response = requests.get(url, data[i])
    # print(f'get_url5 >>\n{response.text}')
    try:
      result = __filter_seat_str(response.text)
      # print(result)
      # result = 'tmp'
      if result:
        tmp = f'{20 + i}일-{result}'
        if tmp not in ans:
          print(f'좌석을 찾았습니다.\n{i+1}번째날({20 + i}일) - {result}')
          __beep_sound()
          ans.append(tmp)
        time.sleep(2)

    except Exception as e:
      print(f'[FindSeatError] {e}')

    time.sleep(random.uniform(0.0, 2.0))


def main_seat():
  # date_url = '/Pages/Perf/Sale/Ajax/Perf/TimeSeatRemain.aspx'
  section_url = '/OSIF/Book.asmx/GetHallMapRemain'

  data = [{
      "idHall": 12487,
      "idTime": 1325885
    },
    {
      "idHall": 12487,
      "idTime": 1326314
  }]
  _find_seat(__n_url(section_url), data)
  pass

if __name__=='__main__':
  cnt = 0
  ans = []
  while True:
    main_seat()
    time.sleep(5)
    # time.sleep(random.randint(1, 3))
    cnt += 1
    if len(ans) == 10:
      print('10회 이상 좌석을 찾았습니다.\n프로그램을 종료합니다.')
      print(ans)
      time.sleep(5)
      break
    else:
      print(f'{cnt}회 탐색 중')