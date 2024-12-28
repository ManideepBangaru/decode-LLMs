reader =  open("rawfile.txt", "r")
punctuation = '''!()-[]{};:'",<>./?@#$%^&*_~'''
succuessor_map = {}
window = []

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

                