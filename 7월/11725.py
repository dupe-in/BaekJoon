# 백준 11725
# 트리의 부모 찾기

class Node:
    def __init__(self, node1, node2):
        self.node1 = node1
        self.node2 = node2

def checkNode(node):
    print(tree[node])


N = int(input())
tree = {}

for i in range(N-1):
    node1, node2 = input().split()
    tree[node1] = Node(node1, node2)

checkNode(tree['1'])