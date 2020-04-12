#! /usr/bin/python
import random

class System:

    def __init__(self):
        # Step 1. Determine jump shadow
        self.jump_shadow = random.randint(1,6) # 100 x diamater of star (relative measurement)

        # Step 2. Number of significant orbits for the star
        n_orbits = self.jump_shadow + random.randint(1,6)
        self.orbits = {
            'inner': [],
            'habitable': [],
            'outer': []
        } 

        # Step 3. Determine if gas giants are present
        gas_giats = 0
        running = True
        counter = 0
        while running:
            if random.randint(2,12) < (10 - counter):
                gas_giants = gas_giants + 1
                counter = counter + 1
            else:
                running = False

        # Step 4. Determine Inner, Habitable, and Outer zones
        # Roll 2d6 and sort into lower and upper rolls 
        rolls = [random.randint(1,6), random.randint(1,6)]
        rolls = rolls.sort()
        last_inner_orbit = rolls[0]
        first_outer_orbit = rolls[1]

        # If one or less orbits between last inner orbit and first outer orbit,
        # there are no habitable orbits
        if (first_outer_orbit - last_inner_orbit) <= 1:
            self.orbits['habitable'] = None
        # Otherwise there are a number of habitable zones equal to the difference in
        # the two dice
        else:
            self.orbits['habitable'] = [None] * (first_outer_orbit - last_inner_orbit)
        self.orbits['outer'] = [None] * (n_orbits - first_outer_orbit)
        self.orbits['inner'] = [None] * (last_inner_orbit)
        companion = False

        # Step 5. Determine orbit characteristics from inner orbit outwards
        for orbit in self.orbits['inner']:
            rolls = [random.randint(1,6), random.randint(1,6)]
            rolls = rolls.sort()
            if rolls == [6,6] and companion is False:
                self.orbits['outer'].append('companion star')
                companion = True
            if rolls == [1,1] and not gas_giants == 0:
                orbit = 'Gas Giant'
                gas_giants -= 1
            else:
                if rolls[0] == 1:
                    orbit = 'small rock'
                    #add planet gen size 1-3
                elif rolls[0] == 2:
                    orbit = 'large rock'
                    #add planet gen size 4+
                elif rolls[0] == 3:
                    orbit = 'planetoid or belt'
                    #add planet gen size 0-1
                elif rolls[0] == 4:
                    orbit = 'small ice'
                    #add planet gen size 2-4
                elif rolls[0] == 5:
                    orbit = 'large ice'
                    #add planet gen size 5+
                else:
                    orbit = 'planetoid or belt'
                    #add planet gen size 0-1

            if self.orbits['habitable'] is not None: 
                for orbit in self.orbits['habitable']:
                rolls = [random.randint(1,6), random.randint(1,6)]
                rolls = rolls.sort()
                if rolls == [6,6] and companion is False:
                    self.orbits['outer'].append('companion star')
                    companion = True
                if rolls[0] == rolls[1] and not gas_giants == 0:
                    orbit = 'Gas Giant'
                    gas_giants -= 1
                else:
                    if (rolls[0] + rolls[1])//2 == 1:
                        orbit = 'small rock'
                        #add planet gen size 1-3
                    elif (rolls[0] + rolls[1])//2 == 2:
                        orbit = 'large rock'
                        #add planet gen size 4+
                    elif (rolls[0] + rolls[1])//2 == 3:
                        orbit = 'planetoid or belt'
                        #add planet gen size 0-1
                    elif (rolls[0] + rolls[1])//2 == 4:
                        orbit = 'small ice'
                        #add planet gen size 2-4
                    elif (rolls[0] + rolls[1])//2 == 5:
                        orbit = 'large ice'
                        #add planet gen size 5+
                    else:
                        orbit = 'planetoid or belt'
                        #add planet gen size 0-1

        for index, orbit in enumerate(self.orbits['outer']):
            rolls = [random.randint(1,6), random.randint(1,6)]
            rolls = rolls.sort()
            if rolls == [6,6] and companion is False:
                self.orbits['outer'].append('companion star')
                companion = True
            if ( (roll[0] + roll[1]) > (index + first_outer_orbit)//2 or rolls[0] == rolls[1] ) and not gas_giants == 0:
                orbit = 'Gas Giant'
                gas_giants -= 1
            else:
                if rolls[1] == 1:
                    orbit = 'small rock'
                    #add planet gen size 1-3
                elif rolls[1] == 2:
                    orbit = 'large rock'
                    #add planet gen size 4+
                elif rolls[1] == 3:
                    orbit = 'planetoid or belt'
                    #add planet gen size 0-1
                elif rolls[1] == 4:
                    orbit = 'small ice'
                    #add planet gen size 2-4
                elif rolls[1] == 5:
                    orbit = 'large ice'
                    #add planet gen size 5+
                else:
                    orbit = 'planetoid or belt'
                    #add planet gen size 0-1
        
        for index in range(gas_giants):
            if companion is False:
                self.orbits['outer'].append('Gas Giant')
            else:
                self.orbits['outer'].insert(-2, 'Gas Giant')

    # Step 6. Mainworld planetary placement using Method 3 from Book 3: Scout
    # Add content
