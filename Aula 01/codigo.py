# Python Power Up: Automação de Tarefas

# Passo a Passo do Projeto 

import subprocess
import pyautogui
import time

# Definindo um tempo de pausa padrão
pyautogui.PAUSE = 0.5

# Abrir o navegador usando subprocesso
subprocess.Popen(["/usr/bin/open", "-a", "/Applications/Google Chrome.app"])

# Dar tempo para o navegador abrir
time.sleep(4)  # Aumente o tempo de espera se necessário

# Digitar o link e pressionar enter
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
pyautogui.write(link)
pyautogui.press("enter")

# Dar uma pausa no código
time.sleep(3)



# Passo 2: Fazer Login
pyautogui.click(x=1944 , y=720)
pyautogui.write("natashabrandao57@hotmail.com")

#escrever a senha
pyautogui.press("tab")
pyautogui.write("sua senha aqui")

# clicar botão de logar
pyautogui.click(x=2110 , y=883 )
time.sleep(3)


# Passo 3: Importar a base de dados
import pandas

tabela = pandas.read_csv("produtos.csv")
print(tabela)

# Passo 4: Cadastrar 1 produto
# para cada linha da minha tabela
for linha in tabela.index: 
    # clicar no primeiro campo
    pyautogui.click(x=2075, y=612)

    # código do produto
    codigo = tabela.loc[linha, "codigo"]
    pyautogui.write(codigo)
    pyautogui.press("tab")

    # marca
    pyautogui.write(tabela.loc[linha, "marca"])
    pyautogui.press("tab")

    # tipo
    pyautogui.write(tabela.loc[linha, "tipo"])
    pyautogui.press("tab")

    # categoria
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")

    # preco
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")

    # custo 
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")

    # obs
    obs = tabela.loc[linha, "obs"]
    if not pandas.isna(obs):
        pyautogui.write()
    pyautogui.press("tab")

    # enviar
    pyautogui.press("enter")
    pyautogui.scroll(5000)


# Passo 5: Repetir o processo de cadastro até acabar 