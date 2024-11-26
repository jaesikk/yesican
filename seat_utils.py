import time
import remain_seat
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


def n_url(url):
  org = 'http://ticket.yes24.com'
  n_url = org + url
  return n_url

def get_seat():
  # date_url = '/Pages/Perf/Sale/Ajax/Perf/TimeSeatRemain.aspx'
  section_url = '/OSIF/Book.asmx/GetHallMapRemain'

  data = [{
    "idHall": 12487,
    "idTime": 1326314
  }]
  remain_seat.get_url5(n_url(section_url), data)
  pass

if __name__=='__main__':
  cnt = 0
  ans = []
  while True:
    get_seat()
    time.sleep(10)
    # time.sleep(random.randint(1, 3))
    cnt += 1
    if len(ans) == 10:
      print('10회 이상 좌석을 찾았습니다.\n프로그램을 종료합니다.')
      print(ans)
      time.sleep(5)
      break
    else:
      print(f'{cnt}회 탐색 중')