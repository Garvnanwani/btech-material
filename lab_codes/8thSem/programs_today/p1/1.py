import re


def tokenize_words(corpus):
    # Tokenize the corpus into words
    words = re.findall(r'\b\w+\b', corpus.lower())
    return words


def calculate_word_count(words):
    # Calculate word count
    word_count = {}
    for word in words:
        word_count[word] = word_count.get(word, 0) + 1
    return word_count


def calculate_vocabulary_size(words):
    # Calculate size of vocabulary
    vocabulary = set(words)
    return len(vocabulary)


def tokenize_sentences(corpus):
    # Tokenize the corpus into sentences
    sentences = re.split(r'(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?)\s', corpus)
    return sentences


def remove_duplicate_sentences(sentences):
    # Remove duplicate sentences and assign unique ids
    unique_sentences = {}
    for index, sentence in enumerate(sentences):
        sentence = sentence.strip()
        if sentence not in unique_sentences:
            unique_sentences[sentence] = index + 1
    return unique_sentences


def display_document(sentences):
    # Display the document with unique sentence ids
    for sentence, sentence_id in sentences.items():
        print(f"ID: {sentence_id}\tSentence: {sentence}")


# Sample text corpus
corpus = '''
This is a sample text corpus. It contains multiple sentences. Some sentences may repeat, while others are unique. 
The program should tokenize the corpus into words and print the words along with their counts.
It should also calculate the size of the vocabulary by removing duplicates.
Finally, it should tokenize the corpus into sentences, remove duplicate sentences, assign unique IDs to each sentence, and display the document.
'''

# Step 1: Tokenize the corpus into words and print the words and word count
words = tokenize_words(corpus)
word_count = calculate_word_count(words)
print("Words and Word Count:")
for word, count in word_count.items():
    print(f"Word: {word}\tCount: {count}")

# Step 2: Calculate the size of the vocabulary
vocabulary_size = calculate_vocabulary_size(words)
print(f"Vocabulary Size: {vocabulary_size}")

# Step 3: Tokenize the corpus into sentences and print the sentences and sentence count
sentences = tokenize_sentences(corpus)
print("\nSentences and Sentence Count:")
for index, sentence in enumerate(sentences):
    print(f"Sentence {index+1}: {sentence}")

# Step 4: Prepare a new document by removing duplicate sentences, assigning unique ids, and display the document
unique_sentences = remove_duplicate_sentences(sentences)
print("\nUnique Sentences:")
display_document(unique_sentences)
