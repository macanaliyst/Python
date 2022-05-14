# default dictionary
from collections import defaultdict

# default를 int로 지정한 dictionary
D = defaultdict(int) 
D['why']
# => 지정되어 있지 않은 key의 값은 0으로 출력해준다.
# => 이를 활용하여 고객별 action 횟수에 대한 dictionary를 쉽게 만들 수 있다.
