import sqlite3
import os

os.remove('q-sql-rolling-anomaly.db') if os.path.exists('q-sql-rolling-anomaly.db') else None
with sqlite3.connect('q-sql-rolling-anomaly.db') as conn:
    cur = conn.cursor()
    cur.executescript(open('q-sql-rolling-anomaly.sql').read())
    
    cur.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cur.fetchall()

    print("Tables in database:")
    for table in tables:
        print(table[0])

        
    table_name = "daily_product_metrics"
    cur.execute(f"PRAGMA table_info({table_name});")
    columns = cur.fetchall()

    print(f"Columns in table '{table_name}':")
    for col in columns:
        print(f"Name: {col[1]}, Type: {col[2]}, NotNull: {col[3]}, Default: {col[4]}, PK: {col[5]}")


    cur.execute('''
    ALTER TABLE daily_product_metrics ADD COLUMN trailing_avg REAL;
    ''')

    cur.execute('''
    ALTER TABLE daily_product_metrics ADD COLUMN lift REAL;
    ''')

    cur.execute('''
    WITH ranked_metrics AS (
        SELECT
            region,
            metric_date,
            activations,
            AVG(activations) OVER (
                PARTITION BY region
                ORDER BY metric_date
                ROWS BETWEEN 7 PRECEDING AND 1 PRECEDING
            ) AS trailing_avg_calc
        FROM daily_product_metrics
    )

    UPDATE daily_product_metrics
    SET trailing_avg = (
        SELECT trailing_avg_calc
        FROM ranked_metrics
        WHERE daily_product_metrics.region = ranked_metrics.region
          AND daily_product_metrics.metric_date = ranked_metrics.metric_date
    );
    ''')

    cur.execute('''
    UPDATE daily_product_metrics
    SET lift = (activations - trailing_avg) / NULLIF(trailing_avg, 0);
    ''')

    cur.execute('''
    SELECT MAX(lift) FROM daily_product_metrics
    WHERE region = 'EMEA'
    ''')
    result = cur.fetchone()
    print("Max lift in EMEA region:", result[0])

#########################################################################################################################

os.remove('q-sql-enterprise-margin.db') if os.path.exists('q-sql-enterprise-margin.db') else None
with sqlite3.connect('q-sql-enterprise-margin.db') as conn:
    cur = conn.cursor()
    cur.executescript(open('q-sql-enterprise-margin.sql').read())
    
    cur.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cur.fetchall()

    print("Tables in database:")
    for table in tables:
        print(table[0])

        
    table_name = "subscription_orders"
    cur.execute(f"PRAGMA table_info({table_name});")
    columns = cur.fetchall()

    print(f"Columns in table '{table_name}':")
    for col in columns:
        print(f"Name: {col[1]}, Type: {col[2]}, NotNull: {col[3]}, Default: {col[4]}, PK: {col[5]}")

    cur.execute('''
        SELECT region, (SUM(revenue_usd - cost_usd) * 1.0 / SUM(revenue_usd)) as gross, SUM(revenue_usd) as total_revenue, SUM(cost_usd) as total_cost
        FROM subscription_orders
        WHERE segment = 'Enterprise' AND DATE(order_date) >= '2024-04-01' AND DATE(order_date) < '2024-06-30'
        GROUP BY region
        ORDER BY gross DESC
        LIMIT 1
    ''')

    result = cur.fetchone()
    print("Region with highest gross margin in Enterprise segment (Apr-Jun 2024):", result[0], "    Gross Margin:", result[1], "    Total Revenue:", result[2], "    Total Cost:", result[3])

#########################################################################################################################

os.remove('q-datasette-facet-revenue.db') if os.path.exists('q-datasette-facet-revenue.db') else None
with sqlite3.connect('q-datasette-facet-revenue.db') as conn:
    cur = conn.cursor()
    cur.executescript(open('q-datasette-facet-revenue.sql').read())

    cur.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cur.fetchall()
    print("Tables in database:")
    for table in tables:
        print(table[0])

    table_name = "orders"
    cur.execute(f"PRAGMA table_info({table_name});")
    columns = cur.fetchall()
    print(f"Columns in table '{table_name}':")
    for col in columns:
        print(f"Name: {col[1]}, Type: {col[2]}, NotNull: {col[3]}, Default: {col[4]}, PK: {col[5]}")

    cur.execute('''
        SELECT region, category, SUM(quantity * unit_price) as total_revenue
        FROM orders
        WHERE status = 'completed'
        GROUP By region, category
        ORDER BY total_revenue DESC
        LIMIT 1
    ''')

    result = cur.fetchone()
    print("Region and category with highest revenue from completed orders:", result[0], result[1], "    Total Revenue:", result[2])

#########################################################################################################################

import duckdb
print(duckdb.sql('''
SELECT * FROM 'q-duckdb-sku-benchmark-shipments.csv' LIMIT 5
''').df())
print(duckdb.sql('''
SELECT * FROM 'q-duckdb-sku-benchmark-sku_master.csv' LIMIT 5
''').df())

print(duckdb.sql('''
    SELECT 
        sku_master.category,
    FROM read_csv_auto('q-duckdb-sku-benchmark-shipments.csv') AS shipments
    LEFT JOIN read_csv_auto('q-duckdb-sku-benchmark-sku_master.csv') AS sku_master
        ON shipments.sku_id = sku_master.sku_id
    WHERE shipments.ship_date >= '2024-05-15'
    GROUP BY sku_master.category
    ORDER BY 
        (SUM(shipments.units * shipments.unit_price)
        - SUM(sku_master.production_cost * shipments.units)) * 1.0
        / SUM(sku_master.production_cost * shipments.units)
    DESC
    LIMIT 1;
''').df())