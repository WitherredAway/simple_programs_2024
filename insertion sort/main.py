def insertion_sort(num_list):
    """Sort a list of numbers using insertion sort"""

    result = num_list.copy()
    n = 0
    for i in range(1, len(result)):
        key = result[i]
        j = i - 1
        while j >= 0 and key < result[j]:
            n += 1
            result[j + 1] = result[j]
            j -= 1
        else:
            result[j + 1] = key

    return n, result


# Take list input and turn each into an integer
num_list = list(
    map(int, input("Please input the numbers in the list separated by space: ").split())
)
assert len(num_list) > 0, "Empty list provided"
print(f"{num_list} is the original list")

n, sorted_list = insertion_sort(num_list)
print(f"{sorted_list} is the sorted list and took {n} iterations to sort.")
