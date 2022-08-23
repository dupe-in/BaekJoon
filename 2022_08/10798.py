# 백준 10798
# 세로 읽기
# idea : 2차원 배열을 받아서 for문을 이용, end=""로 출력
import sys

def read_word():
    # 띄어쓰기 없는 입력을 하나씩 나눠서 list에 저장
    word_l = [list(sys.stdin.readline().rstrip()) for _ in range(5)]
    result_l = []           # 세로 읽은 결과를 저장할 list
    for a in range(15):     # 최대 15개의 글자
        for i in range(5):  # 5줄의 입력
            try:
                result_l.append(word_l[i][a])
            except IndexError:  # 현재 위치에 element가 없을 때
                continue
    # list 형태로 출력 -> 괄호와 콤마 제거
    for n in range(len(result_l)):
        print(result_l[n], end="")

read_word()