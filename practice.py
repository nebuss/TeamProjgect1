import pandas as pd
import numpy as np

travel = pd.read_csv("data/travel(2016_2019).csv", encoding = 'euc-kr')
travel

travel2 = travel.copy() #복사 
travel2_filled = travel2.fillna(0)
travel2.head()

#1. 변수 이름 변경 했는지?
travel2 = travel2.rename(columns={"2016 년" : "2016"}) #이 코드까지 쳐야지 확정됨. 
travel2 = travel2.rename(columns={"2017 년" : "2017"})
travel2 = travel2.rename(columns={"2018 년" : "2018"})
travel2 = travel2.rename(columns={"2019 년" : "2019"})
travel2.head()

#2. 행들을 필터링 했는지?
travel2.query("통계분류 == '7월'")

travel2_filled = travel2.fillna(0)
travel2_filled

#3. 새로운 변수를 생성했는지?
travel2["total"] = travel2["2016"] + travel2["2017"] + travel2["2018"] + travel2["2019"]
travel2.head()

#4. 그룹 변수 기준으로 요약을 했는지?
travel2.query('total >= 100')

#5. 정렬했는지? 
travel2.sort_values('total')

