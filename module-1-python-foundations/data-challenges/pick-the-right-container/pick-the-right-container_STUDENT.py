
#!/usr/bin/env python3
"""Pick the Right Container: see DataChallengeOverview&Steps.md."""

import json
DATA_FILE = "../data/station_taps.csv"  # edit the filepath with the data

with open(DATA_FILE) as f:
    rows = [line.split(",") for line in f.read().splitlines() if line]

header = rows[0]
taps = rows[1:]


# ===== Day 1 =====

# Step 1: Write `scan_for()` and Count Its Comparisons for Three Tap IDs
def scan_for(tap_id, records):
    # TODO: assign `comparisons` to 0
    # TODO: loop over `records`; add 1 to `comparisons` for every row
    # TODO: inside the loop, return `comparisons` when row[0] == tap_id
    # TODO: after the loop, return `comparisons`
    comparisons = 0
    for row in records:
        comparisons += 1
        if row[0] == tap_id:
            return comparisons
    return comparisons


print("columns:", header)
print("rows in the log:", len(taps))
print("comparisons to find T001:", scan_for("T001", taps))
print("comparisons to find T040:", scan_for("T040", taps))
print("comparisons to find T999:", scan_for("T999", taps))

# Step 1, answer 1:
# T001: 1 comparison because it is the first row.
# T040: 40 comparisons because it is the last row.
# T999: 40 comparisons because it is not in the file.
# Step 1, answer 2:
# I would plan around 40 comparisons because a Linear Scan
# may have to check every row before finding a match or
# determining that the ID does not exist.


# Step 2: Print Scan Cost at 5 to 40 Rows, Then Count a Nested Pair Loop
for size in [5, 10, 20, 40]:
    worst = scan_for("T999", taps[:size])
    # TODO: print "rows:", `size`, "| worst-case comparisons:", `worst`
    print("rows:", size, "| worst-case comparisons:", worst)
# TODO: assign `pairs` to 0; loop over `taps` with a loop over `taps` inside
pairs = 0
for first in taps:
    for second in taps:
        # TODO: add 1 to `pairs` in the inner loop
        pairs += 1
# TODO: print len(taps) and `pairs`
print("rows:", len(taps), "| pairs:", pairs)
# TODO: assign `big` to len(taps) * 10
big = len(taps) * 10
# TODO: print the scan's worst case and the pair loop's count on `big` rows
print("scan on", big, "rows:", big)
print("pair loop on", big, "rows:", big * big)

# Step 2, answer 1:
# 5 rows: 5 x 1 = 5 comparisons.
# 10 rows: 10 x 1 = 10 comparisons.
# 20 rows: 20 x 1 = 20 comparisons.
# 40 rows: 40 x 1 = 40 comparisons.
# Pair loop on 40 rows: 40 x 40 = 1600 pairs.
# Scan on 400 rows: 400 x 1 = 400 comparisons.
# Pair loop on 400 rows: 400 x 400 = 160000 pairs.
# Step 2, answer 2:
# The scan grows at the same rate as the number of rows.
# The pair loop grows by multiplying the number of rows
# by itself because every row is paired with every row.


# ===== Day 2 =====

# Step 3: Count Taps Per Card With Two Parallel Lists, and Their Comparisons
# TODO: assign `card_ids` to an empty list (each card, first-seen order)
card_ids = []
# TODO: assign `tap_counts` to an empty list (the count for card_ids[i])
tap_counts = []
# TODO: assign `comparisons` to 0
comparisons = 0
# TODO: loop over `taps`; assign `card` to row[1] and `found` to False
for row in taps:
    card = row[1]
    found = False
    # TODO: inside it, loop over range(len(card_ids)); add 1 to `comparisons`
    for i in range(len(card_ids)):
        comparisons += 1
        # TODO: if card_ids[i] == card, add 1 to tap_counts[i], set found, break
        if card_ids[i] == card:
            tap_counts[i] += 1
            found = True
            break
    # TODO: after the inner loop, if not found, append `card` and 1 to the lists
    if not found:
        card_ids.append(card)
        tap_counts.append(1)

busiest = tap_counts.index(max(tap_counts))
print("distinct cards:", len(card_ids))
print("comparisons the two parallel lists needed:", comparisons)
print("busiest card:", card_ids[busiest], "with", max(tap_counts), "taps")

# Step 3, answer 1:
# Expected comparisons: 190.
# Each new card requires checking the cards already in the list.
# Each repeat card requires checking up to its position in the list.
# Step 3, answer 2:
# The calculated count is 190 comparisons across 40 rows.
# This is bigger than the number of rows because the inner
# loop can check multiple card IDs for each tap.


