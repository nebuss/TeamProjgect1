import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#(단기체류외국인) 월별 단기체류외국인 국적(지역)별 현황


df_exam = pd.read_csv('data/foreigner.csv',  encoding='euc-kr')
df_exam.columns

df_exam2 = exam.copy()

#항목 열을 변경(1.변수 이름 변경 했는지?)
df_exam2 = df_exam.rename(columns={
    '년': 'year',
    '월': 'month',
    '국적지역': 'nationality',
    '단기체류외국인 수': 'visitors'
})

df_exam2

#2.행들을 필터링 했는지?, #5. 정렬했는지? 
#최신년도부터 - 오래된 순
#방문자 수 많은 곳부터 - 적은곳 순으로 정렬
df_exam2.sort_values(['year','visitors'], ascending=[False, False])

#3. 새로운 변수를 생성했는지?
#2022~2024 나라별 방문자 수 합친 새로운 열 생성
# 나라별 visitors 합계 계산
df_country_totals = df_exam2.groupby('nationality')['visitors'].sum().reset_index()


# 새로운 열 추가
df_exam2['country_totals'] = df_exam2['nationality'].map(df_country_totals.set_index('nationality')['visitors'])
df_exam2

#4. 그룹 변수 기준으로 요약을 했는지?
#평균방문자
mean_visitors = df_exam2["country_totals"].mean()
mean_visitors
# 평균보다 많은 방문자를 갖고 있는 국가들 중 5국가 선택

alot_of_visitors = df_exam2[df_exam2['country_totals'] > mean_visitors]['nationality']
alot_of_visitors.head(5)


