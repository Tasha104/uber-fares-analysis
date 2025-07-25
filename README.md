 Uber Fares Dataset Analysis

Introduction to Big Data Analytics (INSY 8413)
Instructor: Eric Maniraguha

---

 Project Overview

This project analyzes the 'Uber Fares Dataset' using Python (Pandas) that i downloaded in Vs code and Power BI Desktop.  
The goal is to uncover insights about fare patterns, ride times, and key metrics, then present them in an interactive Power BI dashboard.

---

Deliverables

This repository includes:

-Python Script: 'uber_analysis.py' — Loads, cleans, and explores the data.
-Cleaned Dataset: 'uber_clean.csv' — Clean data ready for visualization.
-Power BI Dashboard: 'uber_dashboard.pbix' — Interactive dashboard analyzing fares.
-Screenshots: Showing data loading, cleaning, and dashboard views.

---

 Methodology

1. Data Download:
   - Downloaded from [Kaggle Uber Fares Dataset](https://www.kaggle.com/datasets/yasserh/uber-fares-dataset).

2. Data Cleaning & EDA:
   - Loaded data with Pandas.
   - Checked data structure & missing values.
   - Dropped rows with missing coordinates.
   - Performed basic descriptive statistics (mean, median, mode, std dev).
   - Detected outliers using IQR.
   - Engineered new features: hour, day, month, day_of_week, peak/off-peak.

3. Data Export:
   - Saved the cleaned dataset as uber_clean.csv.

4. Dashboard Design in Power BI:
   - Imported 'uber_clean.csv'.
   - Created visualizations:
     - Fare amount distribution (histogram)
     - Rides by hour, day, and month (time series)
     - Pickup locations (map)
     - Filters for day of week and peak/off-peak times.
   - Added slicers for interactivity.
   - Designed layout with clear titles and formatting.

---

 Insights

- Identified fare ranges and peak periods.
- Visualized ride patterns by hour, day, and month.
- Highlighted busiest times for Uber rides.
- Provided spatial overview of pickup locations.

---

 How to View

1. Clone or download this repo.
2. Open `uber_clean.csv` for the cleaned data.
3. Open `uber_dashboard.pbix` in Power BI Desktop to explore the interactive visuals.
4. Check screenshots for a quick overview.

---

Author

KALIZA Natasha peace
kalizanatashapeace@gmail.com  
Course: Introduction to Big Data Analytics — AUCA

---
📂 **Power BI Dashboard (.pbix)**: (https://drive.google.com/file/d/1LdHB555gjaCcgeEDbGCY14rY0R52d6Sm/view?usp=drive_link)

📂 **Cleaned Dataset (.csv)**: (https://drive.google.com/file/d/1SWGRXR88xeSWtBDt5ysKun0a-Z0W6SDe/view?usp=drive_link)
