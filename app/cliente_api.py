"""Exemplo de como acessar uma chave de API de forma segura, via variável de ambiente.

Este módulo existe para contrastar com o cenário de falha 'chave de API exposta':
a forma correta é NUNCA escrever a chave diretamente no código-fonte.
"""

import os


def obter_chave_api():
    """Lê a chave de API da variável de ambiente API_KEY.

    Levanta um erro claro caso a variável não esteja configurada,
    em vez de deixar a chave hardcoded no código.
    """
    chave = os.environ.get("API_KEY")
    if not chave:
        raise RuntimeError(
            "Variável de ambiente API_KEY não configurada. "
            "Defina-a antes de usar o cliente de API."
        )
    return chave


def montar_cabecalho_autenticacao():
    """Monta o cabeçalho HTTP de autenticação usando a chave de API."""
    chave = obter_chave_api()
    return {"Authorization": f"Bearer {chave}"}
