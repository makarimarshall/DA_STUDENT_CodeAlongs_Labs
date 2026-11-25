#!/usr/bin/env python3
"""Meet the Objects: see DataChallengeOverview&Steps.md for the steps."""

import json

DATA_FILE = "../data/bike_stations.json"  # edit the filepath with the data

with open(DATA_FILE) as f:
    stations = json.load(f)


# ===== Day 1 =====

# Step 1: Reproduce the Parallel-List Bug and Name the Wrong Stations
# TODO: assign `names` and `bikes` to two empty lists
names = []
bikes = []
# TODO: loop over `stations`; append each one's "name" to `names`
for station in stations:
    names.append(station["name"])
    # TODO: append the same station's "bikes_available" to `bikes`
    bikes.append(station["bikes_available"])
names.pop(2)

print("stations in the file:", len(stations))
# TODO: loop over range(len(names)); print names[i], "|", bikes[i], "bikes"
for i in range(len(names)):
    print(names[i], "|", bikes[i], "bikes")

# Step 1, answer 1:
# Each record represents one bike station.
# Station ID and name hold text, while capacity and
# bikes_available hold whole numbers.
# needs_maintenance holds a Boolean value.
# No fields appear to be missing or inconsistent.

# Step 1, answer 2:
# pop(2) removes and returns the third station name,
# W 52 St & 11 Ave. Every name after it shifts one
# position to the left, but the bikes list stays the same.

# Step 1, answer 3:
# Cooper Square & Astor Pl gets 4 instead of 40.
# Vernon Blvd & 50 Ave gets 40 instead of 3.
# Bedford Ave & Nassau Ave gets 3 instead of 18.
# E 17 St & Broadway gets 18 instead of 11.
# Grand Concourse & E 161 St gets 11 instead of 20.
# Jackson Ave & 46 Rd gets 20 instead of 2.
# Amsterdam Ave & W 125 St gets 2 instead of 33.
# Amsterdam Ave & W 125 St's real count of 33
# bikes is never displayed.


# Step 2: Define the Station Class and Prove Two Instances Are Independent
class Station:
    # TODO: add __init__ with name (str), capacity and bikes_available (int)
    def __init__(self, name, capacity, bikes_available, needs_maintenance):
        # TODO: in __init__, assign each parameter to self.<same name>
        self.name = name
        self.capacity = capacity
        self.bikes_available = bikes_available
        # TODO: add a parameter and self.<name> for each extra field you agreed
        self.needs_maintenance = needs_maintenance

    # TODO: add needs_restock(self): True if bikes_available < capacity / 4
    def needs_restock(self):
        return self.bikes_available < self.capacity / 4


# TODO: assign `fleet` to []; loop over `stations` as `s`
fleet = []
for s in stations:
    # TODO: append Station(s["name"], s["capacity"], s["bikes_available"])
    fleet.append(Station(s["name"], s["capacity"],
                         s["bikes_available"], s["needs_maintenance"]))
# TODO: assign `busy`, `quiet` to two stations with equal needs_restock()
busy = fleet[1]
quiet = fleet[3]
# TODO: print both needs_restock() answers
print(busy.name, busy.needs_restock())
print(quiet.name, quiet.needs_restock())
# TODO: set busy.bikes_available to 0, then print both answers again
busy.bikes_available = 0
print(busy.name, busy.needs_restock())
print(quiet.name, quiet.needs_restock())

# Step 2, answer 1:
# Proposed attribute list:
# name: "where to send help"
# capacity: "nearly empty or jammed full"
# bikes_available: "nearly empty or jammed full"
# needs_maintenance: "a mechanic goes to stations that need one"

# Step 2, answer 2:
# N/A - No partner. Completed independently.

# Step 2, answer 3:
# I left out station_id because the station name
# identifies each location in this dataset.
# The dispatcher can make decisions using the name,
# capacity, bike count and maintenance status.

