from collections import Counter
from collections import OrderedDict


def sort(this_dict):
    sorted_dict = [(i, thisDict[i]) for i in thisDict]
    sorted_dict.sort(key=lambda x: x[1], reverse=True)
    return sortedDict


words = []
file = open("longtext.txt", 'r')
for line in file:
    for word in line.split():
        words.append(word)
counts = Counter(words)
counts = sort(counts)
print(counts[:250])
