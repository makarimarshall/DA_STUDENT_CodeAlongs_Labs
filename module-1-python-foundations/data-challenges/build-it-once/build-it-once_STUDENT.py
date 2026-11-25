#!/usr/bin/env python3
"""Data Challenge: Build It Once, Use It Again
GitBook Quest 1.2: Build It Once, Use It Again

HOW TO RUN
    Open a terminal in the folder that holds data/ and run:
        python3 build-it-once_STUDENT.py
    If this file sits one folder below data/, run it from the folder
    above instead:  python3 build-it-once/build-it-once_STUDENT.py
    Or make it executable once:
        chmod +x build-it-once_STUDENT.py
    and from then on run it directly:
        ./build-it-once_STUDENT.py
    The first line, #!/usr/bin/env python3 (the "shebang"), is what
    makes ./ work. python3 <file> ignores it as a comment.

THE DATA      data/rec_center_signups.txt

ANSWER EVERYTHING IN THIS FILE
    - Code goes under each step's banner.
    - Written answers go in # comments under each "# Your answer:"
      line.
    - Run the file after every change. It runs top to bottom, so a
      later step can use anything an earlier step made.

HINTS live in the worksheet (DataChallengeOverview&Steps.md), collapsed
under each step. Open one only when you are stuck.

AI TOOLKIT: prompts to try and how to check them are in
DataChallengeOverview&Steps.md.

SUBMIT
    Commit this file (you may rename it build-it-once.py) to your own data
    challenge repo, inside your Module 1 folder. Paste its direct GitHub URL
    into the LMS.
    Submit once, at the end of Day 3. Keep every day's work in here.
"""

############################################################################
#  THE DATA: open data/rec_center_signups.txt and look at it
#  before you write any code. The worksheet's "The Data" section
#  shows how to load it.
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
#  DAY 1
############################################################################

# ===== Step 1: Write total_sessions(), Then Call It on Every Class and on Swim Only =====
# One function that adds up a sessions column, called twice: once on every
# record, once on just the Swim records.
#
# 1. Predict two numbers by hand off the file. Total sessions across every
#    class: add the third field down all 13 records. Total sessions for Swim
#    only: add that same field, but only on the records whose class is Swim.
#    Write both in a comment before you run anything.
# 2. Write total_sessions(records) so it adds up the sessions column across
#    every record in records and hands the total back with return, not
#    print.
# 3. Build swim_only: the records whose class is Swim, and nothing else.
# 4. Run it, and check both printed numbers against your two predictions.
#
# The arithmetic is the same arithmetic a plain loop would do. What changes
# is that the answer comes back to you instead of going to the screen.

# My predictions:
# Total sessions across all classes: 45
# Total Swim sessions: 15

with open("data/rec_center_signups.txt") as f:
    signups = [line for line in f.read().splitlines()
               if line and not line.startswith("#")]

def total_sessions(records):
    # TODO: add up the sessions column across every record in `records`
    # TODO: hand the total back to whoever called this. Do not print it.
    total = 0
    for record in records:
        fields = record.split(",")
        sessions = int(fields[2])
        total += sessions
    return total

swim_only = []
# TODO: fill swim_only with just the Swim records
for record in signups:
    if record.split(",")[1] == "Swim":
        swim_only.append(record)

print("every class:", total_sessions(signups))
print("swim only:  ", total_sessions(swim_only))

# ===== Step 2: Count Long Bookings at Two Different Cutoffs With One Function =====
# The board changed the long-booking cutoff from 4 sessions to 2. Answering
# both should cost you one extra argument, not a second function.
#
# 1. Predict both returned: counts in a comment, reading the third field
#    down the file: once for 4 or more, once for 2 or more.
# 2. Write count_long_bookings(records, minimum) so it counts the records
#    whose sessions number is minimum or more, and returns that count.
# 3. Write show_long_bookings(records, minimum) so it prints a sentence with
#    the same count in it. Only print. Do not add a return.
# 4. Run the whole file, including the lines at the bottom that were written
#    for you.
# 5. Write down what handed_back holds, and why. It is on the last printed
#    line.
# 6. Name the parameter and the arguments, pointing at the lines: which name
#    is minimum, and which values are the 4 and the 2.
#
# One of the two functions you just wrote gives you something back. The
# other only puts something on the screen.

def count_long_bookings(records, minimum):
    # TODO: count the records whose sessions number is `minimum` or more
    # TODO: return the count
    count = 0
    for record in records:
        fields = record.split(",")
        sessions = int(fields[2])
        if sessions >= minimum:
            count += 1
    return count

# My predictions:
# 4 or more sessions: 7 records
# 2 or more sessions: 11 records

def show_long_bookings(records, minimum):
    # TODO: print a sentence with the same count in it. Only print.
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
# Last 15 minutes, back together as a class. Bring:
#
# - Your two totals. Whole file, and Swim only. If your numbers differ from
#   another group's, say so. You read the same file, so one of you has a bug
#   worth finding.
# - Your function next to the loop it replaced. Name the specific thing that
#   got easier. Not "cleaner."
# - What show_long_bookings handed back, and why. Say what that tells you
#   about return versus print.
# - Which name is the parameter and which value is the argument, pointing at
#   your own two lines.
#
# Be ready to answer "why did you do it that way?"

