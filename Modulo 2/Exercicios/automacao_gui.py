import pyautogui as at

def apertar_tab(qtd):
    for i in range(qtd):
        at.press("tab")
        at.sleep(0.02)                    

at.hotkey("win","r")
at.write("Chrome", 0.1)
at.press("enter")
at.sleep(1)
at.write("Youtube.com", 0.1)
at.press("enter")
at.sleep(1)
apertar_tab(4)                 
at.write("tonigon", 0.1)
at.press("enter")               