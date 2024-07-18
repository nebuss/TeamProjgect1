import numpy as np
import pandas as pd
import matplotlib as plt

#엑셀 불러오기, 두번째 줄부터 골라오기
df = pd.read_excel("data/domestic_2022.xlsx", header = 1)
df

#원본유지를 위해 복사본 만들기
df_new = df.copy()
df_new

#행 이름 영문으로 수정하기
df_new = df_new.rename(columns = {"국내전체": "total_domestic",
                                  "국내숙박": "acc_domestic",
                                  "국내당일": "daycation_domestic",
                                  "관광전체": "total_tour",
                                  "관광숙박": "acc_tour",
                                  "관광당일": "daycation_tour",
                                  "기타전체": "total_others",
                                  "기타숙박": "acc_others",
                                  "기타당일": "daycation_others",
                                  "통계분류(1)": "group(1)",
                                  "통계분류(2)": "group(2)"})
df_new



df_new = df.dropna(subset = ')
