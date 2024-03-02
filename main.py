x = input('sequence>>') # '1,23,45,56'

numbers = x.split(',')
numbers = list(map(int, numbers))

print(sum(numbers))


print(sum(numbers) / len(numbers))