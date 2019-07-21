# import instruction_handler
from mars_rover import MarsRover
from mars import Mars


def split_word(word): 
    return [char for char in word]

def set_mars_plateau():
    while True:
        try:
            mars_plateau  = input("Provide the area (length and width) which you want your rover to roam (must be 2 integer values and separated by a space eg: 5 5): \n").split()
            if(len(mars_plateau) < 2 or len(mars_plateau) > 2):
                print("\n***Please add space between values***\n")
                continue

            mars_plateau = Mars(int(mars_plateau[0]),int(mars_plateau[1]))
            return mars_plateau
            
        except ValueError:
            print("\n***Sorry, I didn't understand that. Please provide valid Integer values***\n")
            continue
        else:
            break

def get_rovers_count():
    while True:
        try:
            rovers_count = int(input("How many rovers do you want deployed to Mars?\n"))
            return rovers_count
        except ValueError:
            print("***Sorry, I didn't understand that. Please provide an Integer value***\n")
            continue
        else:
            break

def validate_rover(rover):
    directions = ("N","E","S","W")
    while True:
        try:
            if ((rover[2].upper() in directions) and len(rover) == 3):
                return True
        except IndexError:
            print("Invalid rover coordinates provided, please try again")
            return False
        else:
            break

def validate_instructions(instructions):
    valid_instructions_list = ("L","M","R")
    for instruction in instructions:
        if(instruction in valid_instructions_list):
            continue
        else:
            return False
    return True

def create_new_rover(rover):
    while True:
        try:
            rover_coordinates = input("""Please provide the location of where you want your mars_rover to land by specifying its x and y coordinates as well as the direction 
            separated by spaces eg: 1 3 N: \n""")
            split_coordinates = rover_coordinates.split()
            is_valid_rover = validate_rover(split_coordinates)

            if(is_valid_rover):
                rover = MarsRover(int(split_coordinates[0]),int(split_coordinates[1]), split_coordinates[2].upper())
                return rover
            else:
                continue
            
        except ValueError:
            print("***Sorry, I didn't understand that. Please provide an Integer value ***")
            continue
        else:
            break
   
def get_instructions(rover):
    while True:
        try:
            instructions = input("""Please provide instructions which the mars_rover must follow to roam its environment by only using 'L','R','M' where 'L' means to turn left,
            'R' means to turn right and 'M' means that the mars_rover should move one block in its current direction eg: LMLMLRRLMMR: \n""")
            instruction_list = split_word(instructions)
            isvalid = validate_instructions(instruction_list)
            if(not isvalid):
                continue
            else:
                return instruction_list

        except ValueError:
            continue
        else:
            break

def __main__():
    rovers = []
    print("\n**********To exit this application just press Ctrl + c**********\n")
    roam_area = set_mars_plateau()
    rovers_count = get_rovers_count()

    for rover in range(0,rovers_count):
        marsrover = create_new_rover(rover)
        instructions = get_instructions(rover)
        for instruction in instructions:
            if (instruction == "L"):
                marsrover.turn_left()
            elif(instruction == "R"):
                marsrover.turn_right()
            else:
                marsrover.move_forward()

        rovers.append(marsrover)

    for rv in rovers:
        print(rv.x, rv.y, rv.direction)

if __name__ == "__main__":
    __main__()