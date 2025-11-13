from codrone_edu.drone import *
from time import sleep

drone = Drone()

drone.pair()


drone.takeoff()

for x in range(0, 4, 1):

    drone.set_pitch(50)   

    drone.move(0.5) 
    sleep(2)
    drone.set_pitch(0)    

    drone.set_yaw(-50)   

    drone.move(0.5)

    drone.set_yaw(0)      
    sleep(2)

drone.land()

drone.close()