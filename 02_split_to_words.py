file =  open("rawfile.txt", "r")

# split the whole file into words delimited by space
all_words = []
for sentences in file.readlines():
    for words in sentences.split(" "):
        all_words.append(words)

print(all_words[0])
print(all_words[1])
print(all_words[2])