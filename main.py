numbers = []

for i in range(5):
    numbers.append(int(input()))

avg = sum(numbers) / len(numbers)

for num in numbers:
    if num > avg:
        print(num, end=' ')