# Step 4: Count Taps Per Card With a Dictionary, and Stations With a Set
# TODO: assign `taps_by_card` to an empty dict (card ID: tap count)
taps_by_card = {}
# TODO: assign `lookups` to 0
lookups = 0
# TODO: loop over `taps`; add 1 to `lookups`
for row in taps:
    lookups += 1
    card = row[1]
    # TODO: add 1 to row[1]'s count in `taps_by_card`, or set it to 1 if new
    if card in taps_by_card:
        taps_by_card[card] += 1
    else:
        taps_by_card[card] = 1
# TODO: assign `stations` to set(); loop over `taps` and .add() row[2]
stations = set()
for row in taps:
    stations.add(row[2])
# TODO: assign `repeat_riders` to 0
repeat_riders = 0
# TODO: loop over `taps_by_card`; add 1 to `repeat_riders` if a count is > 1
for card in taps_by_card:
    if taps_by_card[card] > 1:
        repeat_riders += 1

print("distinct cards:", len(taps_by_card))
print("lookups the dictionary needed:", lookups)
print("unique stations:", len(stations), sorted(stations))
print("cards that tapped more than once:", repeat_riders)
print("taps for C001:", taps_by_card["C001"])

# Step 4, answer 1:
# Expected lookups: 40 because the counter increases
# once for every row in the dataset.
# Step 4, answer 2:
# As the Input Size grows, the parallel lists can require
# more comparisons per row as more distinct cards are added.
# As the Input Size grows, the Dictionary version counts
# one lookup per row.
# The parallel lists needed 190 comparisons compared to
# 40 counted lookups for the Dictionary.
# In terms of Big-O, the parallel lists can reach O(n^2)
# in the worst case, while the Dictionary averages O(n).
# Step 4, answer 3:
# The parallel lists store card IDs and their counts at
# matching positions. They use a Linear Scan to find a card.
# The Dictionary maps each card ID to its tap count and
# uses the key for a Lookup instead of scanning a list.
# The Set is a Data Structure that stores unique stations
# and automatically prevents duplicates.
# A list would require checking existing stations before
# adding a new station, causing additional comparisons.
# Step 4, answer 4:
# C012 explains the difference because it only tapped once.
# There are 12 distinct cards but only 11 repeat riders.


# ===== Day 3 =====

# Step 5: Save the Summary as JSON and Read the TypeError a Set Causes
# TODO: replace each None with your Day 2 value; keep `stations` a set
summary = {
    "service_day": "2026-03-02",
    "total_taps": len(taps),
    "distinct_cards": len(taps_by_card),
    "stations": stations,
    "taps_by_card": taps_by_card,
}

print("about to serialize", len(summary), "keys")
# TODO: run the file and answer below before you change anything
# TODO: then put # in front of the next two lines so Step 6 can run
# text = json.dumps(summary, indent=2)
# print(text)

# Step 5, answer 1:
# Expected error: TypeError: Object of type set is not JSON serializable
# Step 5, answer 2:
# The stations key causes the error because its value is a Set.
# JSON does not directly support sets, so the value needs
# to be converted into a list before Serialization.
# Step 5, answer 3:
# The about to serialize message should print before the error.
# This means the summary was created successfully, but
# the error happens when Python tries to convert it to JSON.


# Step 6: Write `tap_summary.json`, Reload It, and Check Which Types Survived
# TODO: assign summary["stations"] to a type JSON can hold; keep the key
summary["stations"] = sorted(stations)
# TODO: json.dump() `summary` into a with open("tap_summary.json", "w")
with open("tap_summary.json", "w") as f:
    json.dump(summary, f, indent=2)
# TODO: replace None with json.load() of "tap_summary.json"
with open("tap_summary.json") as f:
    reloaded = json.load(f)

print("total_taps came back as:", reloaded["total_taps"])
print("taps_by_card came back as a", type(reloaded["taps_by_card"]).__name__)
print("C001 straight out of the file:", reloaded["taps_by_card"]["C001"])
print("stations came back as a", type(reloaded["stations"]).__name__)
print("round trip identical:", reloaded["taps_by_card"] == taps_by_card)

# Step 6, answer 1:
# Yes, the overnight job can access a card's count directly
# from the taps_by_card Dictionary without the original CSV.
# C001 should return 6 taps directly from the JSON file.
# Step 6, answer 2:
# The Dictionary survives the round trip as a Dictionary.
# The Set comes back as a list because it was converted
# before Serialization. The list does not automatically
# prevent duplicate station names.

# AI Output Validation
#
# AI explained that a dictionary is more efficient for
# counting taps by card than scanning parallel lists.
# The terminal output confirms 190 comparisons for the
# lists and 40 counted lookups for the dictionary.
#
# AI explained that a linear scan stops when it finds
# a match. The output confirms 1 comparison for T001
# and 40 comparisons for T040 and T999.
#
# AI explained that JSON does not support sets directly.
# The final output confirms that converting the set
# into a list allows the summary to be saved and reloaded.
#
# AI explained that sets prevent duplicate values.
# The terminal output confirms 6 unique stations
# across 40 taps.