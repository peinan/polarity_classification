#!usr/bin/env python
#coding:utf-8

from bs4 import BeautifulSoup

def parseReviews(rfile):
	soup     = BeautifulSoup(rfile)
	rID			 = soup.findAll("unique_id")
	rRating	 = soup.findAll("rating") 
	rRtext   = soup.findAll("review_text")

	id_ = []; id = []; rating = []; rtext = [];
	review = {}

	for i in rID:
		id_.append(i.text.strip())
	for i in id_:
		if i.isdigit() == False:
			id.append(i)

	for i in rRating:
		rating.append(i.text.strip())

	for i in rRtext:
		rtext.append(i.text.strip())
	for i in range(len(rtext)):
		rtext[i] = rtext[i].replace("\n", "")
	# for i in rtext:
	# 	# print i
	# 	i = i.replace("\n", "")
	# 	i = i.replace("\t", "")
		print rtext[i]
	# print id, len(id)

	output_file = open("fixed.review", "w")
	# print type(rtext[0]), type(id[0]), type(rating[0])
	for i in range(len(id)):
		# print type(rtext[0])
		rtext[i] = rtext[i].strip("\n")
		id[i] = id[i].encode("utf-8")
		rating[i] = rating[i].encode("utf-8")
		rtext[i] = rtext[i].encode("utf-8")
		# print len(id), len(rating), len(rtext)
		# print id[i], rating[i], rtext[i]
		output_file.write(id[i] + "\t" + rating[i] + "\t" + rtext[i] + "\n")
	# print type(rtext[0]), type(id[0]), type(rating[0])

	# for i in range(len(id)):
	# 	review[id[i]] = {"rating":rating[i], "text":rtext[i]}

	# # print review
	# output_file = open("fixed_review.txt", "w")
	# for k, v in review.items():
	# 	output_file.write("%s, " % k)
	# 	for k2, v2 in v.items():
	# 		output_file.write("%s, %s\n" % k2, v2)
	# output_file.close()

	# with open("text_out.txt", "w") as output_file:
	# 	for k, v in review:
	# 		output_file.write("%s %s\n", k, v)
		# output_file.write("test")

if __name__ == '__main__':
	import sys
	# review = open("./sorted_data/apparel/negative.review")
	review = open("./negative.review")
	parseReviews(review)