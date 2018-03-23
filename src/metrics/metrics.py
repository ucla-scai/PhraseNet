import numpy as np

#Unfortunately the event verification had to be done by hand to verify how well this algorithm was working.
#each event number produced by the algorithm had to be tied to an event number.

all_events = {}
for key in range(0, 91):
	all_events[str(key)] = []
'''Full amount of data - jaccard coefficient'''
all_events['0'].append(1)  # new years day (Happy New Year) Multiple peaks so should be not grabbed by algorithm
all_events['0'].append(2)  # new years
all_events['0'].append(7) # new years
all_events['0'].append(12) # new years
all_events['0'].append(18) # new years
all_events['0'].append(21)  # rose bowl
all_events['0'].append(4)  # sugar bowl
all_events['6'].append(84)  # boko haram attack and kill over 2,000 people - massacre
all_events['6'].append(71)  # paris terrorist attack
all_events['6'].append(72)  # paris terrorist attack
all_events['6'].append(74)  # paris terrorist attack
all_events['7'].append(75)  # iraq suicide bombing of a mosque
all_events['10'].append(94)  # cowboys packers game
all_events['10'].append(105)  # george clooney wins lifetime achievement award at golden globes
all_events['11'].append(21)  # ohio vs oregon
all_events['11'].append(70)  # ohio state champions
all_events['14'].append(122)  # pope visits phillipines
all_events['14'].append(127)  # oscar nominations come out
all_events['15'].append(122)  # pope visits phillipines
all_events['16'].append(122)  # pope visits phillipines
all_events['17'].append(122)  # pope visits phillipines
all_events['17'].append(142)  # seahawk/ packers game
all_events['17'].append(94)  # packers game
all_events['17'].append(144)  # seahawk/ packers game russell williams
all_events['18'].append(122)  # pope visits phillipines
all_events['20'].append(155)  # Obama's State of the Union
all_events['23'].append(164)  # FA Cup ("whacky day")
all_events['23'].append(168)  # Golden State Warrior, Klay Thompson, scores the most NBA points in a quarter and the most 3-pointers in a quarter
all_events['24'].append(184)  # SAG awards
all_events['24'].append(174)  # royal rumble
all_events['24'].append(179)  # royal rumble
all_events['24'].append(185)  # north american blizzard (snow storm)
all_events['25'].append(185)  # north american blizzard
all_events['25'].append(183)  # miss jamaica doesn't win miss universe
all_events['29'].append(199)  # Brandon Saad traded to Columbus by Chicago in 2016 NHL Draft
all_events['30'].append(216)  # UFC fight silva vs diaz
all_events['31'].append(211)  # superbowl related clusters
all_events['31'].append(215)  # superbowl related clusters (katy perry)
all_events['31'].append(142)  # superbowl related clusters
all_events['31'].append(218)  # tom brady
all_events['31'].append(228)  # superbowl related clusters Pete Carroll (Seahawks)
all_events['31'].append(226)  # superbowl related clusters Richard Sherman (Seahawks)
all_events['31'].append(213)  # superbowl halftime show
all_events['31'].append(227)  # missy
all_events['31'].append(225)  # katy perry and guest star, lenny kravitz
all_events['31'].append(209)  # Australian Opening Andy Murray
all_events['33'].append(234)  # harper lee announces she will release a sequel to kill a mockingbird
all_events['38'].append(108)  # Grammy Awards (kanye)
all_events['38'].append(252)  # Grammy Awards walking dead
all_events['38'].append(267)  # Grammy Awards (John Legend sang "Glory")
all_events['38'].append(265)  # Grammy Awards (Annie Lennox sings "take me to church" with Hozer)
all_events['38'].append(275)  # Jon Stewart of the Daily Show
all_events['38'].append(263)  # "better call saul" made it's premier showing (spin off tv show from breaking bad)
all_events['38'].append(255)  # Dean Smith passes away at 83
all_events['40'].append(273) # sony makes deal to bring spider man to disney's marvel
all_events['40'].append(258) # blackhawks tv releases a video explaining the coach's unusual Q-isms such as "peanut butter," "pickle head," and "crispy"
all_events['41'].append(246)  # Brian Williams is Suspended from NBC for fake iraq story
all_events['42'].append(283)  # Dr. Drake releases mixtape
all_events['44'].append(102)  # Valentine's Day
all_events['44'].append(277)  # Valentine's Day
all_events['44'].append(292)  # Valentine's Day
all_events['44'].append(195)  # Valentine's Day
all_events['44'].append(92)  # Valentine's Day
all_events['45'].append(303)  # NBA All Star Game
all_events['44'].append(250)  # Fifty shades of grey comes out
all_events['44'].append(293)  # Montclar fashion show on Feb 14, 2015 where models were raised up on platforms
all_events['48'].append(307)  # Mardi Gras ends on this day
all_events['49'].append(317)  # Ash Wednesday
all_events['52'].append(161)  # Oscars
all_events['52'].append(346)  # Oscars (Julie Andrews makes a surprise appearance with Lady Gaga for Sound of Music)
all_events['52'].append(340)  # Oscars (Patricia Arquette won best supporting actress)
all_events['52'].append(341)  # Oscars (Grand Budapest Hotel)
all_events['52'].append(344)  # Oscars (Sean Penn makes a joke that fails)
all_events['52'].append(343)  # Oscars (eddie redmayne won best actor)
all_events['52'].append(342)  # Oscars (joan rivers not in memorial)
all_events['54'].append(355)  # BRIT Awards
all_events['54'].append(358)  # BRIT Awards
all_events['56'].append(92)  # House Of Cards Season 3 came out on Netflix
all_events['56'].append(262)  # shawn mendes releases 'never be alone' official music video
all_events['57'].append(365)  # FCC passed a historic measure to more strictly regulate the Internet - net neutrality
all_events['58'].append(363)  # Leonard Nimoy Died feb 27
all_events['58'].append(364)  # Leonard Nimoy Died
all_events['60'].append(184)  # Shorty Award nominations announced
all_events['60'].append(432)  # Start of UNHRC
all_events['63'].append(427)  # Ferguson shooting - justic department release report - march 4
all_events['63'].append(380)  # 'Would u love me' released on itunes
all_events['63'].append(399)  # Harrison Ford's Plane Crashes
all_events['66'].append(409)  # Daylight Savings Time
all_events['66'].append(314)  # International Women's Day
all_events['66'].append(421)  # NFL Free Agency negotiations start
all_events['67'].append(415)  # ANCHESTER UNITED are ready to sell record buy Angel Di Maria in the summer as they step up their plans to bring in Wales star Gareth Bale
all_events['68'].append(424)  # Blurred Lines Copyright Infridgement Lawsuit settles
all_events['68'].append(414)  # Hardwell joines revealed records radio show - march 9
all_events['69'].append(425)  # march 10, 11, 17, 18, 20 UEFA Champions League
all_events['70'].append(425)  # march 10, 11, 17, 18, 20 UEFA Champions League
all_events['70'].append(428)  # Terry Pratchett dies
all_events['70'].append(432)  # bahrain talks of UNHRC
all_events['71'].append(432)  # bahrain talks of UNHRC
all_events['71'].append(430)  # Disney Gives Star Wars release date and name of film
all_events['72'].append(432)  # bahrain talks of UNHRC
all_events['72'].append(437)  # sammy and skate wassup music video released
all_events['74'].append(451)  # kendrick lamar releases album early
all_events['75'].append(441)  # stitches by shawn mendes is released on itunes
all_events['75'].append(448)  # julian camerena released dancer album
all_events['76'].append(29)   # St. Patrick's day
all_events['76'].append(161)   # St. Patrick's day
all_events['76'].append(269)   # St. Patrick's day (+paddy)
all_events['76'].append(387)   # St. Patrick's day
all_events['76'].append(445)   # St. Patrick's day
all_events['76'].append(457)   # St. Patrick's day
all_events['76'].append(452)   # St. Patrick's day (patty)
all_events['77'].append(465)  # "Empire" on Fox Season Finale
all_events['76'].append(425)  # march 10, 11, 17, 18, 20 UEFA Champions League
all_events['77'].append(425)  # march 10, 11, 17, 18, 20 UEFA Champions League
all_events['77'].append(5)  # march madness (mixed in with Feb and Jan)
all_events['77'].append(464)  # march madness (iowa, georgia)
all_events['78'].append(464)  # march madness
all_events['78'].append(468)  # solar eclipse
all_events['79'].append(425)  # march 10, 11, 17, 18, 20 UEFA Champions League
all_events['80'].append(464)  # march madness
all_events['80'].append(482)  # blackhawks hockey team has a good game
all_events['80'].append(477)  # El Clasico Soccer match
all_events['81'].append(485)  # Ted Cruz Announces President Candandancy
all_events['82'].append(502)  # German Plane goes down because of suicidal Pilot
all_events['83'].append(495)  # Zayne Malik leaves one Direction
all_events['84'].append(496)  # Clarkson dropped from Top Gear officially - march 25
all_events['84'].append(534)  # Religious Freedom Restoration Act
all_events['84'].append(541)  # Relgious Freedom Indiana Law
all_events['84'].append(501)  # Cricket world cup semi-finals australia vs india
all_events['87'].append(513)  # Nigeria Election
all_events['87'].append(509)  # KCA - march 28 but voting a month before so a lot of advertisements
all_events['87'].append(510)  # KCA - march 28 but voting a month before so a lot of advertisements
all_events['87'].append(512)  # KCA - march 28 but voting a month before so a lot of advertisements
all_events['87'].append(521)  # KCA - march 28 but voting a month before so a lot of advertisements
all_events['87'].append(525)  # Wrestle Mania WWE
all_events['87'].append(526)  # notre dame vs kentucky in march madness
all_events['88'].append(518)  # I heart radio awards - march 29
all_events['89'].append(539)  # naughty boy releases solo demo of zayne malik
all_events['90'].append(394)  # justin bieber roasting
all_events['90'].append(540)  # justin bieber roasting (martha stewart)
all_events['90'].append(537)  # april fools

