
directions = ("N","E","S","W")

class MarsRover:
    def __init__(__self__, x, y, direction):
        __self__.x = int(x)
        __self__.y = int(y)
        __self__.direction = direction

    def turn_left(__self__):
        __self__.direction = directions[directions.index(__self__.direction)-1]

    def turn_right(__self__):
        if (__self__.direction == "W"):
            __self__.direction = directions[directions.index(__self__.direction)-3]
        else:
            __self__.direction = directions[directions.index(__self__.direction)+1]

    def move_forward(__self__):
        if(__self__.direction == 'N'):
            __self__.y =  __self__.y + 1
        elif(__self__.direction == 'S'):
            __self__.y = __self__.y- 1  
        elif(__self__.direction == 'E'):
            __self__.x = __self__.x+ 1
        else:
            __self__.x = __self__.x- 1