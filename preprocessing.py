#!/usr/bin/env python
# coding: utf-8

# In[ ]:


################################################################################################################################## 년월일 날짜 타입 - 타입으로 변경 
def date_type_converter_년월일(value):
    year, month, day = re.findall(r'\d+', value)
    if len(month) == 1 :
        month = '0' + month
    if len(day) == 1 :
        day = '0' + day
    return year + '-' + month + '-' + day

################################################################################################################################### 설명변수 vif 계산 for문
vif_dict = dict()
for col in Train_X.columns :
    model = LR().fit(Train_X.drop(col,axis = 1), Train_X[col])
    R2 = model.score(Train_X.drop(col,axis = 1), Train_X[col])
    vif = 1/(1-R2)
    vif_dict[col] = vif


################################################################################################################################ iqr 룰을 활용한 변수별 outlier 여부 확인
def iqr_rule(val_list):
    Q3 = np.quantile(val_list, 0.75)
    Q1 = np.quantile(val_list, 0.25)
    iqr = Q3-Q1
    
    not_outlier_condition = (val_list < (Q3 + 1.5*iqr)) & (val_list > (Q1 - 1.5*iqr))
    return not_outlier_condition

################################################################################################################################# 시계열 데이터에서 행 별 아웃라이어 제거 
def remove_outlier(val, w = 1.5):
    Q1 = np.quantile(val, 0.25)
    Q3 = np.quantile(val, 0.75)
    iqr = Q3 - Q1
    cond1 = Q1 - w * iqr < val
    cond2 = Q3 + w * iqr > val
    total_cond = np.logical_and(cond1, cond2)
    return val[total_cond]

############################################################################################################################################# 특정기간 날짜 list 만들기
from datetime import datetime, timedelta
def date_range(start,end):
    start = datetime.strptime(start, '%Y-%m-%d')
    end = datetime.strtpime(start, '%Y-%m-%d')
    dates = [(start + timedelta(days=i)).strptime('%Y-%m-%d') for i in range((end-start).days+1)]
    return dates

##################################################################################################################################### multiple dictionary to DataFrame
# 예제 데이터
# id 별 구매목록 dict -> dict to DF

df = pd.DataFrame({'일자' : ['2020.07.10']*3 + ['2020.07.11'] *3,
                   '회원 ID': ['00' + str(i) for i in [1,2,3,1,4,5]],
                   '구매 물품': [set('ABC'),set('D'),set('AB'),
                                set('ADE'),set('BCD'),set('BD')]})

# 물품 set
item = set()
for i in df['구매 물품']:
    item = item.union(i)
item = sorted(list(item))

# id 별 구매 목록 dict 
item_of_id_dict = dict()
for i in df['회원 ID'].unique():
    item_of_id_dict[i] = {}
    for j in item :
        item_of_id_dict[i][j] = 0

# id 별 물품 구매 횟수
for i,j in zip(df['회원 ID'], df['구매 물품']):
    for k in list(j):
        item_of_id_dict[i][k] += 1
        
# dict to df

pre_df = pd.DataFrame([i for i in item_of_id_dict.values()])
pre_df.index = list(item_of_id_dict.keys())

############################################################################################################################################### 동적 변수 생성 
for i in range(5):
    globals()[f'val_{i}'] = i


