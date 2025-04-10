import customtkinter as ctk

ctk.set_appearance_mode("Light")
ctk.set_default_color_theme("blue")

root = ctk.CTk() #criando a janela
root.title("conversor de temperatura") #titulo da janela
root.geometry("650x600") #tamanho da janela

def medico():
    try:
        resultado.set("É de tanto a Lara falar")
    except ValueError:
        resultado.set("fala o problema burro")


resultado = ctk.StringVar()

label = ctk.CTkLabel(root, text="FALE SEU PROBLEMA", font=("Arial", 34, "bold"))
label.pack(pady=50)

entry = ctk.CTkEntry(root, font=("Arial", 14), width=200, height=50)
entry.pack(pady=5)

label = ctk.CTkLabel(root, textvariable=resultado, font=("Arial", 20))
label.pack(pady=10)

button = ctk.CTkButton(root, text="RESULTADO", width=200, command=medico)
button.pack(pady=10)

root.mainloop()