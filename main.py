import tkinter as tk

def agregar_tarea():
    tarea = tarea_entry.get()
    if tarea:
        lista_tareas.insert(tk.END, tarea)
        tarea_entry.delete(0, tk.END)
        guardar_tareas()

def marcar_completada():
    seleccion = lista_tareas.curselection()
    if seleccion:
        for indice in seleccion:
            lista_tareas.itemconfig(indice, {'bg': 'light green'})
        guardar_tareas()

def eliminar_tarea():
    seleccion = lista_tareas.curselection()
    if seleccion:
        for indice in reversed(seleccion):
            lista_tareas.delete(indice)
        guardar_tareas()

def marcar_todas_completadas():
    for i in range(lista_tareas.size()):
        lista_tareas.itemconfig(i, {'bg': 'light green'})
    guardar_tareas()

def eliminar_todas_tareas():
    lista_tareas.delete(0, tk.END)
    guardar_tareas()

def guardar_tareas():
    with open('tasks.txt', 'w') as archivo:
        tareas = lista_tareas.get(0, tk.END)
        for tarea in tareas:
            archivo.write(tarea + '\n')

def cargar_tareas():
    try:
        with open('tasks.txt', 'r') as archivo:
            tareas = archivo.readlines()
            for tarea in tareas:
                lista_tareas.insert(tk.END, tarea.strip())
    except FileNotFoundError:
        pass

# Configuración de la ventana principal
ventana = tk.Tk()
ventana.title("Lista de Tareas")
ventana.geometry("600x400")  # Tamaño personalizado (ancho aumentado)
ventana.iconbitmap('planificacionTareas.ico')
# Color de fondo general para la ventana
ventana.configure(bg='lavender')

# Marco para los botones
marco_botones = tk.Frame(ventana,bg='lavender')
marco_botones.pack(pady=10)

# Campo de entrada para agregar tareas 
tarea_entry = tk.Entry(ventana, width=60)
tarea_entry.pack(pady=10)

# Agregar, marcar como completada y eliminar tarea
agregar_btn = tk.Button(marco_botones, text="Agregar tarea", command=agregar_tarea, bg='sky blue', fg='white', relief=tk.RAISED, cursor='hand2')
marcar_btn = tk.Button(marco_botones, text="Marcar como Completada", command=marcar_completada, bg='lime green', fg='white', relief=tk.RAISED, cursor='hand2')
eliminar_btn = tk.Button(marco_botones, text="Eliminar tarea", command=eliminar_tarea, bg='tomato', fg='white', relief=tk.RAISED, cursor='hand2')

agregar_btn.pack(side=tk.LEFT, padx=10)  # Colocar en el lado izquierdo del marco con espacio entre botones
marcar_btn.pack(side=tk.LEFT, padx=10)
eliminar_btn.pack(side=tk.LEFT, padx=10)

# Lista de tareas (más ancha)
lista_tareas = tk.Listbox(ventana, selectbackground='lightgray', selectmode=tk.SINGLE, bg='white', width=60)  # Ancho aumentado
lista_tareas.pack(pady=10)

# Cargar las tareas actuales, allí escritas
cargar_tareas()

# Marcar como completadas y eliminar todas las tareas 
marcar_todas_btn = tk.Button(ventana, text="Marcar todas como Completadas", command=marcar_todas_completadas, bg='lime green', fg='white', relief=tk.RAISED, cursor='hand2')
eliminar_todas_btn = tk.Button(ventana, text="Eliminar todas las tareas", command=eliminar_todas_tareas, bg='tomato', fg='white', relief=tk.RAISED, cursor='hand2')

marcar_todas_btn.pack(side=tk.TOP, padx=10, pady=5, anchor='center')
eliminar_todas_btn.pack(side=tk.TOP, padx=10, pady=5, anchor='center')

ventana.mainloop()


