import pyautogui
import pandas
import time

pyautogui.PAUSE = 1

site = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"

#abrir chrome
pyautogui.press("win")
pyautogui.write("google chrome")
pyautogui.press("enter")
time.sleep(5)
pyautogui.click(x=883, y=410)

#abrir o site para login
time.sleep(3)

pyautogui.write(site)
pyautogui.press("enter")
time.sleep(3)

tabela = pandas.read_csv("produtos.csv")


#cadastrar produtos
time.sleep(2)
pyautogui.click(x=556, y=373)
pyautogui.write("pablo@gmail")
pyautogui.press("tab")
pyautogui.write("12345")
pyautogui.press("tab")
pyautogui.press("enter")
pyautogui.press("enter")
pyautogui.press("enter")
pyautogui.press("enter")
pyautogui.press("enter")

time.sleep(5)
pyautogui.click(x=960, y=356)

#cadastrar produtos
for linha in range(0,2):
    pyautogui.click(x=643, y=249)

    codigo = str(tabela.loc[linha, "codigo"])
    pyautogui.write(codigo)
    pyautogui.press("tab")
    marca = str(tabela.loc[linha, "marca"])
    pyautogui.write(marca)
    pyautogui.press("tab")
    tipo = str(tabela.loc[linha, "tipo"])
    pyautogui.write(tipo)
    pyautogui.press("tab")
    categoria = str(tabela.loc[linha, "categoria"])
    pyautogui.write(categoria)
    pyautogui.press("tab")
    preco_unitario = str(tabela.loc[linha, "preco_unitario"])
    pyautogui.write(preco_unitario)
    pyautogui.press("tab")
    custo = str(tabela.loc[linha, "custo"])
    pyautogui.write(custo)
    pyautogui.press("tab")
    obs = str(tabela.loc[linha, "obs"])
    if obs != "nan":
        pyautogui.write(obs)
    pyautogui.press("tab")
    pyautogui.press("enter")    
    pyautogui.scroll(5000)
