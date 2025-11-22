from codrone_edu.drone import *
drone = Drone()
drone.pair()
#Estacionarse encima del cubo azul
drone.takeoff()
drone.hover(0.5)
drone.move_forward(2.15, "ft", 0.5)
drone.hover(0.5)
drone.land()
drone.close()





