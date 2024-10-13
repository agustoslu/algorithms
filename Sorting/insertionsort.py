def insertion_sortR(arr, n):
    if n > 1:
        
        insertion_sortR(arr, n - 1)

        x = arr[n - 1]
        j = n - 2

        while j >= 0 and arr[j] > x: 
            arr[j + 1] = arr[j]
            j -= 1


        arr[j + 1] = x

if __name__ == "__main__":
    arr = [12, 11, 13, 5, 6]
    insertion_sortR(arr, len(arr))
    print(arr)
