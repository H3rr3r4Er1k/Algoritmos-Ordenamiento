class MergeSort:
    def __init__(self, vector, actualizar_resultado, actualizar_proceso):
        self.vector = vector
        self.actualizar_resultado = actualizar_resultado
        self.actualizar_proceso = actualizar_proceso

    def sort(self):
        self.merge_sort(self.vector)

    def merge_sort(self, vector):
        if len(vector) > 1:
            mid = len(vector) // 2
            left_half = vector[:mid]
            right_half = vector[mid:]

            self.merge_sort(left_half)
            self.merge_sort(right_half)

            i = j = k = 0

            while i < len(left_half) and j < len(right_half):
                if left_half[i] < right_half[j]:
                    vector[k] = left_half[i]
                    i += 1
                else:
                    vector[k] = right_half[j]
                    j += 1
                k += 1

            while i < len(left_half):
                vector[k] = left_half[i]
                i += 1
                k += 1

            while j < len(right_half):
                vector[k] = right_half[j]
                j += 1
                k += 1

            self.actualizar_resultado(vector)
            self.actualizar_proceso("Merge Sort: " + str(vector))


class QuickSort:
    def __init__(self, vector, actualizar_resultado, actualizar_proceso):
        self.vector = vector
        self.actualizar_resultado = actualizar_resultado
        self.actualizar_proceso = actualizar_proceso

    def sort(self):
        self.quick_sort(self.vector, 0, len(self.vector) - 1)

    def quick_sort(self, vector, low, high):
        if low < high:
            pivot_index = self.partition(vector, low, high)
            self.quick_sort(vector, low, pivot_index - 1)
            self.quick_sort(vector, pivot_index + 1, high)

    def partition(self, vector, low, high):
        pivot = vector[high]
        i = low - 1

        for j in range(low, high):
            if vector[j] < pivot:
                i += 1
                vector[i], vector[j] = vector[j], vector[i]

        vector[i + 1], vector[high] = vector[high], vector[i + 1]
        self.actualizar_resultado(vector)
        self.actualizar_proceso("Quick Sort: " + str(vector))


class HeapSort:
    def __init__(self, vector, actualizar_resultado, actualizar_proceso):
        self.vector = vector
        self.actualizar_resultado = actualizar_resultado
        self.actualizar_proceso = actualizar_proceso

    def sort(self):
        n = len(self.vector)
        for i in range(n // 2 - 1, -1, -1):
            self.heapify(self.vector, n, i)

        for i in range(n - 1, 0, -1):
            self.vector[i], self.vector[0] = self.vector[0], self.vector[i]
            self.heapify(self.vector, i, 0)

        self.actualizar_resultado(self.vector)
        self.actualizar_proceso("Heap Sort: " + str(self.vector))

    def heapify(self, vector, n, i):
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2

        if left < n and vector[i] < vector[left]:
            largest = left

        if right < n and vector[largest] < vector[right]:
            largest = right

        if largest != i:
            vector[i], vector[largest] = vector[largest], vector[i]
            self.heapify(vector, n, largest)
