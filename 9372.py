# 백준 9372
# 상근이의 여행
import sys

T = int(sys.stdin.readline())       # test case 횟수 입력 받기
route_list = []

for t in range(T):
    # N : 국가의 수, M : 비행기의 종류
    N, M = [int(x) for x in sys.stdin.readline().split()]
    # 비행기 종류만큼 반복
    for p in range(M):
        a, b = sys.stdin.readline().split()     # a에서 b까지 경로(?)
        route_list.append(a)                    # 출발지 위치 append
        route_list.append(b)                    # 목적지 위치 append
    final_route = list(set(route_list))         # 중복 제거
    print(len(final_route) - 1)                 # 리스트의 길이 - 1 =  최소 개수
    route_list.clear()                          # 다음 testcase를 위해 초기화