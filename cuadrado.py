from codrone_edu.drone import *
import time
drone = Drone()
drone.pair()
#Este código no ha sido probado en un dron, por lo que puede contener errores lógicos
try:
    drone.takeoff()
    i = 0
    #Ciclo para hacer una ruta de vuelo cuadrada
    for i in range(4):
        #Avanza 0.5 m hacia enfrente
        drone.move_distance(0.5, 0, 0, 0.7)
        print("Termine de avanzar")
        time.sleep(0.3)
        #Gira hacia la izquierda
        drone.turn_degree(90, 3)
        print("Giré a la izquierda")
    drone.land()
except:
    print("Aterrizando")
    drone.land()
finally:
    drone.close()