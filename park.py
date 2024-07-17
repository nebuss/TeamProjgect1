import pandas as pd
import numpy as np

df = pd.read_excel('data/domestic_2022.xlsx')

#drop 함수를 쓰고싶은데 drop함수는 데이터프레임의 열을 삭제해준다. 나는 0번째 행을 삭제해야하므로
df.columns = df.iloc[0] #df.columns 를 이용해 변수에 데이터프레임 행/열의 순서로 접근하는 .iloc 함수로 첫번째 \
                         #행을 칼럼으로 지정해준다
                         
df = df.drop(0) # 0번째 칼럼은 모두 2022년 이라는 컬럼 이름을 가지고 있으므로 삭제.

df.columns
df.columns = ['index1', 'index2', 'all_domestic', 'domestic_accommodation', 'day_trip', 'all_tourism', \
              'tourism_accommodation', 'tourism_day', 'all_ect', 'ect_accommodation', 'ect_day']
              #칼럼명 변경


# 분석에 필요없는 행 삭제. range로 범위를 지정해 삭제가능. axis=0은 행을 뜻함. axis=1은 열.
# labes=range()는 판다스 dataframe.drop() 메서드에서 사용되는 인자로 range() 함수는 파이썬에서 \ 
# 연속된 숫자를 생성하는데 사용되며, 일반적으로 시작값, 끝값, 간격을 지정할 수 있다. 기본값은 1 \
  
  
new_df = df.drop(labels=range(11, 25), axis=0) 
new_df 


#loc함수로 행에 접근해서 NaN값을 영어로 컬럼명 지정
new_df.loc[[3], ['index1']] = 'sex'
new_df.loc[[5, 6, 7, 8, 9, 10], ['index1']] = 'age'
new_df.loc[[26, 27, 28, 29, 30, 31], ['index1']] = 'income'

#컬럼명 확인
new_df.columns

#.set_index 함수는 지정한 열을 인덱스로 지정. 두개 이상할때는 리스트 형태에 넣어줌. 기본적으로 원래 값은 \
# 변경되지 않기때문에 변경된 값으로 덮어주려면, inplace = True 값을 인수로 넣음.
new_df.set_index(['index1', 'index2'], inplace=True) #인덱스 두개 지정. 인덱스로 지정되면서 중복된 값 병합 됨.

# 원래 데이터 명을 나머지와 마찬가지로 영어로 변경해줌
new_df.rename(index = {'성별' : 'sex', '연령' : 'age', '가구소득' : 'income'}, inplace= True)


#두번째 인덱스의 데이터들도 이름 영어로 변경
new_df.rename(index = {'남자' : 'male', 
                       '여자' : 'female', 
                       '15~19세' : '15-19', 
                       '20대' : '20s', 
                       '30대' : '30s', 
                       '40대' : '40s', 
                       '50대' : '50s', 
                       '60대' : '60s', 
                       '70세 이상' : '70s up', 
                       '100만원 미만' : 'under_one_million', 
                       '100~200만원 미만' : 'under_one_two', 
                       '200~300만원 미만' : 'under_two_three', 
                       '300~400만원 미만' : 'under_three_four', 
                       '400~500만원 미만' : 'under_four_five', 
                       '500~600만원 미만' : 'under_five_six', 
                       '600만원 이상' : 'more_six_million' 
                       }, inplace= True)
new_df

