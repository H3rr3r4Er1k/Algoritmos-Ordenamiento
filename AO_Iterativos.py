##Bubble Sort
class BubbleSort:
    def __init__(self):
        self.name = "Bubble Sort"

    def sort(self, arr):
        n = len(arr)
        for i in range(n - 1):
            for j in range(n - i - 1):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
                    yield arr[:]

##Insert Sort
class InsertionSort:
    def __init__(self):
        self.name = "Insertion Sort"

    def sort(self, arr):
        for i in range(1, len(arr)):
            key = arr[i]
            j = i - 1
            while j >= 0 and arr[j] > key:
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = key
            yield arr[:]

##Selection Sort
class SelectionSort:
    def __init__(self):
        self.name = "Selection Sort"

    def sort(self, arr):
        n = len(arr)
        for i in range(n - 1):
            min_idx = i
            for j in range(i + 1, n):
                if arr[j] < arr[min_idx]:
                    min_idx = j
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
            yield arr[:]

##Shell Sort
class ShellSort:
    def __init__(self):
        self.name = "Shell Sort"

    def sort(self, arr):
        n = len(arr)
        gap = n // 2
        while gap > 0:
            for i in range(gap, n):
                temp = arr[i]
                j = i
                while j >= gap and arr[j - gap] > temp:
                    arr[j] = arr[j - gap]
                    j -= gap
                arr[j] = temp
                yield arr[:]
            gap //= 2
