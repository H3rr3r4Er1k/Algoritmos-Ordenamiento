##Quick Sort
class QuickSort:
    def __init__(self):
        self.name = "Quick Sort"

    def sort(self, arr):
        yield from self.quick_sort_recursive(arr, 0, len(arr) - 1)

    def quick_sort_recursive(self, arr, low, high):
        if low < high:
            pivot_index = self.partition(arr, low, high)
            yield arr[:]
            yield from self.quick_sort_recursive(arr, low, pivot_index - 1)
            yield from self.quick_sort_recursive(arr, pivot_index + 1, high)

    def partition(self, arr, low, high):
        pivot = arr[high]
        i = low - 1
        for j in range(low, high):
            if arr[j] < pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1

##Merge Sort
class MergeSort:
    def __init__(self):
        self.name = "Merge Sort"

    def sort(self, arr):
        yield from self.merge_sort_recursive(arr)

    def merge_sort_recursive(self, arr):
        if len(arr) > 1:
            mid = len(arr) // 2
            left_half = arr[:mid]
            right_half = arr[mid:]

            yield from self.merge_sort_recursive(left_half)
            yield from self.merge_sort_recursive(right_half)

            i = j = k = 0
            while i < len(left_half) and j < len(right_half):
                if left_half[i] < right_half[j]:
                    arr[k] = left_half[i]
                    i += 1
                else:
                    arr[k] = right_half[j]
                    j += 1
                k += 1
            while i < len(left_half):
                arr[k] = left_half[i]
                i += 1
                k += 1
            while j < len(right_half):
                arr[k] = right_half[j]
                j += 1
                k += 1
        yield arr[:]

##Heap Sort
class HeapSort:
    def __init__(self):
        self.name = "Heap Sort"

    def sort(self, arr):
        n = len(arr)

        for i in range(n // 2 - 1, -1, -1):
            self.heapify(arr, n, i)
            yield arr[:]

        for i in range(n - 1, 0, -1):
            arr[i], arr[0] = arr[0], arr[i]
            self.heapify(arr, i, 0)
            yield arr[:]

    def heapify(self, arr, n, i):
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2

        if left < n and arr[left] > arr[largest]:
            largest = left

        if right < n and arr[right] > arr[largest]:
            largest = right

        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            self.heapify(arr, n, largest)
