from mars_rover import MarsRover

class Mars:
    def __init__(__self__, x,y):
        __self__.x = x
        __self__.y = y

    def validate_boundary(__self__):
        if(MarsRover.x > __self__.x or MarsRover.x < 0):
            return False
        elif(MarsRover.y > __self__.y or MarsRover.y < 0):
            return False
        else: 
            return True