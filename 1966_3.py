import numpy as np

T = int(input())                    # test case
index_list = []
for i in range(T):                  # repeat T times
    N, M = input().split()          # N : document pcs, M : current position
    N_int = int(N)                  # integer numbers
    M_int = int(M)                  # integer numbers
    doc_list = input().split()      # make document list(about important)
    index_list = list(range(N_int)) # make index list(about doc's index)    
    # print(doc_list)
    # print(index_list)
    most_imp = max(doc_list)        # find max result in doc_list : 5, 4, 9
    count = 0                       # how many print
    while True:          # repeat doc pcs(N times)
        if doc_list[0] < most_imp:  # if doc_list have bigger number than doc_list[0]
            doc_list.append(doc_list[0])        # Insert at the end
            doc_list.remove(doc_list[0])        # remove at the begin
            index_list.append(index_list[0])
            index_list.remove(index_list[0])
            # most_imp = max(doc_list)
            # print("2 :", doc_list)
            # print("3 :", doc_list)
            # change value's position
            # go to for n in range
        elif doc_list[0] == most_imp:
            if index_list[0] == M_int:  # if M_int and current position is same
                count += 1
                print(count)
                break
            doc_list.remove(doc_list[0])
            index_list.remove(index_list[0])
            # most_imp = max(doc_list)
            count += 1            
            # print("elif :", count)
        # else:                       # current doc is the most important,
        #     # print("d :", doc_list[n])
        #     del doc_list[0]
        #     count += 1
        # if most_imp not in doc_list and index_list[0] == M_int:      # if index_list[0] is same M_int
        #     print(count)
        #     break
        most_imp = max(doc_list)
        # if count == M_int:
        #     break
        # if doc_list.index(doc_list[0]) == index_list[0]:
        #     print(count)