output_all_events = open('all_events.txt', 'w')
for i in range(0, 91):
	output_all_events.write(str(i) + ' : ' + ','.join(str(x) for x in all_events[str(i)]) + '\n')
output_all_events.close()

# dictionary for storing peak start and end points for each topic/signal
signals_peak_lengths = {}
# number of peaks detected with our algorithm
total_number_of_peaks_detected = 0
ranked_list = []
counter = 1
denom_prec = []
with open('signals_peak_lengths.txt') as peak_lengths_file:
	for line in peak_lengths_file:
		line = line.strip().split(':')
		topic_id = line[0].strip()
		if len(line[1].strip()) == 0:
			signals_peak_lengths[topic_id] = []
		else:
			peak_lengths_str = line[1].strip().split(',')
			total_number_of_peaks_detected = total_number_of_peaks_detected + len(peak_lengths_str)
			peak_lengths = [x.split('-') for x in peak_lengths_str]
			signals_peak_lengths[topic_id] = peak_lengths
			ranked_list.append([topic_id, peak_lengths]) #each peak is an event candidate
			if counter % 25 == 0:
				denom_prec.append(total_number_of_peaks_detected)
			counter +=1
#print(signals_peak_lengths)

number_of_true_positive = 0
true_y_dict = {} #1 for a true event and a 0 for a true topic (this is to track the GT of event candidate peaks)
for i in range(0, 91):
	#print('i : ' + str(i))
	for topic_id in all_events[str(i)]:
		print('Processing topic_id ' + str(topic_id))
		topic_id = str(topic_id)
		if topic_id in signals_peak_lengths:
			if len(signals_peak_lengths[topic_id]) == 0:
				continue
			else:
				for time_period in signals_peak_lengths[topic_id]:
					#print('Processing time_period: ' + '-'.join(time_period))
					# allow 1 day of error
					if (int(time_period[0]) - 1) <= i and i <= (int(time_period[1]) + 1):
						#print('Correct!')
						number_of_true_positive = number_of_true_positive + 1
						if topic_id not in true_y_dict:
							true_y_dict[topic_id] = []
						true_y_dict[topic_id].append(time_period)
						#print topic_id
						#print('Before removal: ')
						#print(signals_peak_lengths[topic_id])
						signals_peak_lengths[topic_id].remove(time_period)
						#print('After removal: ')
						#print(signals_peak_lengths[topic_id])
						break
			# elif int(signals_peak_lengths[topic_id][0][0]) <= i and i <= int(signals_peak_lengths[topic_id][0][1]):
			# 	number_of_true_positive = number_of_true_positive + 1
			# 	signals_peak_lengths[topic_id] = []
