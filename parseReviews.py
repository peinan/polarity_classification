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
	for i in rtext:
		i = i.strip("\n")
	# print id, len(id)

	for i in range(len(id)):
		review[id[i]] = {"rating":rating[i], "text":rtext[i]}

	with open("text_out.txt", "w") as output_file:
		for k, v in review:
			output_file.write("%s %s\n", k, v)
		# output_file.write("test")

if __name__ == '__main__':
	import sys
	review = open("./sorted_data/apparel/negative.review")
	parseReviews(review)