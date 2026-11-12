# 🎯 Adivinhe o Número - Python

Um jogo de adivinhação desenvolvido em Python, no qual o usuário precisa descobrir um número aleatório gerado pelo sistema, dentro do intervalo de 1 a 10.000.

A cada tentativa, o programa fornece dicas indicando se o número correto é maior ou menor que o informado, ajudando o jogador a chegar à resposta.

Ao finalizar o jogo, o sistema contabiliza as tentativas e classifica o desempenho do jogador.

## 🚀 Funcionalidades

- **Geração aleatória:** O sistema gera um número secreto entre 1 e 10.000 utilizando o módulo `random`.
- **Dicas interativas:** Informa se o número correto é maior ou menor que o palpite.
- **Controle de tentativas:** Contabiliza quantas tentativas foram necessárias para encontrar o número.
- **Controle de limites:** Armazena os menores e maiores palpites realizados.
- **Avaliação de desempenho:** Classifica o resultado do jogador conforme a quantidade de tentativas.

## 🛠️ Tecnologias utilizadas

| Tecnologia | Finalidade |
|---|---|
| Python | Linguagem de programação |
| Random | Geração de números aleatórios |
| Input | Entrada de dados do usuário |
| Estruturas condicionais | Comparação dos números e avaliação do desempenho |
| While | Repetição das tentativas até encontrar o número |

## ⚙️ Pré-requisitos

- Python 3.10 ou superior.
- Terminal ou editor de código para executar o programa.

Não é necessário instalar bibliotecas externas, pois o módulo `random` já faz parte da biblioteca padrão do Python.

## ▶️ Como executar

**1. Clone o repositório**

```bash
git clone https://github.com/SEU-USUARIO/Adivinhe-o-Numero.git
```

**2. Entre na pasta do projeto**

```bash
cd Adivinhe-o-Numero
```

**3. Execute o programa**

```bash
python main.py
```

## 🎮 Como funciona

1. O programa gera um número aleatório entre 1 e 10.000.
2. O jogador informa um número pelo terminal.
3. O sistema compara o palpite com o número secreto.
4. Caso o palpite esteja incorreto, o programa fornece uma dica:
   - Número informado menor que o correto: exibe "Número correto é MAIOR".
   - Número informado maior que o correto: exibe "Número correto é MENOR".
5. O processo continua até o jogador encontrar o número.
6. Ao acertar, o sistema apresenta a quantidade de tentativas e a classificação do desempenho.

## 🏆 Classificação de desempenho

O jogo utiliza a quantidade de tentativas para avaliar o desempenho do jogador.

| Tentativas | Classificação |
|---|---|
| Até 10 | Excelente |
| De 11 a 15 | Moderado |
| Acima de 15 | Ruim |

## 💻 Exemplo de execução

```text
Informe um numero: 5000

Numero correto é MAIOR

Informe um numero: 7500

Numero correto é MENOR!

Informe um numero: 6200

Numero correto é MAIOR

...

Informe um numero: 6842

Número encontrado!

DESEMPENHO: Excelente!
TENTATIVAS: 8
```

*Exemplo ilustrativo de execução.*

## 🎯 Objetivo do projeto

Este projeto foi desenvolvido com o objetivo de praticar conceitos fundamentais da linguagem Python, especialmente:

- Geração de números aleatórios.
- Entrada e saída de dados.
- Estruturas condicionais (`if`, `elif` e `else`).
- Laços de repetição (`while`).
- Operadores de comparação.
- Manipulação de variáveis e controle de estado.
- Utilização de valores `None` para inicialização de variáveis.

---

**Desenvolvido com Python 🐍**
