from codrone_edu import *
import time
#Este código no ha sido probado en un dron, por lo que puede contener errores lógicos
drone = Drone()
drone.pair()
#La idea de ésto es que el dron vea si tiene una pared frente a él, si no
#avanza 50 cm hacia enfrente, luego retroceda 50 cm, como si se estuviera meciendo
try:
    drone.takeoff()
    for i in range(5):
        if (drone.detect_wall()):
            print("Encontré un muro, voy a girar del perro coraje q traigo atorado")
            drone.set_drone_LED(255, 0, 0, 255)
            drone.turn_degree(90, 3)
        print("Voy a avanzar medio metro, taka taka, taka taka")
        drone.move_distance(0.5, 0, 0, 0.7)
        print("Me dio miedo, me voy a regresar medio metro")
        drone.move_distance(-0.5, 0, 0, 0.7)
    drone.land()
except:
    print("Algo paso, necesito aterrizar de emergencia")
    drone.land()
finally:
    drone.close()