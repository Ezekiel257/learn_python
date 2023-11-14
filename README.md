# PostgreSQL Query Script

# This Python script connects to a PostgreSQL database and executes SQL queries to answer four specific questions related to cryptocurrency transactions and members' data.

## Author

- **Author**: ezekieloshin@gmail.com

## Questions Addressed

**Question One:**

# sql
SELECT
    txn_type,
    COUNT(*) AS transaction_count
FROM
    raw.transactions
GROUP BY
    txn_type;

# The script executes this query to retrieve the transaction count grouped by transaction type.

# Question Two:
# sql
SELECT
    EXTRACT(YEAR FROM txn_date::date) AS txn_year,
    txn_type,
    COUNT(*) AS txn_count,
    SUM(quantity) AS total_quantity,
    AVG(quantity) AS average_quantity
FROM
    raw.transactions
GROUP BY
    txn_year, txn_type
ORDER BY
    txn_year, txn_type;

# This query calculates various statistics for transactions, such as count, total quantity, and average quantity, grouped by year and transaction type.

# Question Three:
# sql
SELECT
    TO_CHAR(CAST(txn_date AS DATE), 'Month') AS calendar_month,
    SUM(CASE WHEN txn_type = 'BUY' THEN quantity ELSE 0 END) AS buy_quantity,
    SUM(CASE WHEN txn_type = 'SELL' THEN quantity ELSE 0 END) AS sell_quantity
FROM
    raw.transactions
WHERE
    EXTRACT(YEAR FROM txn_date::date) = 2020 AND
    ticker = 'ETH'
GROUP BY
    calendar_month
ORDER BY
    calendar_month;

# This query retrieves the total quantity of buy and sell transactions for a specific cryptocurrency (ETH) in each month of the year 2020.

# Question Four:
# sql
SELECT
    m.first_name,
    SUM(t.quantity) AS total_quantity
FROM
    raw.members AS m
JOIN
    raw.transactions AS t
ON
    m.member_id = t.member_id
WHERE
    t.ticker = 'BTC'
GROUP BY
    m.first_name
ORDER BY
    total_quantity DESC
LIMIT 3;

# The script executes this query to find the top three members with the highest total quantity of transactions for a specific cryptocurrency (BTC).

# Execution
# Ensure you have Python 3.x installed.
# Install the psycopg2 library using pip install psycopg2.
# Modify the database connection details (dbname, user, password, host, and port) in the script according to your PostgreSQL setup.

# Run the script:

python script.py

# Error Handling
# The script includes error handling for database connection errors and general exceptions.

# Database Connection Details
Database Name: metaverse
Username: cryptoverse_admin
Password: handsome
Host: localhost
Port: 5433


# Customize the script as needed based on your PostgreSQL setup and data structure.
# Adjust the SQL queries or add more questions as required.