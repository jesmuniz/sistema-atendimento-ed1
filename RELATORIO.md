# Relatório Técnico – Sistema de Atendimento

## Objetivo

Desenvolver um sistema de gerenciamento de atendimentos utilizando os conceitos estudados na disciplina de Estrutura de Dados I.

O sistema permite o cadastro de clientes e atendentes, gerenciamento de filas, histórico de atendimentos, geração de relatórios e persistência de dados.

---

# Estruturas Utilizadas

## 1. Vetores (Listas Python)

Utilizados para:

- Clientes cadastrados
- Atendentes cadastrados
- Histórico de atendimentos

### Justificativa

As listas Python oferecem simplicidade de implementação e acesso rápido aos elementos.

### Complexidade

| Operação | Complexidade |
|-----------|------------|
| Inserção | O(1) |
| Busca Linear | O(n) |
| Remoção | O(n) |

---

## 2. Busca Binária

Utilizada para busca rápida de clientes por ID.

Antes da busca, os clientes são ordenados por ID.

### Justificativa

Reduz significativamente o tempo de busca quando comparado à busca linear.

### Complexidade

| Operação | Complexidade |
|-----------|------------|
| Busca Binária | O(log n) |

---

## 3. Fila Comum

Utilizada para armazenar clientes sem prioridade.

### Regra

Primeiro cliente a entrar é o primeiro a ser atendido (FIFO).

### Complexidade

| Operação | Complexidade |
|-----------|------------|
| Inserção | O(1) |
| Remoção | O(1) |

---

## 4. Fila Prioritária

Utilizada para clientes prioritários.

### Regra

Clientes prioritários possuem preferência sobre os clientes da fila comum, mantendo a ordem de chegada entre eles.

### Complexidade

| Operação | Complexidade |
|-----------|------------|
| Inserção | O(1) |
| Remoção | O(1) |

---

## 5. Pilha

Utilizada para desfazer a última finalização de atendimento.

### Regra

Último atendimento finalizado é o primeiro a ser recuperado (LIFO).

### Complexidade

| Operação | Complexidade |
|-----------|------------|
| Push | O(1) |
| Pop | O(1) |

---

## 6. Lista Encadeada

Utilizada para armazenar clientes ativos.

### Operações

- Inserção
- Remoção
- Listagem

### Justificativa

Atende ao requisito da disciplina para utilização de listas encadeadas.

### Complexidade

| Operação | Complexidade |
|-----------|------------|
| Inserção | O(n) |
| Remoção | O(n) |
| Busca | O(n) |

---

# Persistência de Dados

O sistema utiliza arquivos JSON para armazenar:

- Clientes
- Atendentes
- Atendimentos

Dessa forma os dados permanecem disponíveis após o encerramento do programa.

---

# Testes

Foram implementados testes básicos para:

- Classe Cliente
- Busca Binária
- Lista Encadeada

Todos os testes executaram com sucesso.

---

# Conclusão

O projeto permitiu aplicar na prática conceitos fundamentais da disciplina de Estrutura de Dados I, utilizando diferentes estruturas de acordo com as necessidades de cada funcionalidade do sistema.

As estruturas escolhidas contribuíram para a organização dos dados, otimização de buscas e gerenciamento eficiente dos atendimentos.