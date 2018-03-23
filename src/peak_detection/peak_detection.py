import peak_detection_funcs as pdf
import statistics
import operator
from collections import Counter
import numpy as np

#paramters for the peak detection function
lag = 5 #timestep window parameter
threshold = 3 #three standard deviations from the window mean
influence = 0.2
std_start_val = 0.2 #have to start with some values so the first events can be found
avg_start_val = 0
gamma = 350 #this is the first gamma of events that are produced in the sorted list. These are considered true events

#dictionary for storing the original signals for phrase clusters
original_signals = {}

#Read signals from the topic_dist file
with open('topic_dist.txt') as dist_file:
	for line in dist_file:
		line = line.strip().split(':')
		topic_id = int(line[0].strip())
		signal = list(map(float, line[1].strip().split(',')))
		original_signals[topic_id] = signal

#dictionary for storing signals after peaks are detected
peak_detected_signals = {}
for topic_id, topic_dist in original_signals.items():
	peak_detected_signals[topic_id] = pdf.find_peak(topic_dist, lag, threshold, influence, std_start_val, avg_start_val, str(topic_id))

output_peak_detected_signals = open('peak_detected_signals.txt', 'w')
for topic_id, topic_dist in peak_detected_signals.items():
	output_peak_detected_signals.write(str(topic_id) + ' : ' + ','.join(str(x) for x in topic_dist) + '\n')
output_peak_detected_signals.close()


#Merge peaks with distance <= 1 together for each signal in peak_detected_signals
#dictionary for storing signals after neighboring peaks are merged 
peak_detected_signals_merged = {}
for topic_id, signal in peak_detected_signals.items():
	signal_after_merging = list(signal)
	for i in range(1, 90):
		if signal_after_merging[i] == 0 and signal_after_merging[i - 1] == 1 and signal_after_merging[i + 1] == 1:
			signal_after_merging[i] = 1
	peak_detected_signals_merged[topic_id] = signal_after_merging

output_peak_detected_signals_merged = open('peak_detected_signals_merged.txt', 'w')
for topic_id, signal in peak_detected_signals_merged.items():
	output_peak_detected_signals_merged.write(str(topic_id) + ' : ' + ','.join(str(x) for x in signal) + '\n')
output_peak_detected_signals_merged.close()


#Apply the peak filter (0,1,0,0,1,1,1,1,0,0,0,0,1...) to the original signal and calculate new peak values for a peak that lasts for more than 1 day.
filtered_signals = {}
signals_peak_lengths = {}


for topic_id, signal_filter in peak_detected_signals_merged.items():
	filtered_signal = [0] * 91
	peak_lengths = []

	start_idx = -1
	end_idx = -1
	for i in range(0, 91):
		if signal_filter[i] == 1:
			if start_idx == -1:
				start_idx = i
			else:
				end_idx = i
		else:
			if start_idx != -1:
				end_idx = i
				final_peak_value = statistics.mean(original_signals[topic_id][start_idx:end_idx])
				filtered_signal[start_idx:end_idx] = [final_peak_value] * (end_idx - start_idx)
				peak_lengths.append([start_idx, end_idx - 1])
				
				start_idx = -1
				end_idx = -1
		
		if i == 90:
			if signal_filter[i] == 1:
				# this is not the first 1 in this peak
				if end_idx != -1:
					end_idx = 91
					final_peak_value = statistics.mean(original_signals[topic_id][start_idx:end_idx])
					filtered_signal[start_idx:end_idx] = [final_peak_value] * (end_idx - start_idx)
					peak_lengths.append([start_idx, end_idx - 1])

				# this is the first 1 in this peak
				else:
					filtered_signal[90] = original_signals[topic_id][90]
					peak_lengths.append([90, 90])

	filtered_signals[topic_id] = filtered_signal
	signals_peak_lengths[topic_id] = peak_lengths

output_filtered_signals = open('filtered_signals.txt', 'w')
for topic_id, signal in filtered_signals.items():
	output_filtered_signals.write(str(topic_id) + ' : ' + ','.join(str(x) for x in signal) + '\n')
output_filtered_signals.close()


# output_signals_peak_lengths = open('signals_peak_lengths.txt', 'w')
# for topic_id, peak_lengths in signals_peak_lengths.items():
# 	if len(peak_lengths) == 1:
# 		output_signals_peak_lengths.write(str(topic_id) + ' : ' + '-'.join(str(x) for x in peak_lengths[0]) + '\n')
# output_signals_peak_lengths.close()


