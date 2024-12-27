file =  open("rawfile.txt", "r")

# split the whole file into words delimited by space
all_words = []
for sentences in file.readlines():
    for words in sentences.split(" "):
        all_words.append(words)

# word_frequencies = {}
# for word in all_words:
#     if word in word_frequencies:
#         word_frequencies[word] += 1
#     else:
#         word_frequencies[word] = 1

# print(word_frequencies)

# replace the above code with the following code
# Using Counter from collections module to count the frequency of each word in the list
from collections import Counter
word_frequencies = Counter(all_words)
print(word_frequencies)