def contains(elements, value):
    left, right = 0, len(elements) - 1
    print(left)
    print(right)
    
    if left <= right:
        middle = (left + right) // 2

        if elements[middle] == value:
            return True
        if elements[middle] < value:
            return contains(elements[middle + 1:], value)
        elif elements[middle] > value:
            return contains(elements[:middle], value)

    return False


lst = [34, 22, 50, 25, 50, 28]
# binary search required sorted list
print(contains(sorted(lst), 25))        
