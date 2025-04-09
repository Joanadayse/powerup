import pyautogui
import time
import subprocess
import pandas

# Caminho do Chrome e URL de login
chrome_path = r'"C:\Program Files\Google\Chrome\Application\chrome.exe"'
url = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"

# Abre o navegador
subprocess.Popen(f'{chrome_path} --profile-directory="Default" {url}')
time.sleep(5)

# Login
pyautogui.click(x=388, y=448)
time.sleep(0.5)
pyautogui.hotkey("ctrl", "a")
pyautogui.press("backspace")
pyautogui.write("daysejoana7@gmail.com", interval=0.1)
pyautogui.press("tab")
time.sleep(0.5)
pyautogui.write("senhateste123", interval=0.1)
pyautogui.press("enter")

# Espera a página da tabela carregar
time.sleep(5)

# Lê o CSV
tabela = pandas.read_csv("produtos.csv")
print(tabela)

# Pega o primeiro produto
produto = tabela.iloc[0]

# Acessa os campos (ajuste os x,y conforme necessário!)
# Campo código
for linha in tabela.index:
    # clicar no campo de código
    pyautogui.click(x=653, y=294)
    # pegar da tabela o valor do campo que a gente quer preencher
    codigo = tabela.loc[linha, "codigo"]
    # preencher o campo
    pyautogui.write(str(codigo))
    # passar para o proximo campo
    pyautogui.press("tab")
    # preencher o campo
    pyautogui.write(str(tabela.loc[linha, "marca"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "tipo"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")
    obs = tabela.loc[linha, "obs"]
    if not pandas.isna(obs):
        pyautogui.write(str(tabela.loc[linha, "obs"]))
    pyautogui.press("tab")
    pyautogui.press("enter") 
    pyautogui.scroll(5000)
