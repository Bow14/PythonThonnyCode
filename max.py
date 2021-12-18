def grabbing_max(numbers):
    if len(numbers) == 1:
        return grabbing_max(0)
    else:
        return max(numbers[0], grabbing_max(numbers[1:]))
    print(grabbing_max(2))
    