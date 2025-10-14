"""
Word Occurrences
Estimate: 10 minutes
Actual:   5 minutes
"""

text = input("Text: ")
word_to_word_count = {}

for word in text.split():
    word_to_word_count[word] = word_to_word_count.get(word, 0) + 1

max_word_length = max(len(word) for word in word_to_word_count)

for word in sorted(word_to_word_count):
    print(f"{word:{max_word_length}} : {word_to_word_count[word]}")
