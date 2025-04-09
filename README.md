

## 🐍 Projeto: Automação de Login e Cadastro de Produtos com PyAutoGUI

Este projeto utiliza **Python**, a biblioteca **PyAutoGUI** e **pandas** para automatizar o login em uma página web e o cadastro de produtos a partir de uma planilha `.csv`.

### 🚀 Funcionalidades

- Abre o navegador Google Chrome com perfil padrão.
- Acessa uma URL de login.
- Preenche os campos de email e senha automaticamente.
- Realiza o login na plataforma.
- Lê uma planilha CSV contendo informações de produtos.
- Preenche os campos da tabela de cadastro com os dados da planilha.
- Cadastra automaticamente o(s) produto(s).

### 📁 Estrutura esperada do CSV

A planilha `produtos.csv` deve conter as seguintes colunas:

| codigo       | marca   | tipo      | categoria | preco_unitario | custo  | obs           |
|--------------|---------|-----------|-----------|----------------|--------|----------------|
| MOLO000251   | Adidas  | Tênis     | 1         | 299.90         | 150.00 | Produto novo   |

> 📝 Observação: A coluna `categoria` deve ser convertida para string no código, caso contenha números.

### 🛠️ Requisitos

- Python 3.x
- [PyAutoGUI](https://pypi.org/project/pyautogui/)
- pandas

### 📦 Instalação

```bash
pip install pyautogui pandas
```

### ▶️ Como usar

1. Altere os caminhos, posições do mouse (`x`, `y`) e tempos de espera conforme necessário.
2. Certifique-se de que o navegador está instalado no caminho especificado.
3. Execute o script:

```bash
python codigo.py
```

---

### ⚠️ Avisos

- A automação depende da posição dos elementos na tela. Use `pyautogui.position()` para identificar os pontos corretos.
- Evite movimentar o mouse durante a execução.
- Esse tipo de automação é mais frágil do que automações baseadas em APIs ou Selenium, pois depende da interface visual.

---

### ✨ Projeto realizado no curso da Hashtag Treinamentos de Python.



