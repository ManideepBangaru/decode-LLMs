file =  open("rawfile.txt", "r")

# split the whole file into words delimited by space
all_words = []
for sentences in file.readlines():
    for words in sentences.split(" "):
        all_words.append(words)

from collections import Counter
word_frequencies = Counter(all_words)
print(word_frequencies)