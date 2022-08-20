# 백준 2490
# 윷 놀이
# idea : 배 또는 등의 개수를 세어서 결과 판별
import sys

def yut():
    for _ in range(3):
        yut_result = list(map(int, sys.stdin.readline().split()))
        if yut_result.count(0) == 1:
            print("A")
        elif yut_result.count(0) == 2:
            print("B")
        elif yut_result.count(0) == 3:
            print("C")
        elif yut_result.count(0) == 4:
            print("D")
        elif yut_result.count(0) == 0:
            print("E")
yut()