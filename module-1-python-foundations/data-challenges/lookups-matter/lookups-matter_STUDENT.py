#!/usr/bin/env python3
"""Lookups Matter: see DataChallengeOverview&Steps.md for the steps."""

import csv

DATA_FILE = "../data/member_directory.csv"  # edit the filepath with the data
CHECKINS_FILE = "../data/door_checkins.txt"  # edit the filepath with the data

with open(DATA_FILE, newline="") as f:
    members = list(csv.DictReader(f))


# Step 1: Write `find_linear()` to Return the Member and Its Comparisons
def find_linear(members, member_id):
    # TODO: assign `comparisons` to 0
    comparisons = 0
    # TODO: loop over `members`; add 1 to `comparisons` for every row
    for row in members:
        comparisons += 1
        # TODO: inside the loop, return row, comparisons on a member_id match
        if row["member_id"] == member_id:
            return row, comparisons
    # TODO: after the loop, return None, comparisons
    return None, comparisons


row, count = find_linear(members, "M1150")
print("members in the directory:", len(members))
print("found:", row["name"], "at", row["home_branch"])
print("comparisons:", count)

# Step 1, answer 1:
# The calculated prediction is 150 comparisons because the IDs
# start at M1001 and are listed in order. Subtracting 1000
# from 1150 gives 150. The terminal output confirmed this count.


# Step 2: Total the Comparisons for All 20 Swipes in `door_checkins.txt`
# TODO: open CHECKINS_FILE in a with block as `f`
with open(CHECKINS_FILE) as f:
    # TODO: inside it, assign `swipes` to f.read().splitlines()
    swipes = f.read().splitlines()

# TODO: assign `linear_total` and `not_members` to 0
linear_total = 0
not_members = 0

# TODO: loop over `swipes`; call find_linear(members, member_id)
for member_id in swipes:
    row, count = find_linear(members, member_id)

    # TODO: print the ID, the name or "NOT A MEMBER", and the comparisons
    if row is not None:
        print(member_id, "|", row["name"], "| comparisons:", count)
    else:
        print(member_id, "| NOT A MEMBER | comparisons:", count)

    # TODO: add each count to `linear_total`
    linear_total += count

    # TODO: add 1 to `not_members` for every swipe with no row
    if row is None:
        not_members += 1

print("swipes:", len(swipes), "| not members:", not_members)
print("linear total comparisons:", linear_total)

# Step 2, answer 1:
# The calculated predictions for the first three swipes are:
# M1004: 4 comparisons because 1004 - 1000 = 4.
# M1012: 12 comparisons because 1012 - 1000 = 12.
# M1027: 27 comparisons because 1027 - 1000 = 27.
# Their combined cost is 4 + 12 + 27 = 43 comparisons.
# A non-member costs 312 comparisons because the function
# must search the entire directory without finding a match.
# The terminal output confirmed these counts.

# Step 2, answer 2:
# M1313 and M2041 tied for the highest cost at 312 comparisons
# each because neither ID exists in the member directory.
# Linear search had to check every member before returning None.


# Step 3: Build `members_by_id` and Find the Swipe Where It Pays Off
# TODO: assign `members_by_id` to an empty dict and `build_steps` to 0
members_by_id = {}
build_steps = 0

# TODO: loop over `members`; store each row under row["member_id"]
for row in members:
    members_by_id[row["member_id"]] = row
    # TODO: add 1 to `build_steps` for every row
    build_steps += 1

# TODO: write find_dict(members_by_id, member_id)
def find_dict(members_by_id, member_id):
    # TODO: make find_dict() return members_by_id.get(member_id), 1
    return members_by_id.get(member_id), 1


print("build cost:", build_steps, "| keys in the dict:", len(members_by_id))

# TODO: assign `linear_running` to 0 and `dict_running` to build_steps
linear_running = 0
dict_running = build_steps

# TODO: assign `pays_off_at` to None and `swipe_number` to 0
pays_off_at = None
swipe_number = 0

