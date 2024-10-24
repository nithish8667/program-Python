def find_difference(n, arr):
    even_sum = sum(arr[i] for i in range(0, n, 2))
    odd_sum = sum(arr[i] for i in range(1, n, 2))
    return abs(even_sum - odd_sum)