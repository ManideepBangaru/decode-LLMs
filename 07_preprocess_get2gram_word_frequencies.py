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

bigram_words = []
window = []
for word in all_words:
    window.append(word)
    if len(window) >= 2:
        # add this new window to bigram_words at each iteration
        bigram_words.append(tuple(window.copy()))
        window.pop(0)

# from collections import Counter
# word_frequencies = Counter(bigram_words)
# print(word_frequencies.most_common(10))

next_words = {}
window = []
for word in all_words:
    window.append(word)
    if len(window) >= 2:
        if window[0] in next_words:
            next_words[window[0]].append(window[1])
            window.pop(0)
        else:
            next_words[window[0]] = [window[1]]
            window.pop(0)

import random
# random.seed(0)

input = "a"
for i in range(20):
    print(input, end=" ")
    input = random.choice(next_words[input])