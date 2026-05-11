#Andres
# Module Imports
from LocoXtreme import Connection
from LocoXtreme import LocoXtreme
from LocoXtreme import MotorDirection as MD
from LocoXtreme import Data
from LocoXtreme import WaitType as WT
from LocoXtreme import Song
from LocoXtreme import Note
import time

# Create Connection Instance
connection = Connection()

# USB Connection Setup
connection.setup()

# Scan for Robots
robots = connection.scan(4000)

# Get Named Robot
robot = connection.get_robot(robots, "T800")

# Create LocoXtreme Object
locoxtreme = LocoXtreme(robot)

# Connect to LocoXtreme
locoxtreme.connect()

# Activate Motors
locoxtreme.activate_motors()

# Enable Sensors
locoxtreme.enable_sensor(Data.ULTRASONIC, 1)

# Pause for Initializations
time.sleep(0.4)
locoxtreme.set_light(0, 0, 0, 0)
locoxtreme.set_light(1, 0, 0, 0)
locoxtreme.set_light(2, 0, 0, 0)
locoxtreme.set_light(3, 0, 0, 0)
locoxtreme.set_light(4, 0, 0, 0)
locoxtreme.set_light(5, 0, 0, 0)
locoxtreme.set_light(6, 0, 0, 0)
locoxtreme.set_light(7, 0, 0, 0)
locoxtreme.sync_lights()

def move_forward():

    locoxtreme.set_light(6, 255, 0, 0)
    locoxtreme.set_light(2, 255, 0, 0)
    locoxtreme.sync_lights()

    time.sleep(0)

    locoxtreme.set_light(3, 255, 0, 0)
    locoxtreme.set_light(5, 255, 0, 0)
    locoxtreme.set_light(6, 0, 0, 0)
    locoxtreme.set_light(2, 0, 0, 0)
    locoxtreme.sync_lights()

    time.sleep(0)

    locoxtreme.set_light(4, 255, 0, 0)
    locoxtreme.set_light(3, 0, 0, 0)
    locoxtreme.set_light(5, 0, 0, 0)
    locoxtreme.sync_lights()

    time.sleep(0)
    locoxtreme.set_light(0, 0, 0, 0)
    locoxtreme.set_light(1, 0, 0, 0)
    locoxtreme.set_light(2, 0, 0, 0)
    locoxtreme.set_light(3, 0, 0, 0)
    locoxtreme.set_light(4, 0, 0, 0)
    locoxtreme.set_light(5, 0, 0, 0)
    locoxtreme.set_light(6, 0, 0, 0)
    locoxtreme.set_light(7, 0, 0, 0)
    locoxtreme.sync_lights()
    
    

def move_backward():

    locoxtreme.set_light(2, 255, 0, 0)
    locoxtreme.set_light(6, 255, 0, 0)
    locoxtreme.sync_lights()

    time.sleep(0)

    locoxtreme.set_light(7, 255, 0, 0)
    locoxtreme.set_light(1, 255, 0, 0)
    locoxtreme.set_light(2, 0, 0, 0)
    locoxtreme.set_light(6, 0, 0, 0)
    locoxtreme.sync_lights()

    time.sleep(0)

    locoxtreme.set_light(0, 255, 0, 0)
    locoxtreme.set_light(7, 0, 0, 0)
    locoxtreme.set_light(1, 0, 0, 0)
    locoxtreme.sync_lights()

    time.sleep(0)
    locoxtreme.set_light(0, 0, 0, 0)
    locoxtreme.set_light(1, 0, 0, 0)
    locoxtreme.set_light(2, 0, 0, 0)
    locoxtreme.set_light(3, 0, 0, 0)
    locoxtreme.set_light(4, 0, 0, 0)
    locoxtreme.set_light(5, 0, 0, 0)
    locoxtreme.set_light(6, 0, 0, 0)
    locoxtreme.set_light(7, 0, 0, 0)
    locoxtreme.sync_lights()
    
