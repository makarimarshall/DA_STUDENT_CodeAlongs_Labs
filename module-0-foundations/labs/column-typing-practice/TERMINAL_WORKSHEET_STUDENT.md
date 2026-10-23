# Lab — Column-Typing & Collection-Concern Practice

**Skills assessed:** Data Literacy, Critical Thinking, Curiosity (see this lab's own `RUBRIC.md`)

**Estimated time:** ~100 minutes (10 min intro · 75 min collaborative work · 15 min shareout)

## Scenario

You've just joined a data team, and someone drops `data/energy_sample.csv` in your lap: country-level energy figures your team wants to use in a report next week. Nobody has documented it. Before a single chart gets made or a single number gets quoted, somebody has to say — out loud, with a reason — what each column actually holds, how much data is really in there, and what about the way it was collected should make a careful analyst cautious. Today that somebody is your group.

*Work with your group, but complete and push/commit your own copy of this lab — collaboration is encouraged, a shared submission isn't.*

## Your Objectives

- **Open the Raw File Before You Classify a Single Column**
  - *Same lab dataset from DATASET.md — a different file than the project's own co2-data, on purpose. Run every command from the module folder, so `data/energy_sample.csv` resolves.*

- **Preview Every Column's Actual Values — All Seven, Not Just the First Few**
  - *Hint: `cut` is new. It pulls specific columns out of a line: `-d,` says the columns are separated by commas, and `-f` says which ones you want.*

- **Classify All Seven Columns, Each With a Reason Drawn From the Data**

- **Confirm How Many Rows and How Many Countries You Actually Have**
  - *Hint: `sort` and `uniq -c` are new, and they work together: `uniq -c` counts repeats, but only ones sitting next to each other, so the values have to be sorted first.*

- **Check Whether Every Country Reports Every Column — Then Name Two Collection Concerns**

## Share Out

Two questions, in this order. First: how did your group figure out whether every country reports every column? Different groups almost certainly took different routes to the same file — compare them before deciding which you'd reach for next time. Second: which collection concerns did your group flag, and which single data-quality question did you sharpen out of them? Put each group's question up where everyone can read it, then ask the class which ones a real analyst could actually go answer — and which ones sound serious but can't be checked.

## My Lab Answers
### 1. Dataset Size

I used wc -l to count 71 lines, including the header.
That means there are 70 data rows across 10 countries.

### 2. Missing Data / Collection Concern #1

I found that Kenya and Nigeria are missing fossil_share_energy values from 2015 to 2021, which is 14 missing values total. This could affect comparisons between countries.

### 3. Column Classifications

1. **country — Categorical (String):** This column contains country names like Australia, Brazil, and Canada. These are labels rather than numerical measurements.

2. **year — Discrete Numerical (Temporal):** This column contains whole-number years from 2015 to 2021, which represent different points in time.

3. **iso_code — Categorical (String):** This column contains three-letter codes like AUS, BRA, and USA that identify countries.

4. **population — Discrete Numerical (Integer):** This column counts how many people live in each country. The values are whole numbers.

5. **energy_per_capita — Continuous Numerical (Float):** This column measures energy consumption per person and includes decimal values like 66879.320.

6. **fossil_share_energy — Continuous Numerical (Float):** This column measures the percentage of energy coming from fossil fuels. It contains decimal values, although Kenya and Nigeria have missing entries.

7. **renewables_share_energy — Continuous Numerical (Float):** This column measures the percentage of energy coming from renewable sources and includes decimal values like 5.955.

### 4. Collection Concern #2

The dataset doesn't have clear documentation showing where the information came from or how it was collected. Without knowing the original source, it's difficult to confirm whether the data is accurate and reliable.

### 5. Data-Quality Question

 Why is fossil_share_energy missing for Kenya and Nigeria from 2015 to 2021? Can we find the missing values from the original source to make the dataset more complete?

### 6. How I Checked for Missing Data
  I used the awk command in Terminal to check all seven columns for empty values. After finding 14 missing values in the fossil_share_energy column, I used another awk command to identify which countries and years were affected. The results showed that Kenya and Nigeria were missing values from 2015 to 2021