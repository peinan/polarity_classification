#!usr/bin/env python
#coding: utf-8

fixed_data = open("fixed_review.txt", "r")
train_data = open("review.train", "w")
l = 1
for line in fixed_data:
	if l >= 501:
		train_data.write(line)
	l += 1
