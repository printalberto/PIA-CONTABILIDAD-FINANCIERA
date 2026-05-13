import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

# =========================================
# CONFIGURACION PRINCIPAL
# =========================================

COLOR_FONDO = "#f4f6f9"
COLOR_BOTON = "#1f4e79"
COLOR_TEXTO = "#ffffff"

# =========================================
# VENTANA PRINCIPAL
# =========================================

ventana = tk.Tk()
ventana.title("Sistema Integral de Presupuesto Maestro")
ventana.geometry("1200x700")
ventana.config(bg=COLOR_FONDO)

# =========================================
# VARIABLES GLOBALES
# =========================================

usuario_actual = ""

# =========================================
# FUNCION LOGIN
# =========================================

def iniciar_sesion():

    usuario = entry_usuario.get()
    password = entry_password.get()

    if usuario == "admin" and password == "1234":

        global usuario_actual
        usuario_actual = usuario

        frame_login.pack_forget()

        mostrar_menu()

    else:

        messagebox.showerror(
            "Error",
            "Usuario o contraseña incorrectos"
        )

# =========================================
# FUNCION MENU PRINCIPAL
# =========================================

def mostrar_menu():

    frame_menu.pack(fill="both", expand=True)

# =========================================
# FUNCION LIMPIAR CONTENIDO
# =========================================

def limpiar_contenido():

    for widget in frame_contenido.winfo_children():
        widget.destroy()

# =========================================
# MODULO VENTAS
# =========================================

def abrir_ventas():

    limpiar_contenido()

    titulo = tk.Label(
        frame_contenido,
        text="Presupuesto de Ventas",
        font=("Arial", 22, "bold"),
        bg="white"
    )

    titulo.pack(pady=20)

    frame_form = tk.Frame(frame_contenido, bg="white")
    frame_form.pack(pady=20)

    tk.Label(
        frame_form,
        text="Unidades a vender:",
        font=("Arial", 12),
        bg="white"
    ).grid(row=0, column=0, padx=10, pady=10)

    entry_unidades = tk.Entry(frame_form, font=("Arial", 12))
    entry_unidades.grid(row=0, column=1)

    tk.Label(
        frame_form,
        text="Precio por unidad:",
        font=("Arial", 12),
        bg="white"
    ).grid(row=1, column=0, padx=10, pady=10)

    entry_precio = tk.Entry(frame_form, font=("Arial", 12))
    entry_precio.grid(row=1, column=1)

    resultado = tk.Label(
        frame_contenido,
        text="",
        font=("Arial", 14),
        bg="white"
    )

    resultado.pack(pady=20)

    def calcular_ventas():

        try:

            unidades = float(entry_unidades.get())
            precio = float(entry_precio.get())

            total = unidades * precio

            resultado.config(
                text=f"Ingreso total proyectado: ${total:,.2f}"
            )

        except:

            messagebox.showerror(
                "Error",
                "Ingresa datos válidos"
            )

    boton = tk.Button(
        frame_contenido,
        text="Calcular Ventas",
        font=("Arial", 12, "bold"),
        bg=COLOR_BOTON,
        fg="white",
        command=calcular_ventas
    )

    boton.pack(pady=10)

# =========================================
# MODULO PRODUCCION
# =========================================

def abrir_produccion():

    limpiar_contenido()

    titulo = tk.Label(
        frame_contenido,
        text="Presupuesto de Producción",
        font=("Arial", 22, "bold"),
        bg="white"
    )

    titulo.pack(pady=20)

    frame_form = tk.Frame(frame_contenido, bg="white")
    frame_form.pack(pady=20)

    tk.Label(
        frame_form,
        text="Unidades requeridas:",
        font=("Arial", 12),
        bg="white"
    ).grid(row=0, column=0, padx=10, pady=10)

    entry_requeridas = tk.Entry(frame_form, font=("Arial", 12))
    entry_requeridas.grid(row=0, column=1)

    tk.Label(
        frame_form,
        text="Inventario inicial:",
        font=("Arial", 12),
        bg="white"
    ).grid(row=1, column=0, padx=10, pady=10)

    entry_inicial = tk.Entry(frame_form, font=("Arial", 12))
    entry_inicial.grid(row=1, column=1)

    resultado = tk.Label(
        frame_contenido,
        text="",
        font=("Arial", 14),
        bg="white"
    )

    resultado.pack(pady=20)

    def calcular_produccion():

        try:

            requeridas = float(entry_requeridas.get())
            inicial = float(entry_inicial.get())

            total = requeridas - inicial

            resultado.config(
                text=f"Producción necesaria: {total:,.0f} unidades"
            )

        except:

            messagebox.showerror(
                "Error",
                "Datos inválidos"
            )

    boton = tk.Button(
        frame_contenido,
        text="Calcular Producción",
        font=("Arial", 12, "bold"),
        bg=COLOR_BOTON,
        fg="white",
        command=calcular_produccion
    )

    boton.pack(pady=10)

