import pyautogui as p

def alterdata():
    p.write('cpd')
    p.press('tab')
    p.press('tab')
    p.write('alterdata')
    p.press('tab')
    p.write('cplus x alterdata')
    p.press('tab')
    p.press('enter')
    p.press('enter')

def cplus():
    p.write('cpd')
    p.press('tab')
    p.press('tab')
    p.write('cplus')
    p.press('tab')
    p.write('Alterar Banco')
    p.press('tab')
    p.press('enter')
    p.press('enter')


def backup():
    p.write('cpd')
    p.press('tab')
    p.press('tab')
    p.write('backup')
    p.press('tab')
    p.write('Rotina')
    p.press('tab')
    p.press('enter')
    p.press('enter')


def novochamado():
    p.hotkey('altleft', 'l')
    p.PAUSE = 0.5
    p.press('down')
    p.press('enter')
    p.PAUSE = 0.5


def abrirPrograma():
    p.hotkey('winleft', 'r')
    p.PAUSE = 2
    p.write('C:\GvlTecnologia\HelpDesk\GestorHelpDesk.exe')
    p.PAUSE = 1
    p.press('enter')
    p.PAUSE = 0.5
    p.hotkey('shift', 'tab')
    p.write('Tiago.Chaves')
    p.press('tab')
    p.write('85')
    p.press('enter')
    p.PAUSE = 1



abrirPrograma()
novochamado()
alterdata()
novochamado()
cplus()
novochamado()
backup()


