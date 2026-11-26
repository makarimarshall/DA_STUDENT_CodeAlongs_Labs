
#!/usr/bin/env python3
"""Looks Right. Is It?: see DataChallengeOverview&Steps.md for the steps."""

DATA_FILE = "../data/timesheet_hours.csv"  # edit the filepath with the data

with open(DATA_FILE) as f:
    lines = f.read().splitlines()


# ===== Day 1 =====

# Step 1: Follow the TypeError in `weekly_hours()` Back to Its Cause
# TODO: run the file as given and read the traceback from the bottom up
# TODO: add print(repr(hours)) as the first line of add_hours(); run again
# TODO: find that printed value in the CSV
# TODO: fix the line that reads the wrong column to read the hours column
# TODO: wrap that value in int() so add_hours() adds a number
# TODO: delete the print(repr(hours)) line once Rosa's total is right
def add_hours(total, hours):
    return total + hours


def weekly_hours(lines, emp_id):
    total = 0
    for row in lines[1:]:
        parts = row.split(",")
        if parts[0] == emp_id:
            total = add_hours(total, int(parts[3]))
    return total


print("Rosa Alvarez, weekly hours:", weekly_hours(lines, "E101"))

# Step 1, answer 1:
# Rosa's expected weekly hours:
# Monday: 8
# Tuesday: 8
# Wednesday: 8
# Thursday: 8
# Friday: 8
# 8 + 8 + 8 + 8 + 8 = 40 hours.
# The corrected program was tested with AI assistance
# and returned 40 hours, matching the calculation.

# Step 1, answer 2:
# - The last line of a traceback identifies the error type
#   and explains what went wrong.
# - Each block above it shows the function, file and line
#   involved in the chain of function calls.
# - Reading from the bottom up helps trace the bad value
#   back to where it originated.
# Source: AI explanation checked against the actual
# traceback produced by the original starter file.

# Step 1, answer 3:
# The traceback ended in add_hours() on original line 20:
# return total + hours
# The actual bug was in weekly_hours() on original line 28:
# total = add_hours(total, parts[2])
# The diagnostic print(repr(hours)) displayed 'Mon'.
# Index 2 contains the day, not the hours.
# Changing parts[2] to int(parts[3]) reads the correct
# column and converts the string into an integer.


# Step 2: Trace the ZeroDivisionError Back to the Hand-Typed Staff List
# TODO: run the file as given; note the last ID that printed
# TODO: compare every ID in `staff` with the IDs in the CSV
# TODO: replace the hand-typed `staff` list with an empty list
# TODO: loop over lines[1:]; append each row's employee ID to `staff` once
# TODO: print "employees in the file:" and len(staff)
def days_worked(lines, emp_id):
    days = 0
    for row in lines[1:]:
        if row.split(",")[0] == emp_id:
            days = days + 1
    return days


staff = []
for row in lines[1:]:
    emp_id = row.split(",")[0]
    if emp_id not in staff:
        staff.append(emp_id)

print("employees in the file:", len(staff))

for emp_id in staff:
    hours = weekly_hours(lines, emp_id)
    days = days_worked(lines, emp_id)
    print(emp_id, "| hours:", hours, "| days:", days,
          "| average per day:", hours / days)

# Step 2, answer 1:
# The expected employee count is 5.
# The unique IDs in the CSV are:
# E101, E102, E103, E104 and E105.
# Each employee has five daily records.
# The corrected program confirmed five employees.

# Step 2, answer 2:
# Three employee report lines printed before the crash.
# Including Rosa's Step 1 output, four lines printed.
# E103 was the last employee successfully printed.
# The program stopped on E106 with ZeroDivisionError
# because E106 does not exist in the CSV.

# Step 2, answer 3:
# The traceback points to hours / days on original line 61,
# but the actual bug is the staff list on original line 56
# because E106 was incorrectly included instead of E104.
# Building staff directly from the CSV fixes the cause
# instead of skipping an employee to avoid the error.


# ===== Day 2 =====

# Step 3: Find Why Four of the Five Weekly Hour Totals Are Wrong
# TODO: add up Rosa's (E101) and Mei's (E103) hours by hand first
# TODO: print("starting", emp, "total is", total) first in the outer loop
# TODO: move the line that sets `total` inside the outer loop
# TODO: delete the "starting" print once all five totals are right
records = []
for row in lines[1:]:
    emp_id, name, day, hours, rate = row.split(",")
    records.append({"id": emp_id, "name": name, "day": day,
                    "hours": int(hours), "rate": float(rate)})

employee_ids = []
for r in records:
    if r["id"] not in employee_ids:
        employee_ids.append(r["id"])

