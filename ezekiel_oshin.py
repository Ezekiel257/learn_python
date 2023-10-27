"""
Author: ezekieloshin@gmail.com
"""
question_one = """
-- SELECT
    txn_type,
    COUNT(*) AS transaction_count
FROM
    raw.transactions
GROUP BY
    txn_type;
"""

question_two = """
-- SELECT
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
"""

question_three = """
-- SELECT
  --  DATE(CAST(txn_date AS DATE)) AS calendar_month,
  --  EXTRACT(MONTH FROM CAST(txn_date AS DATE)) AS calendar_month,
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
"""

question_four = """
-- SELECT
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
"""

# Function to execute SQL queries
def execute_query(query):
    cursor.execute(query)
    return cursor.fetchall()

# Main function to execute the SQL queries
def main():
    # Database connection setup
    try:
        conn = psycopg2.connect(
            dbname="metaverse",
            user="cryptoverse_admin",
            password="handsome",
            host="localhost",
            port="5433"
        )

        cursor = conn.cursor()

        # Execute SQL queries for each question
        result_1 = execute_query(question_one)
        result_2 = execute_query(question_two)
        result_3 = execute_query(question_three)
        result_4 = execute_query(question_four)

        # Process and display the results
        print("Results for Question one:")
        for row in result_1:
            print(row)
        
        print("Results for Question two:")
        for row in result_2:
            print(row)
        
        print("Results for Question three:")
        for row in result_3:
            print(row)
        
        print("Results for Question four:")
        for row in result_4:
            print(row)

    except psycopg2.Error as e:
        print(f"Database error: {e}")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        # Close the database connection
        if conn:
            conn.close()

if __name__ == "__main":
    main()