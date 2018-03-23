import json
import time
import re
from textblob import TextBlob

#These files are left as examples. Use or not use it based on your text characteristics.

# opened_outputfiles = set()
#####################NEED TO CHANGE FILE NAMES HERE TO WHAT YOU WANT#################
with open('../../../raw_input/test.txt') as file:
    for line in file:
        python_tweet = json.loads(line.strip())
        if 'tweet' in python_tweet and 'text' in python_tweet['tweet']:
            if 'lang' in python_tweet['tweet'] and python_tweet['tweet']['lang'] == 'en':
                text = python_tweet['tweet']['text'].replace('\n', ' ').encode('ascii', 'ignore').decode('ascii', 'ignore').lower()
                # remove urls
                text = re.sub('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', ' ', text)

                # Expanding Contractions
                #he's (he has)
                text = re.sub(r"\'s", " ", text)
                text = re.sub(r"hes", "he has", text)
                text = re.sub(r"shes", "she has", text)
                text = re.sub(r"thats", "that has", text)
                text = re.sub(r"whos", "who has", text)
                text = re.sub(r"whats", "what has", text)
                text = re.sub(r"wheres", "where has", text)
                text = re.sub(r"whens", "when has", text)
                text = re.sub(r"whys", "why has", text)
                text = re.sub(r"hows", "how has", text)
                #you've (you have)
                text = re.sub(r"\'ve", " have", text)
                text = re.sub(r"shouldve", "should have", text)
                text = re.sub(r"wouldve", "would have", text)
                text = re.sub(r"couldve", "could have", text)
                text = re.sub(r"mightve", "might have", text)
                text = re.sub(r"mustve", "must have", text)
                text = re.sub(r"Ive", "I have", text)
                text = re.sub(r"youve", "you have", text)
                text = re.sub(r"weve", "we have", text)
                text = re.sub(r"theyve", "they have", text)

                text = re.sub(r"can\'t", "cannot", text)
                text = re.sub(r"won\'t", "will not", text)
                text = re.sub(r"n\'t", " not", text)
                text = re.sub(r"cant", "cannot", text)
                text = re.sub(r"isnt", "is not", text)
                text = re.sub(r"arent", "are not", text)
                text = re.sub(r"wasnt", "was not", text)
                text = re.sub(r"werent", "were not", text)
                text = re.sub(r"havent", "have not", text)
                text = re.sub(r"hasnt", "has not", text)
                text = re.sub(r"hadnt", "had not", text)
                text = re.sub(r"wont", "will not", text)
                text = re.sub(r"wouldnt", "would not", text)
                text = re.sub(r"dont", "do not", text)
                text = re.sub(r"doesnt", "does not", text)
                text = re.sub(r"didnt", "did not", text)
                text = re.sub(r"couldnt", "could not", text)
                text = re.sub(r"shouldnt", "should not", text)
                text = re.sub(r"mightnt", "might not", text)
                text = re.sub(r"mustnt", "must not", text)
                #are or am
                text = re.sub(r"\'re", " are", text)
                text = re.sub(r"\'m", " am", text)
                text = re.sub(r" im ", " i am ", text)
                text = re.sub(r" youre ", " you are ", text)
                text = re.sub(r" theyre ", " they are ", text)
                text = re.sub(r" whatre ", " what are ", text)
                #would or had but we choose just to use would
                text = re.sub(r"\'d", " would", text)
                text = re.sub(r" youd ", " you would ", text)
                text = re.sub(r" itd ", " it would ", text)
                text = re.sub(r" theyd ", " they would ", text)
                text = re.sub(r" thatd ", " that would ", text)
                text = re.sub(r" whod ", " who would ", text)
                text = re.sub(r" whatd ", " what would ", text)
                text = re.sub(r" whered ", " where would ", text)
                text = re.sub(r" whend ", " when would ", text)
                text = re.sub(r" whyd ", " why would ", text)
                text = re.sub(r" howd ", " how would ", text)
                #will
                text = re.sub(r"\'ll", " will", text)
                text = re.sub(r" ill ", " i will ", text) #taking a chance that people who mean sick ill are very low thus most who make this mistake mean I will
                text = re.sub(r" youll ", " you will ", text)
                text = re.sub(r" itll ", " it will ", text)
                text = re.sub(r" theyll ", " they will ", text)
                text = re.sub(r" thatll ", " that will ", text)
                text = re.sub(r" wholl ", " who will ", text)
                text = re.sub(r" whatll ", " what will ", text)
                text = re.sub(r" wherell ", " where will ", text)
                text = re.sub(r" whenll ", " when will ", text)
                text = re.sub(r" whyll ", " why will ", text)
                text = re.sub(r" howll ", " how will ", text)
                # remove special chars
                text = re.sub('[^a-zA-Z0-9]', ' ', text)
                text = ' '.join(text.strip().split())

                if text:
                    cur_date = time.strftime('%Y%m%d', time.gmtime(python_tweet['firstpost_date']))
                    #####################NEED TO CHANGE FILE NAMES HERE TO WHAT YOU WANT#################
                    cur_file = '../../../input/parsed_text_date_' + cur_date + '.txt'
                    target = open(cur_file, 'a')
                    # if target not in opened_outputfiles:
                    # 	opened_outputfiles.add(target)
                    target.write(text + '\n')
                    target.close()

# for file in opened_outputfiles:
# 	file.close()




				# if text:
				# 	cur_date = time.strftime('%Y%m%d', time.gmtime(python_tweet['firstpost_date']))
				# 	# cur_file = 'tweets_by_dates/parsed_tweets_date_' + cur_date + '.txt'
				# 	cur_file = 'verify_dates/parsed_tweets_date_' + cur_date + '.txt'
				# 	target = open(cur_file, 'a')
				# 	# if target not in opened_outputfiles:
				# 	# 	opened_outputfiles.add(target)
				# 	if 'timestamp_ms' in python_tweet['tweet']:
				# 		target.write(text + ' ' + str(python_tweet['firstpost_date']) + ' ' + str(python_tweet['tweet']['timestamp_ms']) + '\n')
				# 	else:
				# 		target.write(text + ' ' + str(python_tweet['firstpost_date']) + ' missing timestamp_ms \n')
				# 	target.close()