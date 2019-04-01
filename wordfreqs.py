from collections import Counter
from collections import OrderedDict


def desc_sort(input_dict):
    sorted_dict = [(i, input_dict[i]) for i in input_dict]
    sorted_dict.sort(key=lambda x: x[1], reverse=True)
    return sorted_dict


words = []
file = open("longtext.txt", 'r')
for line in file:
    for word in line.split():
        words.append(word)
counts = Counter(words)
counts = desc_sort(counts)
print(counts[:250])
