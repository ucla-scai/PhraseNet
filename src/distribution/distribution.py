import os
import operator
import matplotlib.pyplot as plt
import numpy as np
import peakutils
import dist_helper_funcs as dhf
import statistics

#threshold value for same topic
topic_threshold = 0.5
#set of all unique phrases
phrase_set = set()
#dictionary storing counts info for each phrase
phrase_counts = {}
#list storing number of phrases in each day's tweets.
total_phrases_by_day = [0] * 91


#Calculate total_phrases_by_day
idx = 0
#####################NEED TO CHANGE FILE NAMES HERE TO WHAT YOU WANT#################
for tweets_file in sorted(os.listdir('../40topmine_results')):
	if '.txt' in tweets_file:
		count = 0
		#####################NEED TO CHANGE FILE NAMES HERE TO WHAT YOU WANT#################
		with open('../40topmine_results/' + tweets_file) as file:
			for line in file:
				line = line.strip().split(',')
				count = count + len(line)
		total_phrases_by_day[idx] = count #this has redundancies since not total number of unique phrases
		idx = idx + 1


#Calculate phrase_set and initialize phrase_counts
for filename in os.listdir('.'):
	if 'with' in filename:
		with open(filename) as file:
			for line in file:
				phrases = line.strip().split(':')[1].strip().split(',')
				for phrase in phrases:
					if phrase not in phrase_set:
						phrase_set.add(phrase)
						phrase_counts[phrase] = [0] * 92

#Calculate phrase_counts, update everyday counts for each phrase in phrase_set
count = 0

#####################NEED TO CHANGE FILE NAMES HERE TO WHAT YOU WANT#################
for len1file in sorted(os.listdir('../40fp_growth_results_len1')):
	if '.txt' in len1file:
		# print('Processing: ' + len1file)
		len1phrases = {}
		#####################NEED TO CHANGE FILE NAMES HERE TO WHAT YOU WANT#################
		with open('../40fp_growth_results_len1/' + len1file) as l1file:
			for line in l1file:
				line = line.strip().replace(')', '').split(' (')
				len1phrases[line[0]] = line[1]

		for phrase, info in phrase_counts.items():
			if phrase in len1phrases:
				tmp = len1phrases[phrase]
				phrase_counts[phrase][count] = int(tmp)
				phrase_counts[phrase][91] += int(tmp)
				if max(info[0:91]) == 0.0 and count == 90:
					print phrase
				#index 91: sum
		if phrase_counts[phrase][91] == 0.0:
			print phrase
		count = count + 1

# sorted_phrase_counts = sorted(phrase_counts.items(), key=lambda x:x[1][91]) #list of tuples

# Convert dict to list for ease of normalizing
#phrase_counts_list = [[phrase, info] for phrase, info in phrase_counts.items()]

# Normalize phrase_counts using total number of phrase of that day.
#for entry in phrase_counts_list:
	#for i in range(0, 91):
	#	entry[1][i] = entry[1][i]/total_phrases_by_day[i]
for phrase, info in phrase_counts.items():
	for i in range(0, 91):
		phrase_counts[phrase][i] = float(phrase_counts[phrase][i])/float(total_phrases_by_day[i])

# Continue normalize using max and min for the phrase frequencies
for phrase, info in phrase_counts.items():
	min_val = min(phrase_counts[phrase][0:91])
	max_val = max(phrase_counts[phrase][0:91])
	if max_val == 0:
		print phrase
		print sum(info)
		print phrase_counts[phrase]
	for i in range(0, 91):
		phrase_counts[phrase][i] = float(phrase_counts[phrase][i]-min_val)/float(max_val - min_val)
#for entry in phrase_counts_list:
#	min_val = min(entry[1][0:91])
#	max_val = max(entry[1][0:91])
#	for i in range(0, 91):
		#try:
