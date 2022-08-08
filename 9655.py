# 백준 9655
# 돌 게임

def stone_game(N):
    if N % 2 == 0:
        print("CY")
    else:
        print("SK")

N = int(input())
stone_game(N)