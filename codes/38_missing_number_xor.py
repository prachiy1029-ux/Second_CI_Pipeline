def find_missing_number(numbers):
    n = len(numbers) + 1
    result = 0

    for i in range(1, n + 1):
        result ^= i

    for number in numbers:
        result ^= number

    return result 