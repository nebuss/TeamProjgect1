import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 1. 데이터 불러오기

# 원본 데이터(excel)상, 1행과 2행 일부 부분이 병합되어 있음. 
# 2행부터 데이터를 받고자 header = 1로 설정하여 데이터 읽음. 
df = pd.read_excel('data/domestic_2022.xlsx', header = 1)
df.head()


# 데이터 변수 확인
df.columns


# 2. 변수 이름 바꿔보기
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

#변수명 잘 바뀌었는지 확인
df

# 3. 'class1'의 Nan 값에 class에 맞는 값 부여 & 영문명으로 변경
df.loc[0, ['class1']] = "categoty-sum"
df.loc[1:2, ['class1']] = "sex"
df.loc[3:9, ['class1']] = "age"
df.loc[10:16, ['class1']] = "job"
df.loc[17:20, ['class1']] = "edu"
df.loc[21:23, ['class1']] = "fam"
df.loc[24:30, ['class1']] = "income"
df

# 분석할 변수인 sex, age, income를 가진 데이터 추출
# 이를 
df_new = df.query('class1 == ["sex", "age", "income"]')
df_new

# 4. 'class2'국문 내용을 영문으로 변경
#sex
df_new.loc[df_new["class2"] == "남자", "class2"] = "M"
df_new.loc[df_new["class2"] == "여자", "class2"] = "F"

#age
df_new.loc[df_new["class2"] == "15~19세", "class2"] = "10s"
df_new.loc[df_new["class2"] == "20대", "class2"] = "20s"
df_new.loc[df_new["class2"] == "30대", "class2"] = "30s"
df_new.loc[df_new["class2"] == "40대", "class2"] = "40s"
df_new.loc[df_new["class2"] == "50대", "class2"] = "50s"
df_new.loc[df_new["class2"] == "60대", "class2"] = "60s"
df_new.loc[df_new["class2"] == "70세 이상", "class2"] = "70s~"

#income
df_new.loc[df_new["class2"] == "100만원 미만", "class2"] = "~100"
df_new.loc[df_new["class2"] == "100~200만원 미만", "class2"] = "100~200"
df_new.loc[df_new["class2"] == "200~300만원 미만", "class2"] = "200~300"
df_new.loc[df_new["class2"] == "300~400만원 미만", "class2"] = "300~400"
df_new.loc[df_new["class2"] == "400~500만원 미만", "class2"] = "400~500"
df_new.loc[df_new["class2"] == "500~600만원 미만", "class2"] = "500~600"
df_new.loc[df_new["class2"] == "600만원 이상", "class2"] = "600~"

df_new

#############################################################################
# 5. 'class1'과 'class2'를 df_new의 index로 설정[선택사항: set_index 안배움]
# df_new = df_new.set_index(['class1', 'class2'])
# df_new

############################################################################
# 여기까지 했음요

# # 6. age별 dm_total 그래프로 확인해 보기
# import seaborn as sns
# age_group = pd.DataFrame(df_new.loc['age', 'dm_total'])
# type(df_new.loc['age', 'dm_total'])
# type(age_group)
# 
# #그래프로!!
# sns.barplot(data = age_group, x = 'class2', y = 'dm_total')
# 
# plt.show()
# plt.clf()
# 
# 
# 
# #age_group = df_new.query('class1 == "age"')
# #age_group
# #df_new.loc[[df_new.query('class1 == "age"')], 'dm_total']
# #a = df_new.query('class1 == "age"')
# 
# # dm_total_age = sns.barplot(data = df_new, x = 'class2', y = 'dm_total')
# # plt.show()
# # plt.clf()
# 
# df_new['dm_total']
# 
# #dm_total 내림차순으로 정렬
# dm_total_age = age_group.sort_values('dm_total', ascending = False)
# 
# dm_total_age.plot.bar(rot = 0)
# plt.show()
# plt.clf()
