# PhraseNet
Event Detection and Summarization using Phrase Networks

Abstract. Identifying events in real-time data streams such as Twitter
is crucial for many occupations to make timely, actionable decisions.
It is however extremely challenging because of the subtle difference between
“events” and trending topics, the definitive rarity of these events,
and the complexity of modern Internet’s text data. Existing approaches
often utilize topic modeling technique and keywords frequency to detect
events on Twitter, which have three main limitations: 1) supervised
and semi-supervised methods run the risk of missing important, breaking
news events; 2) existing topic/event detection models are base on
words, while the correlations among phrases are ignored; 3) many previous
methods identify trending topics as events. To address these limitations,
we propose the model, PhraseNet, an algorithm to detect and
summarize events from tweets. To begin, all topics are defined as a clustering
of high-frequency phrases extracted from text. All trending topics
are then identified based on temporal spikes of the phrase cluster frequencies.
PhraseNet thus filters out high-confidence events from other
trending topics using number of peaks and variance of peak intensity.
We evaluate PhraseNet on a three month duration of Twitter data and
show the both the efficiency and the effectiveness of our approach.

Keywords: Event Detection, Phrase Network, Event Summarization

Paper: http://ecmlpkdd2017.ijs.si/papers/paperID576.pdf