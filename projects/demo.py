
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
Graph = {'A':{'a':'B','z':'Z'},
		 'B':{'c':'C','d':'D','e':'E'},
		 'Z':{'s':'S'},
		 'C':{'f':'A'}
		 }
from collections import Counter
from treelib import Node,Tree
tree = Tree()
def bfs_tree(graph, start):
	#根节点以start开始
	visited = [start]
	tree.create_node(start,start.lower())
	for edge, nextNode in graph[start].items():
		tree.create_node(nextNode, nextNode.lower(), parent=start.lower())
		queue = [nextNode]
		visited.append(nextNode)
		while queue:
			node = queue.pop(0)
			visited.append(node)
			for k, v in graph[node].items():
				if v not in visited:
					tree.create_node(v, v.lower(), parent=node.lower())
					if v in list(graph.keys()):
						queue.append(v)
					else:
						queue = []
				else:
					tree.create_node(v,v.upper(),parent=node.lower())
					queue = []
	tree.show()
	return tree.paths_to_leaves()

if __name__ == '__main__':
	print(bfs_tree(Graph,'A'))