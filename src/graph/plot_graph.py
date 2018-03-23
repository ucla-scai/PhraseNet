import networkx as nx
import matplotlib.pyplot as plt
import community
import sys
import os
import numpy as np

date = sys.argv[1]

G_nw = nx.Graph()
G_w = nx.Graph()
edge_set= set()

# produce an edge list file from fpgrowth result
#####################NEED TO CHANGE FILE NAMES HERE TO WHAT YOU WANT#################
output_weighted = open('../40edges/' + date + '_edges_with_weights.csv', 'w')
#####################NEED TO CHANGE FILE NAMES HERE TO WHAT YOU WANT#################
output_unweighted = open('../40edges/' + date + '_edges_without_weights.csv', 'w')


len1phrases = {}
#####################NEED TO CHANGE FILE NAMES HERE TO WHAT YOU WANT#################
with open('../40fp_growth_results_len1/%s_fpgrowth_output_len1.txt' %(date)) as l1file:
	for line in l1file:
		line = line.strip().replace(')', '').split(' (')
		len1phrases[line[0]] = int(line[1])

with open(date + '_fpgrowth_output_sorted.txt') as file:
# file produced by FPGrowth, then sorted
	for line in file:
		weight = line.strip().split('  ')[1]
		line = line.strip().split('  ')[0].split(',')

		for index in range(len(line) - 1):
			for second_index in range(index + 1, len(line)):
				# print(line[index], ' ', line[second_index])
				if(line[index] + '_' + line[second_index] not in edge_set):
					#new_weight = np.mean(np.array([float(weight)/float(len1phrases[line[index]]),float(weight)/float(len1phrases[line[second_index]])]))
					new_weight = float(weight)/(float(len1phrases[line[index]])+float(len1phrases[line[second_index]]))
					G_w.add_edge(line[index], line[second_index], weight=float(new_weight))
					G_nw.add_edge(line[index], line[second_index])
					edge_set.add(line[index] + '_' + line[second_index])
					output_weighted.write(line[index] + ',' + line[second_index] + ', %d,Undirected\n' %(float(new_weight)))
					output_unweighted.write(line[index] + ',' + line[second_index] + ',Undirected' + '\n')

output_weighted.close()
output_unweighted.close()

# community.best_partition uses the louvain method for community detection
partitions_nw = community.best_partition(G_nw)
partitions_w = community.best_partition(G_w)
clusters_nw = {}
clusters_w = {}

for key, value in partitions_nw.items():
	if(value not in clusters_nw):
		clusters_nw[value] = [key]
	else:
		clusters_nw[value].append(key)

for key, value in partitions_w.items():
	if(value not in clusters_w):
		clusters_w[value] = [key]
	else:
		clusters_w[value].append(key)


# output a file for all clusters of phrases
#####################NEED TO CHANGE FILE NAMES HERE TO WHAT YOU WANT#################
output_clusters_nw = open('../40clusters/' + date + '_no_weights_clusters.txt', 'w')
#####################NEED TO CHANGE FILE NAMES HERE TO WHAT YOU WANT#################
output_clusters_w = open('../40clusters/' + date + '_with_weights_clusters.txt', 'w')

for key, value in clusters_nw.items():
	output_clusters_nw.write(str(key) + ' : ' + ','.join(value) + '\n')


output_clusters_nw.close()

for key, value in clusters_w.items():
	output_clusters_w.write(str(key) + ' : ' + ','.join(value) + '\n')
output_clusters_w.close()




			
# plt.figure(num=None, figsize=(100, 100), dpi=120)
# plt.axis('off')
# fig = plt.figure(1)
# pos = nx.spring_layout(G)
# nx.draw_networkx_nodes(G,pos)
# nx.draw_networkx_edges(G,pos)
# nx.draw_networkx_labels(G,pos)

# cut = 1.00
# xmax = cut * max(xx for xx, yy in pos.values())
# ymax = cut * max(yy for xx, yy in pos.values())
# plt.xlim(0, xmax)
# plt.ylim(0, ymax)




# nx.draw_networkx(G, with_labels=True)
# plt.show()
# plt.savefig('10->_no_dup.png')
# plt.savefig('test.png')
# del fig
print('finished')
