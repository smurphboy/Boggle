#!/usr/bin/env python3
"""This script checks a list of words against the UK Boggle dictionary and returns
the valid words and scores"""

with open('sowpods.txt', 'r') as f:
    sowpods = f.readlines()
valid_words = [x.strip() for x in sowpods]

def check_words(words):
    """
    returns a list of words checked against the UK Boggle dictionary.
    """
    checked_words = []
    for word in words:
        if word.upper() in valid_words:
            checked_words.append(word)
    return checked_words

def score_words(words):
    """
    returns a zipped list of words and their scores.
    """
    scores = []
    bogglevalue = [0, 0, 0, 1, 1, 2,
                   3, 4, 11, 11, 11, 11,
                   11, 11, 11, 11, 11]
    for word in words:
        scores.append(bogglevalue[len(word)])
        scored = zip(words, scores)
    return scored

if __name__ == "__main__":
    examples = ['hello', 'hat', 'chase', 'catte', 'hats', '', 'fhir']
    print(examples)
    print(check_words(examples))
    scored_list = score_words(check_words(examples))
    example_words, example_scores = zip(*scored_list)
    print(example_words, example_scores)
    print('Total Score: ', sum(example_scores))
    print('Number of words: ', len(example_words))
    print('Total valid words:', len(valid_words))
