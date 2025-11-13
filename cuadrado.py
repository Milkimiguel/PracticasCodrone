from codrone_edu.drone import *
import time
drone = Drone()
drone.pair()
#Este código no ha sido probado en un dron, por lo que puede contener errores lógicos
drone.takeoff()
time.sleep(1)
i = 0
lado = 0.5
#Ciclo para hacer una ruta de vuelo cuadrada
for i in range(4):
    #Si detecta un muro el dron regresará 20 cm y dará media vuelta
    if(drone.detect_wall()):
        print("Encontré un muro, necesito girar")
        drone.set_drone_LED(255, 0, 0, 255)
        drone.move_backward(0.2, "m", 0.5)
        drone.turn_degree(180, 3)
        time.sleep(2)
    #Avanza 0.5 m hacia enfrente si no detecta un muro
    else:
        drone.set_drone_LED(0, 255, 0, 255)
        drone.move_forward(lado, "m", 0.5)
        print("Termine de avanzar, v ", i + 1)
        time.sleep(2)
        #Gira hacia la izquierda0
        drone.turn_degree(90, 3)
        print("Giré a la izquierda, v ", i + 1)
        time.sleep(2)
print("He terminado mi recorrido :), aterrizando...")
drone.land()
drone.close()