# Your notes for the share out:
# Total sessions: 45. Swim sessions: 15.
# Reusing total_sessions avoids rewriting the same loop.
# Return sends a value back to the caller.
# Print displays information in the terminal.
# show_long_bookings returns None because it only prints.
# minimum is a parameter, while 4 and 2 are arguments.

############################################################################
#  DAY 2
############################################################################

# ===== Step 3: Count the Same Bookings Without a Cutoff Parameter, and Compare =====
# Two functions that answer the same question. The one you wrote on Day 1
# takes the cutoff as a parameter. This one takes no cutoff at all.
#
# 1. Predict both printed counts with no new arithmetic. You already
#    produced the count at a cutoff of 4 and the count at a cutoff of 2 in#    Day 1's second step. All you are predicting here is which of those two
#    numbers each of the two identical-looking calls prints. Write both in a
#    comment, and write why.
# 2. Write count_reaching_outside(records) so it counts the same thing
#    count_long_bookings does, but takes no minimum parameter. It reads
#    sessions_cutoff from outside the function instead.
# 3. Call it once at a cutoff of 4, printing the result.
# 4. Call it again, unchanged, after sessions_cutoff becomes 2, and print
#    that result too. The call line is identical both times.
# 5. Print count_long_bookings(signups, 4) underneath for comparison.
#
# Both versions run clean. Decide which of the two you would trust in a file
# you did not write, and say what in the call line told you.

# My predictions:
# Cutoff of 4: 7 bookings
# Cutoff of 2: 11 bookings
# Lowering the cutoff allows more bookings to qualify.

sessions_cutoff = 4

def count_reaching_outside(records):
    # TODO: same count as count_long_bookings, but take NO minimum
    # parameter. Read sessions_cutoff from outside the function instead.
    count = 0
    for record in records:
        fields = record.split(",")
        sessions = int(fields[2])
        if sessions >= sessions_cutoff:
            count += 1
    return count

print("cutoff", sessions_cutoff, "gives", count_reaching_outside(signups))

sessions_cutoff = 2

# TODO: call count_reaching_outside(signups) again, unchanged, and print it
# TODO: print count_long_bookings(signups, 4) underneath for comparison
print("cutoff", sessions_cutoff, "gives", count_reaching_outside(signups))
print("comparison:", count_long_bookings(signups, 4))

# Your answer:
# I would trust count_long_bookings more because the cutoff
# is passed directly into the function as an argument.
# I can see what cutoff is being used without having to
# search for a variable somewhere else in the file.

# ===== Step 4: Pass the Last Member In and Out, Then Trigger an UnboundLocalError =====
# The coordinator wants each sign-up printed next to the one before it. The
# top half is yours to write. The bottom half is written for you, and is
# supposed to raise.
#
# 1. Write log_signup(record, previous_member) so it pulls the member name
#    out of record, prints the previous member and this one on one line, and
#    returns this member's name.
# 2. Call it on signups[0], then on signups[1], storing what it returns back
#    into last_member each time. Predict both printed lines in a comment
#    first, reading the names off the top of the file.
# 3. Leave log_signup_broken exactly as written. It tries the same job by
#    reading and then updating last_seen, a name defined above the function.
# 4. Predict in a comment whether its print line will work. The step above
#    showed a function reading an outside name just fine.
# 5. Run the file, read the traceback, and write down the exception name,
#    the variable and the line it points at, in your own words, before you
#    look anything up.
#
# global is not the fix. The working half of this same step already shows
# what is: pass the value in, return it back out.
#
# This step is supposed to raise UnboundLocalError. Run it, read the
# traceback, answer below, then put a # in front of the line that raises so
# the steps after it can run.

def log_signup(record, previous_member):
    # TODO: pull the member name out of `record`
    # TODO: print the previous member and this one on one line
    # TODO: return this member's name
    current_member = record.split(",")[0]
    print("previous:", previous_member, "current:", current_member)
    return current_member

# Expected output:
# previous: nobody yet current: Nia
# previous: Nia current: Omar

last_member = "nobody yet"
# TODO: call log_signup on signups[0], then on signups[1], storing
# what it returns back into last_member each time
last_member = log_signup(signups[0], last_member)
last_member = log_signup(signups[1], last_member)

last_seen = "nobody yet"

def log_signup_broken(record):
    # Leave this body exactly as written. It is supposed to raise.
    print("previous:", last_seen)
    last_seen = record.split(",")[0]
    return last_seen

# The print statement fails because last_seen is treated
# as a local variable before it is assigned a value.

# log_signup_broken(signups[2])

# Your answer:
# The exception was UnboundLocalError.
# The variable that caused the error was last_seen.
# The original traceback pointed to line 271.
# Python treats last_seen as a local variable because
# it is assigned a value inside the function.
# The print statement tries to access it before that assignment.

