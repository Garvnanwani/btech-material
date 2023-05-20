import re
import math
import pandas as pd

n = int(input("Enter the value of N: "))

def preprocess(text):
    text=text.lower()
    text=re.sub(r'[^a-zA-Z0-9\s]','',text)
    return text.split()

def generate_ngrams(words, n):
    ngrams = {}
    for i in range(len(words) - n + 1):
        ngram = ' '.join(words[i:i+n])
        ngrams[ngram] = ngrams.get(ngram, 0) + 1
    return ngrams

def calculate_probabilities(ngrams, n):
    probabilities = {}
    for ngram, count in ngrams.items():
        prefix = ' '.join(ngram.split()[:-1])
        prefix_count = sum([v for k, v in ngrams.items() if k.startswith(prefix)])
        probabilities[ngram] = (count) / (prefix_count)

    return probabilities

def calculate_sentence_probability(sentence, probabilities, n):
    words = preprocess(sentence)
    ngrams = generate_ngrams(words, n)
    sentence_probability = 1
    for ngram, count in ngrams.items():
        if(ngram in probabilities):
            sentence_probability *= probabilities.get(ngram, 1)
        else:
            return 0
    return sentence_probability

def calculate_perplexity(sentence, probabilities, n):
    probability = calculate_sentence_probability(sentence, probabilities, n)
    # return pow(2, - (1 / n) * math.log(probability))
    return pow(1/probability, 1/n)

with open('corpus.txt', 'r') as file:
    corpus = file.read()


words = preprocess(corpus)
print(words)

ngrams = generate_ngrams(words, n)
print(f"The {n}-grams can be given as:\n")
for ngram, count in ngrams.items():
    print(f"{ngram}:-> {count}")

probabilities = calculate_probabilities(ngrams, n)
print(f"The {n}-gram probabilities can be given as: \n")
for ngram, probability in probabilities.items():
    print(f"{ngram} :-> {probability}")

test_sentence = input("Enter the test sentence: ")

print(f"\nProbability of '{test_sentence}': {calculate_sentence_probability(test_sentence, probabilities, n)}")

print(f"Perplexity of model: {calculate_perplexity(test_sentence, probabilities, n)}")
