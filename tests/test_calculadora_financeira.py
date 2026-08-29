import pytest

from app.calculadora_financeira import (
    calcular_juros_simples,
    calcular_juros_compostos,
    converter_moeda,
    validar_taxa,
    validar_tempo,
)


def test_juros_simples():
    assert calcular_juros_simples(1000, 0.01, 12) == 1120


def test_juros_compostos():
    resultado = calcular_juros_compostos(1000, 0.01, 12)
    assert round(resultado, 2) == 1126.83


def test_converter_moeda():
    assert converter_moeda(100, 5.5) == 550


def test_taxa_negativa_levanta_erro():
    with pytest.raises(ValueError):
        validar_taxa(-0.01)


def test_tempo_invalido_levanta_erro():
    with pytest.raises(ValueError):
        validar_tempo(0)


def test_taxa_cambio_invalida_levanta_erro():
    with pytest.raises(ValueError):
        converter_moeda(100, 0)


def test_juros_simples_com_taxa_invalida_propaga_erro():
    with pytest.raises(ValueError):
        calcular_juros_simples(1000, -0.5, 12)
