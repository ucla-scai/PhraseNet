import statistics
import matplotlib.pyplot as plt

# original_signal: original signal from distribution.py
# lag: number of signals in the moving window
# threshold: number of standard deviation away from the moving mean
# influence: influence of a new peak on the mean and std, between zero and 1
# std_start_val & avg_start_val: used to simulate the statistics information before the signal starts, in 
# 	reality this will be real time.
def find_peak(original_signal, lag, threshold, influence, std_start_val, avg_start_val, graph_no):
	signal_length = len(original_signal)
	peaks = [0] * signal_length
	padded_signal = [avg_start_val] * lag + original_signal
	filtered_signal = list(padded_signal[:lag])
	avgFilter = [avg_start_val]
	stdFilter = [std_start_val]

	for i in range(lag, lag + signal_length):
		if abs(padded_signal[i] - avgFilter[i - lag]) > threshold * stdFilter[i - lag]:
			if padded_signal[i] > avgFilter[i - lag]:
				peaks[i - lag] = 1
			else:
				peaks[i - lag] = 0

			filtered_signal.append(influence*padded_signal[i] + (1-influence)*avgFilter[i - lag])
			# Suppose average of noise is constant, when we detect a peak or an outlier, we should not include it in
			# the calculation of the new mean val. So we append the old mean.
			# filtered_signal.append(avgFilter[i - lag])
			avgFilter.append(statistics.mean(filtered_signal[(i - lag + 1):(i + 1)]))
			stdFilter.append(statistics.pstdev(filtered_signal[(i - lag + 1):(i + 1)]))
		else:
			peaks[i - lag] = 0
			filtered_signal.append(padded_signal[i])
			avgFilter.append(statistics.mean(filtered_signal[(i - lag + 1):(i + 1)]))
			stdFilter.append(statistics.pstdev(filtered_signal[(i - lag + 1):(i + 1)]))

	# yvals = list(peaks)
	# fig = plt.figure()
	# plt.plot(yvals)
	# plt.plot(yvals, 'ro')
	# plt.savefig('peak_detection/peaks/' + graph_no + '-' + str(lag) + '-' + str(threshold) + '-' + str(influence) + '-' + str(std_start_val) + '-peaks.png')
	# plt.close(fig)

	# yvals = list(filtered_signal)
	# fig = plt.figure()
	# plt.plot(yvals)
	# plt.plot(yvals, 'ro')
	# plt.savefig('peak_detection/filteredsigs/' + graph_no + '-' + str(lag) + '-' + str(threshold) + '-' + str(influence) + '-' + str(std_start_val) + '-filteredsig.png')
	# plt.close(fig)

	# yvals = list(avgFilter)
	# fig = plt.figure()
	# plt.plot(yvals)
	# plt.plot(yvals, 'ro')
	# plt.savefig('peak_detection/avg/' + graph_no + '-' + str(lag) + '-' + str(threshold) + '-' + str(influence) + '-' + str(std_start_val) + '-avg.png')
	# plt.close(fig)

	# yvals = list(stdFilter)
	# fig = plt.figure()
	# plt.plot(yvals)
	# plt.plot(yvals, 'ro')
	# plt.savefig('peak_detection/std/' + graph_no + '-' + str(lag) + '-' + str(threshold) + '-' + str(influence) + '-' + str(std_start_val) + '-std.png')
	# plt.close(fig)

	return peaks

class EventCadidate:
	def __init__(self, topic_id, num_peaks, max_peak_intensity, std):
		self.id = topic_id
		self.num_peaks = num_peaks
		self.max_intens = max_peak_intensity
		self.std = std

	def __repr__(self):
		return repr((self.id, self.num_peaks, self.max_intens, self.std))

	def __getitem__(self, index):
		if index < 4:
			if index == 0:
				return self.id
			elif index == 1:
				return self.num_peaks
			elif index == 2:
				return self.max_intens
			else:
				return self.std
		else:
			print "You do not have that mean fields in this class."
