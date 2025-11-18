from codrone_edu.drone import *
drone = Drone()
drone.pair()
drone.takeoff()
drone.hover(1)
arista = 0.5
angulo = 90
i = 0
#Funcion para hacer una ruta de vuelo cuadrada
def cuadrado(i, angulo, arista):
    lado = 3
    #Si detecta un muro el dron regresará 20 cm y dará media vuelta
    if(i > lado):
        print("He terminado mi recorrido :), aterrizando...")
        drone.land()
        drone.close()

    else:
        if(drone.detect_wall()):
            print("Encontré un muro, necesito girar")
            drone.set_drone_LED(255, 0, 0, 255)
            drone.move_backward(0.2, "m", 0.5)
            drone.turn_degree(180, 3)
            drone.hover(2)
            print("Terminé de estabilizarme 180")
            i = 0
        #Avanza 0.5 m hacia enfrente si no detecta un muro
        else:
            if (i == 0):
                drone.set_drone_LED(0, 255, 0, 255)
                drone.move_distance(arista, 0, 0, 0.5)
                print("Termine de avanzar, v ", i + 1)
                drone.hover(2)
                print("Terminé de estabilizarme, v ", i + 1)
            elif(i == 1):
                drone.set_drone_LED(0, 0, 255, 255)
                drone.move_distance(0, arista, 0, 0.5)
                print("Termine de avanzar, v ", i + 1)
                drone.hover(2)
                print("Terminé de estabilizarme, v ", i + 1)
            elif(i == 2):
                drone.set_drone_LED(255, 255, 0, 255)
                drone.move_distance(-arista, 0, 0, 0.5)
                print("Termine de avanzar, v ", i + 1)
                drone.hover(2)
                print("Terminé de estabilizarme, v ", i + 1)
            elif(i == 3):
                drone.set_drone_LED(0, 255, 255, 255)
                drone.move_distance(0, -arista, 0, 0.5)
                print("Termine de avanzar, v ", i + 1)
                drone.hover(2)
                print("Terminé de estabilizarme, v ", i + 1)
            #Gira hacia la izquierda
            drone.turn_degree(angulo * (i + 1), 3)
            print("Giré a la izquierda, v ", i + 1)
            drone.hover(2)
            print("Terminé de estabilizarme, v ", i + 1)
            i = i + 1
        cuadrado(i, angulo, arista)

cuadrado(i, angulo, arista)