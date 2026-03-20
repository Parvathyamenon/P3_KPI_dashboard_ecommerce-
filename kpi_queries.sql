-- FILE: kpi_queries.sql
-- PURPOSE: Core KPI calculations for the executive dashboard

-- KPI 1: Monthly Revenue + MoM Growth
WITH monthly AS (
    SELECT
        strftime('%Y-%m', Order date) AS month,
        SUM(sales) AS revenue,
        SUM(profit) AS profit
    FROM superstore_cleaned sc 
    GROUP BY month
)
SELECT
    month, revenue, profit,
    ROUND(100.0*(revenue - LAG(revenue) OVER (ORDER BY month))
          / NULLIF(LAG(revenue) OVER (ORDER BY month), 0), 1) AS mom_growth_pct
FROM monthly ORDER BY month;

-- KPI 2: Revenue and Profit by Category + Sub-Category
SELECT
    category, sub_category,
    ROUND(SUM(sales),2)   AS revenue,
    ROUND(SUM(profit),2)  AS profit,
    ROUND(AVG(100.0*profit/NULLIF(sales,0)),1) AS avg_margin_pct,
    COUNT(DISTINCT order_id) AS orders
FROM superstore
GROUP BY category, sub_category
ORDER BY revenue DESC;

-- KPI 3: Customer Segment Performance
SELECT
    segment,
    COUNT(DISTINCT customer_id) AS customers,
    ROUND(SUM(sales),2)  AS total_revenue,
    ROUND(SUM(sales)/COUNT(DISTINCT customer_id),2) AS revenue_per_customer,
    ROUND(SUM(profit)/SUM(sales)*100,1) AS profit_margin_pct
FROM superstore
GROUP BY segment ORDER BY total_revenue DESC;

-- KPI 4: Top 10 Customers by CLV
SELECT
    customer_id, customer_name, segment,
    COUNT(DISTINCT order_id) AS total_orders,
    ROUND(SUM(sales),2) AS lifetime_value,
    ROUND(AVG(sales),2) AS avg_order_value
FROM superstore
GROUP BY customer_id, customer_name, segment
ORDER BY lifetime_value DESC LIMIT 10
