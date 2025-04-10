import customtkinter as ctk
import math

ctk.set_appearance_mode("Light")
ctk.set_default_color_theme("blue")

root = ctk.CTk()
root.title("Volume de lata de óleo")
root.geometry("350x500")

opcoes = ["bit", "byte", "KB", "MB", "GB", "TB"]
opcoess = ["bit", "byte", "KB", "MB", "GB", "TB"]

def transformar():
    try:
        
        valor = float(entry.get())
        inicial = combo.get()
        final = comboo.get()

        valorc = valor

        if(inicial=="MB" and final=="KB"):
            valorc = (valor * 1024)
        elif(inicial=="MB" and final=="byte"):
            valorc = (valor * 1024) * 1024
        elif(inicial=="MB" and final=="bit"):
            valorc = (valor * 1024 * 1024 * 8)
        elif (inicial=="MB" and final=="GB"):
            valorc = (valor/1024)
        elif (inicial=="MB" and final=="TB"):
            valorc = (valor/1024) / 1024
        elif(inicial=="byte" and final=="bit"):
            valorc = (valor * 8)
        elif(inicial=="byte" and final=="KB"):
            valorc = (valor / 1024)
        elif (inicial=="byte" and final=="MB"):
            valorc = (valor / 1024) / 1024
        elif (inicial=="byte" and final=="GB"):
            valorc = (valor / 1024 / 1024 / 1024)
        elif (inicial=="byte" and final=="TB"):
            valorc = (valor / 1024 / 1024 / 1024 / 1024)
        elif(inicial=="KB" and final=="bit"):
            valorc = (valor * 1024) * 8
        elif(inicial=="KB" and final=="byte"):
            valorc = (valor * 1024)
        elif (inicial=="KB" and final=="MB"):
            valorc = (valor / 1024)
        elif (inicial=="KB" and final=="GB"):
            valorc = (valor / 1024 / 1024)
        elif (inicial=="KB" and final=="TB"):
            valorc = (valor / 1024 / 1024 / 1024)
        elif(inicial=="MB" and final=="bit"):
            valorc = (valor * 1024 * 1024) * 8
        elif(inicial=="MB" and final=="byte"):
            valorc = (valor * 1024) * 1024
        elif (inicial=="MB" and final=="KB"):
            valorc = (valor * 1024)
        elif (inicial=="MB" and final=="GB"):
            valorc = (valor / 1024)
        elif (inicial=="MB" and final=="TB"):
            valorc = (valor / 1024 / 1024)
        elif(inicial=="GB" and final=="bit"):
            valorc = (valor * 1024 * 1024 * 1024 * 1024) * 8
        elif(inicial=="GB" and final=="byte"):
            valorc = (valor * 1024 * 1024 * 1024 * 1024)
        elif (inicial=="GB" and final=="KB"):
            valorc = (valor * 1024 * 1024 * 1024)
        elif (inicial=="GB" and final=="MB"):
            valorc = (valor * 1024 * 1024)
        elif (inicial=="GB" and final=="TB"):
            valorc = (valor / 1024)
        elif(inicial=="TB" and final=="bit"):
            valorc = (valor * 1024 * 1024 * 1024 * 1024) * 8
        elif(inicial=="TB" and final=="byte"):
            valorc = (valor * 1024 * 1024 * 1024 * 1024)
        elif (inicial=="TB" and final=="KB"):
            valorc = (valor * 1024 * 1024 * 1024)
        elif (inicial=="TB" and final=="MB"):
            valorc = (valor * 1024 * 1024)
        elif (inicial=="TB" and final=="GB"):
            valorc = (valor * 1024)
        resultado.set(f"{valorc}")
    except ValueError:
        resultado.set("valor invalido")

def trocar_tema():
    if ctk.get_appearance_mode() == "Dark":
        ctk.set_appearance_mode("Light")
    else:
        ctk.set_appearance_mode("Dark")

label = ctk.CTkLabel(root,text="Digite um valor para conversão", font=("Arial",16, "bold"))
label.pack(pady=10)

entry = ctk.CTkEntry(root, font=("Arial", 14), width= 200, justify= "left")
entry.pack(pady= 5)

resultado = ctk.StringVar()

combo = ctk.CTkComboBox(root, values=opcoes, width=200)
combo.pack(pady=5)
combo.set("MB")

label = ctk.CTkLabel(root,text="para", font=("Arial",14))
label.pack(pady=5)

comboo = ctk.CTkComboBox(root, values=opcoess, width=200)
comboo.pack(pady=5)
comboo.set("KB")

button = ctk.CTkButton(root, text=("transformar"), width=200, command=transformar)
button.pack(pady=10)

label_result = ctk.CTkLabel(root, textvariable=resultado, font=("Arial", 14, "bold"))
label_result.pack(pady=10)

button = ctk.CTkButton(root, text=("trocar tema"), width=200, command=trocar_tema)
button.pack(pady=90)

root.mainloop()