for emp in employee_ids:
    total = 0
    name = ""
    for r in records:
        if r["id"] == emp:
            name = r["name"]
            total = total + r["hours"]
    print(emp, name, "| weekly hours:", total)

# Step 3, answer 1:
# Expected weekly hours calculated from the CSV:
# Rosa: 8 + 8 + 8 + 8 + 8 = 40 hours.
# Mei: 6 + 7 + 8 + 6 + 5 = 32 hours.
#
# Expected totals for the remaining employees:
# Darnell: 10 + 9 + 10 + 9 + 8 = 46 hours.
# Samuel: 7 + 8 + 8 + 8 + 7 = 38 hours.
# Priya: 9 + 9 + 9 + 8 + 9 = 44 hours.
# The corrected program matched all five totals.

# Step 3, answer 2:
# The original loop carried the previous employee's total
# into the next employee's calculation.
# Starting values calculated from the original loop:
# E101: 0
# E102: 40
# E103: 86
# E104: 118
# E105: 156
# Original line 89 placed total = 0 outside the outer loop.
# Moving it inside the loop resets total for each employee.

# Step 3, answer 3:
# Rosa's number was correct because total started at 0
# for the first employee. Every employee after Rosa
# inherited the previous accumulated hours.
# Priya's incorrect total was 200 because it included
# all five employees' hours:
# 40 + 46 + 32 + 38 + 44 = 200.
# This was a logic error because the code ran without
# crashing but produced incorrect results.


# Step 4: Fix Two Overtime Bugs That Overpay the Firm by $1,810 a Week
# TODO: work out Rosa's, Darnell's and Mei's pay by hand first
# TODO: fix weekly_pay() so it follows the handbook rule word for word
# TODO: fix the other line that compares `total` against 40 the same way
def weekly_pay(hours, rate):
    if hours > 40:
        return 40 * rate + (hours - 40) * rate * 1.5
    return hours * rate


owed_overtime = 0
payroll = 0.0
for emp in employee_ids:
    total = 0
    name = ""
    rate = 0.0
    for r in records:
        if r["id"] == emp:
            name = r["name"]
            rate = r["rate"]
            total = total + r["hours"]
    if total > 40:
        owed_overtime = owed_overtime + 1
    pay = weekly_pay(total, rate)
    payroll = payroll + pay
    print(f"{name:16} {total:3} hrs  ${pay:>9,.2f}")

print("employees owed overtime:", owed_overtime)
print(f"TOTAL PAYROLL: ${payroll:,.2f}")

# Step 4, answer 1:
# Rosa: 40 hours at $24.00 per hour.
# 40 * 24.00 = $960.00.
# Rosa does not qualify for overtime.
#
# Darnell: 46 hours at $31.50 per hour.
# Regular pay: 40 * 31.50 = $1260.00.
# Overtime rate: 31.50 * 1.5 = $47.25.
# Overtime pay: 6 * 47.25 = $283.50.
# Total: 1260.00 + 283.50 = $1543.50.
#
# Mei: 32 hours at $28.00 per hour.
# 32 * 28.00 = $896.00.
# Mei does not qualify for overtime.
#
# The corrected program matched all three calculations.

# Step 4, answer 2:
# Bug 1: Original lines 111-112 used:
# if hours >= 40:
#     return hours * rate * 1.5
# This incorrectly applied overtime to every hour worked.
# Changed the condition to hours > 40 and the calculation
# to 40 * rate + (hours - 40) * rate * 1.5.
#
# Bug 2: Original line 127 used:
# if total >= 40:
# This incorrectly counted employees working exactly
# 40 hours as employees owed overtime.
# Changed it to if total > 40:
#
# Original payroll: $7655.50.
# Corrected payroll: $5845.50.
# Difference: 7655.50 - 5845.50 = $1810.00.
# Original overtime headcount: 3.
# Corrected overtime headcount: 2.

# Step 4, answer 3:
# Rosa's exactly-40-hour week catches the boundary error
# because the handbook says overtime applies only to
# hours beyond 40.
# Employees working fewer than 40 hours are excluded by
# both conditions, while employees working more than 40
# hours are included by both conditions.
# Only an exactly-40-hour week reveals the difference
# between >= 40 and > 40.

# AI Output Validation:
# The calculations and debugging were checked with AI
# assistance against the supplied CSV and starter code.
# The original errors and incorrect payroll were reproduced.
# The corrected output matched the calculated weekly hours,
# payroll amounts and overtime headcount.
# A program running without errors does not guarantee
# that its output is correct.
#
# Collaboration: N/A - individual work.