#		entry[1][i] = (entry[1][i] - min_val)/(max_val - min_val)
		#except ZeroDivisionError:
			#print "We have a problem!!!"
			#print entry[0]

# Continue normalize using max and mean for the phrase frequencies
# for entry in phrase_counts_list:
# 	mean_val = statistics.mean(entry[1][0:91])
# 	max_val = max(entry[1][0:91])
# 	for i in range(0, 91):
# 		if entry[1][i] <= mean_val:
# 			entry[1][i] = 0
# 		else:
# 			entry[1][i] = (entry[1][i] - mean_val)/(max_val - mean_val)

#phrase_counts.clear()
#for entry in phrase_counts_list:
#	phrase_counts[entry[0]] = entry[1]

phrase_counts_out_file = open('phrase_counts.txt', 'w')

for phrase, info in phrase_counts.items():
	phrase_counts_out_file.write(phrase + ' : ' + ', '.join(str(x) for x in info) + '\n')

#Normalize data using max and min of the phrase occurance
# for entry in sorted_phrase_counts:
# 	min_val = min(entry[1][0:91])
# 	max_val = max(entry[1][0:91])
# 	for i in range(0, 91):
# 		entry[1][i] = (entry[1][i] - min_val)/(max_val - min_val)


#Phrases to plot
# toplot_m10 = [sorted_phrase_counts[i] for i in range(708,735)]
# toplot_l10 = [sorted_phrase_counts[i] for i in range(1208,1219)]

# toplot = toplot_m10 + toplot_l10

# Plot original data
# for obj in toplot:
# 	fig = plt.figure()
# 	xvals = list(range(91))
# 	yvals = obj[1][0:91]
# 	plt.plot(yvals)
# 	plt.plot(yvals, 'ro')
# 	plt.title(obj[0])
# 	plt.savefig(obj[0] + '.png')
# 	plt.close(fig)

# Plot normalized data
# for obj in toplot:
# 	fig = plt.figure()
# 	xvals = list(range(91))
# 	yvals = obj[1][0:91]
# 	plt.plot(yvals)
# 	plt.plot(yvals, 'ro')
# 	plt.title(obj[0])
# 	plt.savefig(obj[0] + '_normalized_2.png')
# 	plt.close(fig)


# # dictionary for weights for each phrase
# # phrase_weights = {}

# # index 92: variance
# # index 93: number of peaks
# # for normalized_entry in sorted_phrase_counts:
# # 	normalized_entry[1].append(np.var(normalized_entry[1][0:91]))
# # 	normalized_entry[1].append(len(peakutils.indexes(np.array(normalized_entry[1][0:91]), thres=0.1, min_dist=2).tolist()))
# # 	if normalized_entry[1][93] == 0:
# # 		normalized_entry[1][93] = 1
# #	phrase_weights[normalized_entry[0]] = 1/normalized_entry[1][93]


#Log file
log_file = open('log.txt', 'w')
time = 0

#Set for maintaining current topic set: [[topic id(key), cur topic desc, {curP1:w1, curP2:we...}],[...]...]
topic_set = []
#Dictionary for storing the distribution information over 91 days for each topic, {topic id(key):[0,...0],...}
topic_dist = {}
#Initializing a running topic id as a unique identifier for topics
topic_id = 0
#Dictionary for mapping topic_id to the complete topic_desc
topic_id_desc = {}

