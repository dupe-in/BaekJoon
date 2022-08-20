# 백준 2252
# 줄 세우기
import sys
import collections

def make_line(N, M):
    student_l = collections.deque([])
    for a in range(M):
        A, B = map(str, sys.stdin.readline().split())
        if a == 0:
            student_l.append(A)
            student_l.append(B)
        else:
            if A in student_l:
                student_l.append(B)
            elif B in student_l:
                i = student_l.index(B)
                student_l.insert(i, A)
            else:
                student_l.append(A)
                student_l.append(B)
    for i in range(len(student_l)):
        print(student_l[i], end=' ')


N, M = map(int, sys.stdin.readline().split())
make_line(N, M)