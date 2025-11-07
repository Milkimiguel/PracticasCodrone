from codrone_edu.drone import *
import time
drone = Drone()
drone.pair()
#Este código no ha sido probado en un dron, por lo que puede contener errores lógicos
try:
    drone.takeoff()
    print("Buenos dias estrellitas, el cielo les dice hola")
    drone.move_distance(0.2, 0, 0, 0.7)
    time.sleep(0.2)
    for i in range(3):
        #Si detecta una pared, la luz se vuelve roja y gira 90 grados
        if (drone.detect_wall()):
            print("Encontre un muro")
            drone.set_drone_LED(255, 0, 0, 255)
            drone.turn_degree(90, 3)
            time.sleep(0.2)
        #Si no detecta una pared, la luz es verde y avanza 20 cm
        print("Todo bien, seguimos")
        drone.set_drone_LED(0, 255, 0, 255)
        drone.move_distance(0.2, 0, 0, 0.7)
        time.sleep(0.2)

except:
    print("error, aterrizaje de emergencia")
    drone.land()
finally:
    drone.close()