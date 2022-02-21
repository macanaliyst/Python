#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# 년월일 날짜 타입 - 타입으로 변경 
def date_type_converter_년월일(value):
    year, month, day = re.findall(r'\d+', value)
    if len(month) == 1 :
        month = '0' + month
    if len(day) == 1 :
        day = '0' + day
    return year + '-' + month + '-' + day