# ----- Share Out: Day 2 -----
# Last 15 minutes, back together as a class. Bring:
#
# - Which of the two functions you would trust in a file you did not write,
#   and what in the call line decided it.
# - The exception name and the variable it named, plus your own one-sentence
#   account of the rule. Written before you looked anything up.
# - Why the print line failed when it only reads last_seen, and what
#   deleting the line below it changed.
# - Anything AI told you about global. Say whether it offered it as the fix,
#   and what you did instead.
#
# Be ready to answer "why did you do it that way?"

# Your notes for the share out:
# I would trust count_long_bookings because the cutoff is
# directly passed into the function.
# The exception was UnboundLocalError involving last_seen.
# Python treats a variable assigned inside a function as local
# unless it is declared otherwise.
# The print statement failed because the local variable
# had not been assigned a value yet.
# Removing the assignment would allow Python to read
# last_seen from outside the function.
# AI explained that global was not the recommended fix.
# Instead, the working function passes the previous member
# as an argument and returns the current member.

############################################################################
#  DAY 3
############################################################################

# ===== Step 5: Build Per-Member Totals Out of Three Functions, Not One =====
# The coordinator wants per-member totals. Write this as three functions,
# not one.
#
# 1. Write sessions_in(record) so it pulls the sessions number out of a
#    single record and returns it.
# 2. Write signups_for(records, member) so it returns just the records
#    belonging to one member.
# 3. Write total_for(records, member) so it returns that member's total
#    sessions, doing almost nothing itself. It gets its work done by calling
#    the other two.
# 4. Predict Gwen's total in a comment, adding up Gwen's rows in the file by
#    hand.
# 5. Print one line per member for Nia, Omar, Tess, Rafi and Gwen, and check
#    Gwen's line against your comment.
#
# Before you run it, show your partner the line where each of the three
# functions gets called.

# Three function names. Everything else is yours.

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
    # This one should get its work done by calling the other two.
    total = 0
    for record in signups_for(records, member):
        total += sessions_in(record)
    return total

# Expected Gwen total: 2 + 6 = 8 sessions.

# TODO: print a line per member
members = ["Nia", "Omar", "Tess", "Rafi", "Gwen"]

for member in members:
    print(member, total_for(signups, member))

# ===== Step 6: Run total_for() on Five Inputs Nobody Asked For, Then Judge Each Answer =====
# No new functions. Call the ones you already have on inputs nobody asked
# for, and write a verdict beside each printed result.
#
# 1. total_for on an empty list. Print the result.
# 2. total_for on a list holding exactly one record.
# 3. total_for with a member name that is not in the file at all, such as
#    "Marco".
# 4. total_for with a name differing from a real member's only by
#    capitalization, such as "nia" for Nia.
# 5. signups_for on the empty list.
# 6. Add up the per-member totals for all five members, and print that sum
#    beside total_sessions(signups). The two should agree.
# 7. Write a verdict beside each of the five results in a comment: right, or
#    just a number that did not crash? Argue each one with your partner
#    first.
#
# Every line runs clean. Two of them deserve a different answer than they
# get.

# No new functions. Call the ones you already have, on inputs nobody
# asked for, and write a verdict beside each printed result.

# TODO: an empty list
print("empty list:", total_for([], "Nia"))
# Right: There are no records to count.

# TODO: a list holding exactly one record
print("one record:", total_for([signups[0]], "Nia"))
# Right: Nia booked 4 sessions in the first record.

# TODO: a member name that is not in the file at all
print("missing member:", total_for(signups, "Marco"))
# Misleading: Marco does not exist in the dataset.
# A missing member is different from a member with zero sessions.

# TODO: a name that differs from a real member's only by capitalization
print("lowercase name:", total_for(signups, "nia"))
# Misleading: Nia exists, but Python is case sensitive.

print("empty filtered list:", signups_for([], "Nia"))
# Right: An empty list has no matching records.

# TODO: then: do the per-member totals add up to the whole-file total?
member_sum = 0

for member in members:
    member_sum += total_for(signups, member)

print("member totals:", member_sum, "whole file:", total_sessions(signups))

# ----- Share Out: Day 3 -----
# Last 15 minutes, back together as a class. Bring:
#
# - Your verdict on one edge case. Pick the strangest result. Say whether
#   the answer is right or just quiet, and what you would change if this
#   were the center's real data. If you and your partner disagreed, bring
#   both positions.
# - Your cross-check. Did the five per-member totals add up to the
#   whole-file total? Say how you would run that check on a 430-row file you
#   cannot eyeball.
# - Three functions or one? Say which you wrote and what it cost or saved
#   you.
# - One question you could not settle, or one thing you would do differently
#   starting over. Half-finished thinking is what this slot is for.
#
# Be ready to answer "why did you do it that way?"

# Your notes for the share out:
# The lowercase name returns zero even though Nia has sessions.
# I would make the name comparison case insensitive.
# I would also separate missing members from members with zero sessions.
# The member totals add up to 45, matching the whole file.
# For a larger file I would collect all unique member names
# and compare their combined totals to the whole file total.
# Three functions allow me to reuse different parts of the code
# without rewriting the same logic.
# Next time I would consider how to handle invalid or missing
# session values. 