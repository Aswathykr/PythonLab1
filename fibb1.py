number = 1
prev = 1
total = 0
while number < 4000000:
    if number % 2 == 0:
        total += number
    number, prev = number + prev, number

print(total)
