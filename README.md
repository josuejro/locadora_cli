# 🚗 Locadora CLI

Sistema de gerenciamento para locadoras de veículos executado via linha de comando (CLI). Desenvolvido em Python com foco em Programação Orientada a Objetos, persistência de dados e arquitetura modularizada.

---

## Funcionalidades

- **Gestão de frota:** cadastro de veículos e visualização do estoque com status atualizado automaticamente (Disponível/Alugado)
- **Gestão de clientes:** cadastro com nome, CPF, CNH e data de nascimento, com validação de formato para CPF e CNH
- **Locação:** geração de contratos com datas reais via `datetime` e seleção de plano de seguro
- **Devolução:** cálculo automático do valor final, incluindo multas por atraso (por hora), quilometragem excedente, reabastecimento e avarias
- **Persistência:** leitura e escrita de dados em arquivos `.csv` via pandas, mantendo o estado entre execuções
- **Validação de entrada:** tratamento de exceções nos campos numéricos e validação de formato para CPF/CNH

---

## Estrutura do Projeto

```
locadora_cli/
│
├── main.py                  # Ponto de entrada do programa
├── requirements.txt         # Dependências do projeto
│
├── modelos/                 # Classes de domínio
│   ├── carro.py
│   ├── cliente.py
│   └── contrato.py
│
├── operacoes/               # Lógica de negócio
│   ├── cadastro.py
│   ├── devolucao.py
│   ├── estoque.py
│   └── locacao.py
│
└── utilidades/              # Funções auxiliares
    ├── banco_dados.py       # Leitura e escrita nos CSVs
    ├── calculos.py          # Formatação de moeda e cálculo de multas
    ├── constantes.py        # Valores centralizados de multas e taxas
    ├── interface.py         # Menu e cabeçalhos do terminal
    └── validacoes.py        # Validação de CPF e CNH
```

---

## Pré-requisitos

- Python 3.10 ou superior
- pandas

Instale as dependências com:

```bash
pip install -r requirements.txt
```

---

## Como executar

Clone o repositório e execute o arquivo principal:

```bash
git clone https://github.com/josuejro/locadora_cli.git
cd locadora_cli
pip install -r requirements.txt
python main.py
```

---

## Como usar

Ao iniciar, o menu principal oferece as seguintes opções:

```
1: Cadastrar novo carro
2: Ver estoque de carros
3: Cadastrar cliente
4: Ir para a locação
5: Ir para a devolução
6: Sair do programa
```

**Fluxo básico:**
1. Cadastre um veículo (opção 1)
2. Cadastre um cliente (opção 3)
3. Realize uma locação informando o CPF do cliente e a placa do veículo (opção 4)
4. Na devolução, o sistema calcula automaticamente multas por atraso, quilometragem excedente e avarias (opção 5)

---

## Persistência de dados

Os dados são salvos automaticamente em arquivos CSV na raiz do projeto:

| Arquivo | Conteúdo |
|---|---|
| `carros.csv` | Veículos cadastrados |
| `clientes.csv` | Clientes cadastrados |
| `locacoes.csv` | Contratos de locação |

> Esses arquivos são gerados automaticamente na primeira execução. Não é necessário criá-los manualmente.

---

## Regras de negócio

**Validação de cadastro:**
- CPF: deve conter exatamente 11 dígitos numéricos
- CNH: deve conter exatamente 11 dígitos numéricos

**Multas na devolução:**
| Tipo | Valor |
|---|---|
| Tanque não cheio | R$ 150,00 (fixo) |
| Quilometragem excedente (limite: 1.000 km) | R$ 2,50 por km |
| Atraso na entrega | R$ 30,00 por hora |
| Avarias | Valor informado pelo atendente |

> Os valores de multas e taxas estão centralizados em `utilidades/constantes.py`, facilitando manutenção futura.

**Planos de seguro disponíveis:**

| Plano | Custo |
|---|---|
| Básico | R$ 10,00 |
| Plus | R$ 60,00 |
| VIP | R$ 140,00 |

---

## Boas práticas aplicadas

- **Arquitetura modular:** separação em camadas (modelos, operações, utilidades)
- **Comparações Pythônicas:** uso idiomático de `if not`, `is None` e avaliação direta de booleanos
- **Constantes centralizadas:** valores de multas e taxas em um único arquivo (`constantes.py`)
- **Validação de entrada:** formato de CPF/CNH validado via regex (`validacoes.py`)
- **`__repr__` nos modelos:** facilita depuração e inspeção dos objetos `Carro`, `Cliente` e `Contrato`
- **Segurança:** limpeza de tela via `subprocess.run()` sem `shell=True` (compatível com Python 3.14+)

---

## Tecnologias utilizadas

- Python 3
- pandas
- Módulo `datetime` (datas e cálculo de atraso)
- Módulo `subprocess` (limpeza de tela multiplataforma)
- Módulo `re` (validação de CPF e CNH)
