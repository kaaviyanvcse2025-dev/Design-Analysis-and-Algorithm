import random
import time
import sys

# Increase recursion limit for large arrays
sys.setrecursionlimit(20000)

# Global counter for comparisons
comparisons = 0

def partition(arr, low, high):
    """Standard Lomuto partition scheme."""
    global comparisons
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        comparisons += 1
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def randomized_partition(arr, low, high):
    """Randomized pivot selection to avoid worst-case performance."""
    rand_idx = random.randint(low, high)
    arr[rand_idx], arr[high] = arr[high], arr[rand_idx]
    return partition(arr, low, high)

def quicksort(arr, low, high):
    """Standard quicksort."""
    if low < high:
        pi = partition(arr, low, high)
        quicksort(arr, low, pi - 1)
        quicksort(arr, pi + 1, high)

def randomized_quicksort(arr, low, high):
    """Randomized quicksort."""
    if low < high:
        pi = randomized_partition(arr, low, high)
        randomized_quicksort(arr, low, pi - 1)
        randomized_quicksort(arr, pi + 1, high)

def run_sort(sort_fn, arr):
    """Helper to run a sort function and measure time & comparisons."""
    global comparisons
    comparisons = 0
    a = arr[:]  # Copy to avoid modifying original
    start = time.perf_counter()
    sort_fn(a, 0, len(a) - 1)
    elapsed = time.perf_counter() - start
    return a, comparisons, elapsed

if __name__ == "__main__":
    try:
        n = int(input("Enter number of elements: "))
        if n <= 0:
            raise ValueError("Number of elements must be positive.")
        arr = [random.randint(1, 10000) for _ in range(n)]

        print("\nOriginal array (first 20 elements):", arr[:20])

        sorted_arr, comp, t = run_sort(quicksort, arr)
        print(f"\nStandard Quicksort: {comp} comparisons, {t:.6f} seconds")

        sorted_arr, comp, t = run_sort(randomized_quicksort, arr)
        print(f"Randomized Quicksort: {comp} comparisons, {t:.6f} seconds")

    except ValueError as e:
        print("Error:", e)