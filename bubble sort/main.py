def bubble_sort(num_list):
    """Sort a list of numbers using bubble sort"""

    result = num_list.copy()
    length = len(result)
    n = 0
    for i in range(length):
        for j in range(length - i - 1):
            n += 1
            if result[j] > result[j + 1]:
                result[j], result[j + 1] = result[j + 1], result[j]
    return n, result


# Take list input and turn each into an integer
num_list = list(
    map(int, input("Please input the numbers in the list separated by space: ").split())
)
assert len(num_list) > 0, "Empty list provided"
print(f"{num_list} is the original list")

n, sorted_list = bubble_sort(num_list)
print(f"{sorted_list} is the sorted list and took {n} iterations to sort.")
