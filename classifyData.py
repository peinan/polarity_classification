#!usr/bin/env python
#coding: utf-8

from collections import defaultdict
bag_of_words = {}

fixed_data = open("fixed.review", "r")
train_data = open("train.review", "w")

for line in fixed_data:
	count_of 		 = defaultdict(int)
	total_count  = 0

	id, rating, text = line.split("\t")
	if rating < 3:
		rating = "-1"
	elif rating == 3:
		rating = "0"
	else:
		rating = "+1"
	words = text.split()
	for word in words:
		count_of[word] += 1
		total_count += 1
	bag_of_words[id] = {"rating":rating, "bow":count_of, "total_count":total_count}
	# print bag_of_words
	# break
with open("svm.review", "w") as svm_data:
	for id, v in bag_of_words.items():
		svm_data.write("%s\t" % (bag_of_words[id]["rating"]))
		for w, f in bag_of_words[id]["bow"].items():
			svm_data.write("%s:%s\t" % (w, float(f)/bag_of_words[id]["total_count"]))
		svm_data.write("\n")
# for id, v in bag_of_words.items():
# 	print (v[rating], v["bow"])
# 	break
# for k, v in bag_of_words.items():
# 	print v["rating"], v["bow"]
# 	break