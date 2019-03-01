#! /usr/bin/python
import random

class System:

    def __init__(self):

        self.jump_shadow = random.randint(1,6)
        self.orbits = self.jump_shadow + random.randint(1,6)

        #Determine if gas giants are present
        if random.randint(2,12) < 10:
            self.gas_giants = True
        else:
            self.gas_giants = False
        rolls = [None None]

        #Determine Inner, Habitable, and Outer zones
        for roll in rolls:
            roll = random.randint(1,6)
        if rolls[0] <= rolls[1]:
            lower = rolls[0]
            upper = rolls[1]
        else:
            lower = rolls[1]
            upper = rolls[0]
