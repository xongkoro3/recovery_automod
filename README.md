# recovery_automod

The initial goal is to build a text filter on social networks. We would like to filter out drug-use posts and alcohol-abuse posts. 
Using the linguistic characterics (from LIWC) of posts as features, we build an automatic classifier.

scraper.py - data collection from reddit using its API, utilizing python library PRAW

count_occurrence.py - count the percentage of specific words in a post

convert_arff.py - convert csv to be Weka-readable *.arff file 

The next stage is to use topic modeling codes to generate the top 10 model words for each forum text.
