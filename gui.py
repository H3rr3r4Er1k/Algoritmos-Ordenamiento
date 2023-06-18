import tkinter as tk
from tkinter import messagebox
import random
from AlgoritmosOrdenamiento.AO_Iterativos import BubbleSort, InsertionSort, SelectionSort, ShellSort
from AlgoritmosOrdenamiento.AO_Recursivos import QuickSort, MergeSort, HeapSort


class SortingGUI:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Ordenamiento de Números")
        self.window.geometry("600x600")

        self.frame = tk.Frame(self.window)
        self.frame.pack(pady=20)

        self.label_size = tk.Label(self.frame, text="Tamaño:")
        self.label_size.grid(row=0, column=0, padx=10)
        self.entry_size = tk.Entry(self.frame)
        self.entry_size.grid(row=0, column=1, padx=10)

        self.button_generate = tk.Button(self.frame, text="Generar Arreglo", command=self.generate_array)
        self.button_generate.grid(row=0, column=2, padx=10)

        self.original_array_label = tk.Label(self.window, text="Array sin ordenar:", font=("Arial", 14))
        self.original_array_label.pack(pady=10)

        self.listbox_results = tk.Listbox(self.window, width=50, font=("Courier", 12))
        self.listbox_results.pack(pady=10, expand=True, fill=tk.BOTH)

    def generate_array(self):
        try:
            size = int(self.entry_size.get())
            if size <= 0:
                raise ValueError
            numbers = random.sample(range(1, size * 10 + 1), size)
            self.original_array_label.config(text=f"Array sin ordenar: {numbers}")
            self.sort_array(numbers)
        except ValueError:
            messagebox.showerror("Error", "Por favor ingresa un tamaño válido.")

    def sort_array(self, numbers):
        self.listbox_results.delete(0, tk.END)
        self.listbox_results.insert(tk.END, "Ordenando con Bubble Sort:")
        bubble_sort = BubbleSort()
        for iteration in bubble_sort.sort(numbers.copy()):
            self.listbox_results.insert(tk.END, iteration)
            self.listbox_results.update()
            self.listbox_results.after(500)
        self.listbox_results.insert(tk.END, "Array ordenado con Bubble Sort:\n{}".format(numbers))

        self.listbox_results.insert(tk.END, "Ordenando con Insertion Sort:")
        insertion_sort = InsertionSort()
        for iteration in insertion_sort.sort(numbers.copy()):
            self.listbox_results.insert(tk.END, iteration)
            self.listbox_results.update()
            self.listbox_results.after(500)
        self.listbox_results.insert(tk.END, "Array ordenado con Insertion Sort:\n{}".format(numbers))

        self.listbox_results.insert(tk.END, "Ordenando con Selection Sort:")
        selection_sort = SelectionSort()
        for iteration in selection_sort.sort(numbers.copy()):
            self.listbox_results.insert(tk.END, iteration)
            self.listbox_results.update()
            self.listbox_results.after(500)
        self.listbox_results.insert(tk.END, "Array ordenado con Selection Sort:\n{}".format(numbers))

        self.listbox_results.insert(tk.END, "Ordenando con Shell Sort:")
        shell_sort = ShellSort()
        for iteration in shell_sort.sort(numbers.copy()):
            self.listbox_results.insert(tk.END, iteration)
            self.listbox_results.update()
            self.listbox_results.after(500)
        self.listbox_results.insert(tk.END, "Array ordenado con Shell Sort:\n{}".format(numbers))

        self.listbox_results.insert(tk.END, "Ordenando con Quick Sort:")
        quick_sort = QuickSort()
        for iteration in quick_sort.sort(numbers.copy()):
            self.listbox_results.insert(tk.END, iteration)
            self.listbox_results.update()
            self.listbox_results.after(500)
        self.listbox_results.insert(tk.END, "Array ordenado con Quick Sort:\n{}".format(numbers))

        self.listbox_results.insert(tk.END, "Ordenando con Merge Sort:")
        merge_sort = MergeSort()
        for iteration in merge_sort.sort(numbers.copy()):
            self.listbox_results.insert(tk.END, iteration)
            self.listbox_results.update()
            self.listbox_results.after(500)
        self.listbox_results.insert(tk.END, "Array ordenado con Merge Sort:\n{}".format(numbers))

        self.listbox_results.insert(tk.END, "Ordenando con Heap Sort:")
        heap_sort = HeapSort()
        for iteration in heap_sort.sort(numbers.copy()):
            self.listbox_results.insert(tk.END, iteration)
            self.listbox_results.update()
            self.listbox_results.after(500)
        self.listbox_results.insert(tk.END, "Array ordenado con Heap Sort:\n{}".format(numbers))

    def run(self):
        self.window.mainloop()


if __name__ == "__main__":
    sorting_gui = SortingGUI()
    sorting_gui.run()
