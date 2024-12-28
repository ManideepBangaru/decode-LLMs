reader =  open("rawfile.txt", "r")
punctuation = '''!()-[]{};:'",<>./?@#$%^&*_~'''
succuessor_map = {}
window = []

# for line in reader:
#     for word in line.split():
#         clean_word = word.strip(punctuation).lower()
#         clean_word = clean_word.replace("\n", "")
#         clean_word = clean_word.strip()
#         window.append(clean_word)

#         if len(window) == 3:
#             key = tuple(window[:2])
#             value = window[2]
#             if key in succuessor_map:
#                 succuessor_map[key].append(value)
#                 window.pop(0)
#             else:
#                 succuessor_map[key] = [value]
#                 window.pop(0)

for line in reader:
    for word in line.split():
        clean_word = word.strip(punctuation).lower()
        clean_word = clean_word.replace("\n", "")
        clean_word = clean_word.strip()
        window.append(clean_word)

        if len(window) == 3:
            key = tuple(window[:2])
            value = window[2]
            if key in succuessor_map:
                succuessor_map[key].append(value)
                window.pop(0)
            else:
                succuessor_map[key] = [value]
                window.pop(0)

# # get the keys that have the most values
# max_key = max(succuessor_map, key=lambda x: len(succuessor_map[x]))
# print(max_key, succuessor_map[max_key])

import random
input = ("of","the")
for i in range(30):
    if i == 0:
        print(input[0], input[1], end=" ")
        input = (input[1], random.choice(succuessor_map[input[0], input[1]]))
    else:
        print(input[1], end=" ")
        input = (input[1], random.choice(succuessor_map[input[0], input[1]]))