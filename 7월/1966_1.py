# 백준 1966
# 프린터 큐
# queue로 시도해 본것(미완성)

import queue
from collections import deque

N_list = []
M_list = []
T = int(input())        # 테스트 케이스 입력 : 3
Q = deque()

# 테스트 케이스만큼 반복 : 0, 1, 2
for i in range(T):
    # N : 문서의 개수, M : 인쇄할 문서가 현재 몇 번째에 있는지
    N, M = input().split()    
    N_list.append(N)                    # N = 1, 4, 6
    N_int = int(N)
    M_int = int(M)
    M_list.append(M)    # q_n = 0, 2, 0
    print("N_list :", N_list)
    print("M_list :", M_list)    
    N_important = input().split()           # N = 1일때 : 중요도 5
    print("N_important :", N_important)
    print("type :", type(N_important))
    Q.clear()   # 큐 초기화

    # Q에 중요도 저장 ex) 1 1 9 1 1 1, 
    for a in range(len(N_important)):
        Q.append(N_important[a])
    if len(N_important) == 1:
        print("dddd:", Q[0])
    else:
        print(Q)



    # for n in range(N_int):
    #     Q.put(N_important[n])
    

# print("1 :", Q.get(Q[0]))
# print("2 :", Q.get(Q[5]))
# print("3 :", Q.get(Q[3]))
# print("4 :", Q.get())
# print("5 :", Q.get())