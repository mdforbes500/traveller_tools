#! /usr/bin/python

import mainworld as mw

world = mw.MainWorld()
world.set_name('Ophelia')
world.set_location(1,1)
world.set_size()
world.set_atmo()
world.set_hydro()
world.set_pop()
world.set_gov()
world.set_law()
world.set_starport()
world.set_tech()
world.set_bases()
world.set_amber()
world.update_codes()
print(world)
