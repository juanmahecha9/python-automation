import pyautogui as robot
import time
import random

lista_canciones = ["this is the hunt","stereo love", "dutty love", "bandolero", "agárrala remix"]

# posiciones del curos paso a paso
# estas posiciones varian segun el equipo y la posion de las aplicaiones
browser = 35, 755
url = 395, 78
search_song = 1032, 156
song = 1109, 547
close_browser = 86,44

# funcion para hacer click en la pantalla
def do_click(pos, click=1):
    robot.moveTo(pos)
    robot.click(clicks=click)

# abrir navegador
do_click(browser)
time.sleep(2)

# ubicar en la barra de direcciones
do_click(url)
robot.typewrite("www.youtube.com")
time.sleep(0.5)
robot.hotkey("enter")
time.sleep(3)

# buscar cancion
song_name = random.randint(1, len(lista_canciones)) - 1
do_click(search_song, click=2)
robot.typewrite(lista_canciones[song_name])
robot.hotkey("enter")
time.sleep(2)

# abrir cancion
do_click(song)
time.sleep(20)

# cerrar navegador
do_click(close_browser)