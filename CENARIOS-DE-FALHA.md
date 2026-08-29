# Cenários de Falha — Guia para o Desafio

Este guia mostra como provocar, de propósito, uma falha em cada estágio da
pipeline (`lint` → `testes` → `cobertura` → `seguranca`). A ideia é fazer
cada alteração em um commit separado, dar push e observar o job
correspondente falhar na aba **Actions** do GitHub — depois reverter e
seguir para o próximo cenário.

Como os jobs usam `needs`, ao falhar um estágio os seguintes nem chegam a
rodar (ficam marcados como "skipped").

---

## Cenário 1 — Erro de lint

**Onde:** `app/calculadora_financeira.py`

Adicione uma linha com um problema de estilo que o flake8 acusa, por exemplo
uma variável não usada e uma linha muito longa:

```python
def calcular_juros_simples(capital, taxa, tempo):
    validar_taxa(taxa)
    validar_tempo(tempo)
    variavel_nao_usada = 123  # flake8 vai reclamar: variável atribuída mas nunca usada
    juros = capital * taxa * tempo
    return capital + juros
```

**Resultado esperado:** o job `lint` falha em `flake8 app tests`, apontando
o erro `F841 local variable 'variavel_nao_usada' is assigned to but never used`.
Os jobs `testes`, `cobertura` e `seguranca` são pulados.

---

## Cenário 2 — Teste unitário reprovado

**Onde:** `tests/test_calculadora_financeira.py`

Altere uma asserção para um valor incorreto:

```python
def test_juros_simples():
    assert calcular_juros_simples(1000, 0.01, 12) == 9999  # valor errado de propósito
```

**Resultado esperado:** o job `lint` passa normalmente, mas `testes` falha
no `pytest -v`, mostrando `AssertionError`. Os jobs `cobertura` e
`seguranca` são pulados.

---

## Cenário 3 — Cobertura abaixo do mínimo

**Onde:** `tests/test_calculadora_financeira.py` ou `tests/test_cliente_api.py`

Remova (ou comente) algumas funções de teste, reduzindo a porcentagem de
código coberta. Por exemplo, apague os testes de `cliente_api.py` inteiro
(comente o conteúdo de `tests/test_cliente_api.py`), já que esse módulo tem
funções que só são exercitadas por esses testes.

**Resultado esperado:** `lint` e `testes` passam, mas o job `cobertura`
falha no `pytest --cov=app --cov-fail-under=80`, informando que a cobertura
ficou abaixo dos 80% configurados em `setup.cfg`. O job `seguranca` é pulado.

---

## Cenário 4 — Chave de API exposta

**Onde:** qualquer arquivo, por exemplo `app/cliente_api.py`

Adicione uma linha com uma chave "hardcoded" (nunca faça isso em um projeto
real — aqui é só para o exercício). Um exemplo de chave de teste que o
gitleaks reconhece pelo padrão de uma AWS Access Key:

```python
CHAVE_TEMPORARIA = "AKIAIOSFODNN7EXAMPLE"
```

**Resultado esperado:** `lint`, `testes` e `cobertura` passam normalmente,
mas o job `seguranca` falha no passo do **gitleaks**, que detecta o padrão
de chave no código-fonte e interrompe a pipeline antes que ela chegue a
qualquer deploy.

---

## Depois de cada cenário

Reverta a alteração (`git checkout -- <arquivo>` ou desfaça manualmente) e
faça um novo commit/push para confirmar que a pipeline volta a passar em
todos os estágios antes de simular o próximo cenário.
