import threading, queue
import time
import random

numFilosofo=5
queue = queue.Queue(maxsize=numFilosofo)

comenzar = []

def hambre():

    for item in range(numFilosofo):
        ban = True

        while ban:
            posicion = random.randint(1,numFilosofo)
            if not posicion in comenzar:
                comenzar.append(posicion)
                ban=False  

        if not queue.full():
            queue.put(posicion)

def filosofos():
    cont=0
    while cont < numFilosofo:
        #while True:
        if not queue.empty():
            item = queue.get()
            time.sleep(2)
            print('FILOSOFO', item, 'COMIENDO')
            cont=cont+1
            time.sleep(3)
            print('FILOSOFO',item, 'TERMINO DE COMER')
            time.sleep(2)
            print("FILOSOFOS QUE FALTAN! ", queue.qsize())
            queue.task_done()
        

if __name__ == '__main__':
  
    thread_productor = threading.Thread(target=hambre).start() 
    thread_consumidor = threading.Thread(target=filosofos).start()
        
   