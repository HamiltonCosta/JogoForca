import tkinter as tk
from tkinter import messagebox, simpledialog
import jogo as j
import fileHandler as fH

# Configurar a janela principal
root = tk.Tk()
root.title("Jogo da Forca")
root.geometry("600x600")

# Variáveis globais
letra_var = tk.StringVar()

# Função para exibir scores
def exibir_scores():
    scores = fH.listar_scores()
    score_text = ""
    for i, (nome, score) in enumerate(scores):
        score_text += f"{i+1}. {nome} - {score}\n"
    messagebox.showinfo("Scores", score_text if score_text else "Nenhum score registrado.")



# Layout da interface
palavra_secreta_label = tk.Label(root, text="_ " * 10, font=("Helvetica", 24))
palavra_secreta_label.pack(pady=20)

enforcado_label = tk.Label(root, text=j.desenhar_forca(0), font=("Courier", 18), justify="left")
enforcado_label.pack(pady=10)

letra_entry = tk.Entry(root, textvariable=letra_var, font=("Helvetica", 18), width=5)
letra_entry.pack(pady=10)
letra_entry.focus()

botao_tentar = tk.Button(root, text="Tentar Letra", command=lambda: j.tentar_letra(letra_var, palavra_secreta_label, enforcado_label), font=("Helvetica", 18))
botao_tentar.pack(pady=10)

botao_iniciar = tk.Button(root, text="Iniciar Jogo", command=lambda: j.iniciar_jogo(palavra_secreta_label, enforcado_label, letra_entry), font=("Helvetica", 18))
botao_iniciar.pack(pady=20)

botao_scores = tk.Button(root, text="Ver Scores", command=exibir_scores, font=("Helvetica", 18))
botao_scores.pack(pady=10)

# Iniciar a aplicação
root.mainloop()

