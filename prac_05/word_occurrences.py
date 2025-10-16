"""
Word Occurrences
Estimate: 15 minutes
Actual:   35 minutes
"""

string = "this is a collection of words of nice words this is a fun thing it is"  # input("Text: ")
words = string.split()
word_to_count = {}
for word in words:
    if word in word_to_count:
        word_to_count[word] += 1
    else:
        word_to_count[word] = 1
sorted_words_to_count = dict(sorted(word_to_count.items()))
for word, count in sorted_words_to_count.items():
    print(f"{word:{max(len(word) for word in sorted_words_to_count)}} : {count}")
