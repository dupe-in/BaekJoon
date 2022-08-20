# 백준 11729
# 하노이 탑 이동 순서
import sys
import numpy as np

N = int(sys.stdin.readline())
hanoi_list = list(range(1, N+1))
print(hanoi_list)
hanoi = list([[0, 0, 0], [0, 0, 0], [0, 0, 0]])
print(hanoi)

