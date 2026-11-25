#!/usr/bin/env python3
"""Data Challenge: Build It Once, Use It Again
GitBook Quest 1.2: Build It Once, Use It Again

HOW TO RUN
    python3 build-it-once/build-it-once_STUDENT.py

THE DATA: data/rec_center_signups.txt
"""

############################################################################
# THE DATA
############################################################################

# 1. What does one row represent?
# Your answer:
# Each row represents one member signing up for a class
# and the number of sessions they booked.

# 2. Which fields hold numbers, and which hold text?
# Your answer:
# member and class_name hold text.
# sessions holds numbers.

# 3. What already looks wrong, missing or inconsistent?
# Your answer:
# I don't see any missing values or inconsistent records.
# Each row has a member, class name, and session count.


############################################################################
# DAY 1
############################################################################

# ===== Step 1: Write total_sessions(), Then Call It on Every Class and on Swim Only =====

# My predictions:
# Total sessions across all classes: 45
# Total Swim sessions: 15

with open("data/rec_center_signups.txt") as f:
    signups = [line for line in f.read().splitlines()
               if line and not line.startswith("#")]


def total_sessions(records):
    total = 0
    for record in records:
        fields = record.split(",")
        sessions = int(fields[2])
        total += sessions
    return total


swim_only = []

for record in signups:
    if record.split(",")[1] == "Swim":
        swim_only.append(record)

print("every class:", total_sessions(signups))
print("swim only:  ", total_sessions(swim_only))


# ===== Step 2: Count Long Bookings at Two Different Cutoffs With One Function =====

# My predictions:
# 4 or more sessions: 7 records
# 2 or more sessions: 11 records


def count_long_bookings(records, minimum):
    count = 0
    for record in records:
        fields = record.split(",")
        sessions = int(fields[2])
        if sessions >= minimum:
            count += 1
    return count


def show_long_bookings(records, minimum):
    count = count_long_bookings(records, minimum)
    print(f"There are {count} bookings with {minimum} or more sessions.")


print("returned:", count_long_bookings(signups, 4))
print("returned:", count_long_bookings(signups, 2))

handed_back = show_long_bookings(signups, 4)
print("what show_long_bookings handed back:", handed_back)

# Your answer:
# handed_back is None because show_long_bookings prints
# a message but does not return a value.
# minimum is a parameter in the function definition.
# The values 4 and 2 are arguments passed into the function.


# ----- Share Out: Day 1 -----

# Your notes for the share out:
# Total sessions: 45. Swim sessions: 15.
# Reusing total_sessions avoids rewriting the same loop.
# Return sends a value back to the caller.
# Print displays information in the terminal.
# show_long_bookings returns None because it only prints.
# minimum is a parameter, while 4 and 2 are arguments.


############################################################################
# DAY 2
############################################################################

# ===== Step 3: Count the Same Bookings Without a Cutoff Parameter, and Compare =====

# My predictions:
# Cutoff of 4: 7 bookings
# Cutoff of 2: 11 bookings
# Lowering the cutoff allows more bookings to qualify.

sessions_cutoff = 4


def count_reaching_outside(records):
    count = 0
    for record in records:
        fields = record.split(",")
        sessions = int(fields[2])
        if sessions >= sessions_cutoff:
            count += 1
    return count


print("cutoff", sessions_cutoff, "gives", count_reaching_outside(signups))

sessions_cutoff = 2

print("cutoff", sessions_cutoff, "gives", count_reaching_outside(signups))
print("comparison:", count_long_bookings(signups, 4))

# Your answer:
# I would trust count_long_bookings more because the cutoff
# is passed directly into the function as an argument.
# I can see what cutoff is being used without having to
# search for a global variable somewhere else in the file.


# ===== Step 4: Pass the Last Member In and Out, Then Trigger an UnboundLocalError =====


def log_signup(record, previous_member):
    current_member = record.split(",")[0]
    print("previous:", previous_member, "current:", current_member)
    return current_member


# My predictions:
# previous: nobody yet current: Nia
# previous: Nia current: Omar

last_member = "nobody yet"

last_member = log_signup(signups[0], last_member)
last_member = log_signup(signups[1], last_member)


last_seen = "nobody yet"


def log_signup_broken(record):
    # Leave this body exactly as written. It is supposed to raise.
    print("previous:", last_seen)
    last_seen = record.split(",")[0]
    return last_seen


# Prediction:
# The print statement may fail because the function tries
# to read last_seen before assigning it a local value.

# Commented out after observing the intentional error.
# log_signup_broken(signups[2])

# Your answer:
# The exception was UnboundLocalError.
# The variable that caused the error was last_seen.
# In the original traceback, the error pointed to line 271.
# Python treats last_seen as a local variable because
# it is assigned a value inside the function.
# The print statement tries to access it before that assignment.


# ----- Share Out: Day 2 -----

# Your notes for the share out:
# I would trust count_long_bookings because the cutoff is
# explicitly passed into the function.
# The exception was UnboundLocalError involving last_seen.
# Python treats a variable assigned inside a function as local
# unless it is declared otherwise.
# The print statement failed because the local variable
# had not been assigned a value yet.
# Removing the assignment would allow Python to read
# last_seen from the global scope.
# AI explained that using global was not the recommended fix.
# Instead, the working function passes the previous member
# as an argument and returns the current member.


############################################################################
# DAY 3
############################################################################

# ===== Step 5: Build Per-Member Totals Out of Three Functions, Not One =====


def sessions_in(record):
    fields = record.split(",")
    sessions = int(fields[2])
    return sessions


def signups_for(records, member):
    matches = []
    for record in records:
        if record.split(",")[0] == member:
            matches.append(record)
    return matches


def total_for(records, member):
    total = 0
    for record in signups_for(records, member):
        total += sessions_in(record)
    return total


# My prediction:
# Gwen's total is 2 + 6 = 8 sessions.

members = ["Nia", "Omar", "Tess", "Rafi", "Gwen"]

for member in members:
    print(member, total_for(signups, member))


# ===== Step 6: Run total_for() on Five Inputs Nobody Asked For, Then Judge Each Answer =====

print("empty list:", total_for([], "Nia"))
# Right: There are no records to count.

print("one record:", total_for([signups[0]], "Nia"))
# Right: Nia booked 4 sessions in the first record.

print("missing member:", total_for(signups, "Marco"))
# Misleading: Marco does not exist in the dataset.
# A missing member is different from a member with zero sessions.

print("lowercase name:", total_for(signups, "nia"))
# Misleading: Nia exists, but Python is case sensitive.

print("empty filtered list:", signups_for([], "Nia"))
# Right: An empty list has no matching records.


member_sum = 0

for member in members:
    member_sum += total_for(signups, member)

print("member totals:", member_sum, "whole file:", total_sessions(signups))


# ----- Share Out: Day 3 -----

# Your notes for the share out:
# The lowercase name returns zero even though Nia has sessions.
# I would make the name comparison case insensitive.
# I would also separate missing members from members with zero sessions.
# The member totals should add up to 45, matching the whole file.
# For a larger file I would collect all unique member names
# and compare their combined totals to the whole file total.
# Three functions allow me to reuse different parts of the code
# without rewriting the same logic.
# Next time I would consider how to handle invalid or missing
# session values.