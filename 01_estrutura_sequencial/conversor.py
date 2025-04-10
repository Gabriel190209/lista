import customtkinter as ctk

ctk.set_appearance_mode("Light")
ctk.set_default_color_theme("blue")

root = ctk.CTk() #criando a janela
root.title("conversor de temperatura") #titulo da janela
root.geometry("350x400") #tamanho da janela

#função para conversão
def celsius_para_fahrenheit():
    try:
        celsius = float(entry.get())
        fahrenheit = (celsius*9/5)+32
        resultado.set(f"{fahrenheit:.2f} °F")
    except ValueError:
        resultado.set("entrada invalida")

def fahrenheit_para_celsius():
    try:
        fahrenheit = float(entry.get())
        celsius = (fahrenheit - 32) * 5/9
        resultado.set(f"{celsius:.2f} °C")
    except ValueError:
        resultado.set("entrada invalida")

def alternar_modo():
    if ctk.get_appearance_mode()=="Dark":
        ctk.set_appearance_mode("Light")
    else:
        ctk.set_appearance_mode("Dark")



#crianando os elementos

label = ctk.CTkLabel(root,text="Digite a temperatura", font=("Arial",14))
label.pack(pady=10)

#caixa de entrada (Entry)
entry = ctk.CTkEntry(root,font=("Arial",14),width=200, justify="center")
entry.pack(pady=5)

#botao para conversão de celsius para fahrenheit
botao_celsius= ctk.CTkButton(root,text="Converter para °F", command=celsius_para_fahrenheit)
botao_celsius.pack(pady=5)

botao_fahrenheit= ctk.CTkButton(root,text="Converter para °C", command=fahrenheit_para_celsius)
botao_fahrenheit.pack(pady=5)

#variavel para armazenar o resultado
resultado = ctk.StringVar()

# rotulo para exibir o resultado
label_resultado = ctk.CTkLabel(root,textvariable=resultado,font=("Arial",16, "bold"))
label_resultado.pack(pady=10)

botao_tema = ctk.CTkButton(root,text="Alterar tema", command=alternar_modo)
botao_tema.pack(pady=60)

#rodando a interface grafica
root.mainloop()
