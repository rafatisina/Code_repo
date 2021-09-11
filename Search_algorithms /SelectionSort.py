def selection_sort(arr):
    size = len(arr)
    for i in range(size-1):
        min_index = i
        for j in range(min_index+1,size):
            if arr[j] < arr[min_index]:
                min_index = j
        if i != min_index:
            arr[i], arr[min_index] = arr[min_index], arr[i]


if __name__ == '__main__':
    elements = [234,3,1,56,34,12,9,12,1300]
    selection_sort(elements)
    print(elements)