num_prec = []
counter = 1
number_of_true_positive = 0
for topic_id, time_period in ranked_list: #go through the sorted list
	if topic_id in true_y_dict: #if the topic is a true event then count the peak as a true positive
		number_of_true_positive +=1
	if counter % 25 == 0:
		num_prec.append(number_of_true_positive)
	counter += 1

# total number of events happened
events_set = set()
for topic_id, event_peaks in all_events.items():
	# total_number_of_events = total_number_of_events + len(event_peaks)
	for peak in event_peaks:
		events_set.add(peak)
total_number_of_events = len(events_set)
precision = np.zeros((len(denom_prec),1))
for i in range(0,len(denom_prec)):
	precision[i] = float(num_prec[i])/float(denom_prec[i])
recall = float(number_of_true_positive)/float(total_number_of_events)
f1_score = np.zeros((len(denom_prec),1))
for j in range(0,len(denom_prec)):
	f1_score[j] = (2 * precision[j] * recall)/(precision[j] + recall)

output_results = open('metrics_results.txt', 'w')
for i in range(0,len(denom_prec)):
	output_results.write('---------------------------------------------------')
	output_results.write('Number of peaks detected by our algorithm: ' + str(denom_prec[i]) + '\n')
	output_results.write('True positive counts: ' + str(num_prec[i]) + '\n')
	output_results.write('Precision@' + str(i*25) + ': ' + str(precision[i]) + '\n')
	output_results.write('F1 score: ' + str(f1_score[i]) + '\n')
output_results.write('Total number of events happened: ' + str(total_number_of_events) + '\n')
output_results.write('Recall: ' + str(recall) + '\n')
output_results.close()
