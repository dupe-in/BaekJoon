# 백준 2293
# 동전 1
# idea : 각 1, 2, 5의 최소 가치부터 최대 가치까지 덱으로 저장
# rotate 하면서 계산
import sys

def coin(n, k):
    # for i in range(n):  # 덱 만들기
        



    coin_l = []
    coin_count = 0
    for i in range(n):
        coin_value = int(input())
        coin_l.append(coin_value)
    coin_l.sort()
    for i in range(n):
        num = k // coin_l[i]
        for a in range(num + 1):
            pass


n, k = map(int, sys.stdin.readline().split())
coin(n, k)
