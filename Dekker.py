import threading
import time

value = True
banderas = [0, 0]


def proceso(elemento):
    global banderas
    banderas[elemento] = 1

    if banderas[0] == 1 and banderas[1] == 0:
        print('Pronceso 1 ejecutandose, proceso 2 esperando ...')
        print('Termino proceso 1\n')
        time.sleep(1)
        banderas[0] = 0

    elif banderas[1] == 1 and banderas[0] == 0:
            print('Pronceso 2 ejecutandose, proceso 1 esperando ...')
            print('Termino proceso 2\n')
            time.sleep(1)
            banderas[1] = 0


while value:
    for i in range(2):
        thread = threading.Thread(target=proceso, args=(i, ))
        thread.start()
        thread.join()

