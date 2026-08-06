import random

comparison_count = 0


def min_max_dc(arr, low, high):
    global comparison_count

    # Base Case: One element
    if low == high:
        return arr[low], arr[low]

    # Base Case: Two elements
    if high == low + 1:
        comparison_count += 1
        if arr[low] < arr[high]:
            return arr[low], arr[high]
        else:
            return arr[high], arr[low]

    # Divide
    mid = (low + high) // 2

    left_min, left_max = min_max_dc(arr, low, mid)
    right_min, right_max = min_max_dc(arr, mid + 1, high)

    # Combine
    comparison_count += 1
    overall_min = left_min if left_min < right_min else right_min

    comparison_count += 1
    overall_max = left_max if left_max > right_max else right_max

    return overall_min, overall_max


def min_max_naive(arr):
    minimum = maximum = arr[0]
    comparisons = 0

    for x in arr[1:]:
        comparisons += 1
        if x < minimum:
            minimum = x

        comparisons += 1
        if x > maximum:
            maximum = x

    return minimum, maximum, comparisons


# --------------------------------------------------
# Demo Array (Different from Manual)
# --------------------------------------------------

arr = [18, 7, 29, 45, 3, 56, 11, 40, 24, 9]

comparison_count = 0

mn, mx = min_max_dc(arr, 0, len(arr) - 1)
dc_comparisons = comparison_count

_, _, naive_comparisons = min_max_naive(arr)

print("Array :", arr)
print("Minimum :", mn)
print("Maximum :", mx)
print("D&C Comparisons :", dc_comparisons)
print("Naive Comparisons :", naive_comparisons)

# --------------------------------------------------
# Performance Analysis
# --------------------------------------------------

print("\n")
print(f"{'Size':>8} {'DC Comps':>12} {'Naive Comps':>14} {'Formula':>12}")
print("-" * 52)

for size in [20, 200, 2000, 20000]:

    arr = [random.randint(1, 50000) for _ in range(size)]

    comparison_count = 0

    mn, mx = min_max_dc(arr, 0, len(arr) - 1)

    dc = comparison_count

    _, _, naive = min_max_naive(arr)

    formula = (3 * size) // 2 - 2

    print(f"{size:>8} {dc:>12} {naive:>14} {formula:>12}")
