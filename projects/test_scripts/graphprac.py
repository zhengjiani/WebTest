# -*- coding: utf-8 -*-
# @Time    : 2019/4/11 21:13
# @Author  : zhengjiani
# @Software: PyCharm
# @Blog    ：https://zhengjiani.github.io/
from treelib import Node,Tree
tree = Tree()
myGraph = {'A': ['B', 'C'],
         'B': ['C', 'D'],
         'C': ['D', 'F'],
         'D': ['C'],
         'E': ['F'],
         'F': ['C']}
def bfs_traverse_po(graph,start):
    """
    广度优先遍历有向图
    :param graph: DirectWeightGraph
    :param start: LoginPage
    :return: bfstree
    """
    visited = set()
    queue = [start]
    while queue:
        node = queue.pop(0)
        if node not in visited:
            visited.add(node)
            for nextNode in graph[node]:
                if nextNode not in visited:
                    queue.append(nextNode)
    return visited
def bfs_tree(bfs_po,pos_id):
    tree.create_node(bfs_po[0],pos_id[0])
    len_pos = len(bfs_po)
    for i in range(1,len_pos):
        if i == 1:
            tree.create_node(bfs_po[1], pos_id[1], parent=pos_id[0])
        else:
            tree.create_node(bfs_po[i], pos_id[i], parent=pos_id[i-1])
    return tree
def encoding_tree_node_id(bfs_po):
    l=[]
    for i in bfs_po:
        l.append(i.lower())
    return l

if __name__ == '__main__':
    print("----------------------------------------------------------------------")
    bfs_po = list(bfs_traverse_po(myGraph, 'A'))
    print(bfs_po)
    pos_id = encoding_tree_node_id(bfs_po)
    print(pos_id)
    tree = bfs_tree(bfs_po,pos_id)
    tree.show()
