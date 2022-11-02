numbers = list(map(int, input().split()))

avg = sum(numbers) / len(numbers)

for num in numbers:
    if num > avg:
        print(num, end=' ')