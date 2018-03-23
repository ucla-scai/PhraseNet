#!/bin/bash

#NOTE: Go through each Stage one-by-one. The first section is left uncommented but when moving
# to the second stage, just leave the "cd" lines uncommented as you move to the next stage
# This allows for debugging and you will thank me later. :)

#NOTE that in the python code there are places you have to by hand change the names. Please
#feel free to program that to be more dynamic. 
#You will see "#####################NEED TO CHANGE FILE NAMES HERE TO WHAT YOU WANT#################"
#within the code to tell you where you need to change the filenames.

# parameters for topmine commands
# minimum phrase frequency
minsup=40
# maximum size of phrase (number of words)
maxPattern=8
# significance threshold for merging unigrams into phrases
threshold=5

#Executing topmine commands
echo "Stage 1: topmine"
cd src/topicalPhrases/TopicalPhrases
mkdir ../../../output/40topmine_results
for file in ../../../input/40tweets_by_dates/*
do
	echo "Start processing $file ..."
	python src/clean_data
	./runDataPreparation.sh $file
 	./runCPM.sh $minsup $maxPattern $threshold
 	cp input_dataset_output/input_wordTraining.txt ../../../output/25topmine_results/${file##*/}
 	echo "Finished processing $file."
done
echo "Stage 1 finished!"



# # parameters for fpgrowth commands
# # minimum support
# minfpsup=8
# # minimum length of a frequent pattern
# minLen=2

# #Executing FPTree commands
# echo "Stage 2: FPTree"
#cd ../../../output/25topmine_results
# mkdir ../25fp_growth_results
# mkdir ../25fp_growth_results_sorted
# mkdir ../25fp_growth_results_len1
# for midFile in *
# do
# 	fileDate=$(echo $midFile|cut -f 4 -d '_'|cut -f 1 -d '.')
# 	echo "Processing file for date $fileDate"
# 	fileNameSuffix="_fpgrowth_output"
# 	len1FileNameSuffix="_fpgrowth_output_len1"
# 	outputfilename="$fileDate$fileNameSuffix.txt"
# 	len1outputfilename="$fileDate$len1FileNameSuffix.txt"
# 	../../src/FPTree/fpgrowth -s-$minfpsup -m$minLen -tm -k"," -f"," $midFile ../25fp_growth_results/$outputfilename
# 	../../src/FPTree/fpgrowth -s-$minfpsup -m1 -n1 -ts -k"," -f"," $midFile ../25fp_growth_results_len1/$len1outputfilename
# 	python ../../src/FPTree/postprocessing_sort.py $fileDate
# 	echo "Finished processing file for date $fileDate"
# done
# echo "Stage 2 finished!"


# #Executing python script for constructing edge list file and clustering.

# echo "Stage 3: Graph construction"
#cd ../25fp_growth_results_sorted
# mkdir ../../output/25clusters
# mkdir ../../output/25edges
# for fpFile in *
# do
# 	fpFileDate=$(echo $fpFile|cut -f 1 -d '_')
# 	echo "Now processing file for date $fpFileDate"
# 	python ../../src/graph/plot_graph.py $fpFileDate
# 	echo "Finished processing file for date $fpFileDate"
# done
# echo "Stage 3 finished!"


# #Executing plot phrase and topic distributions

# echo "Stage 4: Phrase and Topic Distribution"
#cd ../25clusters
# mkdir topic_set
# mkdir topic_id_desc_mapping
# python ../../src/distribution/distribution.py
# echo "Stage 4 finished!"




#Executing peak detection
# echo "Stage 5: Peak detection and cleanup"
#cd 0.5-jaccard_coeff
# python ../../../src/peak_detection/peak_detection.py
# echo "Stage 5 finished!"


#Executing metrics evaluation s

#echo "Stage 6: Metrics"
#python ../../../src/metrics/metrics.py
#echo "Stage 6 finished!"

