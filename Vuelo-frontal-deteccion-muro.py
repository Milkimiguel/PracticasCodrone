#Python code
from codrone_edu.drone import *
import time

drone = Drone()
drone.pair()

try:
    ciclo = True
    i = 0
    drone.takeoff()
    #En este ciclo, el dron se va a mover en intervalos de 0.5 m en eje x 
    #hasta que el valor i sea mayor a 1
    #o hasta que detecte un muro enfrente
    while(ciclo):
        #Se mueve medio metro en el eje x a 0.7 de velocidad
        drone.move_distance(0.5, 0, 0, 0.7)
        #Verifica si está detectando un muro y se gira 180°
        if(drone.detect_wall()):
            #Se mueve hacia atrás en el eje x en caso de que termine pegado a la pared detectada
            drone.move_distance(-0.2, 0, 0, 0.1)
            drone.turn_degree(180, 3)
            time.sleep(1) 
            ciclo = False
        if (i > 1):
            ciclo = False
            drone.land()
        i+=1
    drone.land()
    #...acciones del dron...
except:
    print("Interrupción manual, aterrizando...")
    drone.land()
finally:
    drone.close()