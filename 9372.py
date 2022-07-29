# 백준 9372
# 상근이의 여행
import sys

T = int(sys.stdin.readline())
start_list = []
end_list = []

for t in range(T):
    N, M = [int(x) for x in sys.stdin.readline().split()]
    for p in range(M):
        a, b = sys.stdin.readline().split()
        start_list.append(a)
        end_list.append(b)
        temp_list = start_list + end_list
    final_route = list(set(temp_list))
    print(len(final_route) - 1)
    start_list.clear()
    end_list.clear()