def turn_right():
   

    locoxtreme.set_light(0, 0, 255, 255)
    locoxtreme.set_light(4, 0, 255, 255)
    locoxtreme.sync_lights()

    time.sleep(0)

    locoxtreme.set_light(0, 0, 0, 0)
    locoxtreme.set_light(4, 0, 0, 0)
    locoxtreme.set_light(5, 0, 255, 255)
    locoxtreme.set_light(7, 0, 255, 255)
    locoxtreme.sync_lights()

    time.sleep(0)

    locoxtreme.set_light(5, 0, 0, 0)
    locoxtreme.set_light(7, 0, 0, 0)
    locoxtreme.set_light(6, 0, 255, 255)
    locoxtreme.sync_lights()

    time.sleep(0)

    locoxtreme.set_light(6, 0, 0, 0)
    locoxtreme.sync_lights()

    time.sleep(0)
    locoxtreme.set_light(0, 0, 0, 0)
    locoxtreme.set_light(1, 0, 0, 0)
    locoxtreme.set_light(2, 0, 0, 0)
    locoxtreme.set_light(3, 0, 0, 0)
    locoxtreme.set_light(4, 0, 0, 0)
    locoxtreme.set_light(5, 0, 0, 0)
    locoxtreme.set_light(6, 0, 0, 0)
    locoxtreme.set_light(7, 0, 0, 0)
    locoxtreme.sync_lights()
    
    
def rotate_180():
   

    locoxtreme.sync_lights()
    locoxtreme.set_light(0, 255, 255, 0)
    locoxtreme.sync_lights()

    time.sleep(0)

    locoxtreme.set_light(1, 255, 255, 0)
    locoxtreme.sync_lights()

    time.sleep(0)


    locoxtreme.set_light(2, 255, 255, 0)
    locoxtreme.sync_lights()

    time.sleep(0)


    locoxtreme.set_light(3, 255,255, 0)
    locoxtreme.sync_lights()

    time.sleep(0)


    locoxtreme.set_light(4, 255,255, 0)
    locoxtreme.sync_lights()

    time.sleep(0)


    
    locoxtreme.set_light(5, 255,255, 0)
    locoxtreme.sync_lights()

    time.sleep(0)


    locoxtreme.set_light(6, 255,255, 0)
    locoxtreme.sync_lights()

    time.sleep(0)


    locoxtreme.set_light(7, 255,255, 0)    
    locoxtreme.sync_lights()

    time.sleep(0)
    locoxtreme.set_light(4, 0, 0, 0)
    locoxtreme.set_light(0, 0, 0, 0)
    locoxtreme.set_light(1, 0, 0, 0)
    locoxtreme.set_light(2, 0, 0, 0)
    locoxtreme.set_light(3, 0, 0, 0)
    locoxtreme.set_light(4, 0, 0, 0)
    locoxtreme.set_light(5, 0, 0, 0)
    locoxtreme.set_light(6, 0, 0, 0)
    locoxtreme.set_light(7, 0, 0, 0)
    locoxtreme.sync_lights()

while True:
    move_forward()
    locoxtreme.setup_wait(WT.TIME, 1)   # move for 2 seconds
    locoxtreme.move(MD.FORWARD, MD.FORWARD, 5,5, False)
    locoxtreme.enable_sensor(Data.ULTRASONIC, 1)
    distance = locoxtreme.get_sensor_value(Data.ULTRASONIC)
    time.sleep(0)
    if distance <=17.5:
        locoxtreme.setup_wait(WT.TIME, 0)   # move for 2 seconds
        locoxtreme.move(MD.FORWARD, MD.FORWARD, 0,0, True)
        turn_right()
        distance2 =locoxtreme.get_sensor_value(Data.ULTRASONIC)
        
        locoxtreme.setup_wait(WT.ROTATION, 90) # 
        locoxtreme.move(MD.FORWARD, MD.BACKWARD, 3, 3, True)
        time.sleep(0)
        
        for i in range(1):
             # move for 2 seconds
            locoxtreme.setup_wait(WT.TIME, 0)   # move for 2 seconds
            locoxtreme.move(MD.FORWARD, MD.FORWARD, 0, 0, True) # Stop 
            
            locoxtreme.move(MD.FORWARD, MD.FORWARD, 3,3, False)
            distance3 = locoxtreme.get_sensor_value(Data.ULTRASONIC)
            time.sleep(0)
        
            if distance3 <=25:
                rotate_180()
                locoxtreme.setup_wait(WT.ROTATION, 180)
                locoxtreme.move(MD.FORWARD, MD.BACKWARD, 3, 3, True)
                time.sleep(0)
                continue
            
            


# Deactivate Motors
locoxtreme.deactivate_motors()

# Disconnect From LocoXtreme
locoxtreme.disconnect()