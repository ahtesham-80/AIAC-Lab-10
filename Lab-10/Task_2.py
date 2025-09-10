def find_common(a, b):
    return list(set(a) & set(b))
print(find_common([1, 2, 3, 4, 5], [4, 5, 6, 7, 8]))
print(find_common([1, 2, 3, 4, 5], [6, 7, 8, 9, 10]))
print(find_common([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]))








