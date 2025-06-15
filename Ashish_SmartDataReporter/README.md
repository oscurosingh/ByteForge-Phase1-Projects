# People Data Report

This project generates a detailed PDF report summarizing demographic and job data from a dataset of people.

---

## Overview

The script processes a CSV file containing information about individuals to produce:

- *Total number of people*  
- *Gender distribution* with counts and percentages  
- *Top 5 most common job titles*  
- A *pie chart* visualizing gender distribution  
- A *PDF report* compiling all results and the chart

---

## Input Data

- **File:** *people.csv*  
- **Required columns:**  
  - *Sex* (e.g., Male, Female)  
  - *Job Title*  

The script works best with datasets similar in structure and size (100 records) but can handle variations.

---

## How It Works

1. **Load Data:** Reads the CSV using pandas.  
2. **Compute Stats:** Counts total entries, gender breakdown, and top jobs.  
3. **Create Visualization:** Generates and saves a gender pie chart image.  
4. **Generate Report:** Uses FPDF to create a PDF summarizing the data and embeds the chart.

---

## Files Created

- *gender.png* — Pie chart image showing gender percentages  
- *Report.pdf* — Complete report with stats and visuals

---

## Setup Instructions

Install dependencies using pip:

```bash
pip install pandas matplotlib fpdf
