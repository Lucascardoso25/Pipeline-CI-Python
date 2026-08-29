"""Funções de cálculo financeiro simples, usadas como app de exemplo da pipeline."""


def validar_taxa(taxa):
    """Garante que a taxa de juros não é negativa."""
    if taxa < 0:
        raise ValueError("A taxa de juros não pode ser negativa.")
    return taxa


def validar_tempo(tempo):
    """Garante que o tempo (em períodos) é maior que zero."""
    if tempo <= 0:
        raise ValueError("O tempo deve ser maior que zero.")
    return tempo


def calcular_juros_simples(capital, taxa, tempo):
    """Calcula o montante final usando juros simples."""
    validar_taxa(taxa)
    validar_tempo(tempo)
    juros = capital * taxa * tempo
    return capital + juros


def calcular_juros_compostos(capital, taxa, tempo):
    """Calcula o montante final usando juros compostos."""
    validar_taxa(taxa)
    validar_tempo(tempo)
    return capital * (1 + taxa) ** tempo


def converter_moeda(valor, taxa_cambio):
    """Converte um valor monetário usando uma taxa de câmbio."""
    if taxa_cambio <= 0:
        raise ValueError("A taxa de câmbio deve ser maior que zero.")
    return round(valor * taxa_cambio, 2)
