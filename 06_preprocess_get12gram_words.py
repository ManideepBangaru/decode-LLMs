file =  open("rawfile.txt", "r")

# split the whole file into words delimited by space
all_words = []
punctuation = '''!()-[]{};:'",<>./?@#$%^&*_~'''
for sentences in file.readlines():
    sentences = sentences.lower().strip(punctuation)
    sentences = sentences.replace("\n", "")
    for words in sentences.split(" "):
        if words:
            all_words.append(words)

# unigram_words = []
# for word in all_words:
#     unigram_words.append(word)

# print(unigram_words)

bigram_words = []
window = []
for word in all_words:
    window.append(word)
    if len(window) >= 2:
        # add this new window to bigram_words at each iteration
        bigram_words.append(tuple(window.copy()))
        window.pop(0)
print(bigram_words)

from collections import Counter
word_frequencies = Counter(bigram_words)
print(word_frequencies)