#!/usr/bin/env python3
"""Validate, Catch, Keep Going: see DataChallengeOverview&Steps.md."""

DATA_FILE = "../data/service_requests.csv"  # edit the filepath with the data

with open(DATA_FILE) as f:
    lines = f.read().splitlines()

header = lines[0]
rows = [line for line in lines[1:] if line]


# ===== Day 1 =====

# Step 1: Write `validate_request()` to Return a Verdict and a Reason
# TODO: assign `EXPECTED_FIELDS` to 5
EXPECTED_FIELDS = 5
# TODO: assign `ALLOWED_STATUS` to ["Open", "In Progress", "Closed"]
ALLOWED_STATUS = ["Open", "In Progress", "Closed"]


def validate_request(row):
    # TODO: assign `fields` to `row` split on commas
    fields = row.split(",")
    if len(fields) != EXPECTED_FIELDS:
        return False, "wrong field count: " + str(len(fields))
    # TODO: unpack `fields` into the five names in the CSV header
    request_id, complaint_type, borough, days_open, status = fields
    # TODO: if `borough` is empty, return False and "borough is empty"
    if borough == "":
        return False, "borough is empty"
    # TODO: if `status` is not in ALLOWED_STATUS, return False and a reason
    # TODO: make that reason "status not allowed: " plus `status`
    if status not in ALLOWED_STATUS:
        return False, "status not allowed: " + status
    # TODO: return True and "ok"
    return True, "ok"


print(validate_request("SR-1001,Noise - Residential,Brooklyn,3,Closed"))
print(validate_request("SR-1004,Rodent,,6,Closed"))
print(validate_request("SR-1009,Water System,Queens,4,Escalated"))

# Step 1, answer 1:
# Each row represents one service request with an ID,
# complaint type, borough, days open and status.
# Days open should contain numbers and the other fields
# contain text. Some rows have missing fields, invalid
# statuses and invalid numbers.
# Step 1, answer 2:
# The caller uses ok, reason = validate_request(row).
# The function returns a tuple containing a Boolean
# and a string explaining the result.


# Step 2: Run All 15 Rows Through the Validator and Report Each Rejection
# TODO: assign `valid` to 0
valid = 0
# TODO: loop over `rows`; unpack validate_request(row) into ok, reason
for row in rows:
    ok, reason = validate_request(row)
    # TODO: if `ok`, add 1 to `valid`
    if ok:
        valid += 1
    # TODO: else print row.split(",")[0], "REJECTED -" and `reason`
    else:
        print(row.split(",")[0], "REJECTED -", reason)

print("header:", header)
print("rows read:", len(rows))
print("passed Day 1 validation:", valid)

# Step 2, answer 1:
# Three rows fail the validation rules.
# SR-1004 has an empty borough.
# SR-1009 has a status that is not allowed.
# SR-1011 has four fields instead of five.
# 15 - 3 = 12 rows should pass.
# Step 2, answer 2:
# SR-1007 and SR-1013 passed when they should not have.
# SR-1007 contains "3 days" and SR-1013 contains -3.
# The validator does not check whether days_open is
# a valid number or whether it is negative.


# ===== Day 2 =====

# Step 3: Build the Days-Open Report With No Protection and Watch It Crash
# TODO: assign `total_days` and `counted` to 0
# total_days = 0
# counted = 0
# TODO: loop over `rows`; `continue` past any row validate_request() rejects
# for row in rows:
#     ok, reason = validate_request(row)
#     if not ok:
#         continue
# TODO: assign `days_open` to int() of the row's fourth field
#     days_open = int(row.split(",")[3])
# TODO: add `days_open` to `total_days` and 1 to `counted`
#     total_days += days_open
#     counted += 1
# TODO: print the row's ID, "days open:" and `days_open`
#     print(row.split(",")[0], "days open:", days_open)
# TODO: after your answers, comment out this step so Step 4 can run

# print("average days open:", total_days / counted)

# Step 3, answer 1:
# I expect 5 report lines before the crash.
# SR-1007 stops the loop because its days_open
# value is "3 days".

# Step 3, answer 2:
# ValueError: invalid literal for int() with base 10: '3 days'
# Five rows were counted before the exception.

# Step 3, answer 3:
# The remaining rows are not processed because
# the exception stops the program before it
# can finish calculating the average.


# Step 4: Rebuild the Report So Every Row Is Counted or Skipped
def check_days_open(value):
    # TODO: in a try, assign `days` to int(value)
    try:
        days = int(value)
    # TODO: in except ValueError, return False and a reason
    # TODO: make that reason "days_open is not a number: " plus `value`
    except ValueError:
        return False, "days_open is not a number: " + value
    # TODO: if `days` is below 0, return False and a reason
    # TODO: make that reason "days_open is negative: " plus `value`
    if days < 0:
        return False, "days_open is negative: " + value
    # TODO: return True and "ok"
    return True, "ok"


# TODO: assign `total_days`, `counted` and `skipped` to 0
total_days = 0
counted = 0
skipped = 0
# TODO: loop over `rows`; unpack validate_request(row) into ok, reason
for row in rows:
    ok, reason = validate_request(row)
    # TODO: if ok, unpack check_days_open() of the fourth field into ok, reason
    if ok:
        ok, reason = check_days_open(row.split(",")[3])
    # TODO: if still ok, add the days to `total_days` and 1 to `counted`
    if ok:
        total_days += int(row.split(",")[3])
        counted += 1
    # TODO: else add 1 to `skipped`; print the ID, "SKIPPED -" and `reason`
    else:
        skipped += 1
        print(row.split(",")[0], "SKIPPED -", reason)

print("counted:", counted, "| skipped:", skipped)
print("average days open:", round(total_days / counted, 1))

# Step 4, answer 1:
# Five rows should be skipped.
# SR-1007 and SR-1013 are the two additional rows
# that passed the Day 1 validator.
# Step 4, answer 2:
# The try and except catch "3 days" because int()
# raises a ValueError. An if could check the string
# before conversion, but try handles the conversion error.
# The if catches -3 because it is a valid integer
# but an invalid number of days.
# An except would not catch -3 because int() works.
# Step 4, answer 3:
# 10 counted + 5 skipped = 15 total rows.
# Every row is accounted for.
# The total is 82 days and the average is 8.2 days.

# AI Output Validation
#
# AI explained that validation checks whether a row
# meets the expected requirements. The terminal output
# confirms that 12 out of 15 rows passed Day 1.
#
# AI explained that int() cannot convert "3 days".
# A separate test reproduced the ValueError.
#
# AI explained that -3 can be converted into an integer
# but is invalid for days_open. The final report confirms
# that an if statement rejects this value.
#
# AI explained that try and except prevent a conversion
# error from stopping the entire report.
#
# The final terminal output confirms 10 counted rows,
# 5 skipped rows and an average of 8.2 days.
# 10 + 5 = 15, so every row is accounted for.