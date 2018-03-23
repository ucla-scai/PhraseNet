import sys

date = sys.argv[1]

#####################NEED TO CHANGE FILE NAMES HERE TO WHAT YOU WANT#################
with open('../40fp_growth_results/' + date + '_fpgrowth_output.txt') as file:
	lines = [line.replace(')', '').split('(') for line in file]
	lines.sort(key=lambda x: int(x[1]), reverse=True)

#####################NEED TO CHANGE FILE NAMES HERE TO WHAT YOU WANT#################
with open('../40fp_growth_results_sorted/' + date + '_fpgrowth_output_sorted.txt', 'w') as fout:
	for newl in lines:
		fout.write(' '.join(newl))