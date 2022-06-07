def read_file():
    file = open("headlines.txt", 'r')
    lines = file.readlines()

    for line in lines:
        i = 0
        words = line.split()
        for word in words:
            if word[0] == "‘":
                word = word[1:]
            if word[len(word) - 1] == "’":
                word = word[:len(word) - 1]
            if i == 0:
                startingWords.append(word)
            if i == len(words) - 1 and word in markovDictionary.keys():
                markovDictionary[word].append(None)
            elif i == len(words) - 1:
                markovDictionary[word] = [None]
            else:
                nxt = words[i + 1]
                if nxt[len(nxt) - 1] == "’":
                    nxt = nxt[:len(nxt) - 1]
                if nxt[0] == "‘":
                    nxt = nxt[1:]
                if word in markovDictionary.keys():
                    markovDictionary[word].append(nxt)
                else:
                    markovDictionary[word] = [nxt]
            i += 1


def return_starting_words():
    return startingWords


def return_dictionary():
    return markovDictionary


startingWords = []
markovDictionary = {}