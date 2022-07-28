# 백준 1966
# 프린터 큐

T = int(input())                    # 테스트 케이스 입력
index_list = []
for i in range(T):
    N, M = input().split()
    N_int = int(N)
    M_int = int(M)
    doc_list = input().split()
    index_list = list(range(N_int)) # 인덱스를 비교할 index_list 생성
    most_imp = max(doc_list)        # doc_list 중에서 가장 중요도가 높은 것 변수에 저장
    count = 0                       # 몇 번째로 출력 되는지 확인하기 위함
    while True:                     # 몇 번 반복될지 모르기 때문에 while
        if doc_list[0] < most_imp:              # 현재 비교하는 문서 중요도 < 가장 높은 중요도
            doc_list.append(doc_list[0])        # 맨 뒤에 0번 인덱스 값을 삽입
            doc_list.remove(doc_list[0])        # 맨 앞의 값을 삭제
            index_list.append(index_list[0])    # 맨 뒤에 인덱스 번호 삽입
            index_list.remove(index_list[0])    # 맨 앞의 인덱스 번호를 삭제
        elif doc_list[0] == most_imp:           # 현재 비교하는 문서 중요도 = 가장 높은 중요도
            if index_list[0] == M_int:          # 현재 비교하는 문서의 초기 위치 = M
                count += 1                      # 출력 횟수 증가
                print(count)                    # 출력
                break                           # 종료
            # 현재 비교하는 문서 중요도 != 가장 높은 중요도
            doc_list.remove(doc_list[0])        # 맨 앞의 값을 삭제
            index_list.remove(index_list[0])    # 맨 앞의 인덱스 번호를 삭제
            count += 1                          # 출력 횟수 증가
        most_imp = max(doc_list)                # 가장 높은 중요도 재 지정