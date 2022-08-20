# 백준 1991
# 트리 순회(완성/다시 해보기)

# Node 클래스
class Node:
    def __init__(self, node, l_node, r_node):
        self.node = node
        self.l_node = l_node
        self.r_node = r_node

# 전위 순회
# 전위 순회한 결과 : ABDCEFG // (루트) (왼쪽 자식) (오른쪽 자식)
def pre_order(current):
    # 공백 없이 한 번에 출력
    print(current.node, end="")
    # l_node에 node가 있다면
    if current.l_node != None:
        pre_order(tree[current.l_node])
    # r_node에 node가 있다면
    if current.r_node != None:
        pre_order(tree[current.r_node])

# 중위 순회
# 중위 순회한 결과 : DBAECFG // (왼쪽 자식) (루트) (오른쪽 자식)
def in_order(current):
    # l_node에 node가 있다면
    if current.l_node != None:
        in_order(tree[current.l_node])
    # 공백 없이 한 번에 출력
    print(current.node, end="")
    # r_node에 node가 있다면
    if current.r_node != None:
        in_order(tree[current.r_node])

# 후위 순회
# 후위 순회한 결과 : DBEGFCA // (왼쪽 자식) (오른쪽 자식) (루트)
def post_order(current):
    # l_node에 node가 있다면
    if current.l_node != None:
        post_order(tree[current.l_node])
    # r_node에 node가 있다면
    if current.r_node != None:
        post_order(tree[current.r_node])
    # 공백 없이 한 번에 출력
    print(current.node, end="")

N = int(input())
tree = {}

# N번만큼 반복
# 각 노드를 다 방문
for i in range(N):
    node, l_node, r_node = input().split()
    # 노드가 "."이라면 없는 걸로 인식
    if l_node == ".":
        l_node = None
    if r_node == ".":
        r_node = None
    tree[node] = Node(node, l_node, r_node)
    
pre_order(tree['A'])
print()
in_order(tree['A'])
print()
post_order(tree['A'])