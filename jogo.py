from random import choice
import fileHandler as fH
import desenhos as d
from tkinter import messagebox, simpledialog

# Variáveis globais do jogo
palavra_sorteada = ""
digitadas = []
acertos = []
erros = 0

# Função para iniciar o jogo
def iniciar_jogo(palavra_secreta_label, enforcado_label, entrada_letra):
    global palavra_sorteada, digitadas, acertos, erros
    lista_palavras = fH.abrir_palavras()
    palavra_sorteada = choice(lista_palavras)
    digitadas = []
    acertos = []
    erros = 0
    atualizar_palavra_secreta(palavra_secreta_label)
    enforcado_label.config(text=desenhar_forca(erros))
    entrada_letra.config(state="normal")

# Função para atualizar a palavra secreta exibida
def atualizar_palavra_secreta(palavra_secreta_label):
    adivinha = ""
    for letra in palavra_sorteada:
        if letra in acertos:
            adivinha += letra + " "
        else:
            adivinha += "_ "
    palavra_secreta_label.config(text=adivinha)

# Função para desenhar a forca e o boneco conforme os erros
def desenhar_forca(erros):
    estagios = [
        """
           -----
           |   |
               |
               |
               |
               |
         =========
        """,
        """
           -----
           |   |
           O   |
               |
               |
               |
         =========
        """,
        """
           -----
           |   |
           O   |
           |   |
               |
               |
         =========
        """,
        """
           -----
           |   |
           O   |
          /|   |
               |
               |
         =========
        """,
        """
           -----
           |   |
           O   |
          /|\\  |
               |
               |
         =========
        """,
        """
           -----
           |   |
           O   |
          /|\\  |
          /    |
               |
         =========
        """,
        """
           -----
           |   |
           O   |
          /|\\  |
          / \\  |
               |
         =========
        """
    ]
    return estagios[erros]

# Função para tentar adivinhar uma letra
def tentar_letra(letra_var, palavra_secreta_label, enforcado_label):
    global erros
    tentativa = letra_var.get().lower()
    letra_var.set("")

    if tentativa in digitadas:
        messagebox.showinfo("Erro", "Você já usou essa letra!")
        return

    digitadas.append(tentativa)
    if tentativa in palavra_sorteada:
        acertos.append(tentativa)
        atualizar_palavra_secreta(palavra_secreta_label)
        if "_" not in palavra_secreta_label.cget("text"):
            messagebox.showinfo("Parabéns!", "Você acertou a palavra!")
            salvar_score()
            letra_var.set("")
    else:
        erros += 1
        enforcado_label.config(text=desenhar_forca(erros))  # Atualiza o desenho do boneco com o erro atual
        if erros == 6:
            messagebox.showinfo("Fim de Jogo", f"Você foi enforcado! A palavra era {palavra_sorteada}.")
            salvar_score()
            letra_var.set("")


# Função para salvar o score
def salvar_score():
    nome = simpledialog.askstring("Nome", "Qual o seu nome?")
    if nome:
        score = 1000 - (erros * 200)
        fH.inserir_score(nome, score)
        messagebox.showinfo("Score", f"Score de {score} salvo para {nome}!")
