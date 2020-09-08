def countsamewords(words):
    sample = {}
    for word in words:
        if word in sample:
            sample[word] = sample[word] + 1
        else:
            sample[word] = 1
    return sample


# def countsamewords(words, setwords):
#     sample = {}
#     for word in setwords:
#         sample[word] = 0
#     for word in words:
#         sample[word] = sample[word] + 1
#
#     return sample


words = []
with open("I have a dream.txt","r") as f:
    lines = f.readlines()
    # print(lines)
    for line in lines:
        line = line.replace(',', ' ')
        line = line.replace('.', ' ')
        line = line.replace('!', ' ')
        line = line.replace('?', ' ')
        line = line.replace(':', ' ')
        line = line.replace('"', ' ')
        line = line.replace('\'', ' ')
        line = line.replace('-', ' ')
        line = line.replace('\n', ' ')

        for word in line.split(' '):
            if word:
                words.append(word)
    set_words = set(words)
    print(len(words))
    print(len(set_words))
    temp = countsamewords(words)
    # temp = countsamewords(words, set_words)
    print(temp)

