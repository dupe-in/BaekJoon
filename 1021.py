# 백준 1021
# 회전하는 큐

import collections
import sys

def rotation_Q(N):
    de = collections.deque(list(range(1, N + 1)))           # deque 타입의 list 선언
    num_l = list(map(int, sys.stdin.readline().split()))    # 사용자가 입력한 수를 list에 저장
    count = 0
    for _ in range(10000):
        # 첫 번째 원소가 서로 같을 때 : 뽑아내기
        if de[0] == num_l[0]:
            de.popleft()
            num_l.pop(0)
            if len(num_l) != 0:
                pass
            else:                       # 만약 원소가 없다면 종료
                break
        # 첫 번째 원소가 서로 다를 때 : rotate
        elif de[0] != num_l[0]:
            de_i = de.index(num_l[0])   # num_l의 첫번째 원소가 de에 몇 번 인덱스에 있는지 확인
            if len(de) / 2 > de_i:      # 어느 방향으로 rotate 할 것인지 판단
                de.rotate(-1)           # 왼쪽으로 rotate
                count += 1
            else:
                de.rotate(1)            # 오른쪽으로 rotate
                count += 1
    print(count)                        # count 결과 출력


N, M = map(int, input().split())
rotation_Q(N)