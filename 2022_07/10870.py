# 백준 10870
# 피보나치 수열 문제(완성)

N = int(input(""))          # N 입력

if N == 0:                  # N이 0일 때
    print(0)
elif N == 1:                # N이 1일 때
    print(1)
else:                       # N이 2 이상일 때
    num1 = 0                # 0번째 수
    num2 = 1                # 1번째 수
    for i in range(1, N):   # 피보나치 수열 계산
        num3 = num1 + num2
        num1 = num2
        num2 = num3
    print(num3)             # N번째 피보나치 수 출력