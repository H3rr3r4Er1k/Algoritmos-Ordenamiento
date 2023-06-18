import tkinter as tk
from tkinter import messagebox
import random
from AO_Iterativos import *
from AO_Recursivos import *

# Funciones de la GUI
def generate_array():
    try:
        size = int(entry_size.get())
        if size <= 0:
            raise ValueError
        numbers = random.sample(range(1, size * 10 + 1), size)
        original_array_label.config(text=f"Array sin ordenar: {numbers}")
        sort_array(numbers)
    except ValueError:
        messagebox.showerror("Error", "Por favor ingresa un tamaño válido.")


def sort_array(numbers):
    listbox_results.delete(0, tk.END)

    algorithms = [
        BubbleSort(),
        InsertionSort(),
        SelectionSort(),
        ShellSort(),
        QuickSort(),
        MergeSort(),
        HeapSort()
    ]

    for algorithm in algorithms:
        listbox_results.insert(tk.END, f"Ordenando con {algorithm.name}:")
        for iteration in algorithm.sort(numbers.copy()):
            listbox_results.insert(tk.END, iteration)
            listbox_results.update()
            listbox_results.after(500)
        listbox_results.insert(tk.END, f"Array ordenado con {algorithm.name}:\n{numbers}")


# Crear ventana principal
window = tk.Tk()
window.title("Ordenamiento de Números")
window.geometry("600x600")

# Crear frame
frame = tk.Frame(window)
frame.pack(pady=20)

# Crear etiqueta y entrada para el tamaño del vector
label_size = tk.Label(frame, text="Tamaño:")
label_size.grid(row=0, column=0, padx=10)
entry_size = tk.Entry(frame)
entry_size.grid(row=0, column=1, padx=10)

# Crear botón para generar el arreglo de números aleatorios
button_generate = tk.Button(frame, text="Generar Arreglo", command=generate_array)
button_generate.grid(row=0, column=2, padx=10)

# Crear etiqueta para mostrar el arreglo original sin ordenar
original_array_label = tk.Label(window, text="Array sin ordenar:", font=("Arial", 14))
original_array_label.pack(pady=10)

# Crear lista para mostrar los resultados
listbox_results = tk.Listbox(window, width=50, font=("Courier", 12))
listbox_results.pack(pady=10, expand=True, fill=tk.BOTH)

# Iniciar bucle de la GUI
window.mainloop()
