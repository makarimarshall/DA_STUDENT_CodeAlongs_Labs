#!/usr/bin/env python3
"""One Job at a Time: see DataChallengeOverview&Steps.md for the steps."""

import json

DATA_FILE = "../data/pantry_donations.csv"  # edit the filepath with the data


# ===== Day 1 =====

# Step 1: Write the Read-and-Validate Pair, Each With a Docstring
def read_donations(path):
    """Read the donation log into one raw string per record."""
    records = []
    with open(path) as f:
        for line in f.read().splitlines()[1:]:
            if line.strip():
                records.append(line)
    return records


def validate_donation(record):
    # TODO: add a one-sentence docstring naming its one job
    """Validate a single donation record."""
    # TODO: assign `parts` to `record` split on commas
    parts = record.split(",")
    # TODO: return False, "wrong field count" if `parts` lacks 5 fields
    if len(parts) != 5:
        return False, "wrong field count"
    # TODO: return False, "missing category" if parts[2].strip() is ""
    if parts[2].strip() == "":
        return False, "missing category"
    # TODO: in a try, call float(parts[3])
    try:
        float(parts[3])
    # TODO: in except ValueError, return False, "pounds is not a number"
    except ValueError:
        return False, "pounds is not a number"
    # TODO: return True and ""
    return True, ""


# TODO: assign `records` to read_donations(DATA_FILE), `valid` to []
records = read_donations(DATA_FILE)
valid = []
# TODO: loop over `records`; unpack validate_donation(record) as ok, reason
for record in records:
    ok, reason = validate_donation(record)
    # TODO: if `ok`, append `record` to `valid`
    if ok:
        valid.append(record)
    # TODO: else print "rejected", the record's ID plus ":", and `reason`
    else:
        print("rejected", record.split(",")[0] + ":", reason)

print(len(valid), "usable records out of", len(records))

# Step 1, answer 1:
# Each record holds a donation ID, item, category,
# pounds and the date it was received.
# Pounds holds numbers and the other fields hold text.
# D009 is missing a category.
# D013 has "twenty" instead of a number.
# D017 is missing the pounds field.

# Step 1, answer 2:
# The validator makes sure each record has five fields,
# a category that is not empty and a pounds value
# that can be converted into a number.


# Step 2: Write `summarize_donations()` for the Category Breakdown Only
def summarize_donations(valid_records):
    # TODO: add a one-sentence docstring naming its one job
    """Summarize usable donations by category."""
    # TODO: assign `by_category` to {} and `total_pounds` to 0.0
    by_category = {}
    total_pounds = 0.0
    # TODO: loop over `valid_records`; split each record on commas into `parts`
    for record in valid_records:
        parts = record.split(",")
        # TODO: assign `category` to parts[2], `pounds` to float(parts[3])
        category = parts[2]
        pounds = float(parts[3])
        # TODO: if `category` is not in `by_category`, add an entry for it
        # TODO: start that entry as {"donations": 0, "pounds": 0.0}
        if category not in by_category:
            by_category[category] = {"donations": 0, "pounds": 0.0}
        # TODO: add 1 to its "donations" and `pounds` to its "pounds"
        by_category[category]["donations"] += 1
        by_category[category]["pounds"] += pounds
        # TODO: add `pounds` to `total_pounds`
        total_pounds += pounds
    # TODO: return a dict of "records", "total_pounds" and "by_category"
    return {
        "records": len(valid_records),
        "total_pounds": total_pounds,
        "by_category": by_category
    }


# TODO: assign `summary` to summarize_donations(valid)
summary = summarize_donations(valid)
print("records:", summary["records"], "| total pounds:",
      summary["total_pounds"])
for category, stats in summary["by_category"].items():
    print(category, stats["donations"], "donations,", stats["pounds"],
          "lbs")

# Step 2, answer 1:
# The grains category has 25 + 30 + 10 + 15 = 80 pounds.
# D013 is not included because its pounds value is invalid.
# The expected printed total is 4 donations and 80.0 lbs.


