#! /usr/bin/python
import random

class System:

    def __init__(self):

        self.jump_shadow = random.randint(1,6)
        self.orbits = self.jump_shadow + random.randint(1,6)

        #Determine if gas giants are present
        self.gas_giats = 0
        running = True
        counter = 0
        while running:
            if random.randint(2,12) < (10 - counter):
                self.gas_giants = self.gas_giants + 1
                counter = counter + 1
            else:
                running = False

        #Determine Inner, Habitable, and Outer zones
        roll_one = random.randint(1,6)
        roll_two = random.randint(1,6)
        if roll_one <= roll_two:
            lower = roll_one
            upper = roll_two
        else:
            lower = roll_two
            upper = roll_one

        self.inner = [None]*lower
        if (self.orbits - upper) >= 0:
            self.outer = [None]*(self.orbits - upper)
        else:
            self.outer = []
        if  (upper - lower) > 1 and ():
            self.habitable = [None]*(upper - lower)
