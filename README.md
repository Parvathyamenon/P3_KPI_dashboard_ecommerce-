# E-Commerce KPI Dashboard
### Revenue · CLV · Retention · Trends · Tableau Public

![SQL](https://img.shields.io/badge/SQL-SQLite-blue?style=flat-square)
![Python](https://img.shields.io/badge/Python-Pandas%20%7C%20NumPy-green?style=flat-square)
![Tableau](https://img.shields.io/badge/Tableau-Public-purple?style=flat-square)
![Status](https://img.shields.io/badge/Status-Complete-brightgreen?style=flat-square)

---

## Live Dashboard
 <p align="center">
  <img src="output/superstore_dashboard.twbx" width="900" alt="Product Analytics Dashboard">
</p>



---

## Project Overview

A full end-to-end BI pipeline built on the Superstore Sales dataset — **9,994 orders across 3 years**. This project demonstrates the complete data analyst workflow: from raw data ingestion through Python cleaning, SQL KPI analysis, and finally a published interactive Tableau dashboard built for an executive audience.

**Business questions answered:**
- Which product categories and sub-categories drive the most revenue and profit?
- How is Monthly Recurring Revenue trending — are we growing?
- Who are our highest-value customers by lifetime spend?
- Which customer segments (Consumer, Corporate, Home Office) are most profitable?
- Where geographically is revenue concentrated across the US?

---

## Key KPIs

| Metric | Value |
|---|---|
| Total Revenue | $2.3M |
| Total Profit | $286K |
| Profit Margin | 12.5% |
| Avg Customer CLV | $1,192 |
| Total Orders | 9,994 |
| Unique Customers | 793 |

---

## Dashboard Visuals (6 Sheets)

| Sheet | Type | Business Question |
|---|---|---|
| Revenue Trend | Line chart + trend line | Is revenue growing month over month? |
| Category Treemap | Treemap coloured by margin | Which sub-categories are most profitable? |
| Segment Performance | Dual-axis bar chart | How do Consumer / Corporate / Home Office compare? |
| Geographic Map | Choropleth map | Where is revenue concentrated? |
| Top 10 Customers | Sorted bar chart | Who are our highest-value customers? |
| KPI Summary Cards | Text / number cards | Executive headline numbers at a glance |

---

## Tech Stack

- **Python / Pandas** — Data cleaning, date engineering, CLV calculation
- **NumPy** — Profit margin computation
- **SQL (SQLite-style)** — KPI queries: MoM growth, segment analysis, top customer ranking
- **Tableau Public** — Interactive dashboard, published live with a shareable URL

---

## Project Structure

```
ecommerce-kpi-dashboard/
├── data/
│   └── superstore.csv            # Raw Superstore dataset
├── output/
│   ├── superstore_cleaned.csv    # Cleaned data with CLV columns added
│   └── customer_clv.csv          # Customer-level CLV summary
├── data_prep.py                  # Python cleaning + CLV calculation script
├── kpi_queries.sql               # SQL KPI queries (MoM growth, segments, top 10)
├── requirements.txt              # Python dependencies
└── README.md                     # This file
```

---

## How to Run Locally

```bash
# 1. Clone this repository
git clone https://github.com/YOUR_USERNAME/ecommerce-kpi-dashboard
cd ecommerce-kpi-dashboard

# 2. Install dependencies
pip install -r requirements.txt

# 3. Add the raw dataset
# Download superstore.csv from Kaggle or Tableau's sample data
# Place it in the data/ folder

# 4. Run the cleaning script
python data_prep.py
# Output: "Saved 9994 rows to output/superstore_cleaned.csv"

# 5. Open Tableau Public and connect to output/superstore_cleaned.csv
```

---

## Key SQL Queries

The `kpi_queries.sql` file contains four analytical queries:

1. **Monthly Revenue + MoM Growth** — Uses `LAG()` window function to calculate month-over-month growth %
2. **Category & Sub-Category Performance** — Revenue, profit, and margin ranked by sub-category
3. **Customer Segment Analysis** — Revenue per customer and margin % by segment
4. **Top 10 Customers by CLV** — Ranked by lifetime spend with order count and avg order value

---

## Why Tableau Public?

Tableau is used at Google, Stripe, Salesforce, and most non-Microsoft product companies. Unlike Power BI, Tableau Public lets you **publish a live, interactive dashboard with a public URL** — paste that URL directly into a job application and the interviewer can click and interact with it. No screenshot needed.

---

## About

Built as part of a data analyst portfolio project. Demonstrates end-to-end BI skills: data engineering, SQL analysis, and executive dashboard design.
**Connect:** [LinkedIn](https://www.linkedin.com/in/parvathy-menon-1aa75a100/)