for member_id in swipes:
    # TODO: add 1 to `swipe_number`
    swipe_number += 1
    _, linear_count = find_linear(members, member_id)
    _, dict_count = find_dict(members_by_id, member_id)

    # TODO: add each search's count to its running total
    linear_running += linear_count
    dict_running += dict_count

    # TODO: print swipe_number, the ID and both running totals
    print("swipe", swipe_number, member_id,
          "| linear so far:", linear_running,
          "| dict so far:", dict_running)

    # TODO: the first time dict_running < linear_running, set `pays_off_at`
    if pays_off_at is None and dict_running < linear_running:
        pays_off_at = swipe_number

print("dict pays off at swipe:", pays_off_at)
print("morning totals | linear:", linear_running, "| dict:", dict_running)

# Step 3, answer 1:
# The calculated prediction is that the dictionary pays off
# at swipe 6 because its initial build cost is 312 steps.
# After five swipes, linear search costs 262 comparisons
# while the dictionary costs 312 + 5 = 317 steps.
# The sixth swipe is a non-member, adding 312 comparisons
# to linear search but only one lookup to the dictionary.
# Linear search then costs 574 and the dictionary costs 318.
# The terminal output confirmed that swipe 6 is the pay-off.

# Step 3, answer 2:
# A dictionary keyed on member_id is a better fit because
# the door needs to find specific members repeatedly.
# Dictionary lookup retrieves a record by its key instead
# of searching through every member individually.
# The dictionary pulled ahead at:
# swipe 6 M1313 | linear so far: 574 | dict so far: 318

# Step 3, answer 3:
# A plain list would be a better choice on a quiet morning
# with only a few swipes from members near the beginning
# of the directory. Building the dictionary might require
# more work than performing those few linear searches.


# Step 4: Test an AI Speed Claim Against Your Totals and Write a Verdict
# TODO: replace the text below with your AI's claim, word for word
ai_claim = "For 20 lookups in a list of 312 members, linear search can require up to 6240 comparisons, while dictionary lookup requires 20 counted lookup steps in the average-case model. That is up to 312 times fewer lookup steps, excluding the dictionary build cost."
print("AI CLAIM:", ai_claim)

# TODO: unpack find_linear() for swipes[0] into `_, front_count`
_, front_count = find_linear(members, swipes[0])

# TODO: unpack find_linear() for "M1313" into `_, absent_count`
_, absent_count = find_linear(members, "M1313")

# TODO: assign `ratio` to round(linear_running / dict_running, 1)
ratio = round(linear_running / dict_running, 1)

print("one front-of-file swipe | linear:", front_count, "| dict: 1")
print("one non-member swipe | linear:", absent_count, "| dict: 1")
print("whole morning | linear:", linear_running, "| dict:", dict_running,
      "| ratio:", ratio)

# TODO: replace the text below with your own verdict
verdict = "Linear search is O(n), while dictionary lookup is O(1) Average-Case. Linear search required 2924 comparisons during the morning, while the dictionary required 332 steps including its build cost. The actual operation-count ratio was 8.8, so the AI's upper-bound estimate did not represent the entire morning."
print("VERDICT:", verdict)

# Step 4, answer 1:
# The original AI claim described an upper-bound ratio of 312.
#
# Comparison 1: The first swipe required 4 linear comparisons
# and 1 dictionary lookup, giving a ratio of 4.
#
# Comparison 2: The non-member swipe required 312 linear
# comparisons and 1 dictionary lookup, giving a ratio of 312.
#
# Comparison 3: The whole morning required 2924 linear
# comparisons and 332 dictionary steps, giving a ratio of 8.8.
#
# The AI's upper-bound ratio matched the non-member swipe
# but did not match the first swipe or the whole morning.

# Step 4, answer 2:
# The original AI claim excluded the dictionary build cost.
# The terminal results were provided back to the AI.
# After including the 312 build steps and 20 dictionary
# lookups, the AI confirmed a total cost of 332 steps.
# Dividing 2924 by 332 gives approximately 8.8.
# The AI clarified that this measures counted operations,
# not actual execution time.
#
# AI Output Validation:
# Source: Python documentation, Time complexity of operations
# on built-in types, under the dict section.
# https://docs.python.org/3.14/builtins/time-complexity.html
#
# The documentation confirms that dictionary lookup is
# O(1) on average and can be O(n) in the worst case.
# The terminal output supports the assignment's average-case
# operation-count model.
#
# The main takeaway is that AI estimates should be checked
# against actual data and should include relevant costs
# before being used to draw a conclusion.