# Step 2, answer 4:
# Flatbush Ave & Bergen St and Cooper Square & Astor Pl
# both return False before the change.
# After setting Flatbush's bike count to 0, it returns
# True while Cooper Square still returns False.
# This proves that each instance has its own attributes.


# ===== Day 2 =====

# Step 3: Add `__str__` and Find Out Which of Four Prints It Changes
print(fleet[0])
print(fleet[:2])


# TODO: copy your Station class from Step 2 here
class Station:
    def __init__(self, name, capacity, bikes_available, needs_maintenance):
        self.name = name
        self.capacity = capacity
        self.bikes_available = bikes_available
        self.needs_maintenance = needs_maintenance

    def needs_restock(self):
        return self.bikes_available < self.capacity / 4

    # TODO: add __str__(self) to return text like "Grand Army Plaza: 6 of 48 bikes"
    # TODO: build it from self.name, self.bikes_available and self.capacity
    def __str__(self):
        return f"{self.name}: {self.bikes_available} of {self.capacity} bikes"


# TODO: rebuild `fleet` from this class with the same loop as Step 2
fleet = []
for s in stations:
    fleet.append(Station(s["name"], s["capacity"],
                         s["bikes_available"], s["needs_maintenance"]))

print(fleet[0])
print(fleet[:2])

# Step 3, answer 1:
# Prediction 1: One object with a memory address.
# Prediction 2: A list of two objects with memory addresses.
# Prediction 3: Grand Army Plaza: 6 of 48 bikes.
# Prediction 4: A list of two readable station descriptions.

# Step 3, answer 2:
# Prediction 4 is expected to be wrong.
# A list uses __repr__ for its objects instead of __str__.
# Adding __str__ changes the individual station print,
# but not how the station appears inside a list.


# Step 4: Add `__repr__` and Print the Van List for You and the Dispatcher
# TODO: copy your Station class from Step 3 here
class Station:
    def __init__(self, name, capacity, bikes_available, needs_maintenance):
        self.name = name
        self.capacity = capacity
        self.bikes_available = bikes_available
        self.needs_maintenance = needs_maintenance

    def needs_restock(self):
        return self.bikes_available < self.capacity / 4

    def __str__(self):
        return f"{self.name}: {self.bikes_available} of {self.capacity} bikes"

    # TODO: add __repr__(self) to return text like "Station('Grand Army Plaza', 6)"
    def __repr__(self):
        return f"Station('{self.name}', {self.bikes_available})"


# TODO: rebuild `fleet` from this class with the same loop as Step 2
fleet = []
for s in stations:
    fleet.append(Station(s["name"], s["capacity"],
                         s["bikes_available"], s["needs_maintenance"]))
# TODO: assign `van_list` to []; loop over `fleet`
van_list = []
for station in fleet:
    # TODO: append each station whose needs_restock() returns True to `van_list`
    if station.needs_restock():
        van_list.append(station)

print(van_list)
for station in van_list:
    print(station)

# Step 4, answer 1:
# I expect 5 stations to land in van_list.
# print(van_list) will use __repr__ for each station.

# Step 4, answer 2:
# __str__ gives the dispatcher a readable description
# of the station and its bike count.
# __repr__ helps the programmer identify objects
# when inspecting a list or debugging.

# Step 4, answer 3:
# I would give the dispatcher the second printout
# because each station is on its own line and shows
# how many bikes it has compared to its capacity.

# AI Output Validation
#
# AI explained that removing an item from only one
# parallel list causes the remaining positions to
# become misaligned.
#
# The dataset shows that seven stations receive
# incorrect bike counts after names.pop(2).
#
# AI explained that self refers to the individual
# object that calls a method.
# The two-station test should demonstrate that
# changing one object's attributes does not change
# the other object's attributes.
#
# AI explained that print(object) uses __str__,
# while a list uses __repr__ for its elements.
# The four prints can be used to check this.
#
# The dataset predicts five stations needing restock.
# Each station's bike count is compared to one
# quarter of its capacity.