# 백준 10866
# 덱

import collections
from collections import deque
import sys

def deque_program(N):
    de = collections.deque([])
    for _ in range(N):
        arr = list(map(str, sys.stdin.readline().split()))
        if arr[0] == "push_front":
            de.appendleft(arr[1])
        elif arr[0] == "push_back":
            de.append(arr[1])
        elif arr[0] == "pop_front":
            if len(de) == 0:
                print("-1")
            else:
                print(de[0])
                de.popleft()
        elif arr[0] == "pop_back":
            if len(de) == 0:
                print("-1")
            else:
                print(de[-1])
                de.pop()
        elif arr[0] == "size":
            print(len(de))
        elif arr[0] == "empty":
            if len(de) == 0:
                print("1")
            else:
                print("0")
        elif arr[0] == "front":
            if len(de) == 0:
                print("-1")
            else:
                print(de[0])
        elif arr[0] == "back":
            if len(de) == 0:
                print("-1")
            else:
                print(de[-1])

N = int(input())
deque_program(N)