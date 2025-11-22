from codrone_edu.drone import *
drone = Drone()
drone.pair()
#Estacionarse en el cubo azul
drone.takeoff()

#Entra en un ciclo hasta que encuentre la pared bajo el aro verde
while(pared == 0):
    if(drone.detect_wall()):
        pared = 1
        print("encontre una pared")
    else:
        drone.move_forward(0.5, "ft", 0.5)

#Sale del while después de encontrar la pared del aro y lo atravieza
drone.hover(0.5)
drone.move_distance(0, 0, 20, 0.5)
drone.hover(0.5)
drone.move_forward(3, "ft", 0.5)
drone.hover(0.5)
drone.land()
drone.close()