# =========================================
# MODULO GASTOS
# =========================================

def abrir_gastos():

    limpiar_contenido()

    titulo = tk.Label(
        frame_contenido,
        text="Gastos Operativos",   
        font=("Arial", 22, "bold"),
        bg="white"
    )

    titulo.pack(pady=20)

    frame_form = tk.Frame(frame_contenido, bg="white")
    frame_form.pack(pady=20)

    gastos = [
        "Renta",
        "Luz",
        "Agua",
        "Internet",
        "Nómina"
    ]

    entries = []

    for i, gasto in enumerate(gastos):

        tk.Label(
            frame_form,
            text=gasto + ":",
            font=("Arial", 12),
            bg="white"
        ).grid(row=i, column=0, padx=10, pady=10)

        entry = tk.Entry(frame_form, font=("Arial", 12))
        entry.grid(row=i, column=1)

        entries.append(entry)

    resultado = tk.Label(
        frame_contenido,
        text="",
        font=("Arial", 14),
        bg="white"
    )

    resultado.pack(pady=20)

    def calcular_gastos():

        try:

            total = 0

            for entry in entries:
                total += float(entry.get())

            resultado.config(
                text=f"Gastos operativos totales: ${total:,.2f}"
            )

        except:

            messagebox.showerror(
                "Error",
                "Ingresa valores válidos"
            )

    boton = tk.Button(
        frame_contenido,
        text="Calcular Gastos",
        font=("Arial", 12, "bold"),
        bg=COLOR_BOTON,
        fg="white",
        command=calcular_gastos
    )

    boton.pack(pady=10)

# =========================================
# LOGIN FRAME
# =========================================

frame_login = tk.Frame(
    ventana,
    bg="white",
    padx=40,
    pady=40
)

frame_login.pack(pady=100)

titulo_login = tk.Label(
    frame_login,
    text="Inicio de Sesión",
    font=("Arial", 24, "bold"),
    bg="white"
)

titulo_login.pack(pady=20)

tk.Label(
    frame_login,
    text="Usuario",
    font=("Arial", 12),
    bg="white"
).pack()

entry_usuario = tk.Entry(
    frame_login,
    font=("Arial", 12)
)

entry_usuario.pack(pady=10)

tk.Label(
    frame_login,
    text="Contraseña",
    font=("Arial", 12),
    bg="white"
).pack()

entry_password = tk.Entry(
    frame_login,
    font=("Arial", 12),
    show="*"
)

entry_password.pack(pady=10)

boton_login = tk.Button(
    frame_login,
    text="Ingresar",
    font=("Arial", 12, "bold"),
    bg=COLOR_BOTON,
    fg="white",
    padx=20,
    pady=10,
    command=iniciar_sesion
)

boton_login.pack(pady=20)

# =========================================
# FRAME MENU
# =========================================

frame_menu = tk.Frame(
    ventana,
    bg=COLOR_FONDO
)

# =========================================
# SIDEBAR
# =========================================

sidebar = tk.Frame(
    frame_menu,
    bg="#16324f",
    width=250
)

sidebar.pack(side="left", fill="y")

titulo_sidebar = tk.Label(
    sidebar,
    text="MENÚ",
    font=("Arial", 20, "bold"),
    bg="#16324f",
    fg="white"
)

titulo_sidebar.pack(pady=20)

# =========================================
# BOTONES MENU
# =========================================

botones = [
    ("Ventas", abrir_ventas),
    ("Producción", abrir_produccion),
    ("Gastos", abrir_gastos)
]

for texto, comando in botones:

    boton = tk.Button(
        sidebar,
        text=texto,
        font=("Arial", 12, "bold"),
        bg=COLOR_BOTON,
        fg="white",
        width=20,
        height=2,
        command=comando
    )

    boton.pack(pady=10)

# =========================================
# CONTENIDO PRINCIPAL
# =========================================

frame_contenido = tk.Frame(
    frame_menu,
    bg="white"
)

frame_contenido.pack(
    side="right",
    expand=True,
    fill="both"
)

# =========================================
# EJECUTAR
# =========================================

ventana.mainloop()