def float_binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    counter = 0

    if x > arr[high]:
        return (counter, -1)

    if x < arr[low]:
        return (counter, 0)

    while (low + 1) != high:
        counter += 1
        mid = (high + low) // 2
        # якщо x більше за значення посередині списку, ігноруємо ліву половину
        if arr[mid] < x:
            low = mid
        # якщо x менше за значення посередині списку, ігноруємо праву половину
        elif arr[mid] > x:
            high = mid

    return (counter, high)


arr = [2.1, 3.9, 4.5, 10.1, 40.7, 44.9, 46.8, 54.1]
x = 15
result = float_binary_search(arr, x)
if result[1] != -1:
    print(
        f"Element {arr[result[1]]} is present at index {result[1]}, it find by {result[0]} round of cycle."
    )
else:
    print("Element is not present in array.")
