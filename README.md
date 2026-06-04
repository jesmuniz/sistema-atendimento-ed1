# Sistema de Atendimento - Estrutura de Dados I

## Integrantes

- Jhessy Eduarda Soares Muniz
- Camila dos Santos Fernandes
- Sadrack Jenivaldo Ambrósio
- Vércio Henrique Soares Muniz

---

## Descrição

Sistema de gerenciamento de atendimentos desenvolvido para a disciplina de Estrutura de Dados I.

O sistema permite o cadastro de clientes e atendentes, gerenciamento de filas de atendimento, histórico de atendimentos, geração de relatórios e persistência de dados.

O projeto foi desenvolvido utilizando estruturas de dados estudadas durante o semestre, incluindo vetores, filas, pilhas, listas encadeadas e busca binária.

---

## Funcionalidades

### Clientes

- Cadastro de clientes
- Listagem de clientes
- Busca de cliente por ID utilizando busca binária
- Remoção de clientes inativos
- Listagem de clientes ativos

### Atendentes

- Cadastro de atendentes
- Listagem de atendentes

### Atendimentos

- Entrada em fila de atendimento
- Fila comum
- Fila prioritária
- Chamada do próximo atendimento
- Finalização de atendimento
- Histórico geral de atendimentos
- Histórico por cliente

### Relatórios

- Relatório de atendimentos
- Cálculo do tempo médio de atendimento
- Exportação de relatório em CSV

### Extras

- Persistência de dados em JSON
- Sistema de logs
- Testes básicos do sistema

---

## Estruturas de Dados Utilizadas

### Vetor (Lista Python)

Utilizado para:

- Cadastro de clientes
- Cadastro de atendentes
- Histórico de atendimentos

Complexidade:

- Inserção: O(1)
- Busca linear: O(n)

---

### Busca Binária

Utilizada para busca rápida de clientes por ID.

Complexidade:

- Busca: O(log n)

---

### Fila Comum

Utilizada para armazenar clientes sem prioridade.

Regra:

- Primeiro a entrar é o primeiro a ser atendido (FIFO).

Complexidade:

- Inserção: O(1)
- Remoção: O(1)

---

### Fila Prioritária

Utilizada para clientes prioritários.

Regra:

- Clientes prioritários são atendidos antes dos clientes da fila comum.
- Mantém a ordem de chegada entre clientes prioritários.

Complexidade:

- Inserção: O(1)
- Remoção: O(1)

---

### Pilha

Utilizada para desfazer a última finalização de atendimento.

Regra:

- Último atendimento finalizado é o primeiro a ser restaurado (LIFO).

Complexidade:

- Push: O(1)
- Pop: O(1)

---

### Lista Encadeada

Utilizada para armazenar os clientes ativos.

Operações:

- Inserção
- Remoção
- Listagem

Complexidade:

- Inserção: O(n)
- Remoção: O(n)
- Busca: O(n)

---

## Organização do Projeto

```text
sistema-atendimento-ed1/

├── data/
│   ├── clientes.json
│   ├── atendentes.json
│   └── atendimentos.json
│
├── models/
│   ├── cliente.py
│   ├── atendente.py
│   └── atendimento.py
│
├── services/
│   ├── cliente_services.py
│   ├── atendimento_services.py
│   ├── relatorio_service.py
│   └── validacoes.py
│
├── structures/
│   └── lista_encadeada.py
│
├── utils/
│   ├── arquivo.py
│   └── logger.py
│
├── tests/
│   ├── test_cliente.py
│   ├── test_busca_binaria.py
│   └── test_lista_encadeada.py
│
├── main.py
├── README.md
└── requirements.txt
```

---

## Persistência de Dados

O sistema utiliza arquivos JSON para armazenar os dados.

Arquivos:

- clientes.json
- atendentes.json
- atendimentos.json

Os dados permanecem salvos mesmo após o encerramento do programa.

---

## Logs

As principais operações realizadas pelos usuários são registradas em arquivo de log.

Exemplos:

- Cadastro de cliente
- Cadastro de atendente
- Abertura de atendimento
- Finalização de atendimento
- Consulta de histórico
- Geração de relatórios

---

## Testes

O projeto possui testes básicos para validação das principais estruturas.

Executar:

```bash
python -m tests.test_cliente
python -m tests.test_busca_binaria
python -m tests.test_lista_encadeada
```

Resultado esperado:

```text
Teste cliente: OK
Teste busca binária: OK
Teste lista encadeada: OK
```

---

## Como Executar

### 1. Clonar o repositório

```bash
git clone <url-do-repositorio>
```

### 2. Entrar na pasta

```bash
cd sistema-atendimento-ed1
```

### 3. Executar o sistema

```bash
python main.py
```

---

## Tecnologias Utilizadas

- Python 3
- JSON
- Git
- GitHub

---

## Conclusão

Este projeto permitiu a aplicação prática dos conceitos estudados em Estrutura de Dados I, utilizando diferentes estruturas para resolver problemas reais de gerenciamento de atendimentos, priorização de filas, armazenamento de dados e geração de relatórios.