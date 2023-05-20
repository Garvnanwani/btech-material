# Given a text corpus in a file, for N=2 as an input
# (i) Generate and print all the N-grams.
# (ii) Caleulate the N-gram count.
# (iii). Calculate the N-gram Probabilities.
# (iv) Calculate the Probability of a given test sentence.
# (v) Calculate the Perplexity of the model.

import pandas as pd
from nltk import ngrams


def generate(text, n):
    generated_ngrams = ngrams(text.split(), n)
    return [' '.join(grams) for grams in generated_ngrams]

def calculate_counts(ngrams):
    ngram_counts = {}
    for ngram in ngrams:
        if ngram in ngram_counts:
            ngram_counts[ngram] += 1
        else:
            ngram_counts[ngram] = 1
    return ngram_counts

def calculate_probabilities(ngram_counts, total_ngrams):
    ngram_probabilities = {}
    for ngram, count in ngram_counts.items():
        ngram_probabilities[ngram] = count / total_ngrams
    return ngram_probabilities

def calculate_sentence_probability(sentence, ngram_probabilities, n):
    sentence_probability = 1
    sentence_ngrams = generate(sentence, n)
    for ngram in sentence_ngrams:
        if ngram in ngram_probabilities:
            sentence_probability *= ngram_probabilities[ngram]
        else:
            return 0
    return sentence_probability

def calculate_perplexity(sentence, ngram_probabilities, n):
    sentence_probability = calculate_sentence_probability(sentence, ngram_probabilities, n)
    sentence_length = len(sentence.split())
    return pow(1/sentence_probability, 1/sentence_length)

def print_ngram_probabilities(ngram_probabilities):
    df = pd.DataFrame.from_dict(ngram_probabilities, orient='index', columns=['Ngrams             Probability'])
    print(df)

text = "this is this is a sample text"
n = 2

generated_ngrams = generate(text, n)

ngram_counts = calculate_counts(generated_ngrams)
print(ngram_counts)

ngram_probabilities = calculate_probabilities(ngram_counts, len(generated_ngrams))
print(ngram_probabilities)

sentence = "sample a"

sentence_probability = calculate_sentence_probability(sentence, ngram_probabilities, n)
print(sentence_probability)

perplexity = calculate_perplexity(sentence, ngram_probabilities, n)
print(perplexity)

# print_ngram_probabilities(ngram_probabilities)

# def find1(s,dct1):
#     try:
#         return dct1[s]
#     except:
#         return 0

# def print_probability_table(distinct_tokens,dct,dct1):
#     n=len(distinct_tokens)
#     l=[[]*n for i in range(n)]
#     for i in range(n):
#         denominator = dct[distinct_tokens[i]]
#         for j in range(n):
#             numerator = find1(distinct_tokens[i]+" "+distinct_tokens[j],dct1)
#             l[i].append(float("{:.3f}".format(numerator/denominator)))
#     return l
# d=input("Enter corpus = ")
# print("\n"+'\033[1m'+"Given Corpus"+'\033[0m')
# print(d)

# probability_table=print_probability_table(distinct_tokens,dct,dct1)
# print("\n"+'\033[1m'+"Probability table"+'\033[0m'+"\n")

# n=len(distinct_tokens)
# print("\t"+'\033[1m', end="")
# for i in range(n):
#     print(distinct_tokens[i],end="\t")
# print('\033[0m'+"\n")

# for i in range(n):
#     print('\033[1m',distinct_tokens[i],'\033[0m',end="\t")
#     for j in range(n):
#         print(probability_table[i][j],end="\t")
#     print("")
