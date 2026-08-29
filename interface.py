import tkinter as tk
from tkinter import messagebox

from app.calculadora_financeira import (
    calcular_juros_simples,
    calcular_juros_compostos,
    converter_moeda,
)


def calcular_simples():
    try:
        capital = float(entrada_capital_simples.get())
        taxa = float(entrada_taxa_simples.get())
        tempo = float(entrada_tempo_simples.get())
        resultado = calcular_juros_simples(capital, taxa, tempo)
        resultado_simples.config(text=f"Montante: {resultado:.2f}")
    except ValueError as erro:
        messagebox.showerror("Erro", str(erro) or "Preencha os campos com números válidos.")


def calcular_compostos():
    try:
        capital = float(entrada_capital_compostos.get())
        taxa = float(entrada_taxa_compostos.get())
        tempo = float(entrada_tempo_compostos.get())
        resultado = calcular_juros_compostos(capital, taxa, tempo)
        resultado_compostos.config(text=f"Montante: {resultado:.2f}")
    except ValueError as erro:
        messagebox.showerror("Erro", str(erro) or "Preencha os campos com números válidos.")


def calcular_conversao():
    try:
        valor = float(entrada_valor_cambio.get())
        taxa_cambio = float(entrada_taxa_cambio.get())
        resultado = converter_moeda(valor, taxa_cambio)
        resultado_cambio.config(text=f"Valor convertido: {resultado:.2f}")
    except ValueError as erro:
        messagebox.showerror("Erro", str(erro) or "Preencha os campos com números válidos.")


def criar_secao(container, titulo, campos, texto_botao, comando):
    """Cria uma seção da interface com título, campos de entrada e botão de calcular."""
    secao = tk.LabelFrame(container, text=titulo, font=("Arial", 11, "bold"), padx=10, pady=10)
    secao.pack(fill="x", padx=10, pady=8)

    entradas = []
    for rotulo in campos:
        linha = tk.Frame(secao)
        linha.pack(fill="x", pady=2)
        tk.Label(linha, text=rotulo, width=14, anchor="w").pack(side="left")
        entrada = tk.Entry(linha)
        entrada.pack(side="left", fill="x", expand=True)
        entradas.append(entrada)

    tk.Button(secao, text=texto_botao, command=comando, bg="#4CAF50", fg="white").pack(
        pady=(8, 4), fill="x"
    )
    resultado = tk.Label(secao, text="", font=("Arial", 10, "bold"))
    resultado.pack()

    return entradas, resultado


# --- Montagem da janela ---
janela = tk.Tk()
janela.title("Calculadora Financeira")
janela.geometry("360x560")
janela.resizable(False, False)

titulo_geral = tk.Label(janela, text="Calculadora Financeira", font=("Arial", 14, "bold"))
titulo_geral.pack(pady=10)

(entrada_capital_simples, entrada_taxa_simples, entrada_tempo_simples), resultado_simples = (
    criar_secao(
        janela,
        "Juros Simples",
        ["Capital:", "Taxa (ex: 0.01):", "Tempo:"],
        "Calcular",
        calcular_simples,
    )
)

(entrada_capital_compostos, entrada_taxa_compostos, entrada_tempo_compostos), resultado_compostos = (
    criar_secao(
        janela,
        "Juros Compostos",
        ["Capital:", "Taxa (ex: 0.01):", "Tempo:"],
        "Calcular",
        calcular_compostos,
    )
)

(entrada_valor_cambio, entrada_taxa_cambio), resultado_cambio = criar_secao(
    janela,
    "Conversão de Moeda",
    ["Valor:", "Taxa de câmbio:"],
    "Converter",
    calcular_conversao,
)

janela.mainloop()
