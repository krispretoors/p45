def change_direction(current_direction, instruction):
    direction_list = ('N','E','S','W')
    if (instruction == 'L'):
        return direction_list[direction_list.index(current_direction) -1]
    elif(current_direction == 'W'):
        return direction_list[direction_list.index(current_direction) -3]
    else:
        return direction_list[direction_list.index(current_direction) +1]

def change_position(rover):
    direction = rover.direction
    if(direction == 'N' or direction == 'S'):
        if(direction == 'N'):
            rover.y = rover.y + 1
            return rover
        else: 
            rover.y = rover.y - 1
            return rover
    else:
        if(direction == 'E'):
            rover.x = rover.x + 1
            return rover
        else: 
            rover.x = rover.x - 1
            return rover