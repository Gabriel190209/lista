import customtkinter as ctk
import math

ctk.set_appearance_mode("Light")
ctk.set_default_color_theme("blue")

root = ctk.CTk()
root.title("Volume de lata de óleo")
root.geometry("350x500")

def mudar_tema():
    if ctk.get_appearance_mode()=="Dark":
        ctk.set_appearance_mode("Light")
    else:
        ctk.set_appearance_mode("Dark")

def volume():
    try:
        raio = float(entry_raio.get())
        altura = float(entry_altura.get())
        volume =  math.pi * raio**2 * altura
        resultado.set(f"{volume:.2f}cm³")
    except ValueError:
        resultado.set("Valor invalido")



label = ctk.CTkLabel(root, text="Valor do raio", font=("Arial", 14))
label.pack(pady=10)

entry_raio = ctk.CTkEntry(root, font=("Arial", 14), width=200, justify="center")
entry_raio.pack(pady=5)

label = ctk.CTkLabel(root, text="valor de altura", font=("Arial", 14))
label.pack(pady=10)

entry_altura = ctk.CTkEntry(root, font=("Arial", 14), width=200, justify="center")
entry_altura.pack(pady=5)

button = ctk.CTkButton(root, text="Calcular volume", command=volume)
button.pack(pady=5)

resultado = ctk.StringVar()

label = ctk.CTkLabel(root, textvariable=resultado, font=("Arial", 20))
label.pack(pady=30)

button = ctk.CTkButton(root, text="Mudar Tema", width=200, command=mudar_tema)
button.pack(pady=90)

root.mainloop()