# ===== Day 2 =====

# Step 3: Add `export_summary()` and `run_pipeline()`, Then Print Docstrings
def export_summary(summary, path):
    # TODO: add a one-sentence docstring naming its one job
    """Write a donation summary to a JSON file."""
    # TODO: in a with open(path, "w") block, json.dump `summary`, indent=2
    with open(path, "w") as f:
        json.dump(summary, f, indent=2)
    # TODO: return `path`
    return path


def run_pipeline(in_path, out_path, summarize):
    # TODO: add a one-sentence docstring naming its one job
    """Coordinate the donation reporting pipeline."""
    # TODO: assign `kept` to [] and loop over read_donations(in_path)
    kept = []
    for record in read_donations(in_path):
        # TODO: append each record that validate_donation() passes to `kept`
        ok, reason = validate_donation(record)
        if ok:
            kept.append(record)
    # TODO: return export_summary() of summarize(kept) and `out_path`
    return export_summary(summarize(kept), out_path)


written = run_pipeline(DATA_FILE, "donation_summary.json",
                       summarize_donations)
print("wrote", written)
for func in [read_donations, validate_donation, summarize_donations,
             export_summary]:
    print(func.__name__ + ":", func.__doc__.splitlines()[0])

# Step 3, answer 1:
# print(len) displays <built-in function len>.
# print(len("abc")) displays 3.
# Parentheses call the function.
# Without parentheses, len refers to the function itself.

# Step 3, answer 2:
# None of the four docstrings need "and" twice.
# Each function has one specific responsibility.
# One reads, one validates, one summarizes and one exports.


# Step 4: Swap In `summarize_by_day()` and Count the Functions You Edited
def summarize_by_day(valid_records):
    # TODO: add a one-sentence docstring naming its one job
    """Summarize usable donations by date."""
    # TODO: return the same dict shape, with "by_day" keyed by parts[4]
    by_day = {}
    total_pounds = 0.0

    for record in valid_records:
        parts = record.split(",")
        day = parts[4]
        pounds = float(parts[3])

        if day not in by_day:
            by_day[day] = {"donations": 0, "pounds": 0.0}

        by_day[day]["donations"] += 1
        by_day[day]["pounds"] += pounds
        total_pounds += pounds

    return {
        "records": len(valid_records),
        "total_pounds": total_pounds,
        "by_day": by_day
    }


# TODO: call run_pipeline(DATA_FILE, "donation_summary.json", summarize_by_day)
run_pipeline(DATA_FILE, "donation_summary.json", summarize_by_day)
# TODO: replace None with json.load() of "donation_summary.json"
with open("donation_summary.json") as f:
    reloaded = json.load(f)

print("records:", reloaded["records"], "| total pounds:",
      reloaded["total_pounds"])
for day, stats in sorted(reloaded["by_day"].items()):
    print(day, stats["donations"], "donations,", stats["pounds"], "lbs")

# Step 4, answer 1:
# Zero other functions need to be edited for the swap.
# The pipeline uses the summarize parameter instead of
# depending on one specific summarizer.

# Step 4, answer 2:
# September 5, September 7 and September 9 each have
# one usable donation because D009, D013 and D017
# were rejected during validation.
# The coordinator should see that these totals only
# include usable donations and that three records
# need to be corrected.


# AI Output Validation
#
# AI explained that each function should have one
# specific responsibility. Each docstring describes
# the job of its function in one sentence.
#
# AI explained that passing a function without
# parentheses allows another function to call it later.
# print(len) should display the function itself.
# print(len("abc")) should display 3.
#
# AI calculated 80 pounds for the grains category.
# The CSV confirms 25 + 30 + 10 + 15 = 80 pounds.
#
# AI predicted that changing the summarizer would not
# require changes to the other functions.
# The pipeline accepts either summarizer through
# the summarize parameter.
#
# The expected results are 17 usable records,
# 3 rejected records and 300.0 total pounds.