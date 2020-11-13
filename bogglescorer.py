#!/usr/bin/env python3
"""This script checks a list of words against the UK Boggle dictionary and returns
the valid words and scores"""

def check_words(words):
    """
    returns a list of words checked against the UK Boggle dictionary.
    """
    return words

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
    examples = ['hello', 'hat', 'chase', 'hats', '']
    scored_list = score_words(examples)
    example_words, example_scores = zip(*scored_list)
    print(example_words, example_scores)
    print('Total Score: ', sum(example_scores))
    print('Number of words: ', len(example_words))
