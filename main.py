import tkinter as tk
import random
from tkinter import messagebox

from generadorVector import VectorGenerator
from AOIterativo import BubbleSort, InsertionSort, SelectionSort, ShellSort
from AORecursivos import MergeSort, QuickSort, HeapSort


class OrdenamientoGUI:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Ordenamiento de Vectores")

        # Establecer el tamaño de la ventana para ocupar toda la pantalla
        width = self.window.winfo_screenwidth()
        height = self.window.winfo_screenheight()
        self.window.geometry(f"{width}x{height}")

        self.label_titulo = tk.Label(self.window, text="Ordenamiento de Vectores", font=("Arial", 16))
        self.label_titulo.pack(pady=10)

        # Frame para contener los elementos relacionados con la generación del vector
        frame_generacion = tk.Frame(self.window)
        frame_generacion.pack()

        self.label_tamano = tk.Label(frame_generacion, text="Ingrese el tamaño del vector:")
        self.label_tamano.grid(row=0, column=0, padx=5, pady=5)

        self.entry_tamano = tk.Entry(frame_generacion)
        self.entry_tamano.grid(row=0, column=1, padx=5, pady=5)

        self.boton_generar = tk.Button(frame_generacion, text="Generar Vector", command=self.generar_vector)
        self.boton_generar.grid(row=0, column=2, padx=5, pady=5)

        self.label_vector = tk.Label(self.window, text="Vector generado:")
        self.label_vector.pack()

        # Frame para contener los elementos relacionados con la selección de algoritmos
        frame_algoritmos = tk.Frame(self.window)
        frame_algoritmos.pack(pady=10)

        self.label_iterativos = tk.Label(frame_algoritmos, text="Algoritmos de Ordenamiento Iterativo")
        self.label_iterativos.grid(row=0, column=0, padx=5, pady=5)

        self.listbox_algoritmos_iterativos = tk.Listbox(frame_algoritmos, selectmode=tk.SINGLE)
        self.listbox_algoritmos_iterativos.insert(tk.END, "Bubble Sort")
        self.listbox_algoritmos_iterativos.insert(tk.END, "Insert Sort")
        self.listbox_algoritmos_iterativos.insert(tk.END, "Selection Sort")
        self.listbox_algoritmos_iterativos.insert(tk.END, "Shell Sort")
        self.listbox_algoritmos_iterativos.grid(row=1, column=0, padx=5, pady=5)

        self.label_recursivos = tk.Label(frame_algoritmos, text="Algoritmos de Ordenamiento Recursivo")
        self.label_recursivos.grid(row=0, column=1, padx=5, pady=5)

        self.listbox_algoritmos_recursivos = tk.Listbox(frame_algoritmos, selectmode=tk.SINGLE)
        self.listbox_algoritmos_recursivos.insert(tk.END, "Merge Sort")
        self.listbox_algoritmos_recursivos.insert(tk.END, "Quick Sort")
        self.listbox_algoritmos_recursivos.insert(tk.END, "Heap Sort")
        self.listbox_algoritmos_recursivos.grid(row=1, column=1, padx=5, pady=5)

        self.boton_ordenar = tk.Button(self.window, text="Ordenar", command=self.ordenar_vector)
        self.boton_ordenar.pack(pady=10)

        # Frame para contener los elementos relacionados con el proceso de ordenamiento
        frame_proceso = tk.Frame(self.window)
        frame_proceso.pack()

        self.label_proceso = tk.Label(frame_proceso, text="Proceso de ordenamiento:")
        self.label_proceso.pack(side=tk.LEFT, padx=5, pady=5)

        self.scrollbar = tk.Scrollbar(frame_proceso)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.text_proceso = tk.Text(frame_proceso, height=10, width=50, yscrollcommand=self.scrollbar.set)
        self.text_proceso.pack()

        self.scrollbar.config(command=self.text_proceso.yview)

        self.label_resultado = tk.Label(self.window, text="Vector ordenado:")
        self.label_resultado.pack()

        self.vector = []

        self.window.mainloop()

    def generar_vector(self):
        try:
            tamano = int(self.entry_tamano.get())
            vector_generator = VectorGenerator()
            self.vector = vector_generator.generate_vector(tamano)
            self.label_vector.config(text="Vector generado: " + str(self.vector))
        except ValueError:
            messagebox.showerror("Error", "Ingrese un tamaño válido para el vector.")

    def ordenar_vector(self):
        algoritmo_iterativo = self.listbox_algoritmos_iterativos.get(tk.ACTIVE)
        algoritmo_recursivo = self.listbox_algoritmos_recursivos.get(tk.ACTIVE)

        if algoritmo_iterativo:
            if algoritmo_iterativo == "Bubble Sort":
                bubble_sort = BubbleSort(self.vector, self.actualizar_resultado, self.actualizar_proceso)
                bubble_sort.sort()
            elif algoritmo_iterativo == "Insert Sort":
                insertion_sort = InsertionSort(self.vector, self.actualizar_resultado, self.actualizar_proceso)
                insertion_sort.sort()
            elif algoritmo_iterativo == "Selection Sort":
                selection_sort = SelectionSort(self.vector, self.actualizar_resultado, self.actualizar_proceso)
                selection_sort.sort()
            elif algoritmo_iterativo == "Shell Sort":
                shell_sort = ShellSort(self.vector, self.actualizar_resultado, self.actualizar_proceso)
                shell_sort.sort()
        elif algoritmo_recursivo:
            if algoritmo_recursivo == "Merge Sort":
                merge_sort = MergeSort(self.vector, self.actualizar_resultado, self.actualizar_proceso)
                merge_sort.sort()
            elif algoritmo_recursivo == "Quick Sort":
                quick_sort = QuickSort(self.vector, self.actualizar_resultado, self.actualizar_proceso)
                quick_sort.sort()
            elif algoritmo_recursivo == "Heap Sort":
                heap_sort = HeapSort(self.vector, self.actualizar_resultado, self.actualizar_proceso)
                heap_sort.sort()
        else:
            messagebox.showerror("Error", "Seleccione un algoritmo de ordenamiento.")

    def actualizar_resultado(self, resultado):
        self.label_resultado.config(text="Vector ordenado: " + str(resultado))

    def actualizar_proceso(self, proceso):
        self.text_proceso.delete("1.0", tk.END)
        self.text_proceso.insert(tk.END, proceso)


if __name__ == "__main__":
    ordenamiento_gui = OrdenamientoGUI()
