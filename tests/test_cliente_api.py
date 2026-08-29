import pytest

from app.cliente_api import obter_chave_api, montar_cabecalho_autenticacao


def test_obter_chave_api_sem_variavel_levanta_erro(monkeypatch):
    monkeypatch.delenv("API_KEY", raising=False)
    with pytest.raises(RuntimeError):
        obter_chave_api()


def test_obter_chave_api_com_variavel_configurada(monkeypatch):
    monkeypatch.setenv("API_KEY", "chave-de-teste-123")
    assert obter_chave_api() == "chave-de-teste-123"


def test_montar_cabecalho_autenticacao(monkeypatch):
    monkeypatch.setenv("API_KEY", "chave-de-teste-123")
    cabecalho = montar_cabecalho_autenticacao()
    assert cabecalho == {"Authorization": "Bearer chave-de-teste-123"}
