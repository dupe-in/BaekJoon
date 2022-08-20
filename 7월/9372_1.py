# 백준 9372
# 상근이의 여행

import sys

T = int(sys.stdin.readline())       # test case 횟수 입력 받기
for t in range(T):
    # N : 국가의 수, M : 비행기의 종류
    N, M = [int(x) for x in sys.stdin.readline().split()]
    for p in range(M):                      # repeat plane times
        a, b = sys.stdin.readline().split() # a에서 b까지 경로(?)
    print(N - 1)