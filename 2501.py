# 백준 2501
# 약수 구하기 문제

def divisor(num1, num2):
    N = int(num1)              # 자연수를 N에 저장
    K = int(num2)              # 뽑아낼 n번째 수를 K에 저장

    remainderList = []              # 약수 리스트

    # 1부터 입력한 자연수만큼 반복
    for i in range(1, N + 1):
        remainder = N % i           # 나눗셈
        if remainder == 0:          # 만약 나머지가 0과 같다면
            remainderList.append(i) # 약수 리스트에 추가

    if len(remainderList) < K:      # 만약 약수의 갯수보다 K의 수가 크다면
        print(0)                    # 0 출력
    else:                           # 아니라면(약수 범위 안에 있다면)
        print(remainderList[K - 1]) # K번째 약수 출력

inputNum = input("")            # 입력값 받기
number = inputNum.split()       # 띄어쓰기를 기준으로 끊기
divisor(number[0], number[1])