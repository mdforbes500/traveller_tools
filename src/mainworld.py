#! /usr/bin/python

import random

class MainWorld:

    def __init__(self):
        self.uwp = []

    def get_name(self):
        return self.uwp[0]

    def get_location(self):
        return self.uwp[1]

    def get_starport(self):
        return self.uwp[2]

    def get_size(self):
        return self.uwp[3]

    def get_atmo(self):
        return self.uwp[4]

    def get_hydro(self):
        return self.uwp[5]

    def get_pop(self):
        return self.uwp[6]

    def get_gov(self):
        return self.uwp[7]

    def get_law(self):
        return self.uwp[8]

    def get_tech(self):
        return self.uwp[9]

    def get_bases(self):
        return self.uwp[10]

    def get_codes(self):
        return self.uwp[11]

    def get_zone(self):
        return self.uwp[12]

    def set_name(self, name):
        self.uwp[0] = str(name)

    def set_location(self, x, y):
        self.uwp[1] = (x, y)

    def set_size(self):
        self.uwp[3] = random.randi(0,10)

    def set_atmo(self):
        lower = self.get_size() - 5
        upper = self.get_size() + 5
        self.uwp[4] = random.randi(lower, upper)

    def find_temperature(self):
        roll = random.randi(2, 12)
        if self.get_atmo() == 0 or self.get_atmo() == 1:
            temp = roll
        elif self.get_atmo() == 2 or self.get_atmo() == 3:
            temp = roll - 2
        elif self.get_atmo() == 4 or self.get_atmo() == 5 or self.get_atmo() == 14:
            temp = roll - 1
        elif self.get_atmo() == 6 or self.get_atmo() == 7:
            temp = roll
        elif self.get_atmo() == 8 or self.get_atmo() == 9:
            temp = roll + 1
        elif self.get_atmo() == 10 or self.get_atmo() == 13 or self.get_atmo() == 15:
            temp = roll + 2
        elif self.get_atmo() == 11 or self.get_atmo() == 12:
            temp = roll + 6
        else:
            print("Please set atmosphere...")
            return None
        return temp

    def set_hydro(self):
        temp = self.find_temp()
        lower = self.get_size() - 5
        upper = self.get_size() + 5
        roll = random.randi(lower, upper)
        if self.get_size() == 0 or self.get_size() == 1:
            self.uwp[5] = 0
        elif self.get_atmo() ~= 13 and (temp == 10 or temp == 11):
            self.uwp[5] = roll - 2
        elif self.get_atmo() ~= 13 and temp >= 12:
            self.uwp[5] = roll - 6
        else:
            self.uwp[5] = roll

    def set_pop(self):
        self.uwp[6] = random.randi(0,12)

    def set_gov(self):
        if self.get_pop() == 0:
            self.uwp[7] = 0
        else:
            self.uwp[7] = random.randi(-5, 5) + self.get_pop()

    def set_law(self):
        #I AM THE LAW
        if self.get_pop() == 0:
            self.uwp[8] = 0
        else:
            self.uwp[8] = random.randi(-5, 5) + self.get_gov()

    def set_starport(self):
        roll = random.randi(2, 12)
        if roll <= 2:
            self.uwp[2] = 'X'
        elif roll >= 3 and roll <= 4:
            self.uwp[2] = 'E'
        elif roll >= 5 and roll <= 6:
            self.uwp[2] = 'D'
        elif roll >= 7 and roll <= 8:
            self.uwp[2] = 'C'
        elif roll >= 9 and roll <= 10:
            self.uwp[2] = 'B'
        elif roll >= 11:
            self.uwp[2] = 'A'
        else:
            self.uwp[2] = 'X'

    def set_tech(self):
        roll = random.randi(1,6)
        if self.get_starport() == 'A':
            roll = roll + 6
        if self.get_starport() == 'B':
            roll = roll + 4
        if self.get_starport() == 'C':
            roll = roll + 2
        if self.get_size() == 0 or self.get_size() == 1:
            roll = roll + 2
        if self.get_size() == 2 or self.get_size() == 3 or self.get_size() == 4:
            roll = roll + 1
        if self.get_atmo() <= 3 or self.get_atmo() >= 10:
            roll = roll + 1
        if self.get_hydro() == 0 or self.get_hydro() == 9:
            roll = roll + 1
        if self.get_hydro() == 10:
            roll = roll + 2
        if (self.get_pop() >= 1 and self.get_pop() <= 5) or self.get_pop() == 9:
            roll = roll + 1
        if self.get_pop() == 10:
            roll = roll + 2
        if self.get_pop() == 11:
            roll = roll + 3
        if self.get_pop() == 12:
            roll = roll + 4
        if self.get_gov() == 0 or self.get_gov() == 5:
            roll = roll + 1
        if self.get_gov() == 7:
            roll = roll + 2
        if self.get_gov() == 13 or self.get_gov() == 14:
            roll = roll - 2
        self.uwp[9] = roll

    def set_bases(self):
        bases = []
        if self.get_starport() == 'A':
            if random.randi(2, 12) >= 8:
                bases.append('N')
            if random.randi(2, 12) >= 10:
                bases.append('S')
            if random.randi(2, 12) >= 8:
                bases.append('R')
            if random.randi(2, 12) >= 4:
                bases.append('TAS')
            if random.randi(2, 12) >= 6:
                bases.append('IC')
        elif self.get_starport() == 'B':
            if random.randi(2, 12) >= 8:
                bases.append('N')
            if random.randi(2, 12) >= 8:
                bases.append('S')
            if random.randi(2, 12) >= 10:
                bases.append('R')
            if random.randi(2, 12) >= 6:
                bases.append('TAS')
            if random.randi(2, 12) >= 8:
                bases.append('IC')
            if random.randi(2,12) >= 12:
                bases.append('P')
        elif self.get_starport() == 'C':
            if random.randi(2, 12) >= 8:
                bases.append('S')
            if random.randi(2, 12) >= 10:
                bases.append('R')
            if random.randi(2, 12) >= 10:
                bases.append('TAS')
            if random.randi(2, 12) >= 10:
                bases.append('IC')
            if random.randi(2, 12) >= 10:
                bases.append('P')
        elif self.get_starport() == 'D':
            if random.randi(2, 12) >= 7:
                bases.append('S')
            if random.randi(2, 12) >= 12:
                bases.append('P')
        elif self.get_starport() == 'E':
            if random.randi(2, 12) >= 12:
                bases.append('P')
        else:
            bases = []
        self.uwp[10] = bases

        def set_amber(self):
            if self.get_atmo() >= 10 or self.get_gov() == 0 or self.get_gov() == 7 or self.get_gov() == 10 or self.get_law() == 0 or self.get_law() >= 9:
                self.uwp[12] = 'A'

        def set_red(self):
            if self.get_zone() ~= 'R':
                self.uwp[12] = 'R'
            else:
                self.uwp[12] = ''

        
