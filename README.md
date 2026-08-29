# Pipeline CI Completa (Python)

Projeto de exemplo com uma pipeline de Integração Contínua no GitHub Actions
cobrindo quatro estágios: **análise de código (lint)**, **testes unitários**,
**cobertura de código** e **análise de segurança**.

## Estrutura do projeto

```
pipeline-ci-python/
├── .github/
│   └── workflows/
│       └── ci.yml              # Pipeline de CI (4 jobs encadeados)
├── app/
│   ├── calculadora_financeira.py
│   └── cliente_api.py           # Exemplo de uso seguro de chave de API (via env var)
├── tests/
│   ├── test_calculadora_financeira.py
│   └── test_cliente_api.py
├── interface.py                 # Interface gráfica (Tkinter)
├── requirements.txt
├── requirements-dev.txt
├── .flake8
├── .bandit.yml
├── setup.cfg                    # Configuração da cobertura mínima (80%)
├── CENARIOS-DE-FALHA.md         # Guia para simular cada tipo de falha
└── README.md
```

## Como executar localmente

Requer Python 3.10+.

```bash
pip install -r requirements-dev.txt
```

**Rodar a interface gráfica:**

```bash
python interface.py
```

Abre uma janela com três seções: Juros Simples, Juros Compostos e
Conversão de Moeda — preencha os campos e clique em calcular/converter.
O Tkinter já vem com a instalação padrão do Python; no Linux, se faltar,
instale com `sudo apt install python3-tk`.

**Rodar o lint:**

```bash
flake8 app tests
```

**Rodar os testes:**

```bash
pytest -v
```

**Rodar os testes com cobertura:**

```bash
pytest --cov=app --cov-report=term-missing --cov-fail-under=80
```

**Rodar a análise de segurança:**

```bash
bandit -r app -c .bandit.yml
```

Para o gitleaks (detecção de segredos), a forma mais simples é deixar o
próprio GitHub Actions rodar — ele já vem configurado no workflow.

## Pipeline de CI (GitHub Actions)

A cada `push` ou `pull request` na branch `main`, o workflow em
`.github/workflows/ci.yml` executa 4 jobs **encadeados com `needs`**, na
ordem abaixo. Se um job falhar, os seguintes não rodam:

1. **`lint`** — roda o `flake8` sobre `app/` e `tests/`
2. **`testes`** (needs: `lint`) — roda os testes unitários com `pytest`
3. **`cobertura`** (needs: `testes`) — roda os testes novamente com
   `pytest-cov`, exigindo no mínimo **80%** de cobertura
4. **`seguranca`** (needs: `cobertura`) — roda o `bandit` (análise estática
   de segurança) e o **gitleaks** (detecção de segredos/chaves de API
   expostas no código)

O status de cada execução pode ser acompanhado na aba **Actions** do
repositório no GitHub.

## Simulando cenários de falha

O arquivo [`CENARIOS-DE-FALHA.md`](./CENARIOS-DE-FALHA.md) tem o passo a
passo para provocar, de propósito, uma falha em cada um dos 4 estágios:

- Erro de lint
- Teste unitário reprovado
- Cobertura abaixo do mínimo
- Chave de API exposta no código
