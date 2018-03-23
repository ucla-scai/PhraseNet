import json

#These files are left as examples. Use or not use it based on your text characteristics.
output_tweets = open("extracted_tweets.txt", 'w')

with open('tweets.txt') as file:
	for line in file:
		python_tweet = json.loads(line.strip())
		if "tweet" in python_tweet:
			if "text" in python_tweet["tweet"]:
				text = python_tweet["tweet"]["text"].replace("\n", " ").encode('ascii','ignore').decode('ascii','ignore')
				if text:
					output_tweets.write(text + "\n")

output_tweets.close()