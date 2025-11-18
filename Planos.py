from codrone_edu.drone import *
drone = Drone()
drone.pair()
drone.takeoff()
drone.hover(1.5)

#Adelante
print("adelante")
drone.move_distance(0.5, 0, 0, 0.5)
drone.hover(1)
#Atrás
print("atras")
drone.move_distance(-0.5, 0, 0, 0.5)
drone.hover(1)
#Izquierda(?
print("izquierda")
drone.move_distance(0, 0.5, 0, 0.5)
drone.hover(1)
#Derecha(?
print("derecha")
drone.move_distance(0, -0.5, 0, 0.5)
drone.hover(1)
drone.land()
drone.close()