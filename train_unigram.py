#!/usr/bin/env python

def train_unigram(training_file, model_file):
  """Train unigram counts"""
  from collections import defaultdict
  count_of    = defaultdict(int)
  total_count = 0

  for line in open(training_file):
    line = line.strip()
    words = line.split()
    words.append("</s>")
    for word in words:
      count_of[word] += 1
      total_count    += 1

  with open(model_file, "w") as model:
    for word, count in count_of.items():
      probability = float(count_of[word]) / total_count
      model.write("%s\t%f\n" % (word, probability))
      

if __name__ == "__main__":
  import sys
  train_unigram(sys.argv[1], sys.argv[2])
