import pyautogui as pa

def acessar_blocodenotas():
    pa.PAUSE = 1
    pa.press("win")
    pa.write("Bloco de notas")
    pa.press("Enter")
    pa.write("BEM VINDOS AO MEU PORTIFOLIO, AUTOMACAO EM PYTHON :)")
    pa.press("Enter")

def salvar_arquivo():
    pa.click(x=1503, y=220)
    pa.click(x=727, y=434)
    pa.write("PORTIFOLIO PYTHON")
    pa.press("Enter")

acessar_blocodenotas()

for x in range(1):
    pa.press("Enter")
    pa.write("OLA TODOS")
    pa.press("Enter")

salvar_arquivo()