#Calculating topic_set and topic_dist
day = 0
for filename in sorted(os.listdir('.')):
	if 'with' in filename:
		log_file.write('===============================================================================================================================================================================\n')
		log_file.write('Processing file:' + filename + '\n')
		with open(filename) as file:
			for line in file:

				#dump the snapshot of the current topic set to a file.
				#os.system('mkdir 25topic_set')
				cur_topic_set_snapshot = open('topic_set/topic_set_' + str(time) + '.txt', 'w')
				for cur_topic in topic_set:
					cur_topic_set_snapshot.write(str(cur_topic[0]) + ' : ' + ','.join(cur_topic[1]) + '\n')
					for phrase, weight in cur_topic[2].items():
						cur_topic_set_snapshot.write('\t' + phrase + ' : ' + str(weight) + '\n')
				cur_topic_set_snapshot.close()
				#os.system('25topic_id_desc_mapping')
				#dump the snapshot of the topic_id to desc mapping to a file.
				cur_topic_id_desc_mapping_snapshot = open('topic_id_desc_mapping/topic_id_desc_mapping_' + str(time) + '.txt', 'w')
				for top_id, desc in topic_id_desc.items():
					cur_topic_id_desc_mapping_snapshot.write(str(top_id) + ' : ' + ','.join(desc) + '\n')
				cur_topic_id_desc_mapping_snapshot.close()

				topic = line.strip().split(':')[1].strip().split(',')
				log_file.write('\n---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\nCurrent topic from file:' + ','.join(topic) + '\n')
				merged_flag = 0

				tmp_highest_sim_score = 0
				tmp_highest_sim_topic_info = []
				tmp_highest_sim_cur_topic = []

				for cur_topic in topic_set:

					log_file.write('\tAt time: ' + str(time) + '. Comparing with: topic id: ' + str(cur_topic[0]) + ' with desc: ' + ','.join(cur_topic[1]) + '\n')

					rel = dhf.helper1(topic, cur_topic[1], cur_topic[2], phrase_counts, topic_threshold, day, topic_id_desc[cur_topic[0]])

					if rel[0] == 1:
						log_file.write('\tSimilarity score:' + str(rel[4]) + '\n')
						if rel[4] > tmp_highest_sim_score:
							tmp_highest_sim_score = rel[4]
							tmp_highest_sim_topic_info = rel[1:4]
							tmp_highest_sim_cur_topic = cur_topic
						#set flag
						merged_flag = 1
					else:
						log_file.write('\tSimilarity score: ' + str(rel[1]) + '\n')

				if merged_flag == 1:
					log_file.write('Merged with topic id: ' + str(tmp_highest_sim_cur_topic[0]) + '\n')
					#Update mapping in topic_id_desc to a new desc
					topic_id_desc[tmp_highest_sim_cur_topic[0]] = tmp_highest_sim_topic_info[2]
					#Update entry in topic_set
					tmp_highest_sim_cur_topic[1] = tmp_highest_sim_topic_info[0]
					tmp_highest_sim_cur_topic[2] = tmp_highest_sim_topic_info[1]
					#Update entry in topic_dist
					topic_dist[tmp_highest_sim_cur_topic[0]][day] = dhf.helper2(tmp_highest_sim_topic_info[0], phrase_counts, day)
				#if no merge performed, we need to add the new topic
				else: #merged_flag == 0:
					log_file.write('Added new topic to topic set\n')
					#add new mapping into topic_id_desc
					topic_id_desc[topic_id] = topic
					#add new entry into topic_set
					topic_phrase_mapping = {}
					for phr in topic:
						topic_phrase_mapping[phr] = phrase_counts[phr][day]
					topic_set_entry = [topic_id, topic, topic_phrase_mapping]
					topic_set.append(topic_set_entry)
					#add new entry into topic_dist
					topic_dist[topic_id] = [0]*91
					topic_dist[topic_id][day] = dhf.helper2(topic, phrase_counts, day)
					topic_id = topic_id + 1

				time = time + 1

		day = day + 1

log_file.close()


output_file = open('topic_dist.txt', 'w')
for topic_id, distribution in topic_dist.items():
	output_file.write(str(topic_id) + ' : ' + ','.join(str(x) for x in distribution) + '\n')
output_file.close()


output_file_2 = open('topic_id_map.txt', 'w')
for topic_id, topic_desc in topic_id_desc.items():
	output_file_2.write(str(topic_id) + ' : ' + ','.join(topic_desc) + '\n')
output_file_2.close()
