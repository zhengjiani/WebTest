"""
广度优先遍历图生成遍历树
"""
import json
from collections import defaultdict
def tree():
	return defaultdict(tree)
pages=tree()
pages['LoginPage']['login'] = 'HomePage'
print(json.dumps(pages))

taxonomy = tree()
taxonomy['Animalia']['Chordata']['Mammalia']['Carnivora']['Felidae']['Felis']['cat']
taxonomy['Animalia']['Chordata']['Mammalia']['Carnivora']['Felidae']['Panthera']['lion']
taxonomy['Animalia']['Chordata']['Mammalia']['Carnivora']['Canidae']['Canis']['dog']
taxonomy['Animalia']['Chordata']['Mammalia']['Carnivora']['Canidae']['Canis']['coyote']
taxonomy['Plantae']['Solanales']['Solanaceae']['Solanum']['tomato']
taxonomy['Plantae']['Solanales']['Solanaceae']['Solanum']['potato']
taxonomy['Plantae']['Solanales']['Convolvulaceae']['Ipomoea']['sweet potato']
def dicts(t):
	return {k:dicts(t[k]) for k in t}
print(dicts(taxonomy))

# def add(t,path):
# 	for node in path:
# 		t=t[node]
# add(taxonomy,'Animalia>Chordata>Mammalia>Cetacea>Balaenopteridae>Balaenoptera>blue whale'.split('>'))