# output_signals_peak_lengths = open('signals_peak_lengths.txt', 'w')
# for topic_id, peak_lengths in signals_peak_lengths.items():
# 	output_signals_peak_lengths.write(str(topic_id) + ' : ' + ','.join('-'.join(str(y) for y in x) for x in peak_lengths) + '\n')
# output_signals_peak_lengths.close()


# Collect statistics for each signal for ranking
# {signal_id : [number_of_peaks, standard_deviation_for_different_peak_values]}
signals_stats = {}
ranked_signals = []
for topic_id, filtered_signal in filtered_signals.items():
	# print('Processing topic: ' + str(topic_id))
	unique_values_in_signal = set(filtered_signal)
	unique_values_in_signal.remove(0)
	if unique_values_in_signal.__len__() == 0:
		signals_stats[topic_id] = [0, 0, 0]
	else: #make the number of peaks field negatives so we can order
		signals_stats[topic_id] = [-unique_values_in_signal.__len__(), np.max(filtered_signals[topic_id]), statistics.pstdev(list(unique_values_in_signal))]
		ranked_signals.append(pdf.EventCadidate(topic_id,-unique_values_in_signal.__len__(), np.max(filtered_signals[topic_id]), statistics.pstdev(list(unique_values_in_signal))))
output_signal_stats = open('signal_stats.txt', 'w')
for topic_id, stats in signals_stats.items():
	output_signal_stats.write(str(topic_id) + ' : ' + ','.join(str(x) for x in stats) + '\n')
output_signal_stats.close()
'''
#Rank by number of peaks(ascending), then std of peak values(descending):
ranked_signals_1 = sorted(signals_stats.items(), key=lambda x:(x[1][0], (0-x[1][1])))
output_ranked_signals_1 = open('signal_ranking_by_num_of_peaks_1st.txt', 'w')
output_ranked_signals_1.write('Topic_id : Number_of_peaks, std_of_peaks\n')
for signal in ranked_signals_1:
	output_ranked_signals_1.write(str(signal[0]) + ' : ' + str(signal[1][0]) + ', ' + str(signal[1][1]) + '\n')
output_ranked_signals_1.close()


#Rank by std of peak values first(descending), then number of peaks(ascending):
ranked_signals_2 = sorted(signals_stats.items(), key=lambda x:((0-x[1][1]), x[1][0]))
output_ranked_signals_2 = open('signal_ranking_by_std_of_peaks_1st.txt', 'w')
output_ranked_signals_2.write('Topic_id : Number_of_peaks, std_of_peaks\n')
for signal in ranked_signals_2:
	output_ranked_signals_2.write(str(signal[0]) + ' : ' + str(signal[1][0]) + ', ' + str(signal[1][1]) + '\n')
output_ranked_signals_2.close()
'''

ranked_signals = sorted(ranked_signals, key=operator.itemgetter(1,2,3), reverse=True)
output_ranked_signals = open('signal_ranking.txt', 'w')
output_ranked_signals.write('Topic_id : Number_of_peaks, max_peak_intensity, std_of_peaks\n')
for signal in ranked_signals:
	output_ranked_signals.write(str(signal[0]) + ' : ' + str(-signal[1]) + ', ' + str(signal[2])+ ', ' + str(signal[3]) + '\n')
output_ranked_signals.close()

top_event_cand = [x[0] for x in ranked_signals[:gamma]]
output_signals_peak_lengths = open('signals_peak_lengths.txt', 'w')
for topic_id in top_event_cand: #everything should be in order of the ranking in singals_peak_lengths
	output_signals_peak_lengths.write(str(topic_id) + ' : ' + ','.join('-'.join(str(y) for y in x) for x in signals_peak_lengths[topic_id]) + '\n')
output_signals_peak_lengths.close()


#See what events/topics occured on each day:
day_peaks = {}
for i in range(0, 91):
	peaks = []
	for topic_id, signal in filtered_signals.items():
		if signal[i] > 0:
			peaks.append([topic_id, signal[i]])
	peaks.sort(key=lambda x:x[1], reverse=True)
	day_peaks[i] = peaks

output_peaks_each_day = open('peaks_each_day.txt', 'w')
output_peaks_each_day.write('Day: [topic_id, weight]...\n')
for day, peaks in day_peaks.items():
	output_peaks_each_day.write(str(day) + ' : ' + ','.join(('[' + str(peak[0]) + ',' + str(peak[1]) + ']') for peak in peaks) + '\n')
output_peaks_each_day.close()











