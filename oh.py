import pandas as pd
import numpy as np

# 데이터 불러오기
# 원본 데이터(excel)상, 1행과 2행 일부 부분이 병합되어 있음. 
# 2행부터 데이터를 받고자 header = 1로 설정하여 데이터 읽음. 
df = pd.read_excel('data/domestic_2022.xlsx', header = 1)
df.head()


# 데이터 변수 확인 
df.columns


# 변수 이름 바꿔보기
df = df.rename(columns = {'통계분류(1)' : 'class1',
                          '통계분류(2)' : 'class2',
                          '국내전체'    : 'dm_total',
                          '국내숙박'    : 'dm_stay',
                          '국내당일'    : 'dm_1day',
                          '관광전체'    : 'tr_total',
                          '관광숙박'    : 'tr_stay',
                          '관광당일'    : 'tr_1day',
                          '기타전체'    : 'ot_total',
                          '기타숙박'    : 'ot_stay',
                          '기타당일'    : 'ot_1day'
                          })
df #df 잘 바뀌었는지 확인

# 'class1'의 Nan 값에 class에 맞는 값 부여
df.loc[2, ['class1']] = "성별"
df.loc[4:9, ['class1']] = "연령"
df.loc[11:16, ['class1']] = "직업"
df.loc[18:20, ['class1']] = "학력"
df.loc[22:23, ['class1']] = "가구원수"
df.loc[25:30, ['class1']] = "가구소득"


# 행렬 바꿔서 이름 부여
df2 = df.transpose()
df2
df2.columns


#rename 코드 짧게 짤 수 있는 분은 수정 부탁드립니다.

df2 = df2.rename(columns = {0  : 'category'})
df2 = df2.rename(columns = {1  : 'sex'})
df2 = df2.rename(columns = {2  : 'sex'})
df2 = df2.rename(columns = {3  : 'age',
                            4  : 'age',
                            5  : 'age',
                            6  : 'age',
                            7  : 'age',
                            8  : 'age',
                            9  : 'age',
                            10 : 'job',
                            11 : 'job',
                            12 : 'job',
                            13 : 'job',
                            15 : 'job',
                            16 : 'job',
                            17 : 'edu',
                            18 : 'edu',
                            19 : 'edu',
                            20 : 'edu',
                            21 : 'fam',
                            22 : 'fam',
                            23 : 'fam',
                            24 : 'income',
                            25 : 'income',
                            26 : 'income',
                            27 : 'income',
                            28 : 'income',
                            29 : 'income',
                            30 : 'income'})
                            
#df2에 잘 반영되었는지 확인
df2

#df_new로 그냥 행렬 바꿔서 보고 싶었음
df_new = df2.transpose()
df_new
