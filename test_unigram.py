#!/usr/bin/python

def load_unigram_model(model_file):
  """Load a unigram map from a model file"""
  # Reading a model file
  prob_of = {}
  for line in open(model_file):
    line = line.strip()
    (word, P) = line.split("\t")
    # need to be in UTF-8
    word = word.decode("utf-8")
    prob_of[word] = float(P)
  return prob_of

def calc_prob(word, unigram):
  """Calcurate unigram probability with smoothing"""
  lambda_1   = 0.95
  lambda_unk = 1 - lambda_1
  V          = 1000000

  P = lambda_unk / V
  if word in unigram:
    P += lambda_1 * unigram[word]

  return P

def test_unigram(test_file, model_file):
  """Compute Entropy and Coverage"""
  import math
  W   = 0
  H   = 0
  unk = 0

  prob_of = load_unigram_model(model_file)

  # Evaluation and print results
  for line in open(test_file):
    line = line.strip()
    words = line.split()
    words.append("</s>")
    for word in words:
      W += 1
      P = calc_unigram(word, prob_of)

      if word not in prob_of:
        unk += 1

      H += -math.log(P, 2)

  print "entropy = %f"  % (H / W)
  print "coverage = %f" % (float(W - unk) / W)

if __name__ == "__main__":
  import sys
  test_unigram(sys.argv[1], sys.argv[2])
