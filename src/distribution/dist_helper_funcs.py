import operator


#check if topic1 and topic2 are the same, 
#	topic1: new topic read from file
# 	topic2: topic in the cur topic_set
#	if same return[1, union of phrases from two topics]
#   if different return 0
def helper1(topic1, topic2, topic2_phrases_dist, phrase_counts, topic_threshold, day, original_desc):
	# print('Calculating topic: ' + ','.join(topic1) + ' and topic: ' + ','.join(topic2) + '\n')
	# intersection = list(filter(lambda x: x in topic1, topic2))
	intersection_dict = {}

	# log_file = open('log.txt', 'a')

	for phr1 in topic1:
		# print('Checking phrase: ' + phr1 + '\n')
		tmp_highest_match = None
		tmp_highest_score = 0

		for phr2 in topic2:
			phr1_list = phr1.split(' ')
			phr2_list = phr2.split(' ')
			score = len(list(filter(lambda x: x in phr1_list, phr2_list)))/len(list(set().union(phr1_list, phr2_list)))
			if score > tmp_highest_score:
				tmp_highest_match = phr2
				tmp_highest_score = score

		if tmp_highest_score != 0:
			intersection_dict[phr1] = (tmp_highest_match, tmp_highest_score)
			# print('Matches: ' + phr1 + ' : ' + tmp_highest_match + ' . Score: ' + str(tmp_highest_score) + '\n')

		# print(intersection_dict)


	#####################################################
	# Calculate final score using the max of score_1 and score_2, if either is greater than the threshold, merge

	score_1 = 0
	score_2 = 0

	score_1_sum = 0
	for phr in topic1:
		score_1_sum = score_1_sum + phrase_counts[phr][day]
	score_1_intersection = 0
	for phr, info in intersection_dict.items():
		score_1_intersection = score_1_intersection + phrase_counts[phr][day]*info[1]
	score_1 = score_1_intersection/score_1_sum


	score_2_sum = 0
	for phr in topic2:
		score_2_sum = score_2_sum + topic2_phrases_dist[phr]
	score_2_intersection = 0
	for phr, info in intersection_dict.items():
		score_2_intersection = score_2_intersection + topic2_phrases_dist[info[0]]*info[1]
	score_2 = score_2_intersection/score_2_sum

	res = max(score_1, score_2)
	#######################################################



	########################################
	## Calculate final score using both topics

	# intersection_weight = 0
	# union_weight = 0

	# for phr1, info in intersection_dict.items():
	# 	intersection_weight = intersection_weight + phrase_counts[phr1][day]*info[1]
	# 	intersection_weight = intersection_weight + topic2_phrases_dist[info[0]]*info[1]

	# if intersection_weight == 0:
	# 	return[0, 0]

	# for phr in topic1:
	# 	union_weight = union_weight + phrase_counts[phr][day]
	# for phr in topic2:
	# 	union_weight = union_weight + topic2_phrases_dist[phr]

	# res = intersection_weight/union_weight

	########################################


	if res > topic_threshold:
		new_topic_desc = list(set(topic1).union(original_desc))
		new_phrase_weights = {}
		new_phrase_weights_tmp = {}

		for phr, weight in topic2_phrases_dist.items():
			new_phrase_weights_tmp[phr] = weight
		for phr in topic1:
			new_phrase_weights_tmp[phr] = phrase_counts[phr][day]

		# Take the 10 phrases with most weights
		if len(new_phrase_weights_tmp) > 10:
			new_phrase_weights_tmp_list = sorted(new_phrase_weights_tmp.items(), key=operator.itemgetter(1), reverse=True)
			new_phrase_weights_tmp_list = new_phrase_weights_tmp_list[0:10]
			for mapping in new_phrase_weights_tmp_list:
				new_phrase_weights[mapping[0]] = mapping[1]
		else:
			new_phrase_weights = new_phrase_weights_tmp.copy()


		topic1_new = []
		for phr, weight in new_phrase_weights.items():
			topic1_new.append(phr)

		# for phr in topic1:
		# 	new_phrase_weights[phr] = phrase_counts[phr][day]
		return [1, topic1_new, new_phrase_weights, new_topic_desc, res]
	else:
		return [0, res]


#calculate weight of a topic based on the phrase weights
def helper2(topic, phrase_counts, day):
	res = 0
	for phr in topic:
		res = res + phrase_counts[phr][day]
	return res
