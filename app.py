
import instruction_handler

def split_word(word):
    return [char for char in word]

def __main__():
    print("\n**********To exit this application just press Ctrl + c**********\n")
    rovers = []
    print("How many mars-rovers do you want to send to mars?")
    mars_rovers_count = int(input())

    for rover in range(mars_rovers_count):

        print("Please provide the width of the area which you want your rovers to roam:")
        area_length = int(input())

        print("Please provide the width of the area which you want your rovers to roam:")
        area_width = int(input())

        print("""Please provide the location of where you want your first mars_rover to land by specifying its x and y coordinates as well as the direction 
            separated by spaces eg: 1 3 N""")
        rover_coordinates = input()

        splitCoordinates = rover_coordinates.split()

        mars_rover = { "x": splitCoordinates[0], "y": splitCoordinates[1], "direction": splitCoordinates[2] }

        print("""Please provide instructions which the mars_rover must follow to roam its environment by only using 'L','R','M' where 'L' means left,
        'R' means right and 'M' means the mars_rover should move one block in its current direction eg: LMLMLMLMMR""")
        instructions = input()

        inst = split_word(instructions)

        for instruction in inst:
            if (instruction == 'L' or instruction == 'R'):
                mars_rover = instruction_handler.change_direction(mars_rover.direction, instruction)
            else: 
                mars_rover = instruction_handler.change_position(mars_rover)


if __name__ == "__main__":
    __main__()
