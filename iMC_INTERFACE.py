# Tkinter biblioteca gráfica
# Importa as classes do módulo tkinter
import tkinter as tk
from tkinter import ttk

def calcular_imc(peso, altura):
    imc = peso / (altura**2)
    return imc

def indice(imc):
    if imc < 18.5:
        return "Abaixo do peso"
    elif 18.5 <= imc < 24.9:
        return "Peso normal"
    elif 25 <= imc <= 29.9:
        return "Sobrepeso"
    elif 30 <= imc < 34.9:
        return "Obesidade grau I"
    elif 35 <= imc < 39.9:
        return "Obesidade grau II"
    else:
        return "Obesidade Grau III"

def exibir_mensagem():
    nome = nome_entry.get()
    idade = int(idade_entry.get())
    altura = float(altura_entry.get())
    peso = float(peso_entry.get())
    imc = calcular_imc(peso, altura)
    resultado = indice(imc)

    mensagem_label.config(text=f"Nome: {nome}\nIdade: {idade} anos\nPeso: {peso} kg\nAltura: {altura} m\nIMC: {imc:.2f}")
    classificacao_label.config(text=f"A classificação é: {resultado}")

# Cria a janela principal
root = tk.Tk()
root.title("Inova Uniesp")


#define o tamanho da janela 
root.geometry ("500x500")

#definir cor de fundo de janela 
root.configure( bg="#001030")

#Definir fonte

fonte = ("Arial" ,10)

#crie widgets
nome_label = ttk.Label(root, text="Nome: ", font= (fonte), foreground="white", background="#001030")
nome_entry = ttk.Entry(root, font= fonte, width=30)

idade_label = ttk.Label(root, text="Idade: ", font= (fonte), foreground="white", background="#001030")
idade_entry = ttk.Entry(root, font= fonte, width=30)

peso_label = ttk.Label(root, text="Peso (Kg): ", font= (fonte), foreground="white", background="#001030")
peso_entry = ttk.Entry(root, font= fonte, width=30)

altura_label = ttk.Label(root, text="Altura (m): ", font= (fonte), foreground="white", background="#001030")
altura_entry = ttk.Entry(root, font= fonte, width=30)

# Ajusta a posição geometricamente na tela
nome_label.pack(padx=20, pady=20)

#Posiciona os widgets na janela
nome_label.grid(row=0, column=0, padx=10, pady=5 )
nome_entry.grid(row=0, column=1, padx=10, pady=5 )

idade_label.grid(row=1, column=0, padx=10, pady=5 )
idade_entry.grid(row=1, column=1, padx=10, pady=5 )

peso_label.grid(row=2, column=0, padx=10, pady=5 )
peso_entry.grid(row=2, column=1, padx=10, pady=5 )

altura_label.grid(row=3, column=0, padx=10, pady=5 )
altura_entry.grid(row=3, column=1, padx=10, pady=5 )


#Adicione um botão e posiciona na janela 
botao = ttk.Button(root, text= "Caclcule o Imc", command=exibir_mensagem)
botao.grid( row=6, column=0, columnspan=2, padx=5, pady=10)

mensagem_label = ttk.Label(root, text="", font=fonte)
mensagem_label.grid(row=10, column=0, columnspan=2, pady= 5)

classificacao_label = ttk.Label(root, text="", font=fonte)
classificacao_label.grid(row=11, column=0, columnspan=2, pady= 5)


# Inicia a interface gráfica
root.mainloop()
