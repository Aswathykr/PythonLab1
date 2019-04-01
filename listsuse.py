def find_max(input_list):
    return max(input_list)


def reverse(input_list):
    return input_list[::-1]


def contains(input_list, element):
    return element in input_list


def odd_list(input_list):
    return input_list[0::2]


def running_total(input_list):
    total = 0
    for element in input_list:
        total = total + element
    return total


list1 = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
list2 = [3, 4, 5, 8, 13, 17, 35, 42]


print("MAX : ", find_max(list1))
print("MAX : ", find_max(list2))

print("Contains Pear in list : ", contains(list1, "pear"))
print("Contains 5 in list : ", contains(list2, 5))
print("Contains Per in list : ", contains(list1, "per"))
print("Contains 80 in list : ", contains(list2, 80))

print("Odd List : ", odd_list(list1))
print("Odd List : ", odd_list(list2))

print("Running total : ", running_total(list2))

print("Reverse List : ", reverse(list1))
print("Reverse List : ", reverse(list2))

