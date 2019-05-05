# -*- coding: utf-8 -*-
# @Time    : 2019/4/10 10:17
# @Author  : zhengjiani
# @Software: PyCharm
# @Blog    ：https://zhengjiani.github.io/
"""
广度优先算法生成广度优先树
"""
#树的API
from projects.util import DirectWeightGraph
from treelib import Node,Tree
myGraph = {'A': ['B', 'C'],
         'B': ['C', 'D'],
         'C': ['D', 'F'],
         'D': ['C'],
         'E': ['F'],
         'F': ['C']}
poGraph = {"LoginPage": {"login": "HomePage"},
                           "HomePage": {"goto_user": "UserPage", "goto_stat": "StatPage", "goto_region": "RegionPage", "goto_sys": "SysPage", "goto_promotion": "PromotionPage", "goto_good": "GoodPage", "logout": "HomePage"},
                           "ModifyPasswordPage": {"modify_password": "ModifyPasswordPage"},
                           "UserPage": {"search_user": "UserPage", "add_user": "UserPage", "get_user_data": "UserPage"},
                           "AddressPage": {"search_address": "AddressPage"},
                           "CollectPage": {"search_collect": "CollectPage"},
                           "FootprintPage": {"search_footprint": "FootprintPage"},
                           "HistoryPage": {"search_history": "HistoryPage"},
                           "FeedbackPage": {"search_feedback": "FeedbackPage"},
                           "RegionPage": {"search_region": "RegionPage"},
                           "BrandPage": {"add_brand": "BrandPage", "search_brand": "BrandPage"},
                           "CategoryPage": {"search_category": "CategoryPage"},
                           "OrderPage": {"search_order": "OrderPage"},
                           "IssuePage": {"search_issue": "IssuePage"},
                           "KeywordPage": {"search_keyword": "KeywordPage", "add_keyword": "KeywordPage"},
                           "GoodPage": {"search_good": "GoodPage", "add_good": "GoodPage"},
                           "CreatePage": {"add_good": "GoodPage"},
                           "CommentPage": {"search_comment": "CommentPage"},
                           "PromotionPage": {"search_promotion": "PromotionPage", "add_ad": "AdPage"},
                           "TopicPage": {"add_topic": "TopicPage"},
                           "Groupon_rulePage": {"add_rule": "Groupon_rulePage", "search_rule": "Groupon_rulePage"},
                           "Groupon_activityPage": {"search_activity": "Groupon_activityPage"},
                           "SysPage": {"add_admin": "SysPage"},
                           "OsPage": {"add_object": "OsPage"}}

def bfs_traverse(graph,start):
    visited,queue = set(),[start]
    while queue:
        node = queue.pop(0)
        if node not in visited:
            visited.add(node)
            for nextNode in graph[node]:
                if nextNode not in visited:
                    queue.append(nextNode)
    return visited
def traverse_po(graph,start):
    """
    广度优先遍历有向图,除环
    :param graph: DirectWeightGraph
    :param start: LoginPage
    :return: bfstree
    """
    visited,queue = [],[start]
    while queue:
        node = queue.pop(0)
        for next_node in graph[node]:
            pass

def find_all_path(graph,start,end,path=[]):
    path = path + [start]
    print(path)
    if (start == end):
        return [path]
    if not start in graph:
        return None
    paths = []
    for node in graph[start]:
        if node not in path:
            newpaths = find_all_path(graph,node,end,path)
            for newpath in newpaths:
                paths.append(newpath)
    return paths
def find_shortest_path(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return path
    if start not in graph:
        return None
    shortest = None
    for node in graph[start]:
        if node not in path:
            newpath = find_shortest_path(graph, node, end, path)
            if newpath:
                if not shortest or len(newpath) < len(shortest):
                    shortest = newpath
    return shortest
if __name__ == '__main__':
    print(find_all_path(myGraph,'A','F'))
    print("----------------------------------------------------------------------")
    print(bfs_traverse(myGraph,'A'))
    print(find_shortest_path(myGraph,'A','F'))
    print("----------------------------------------------------------------------")
