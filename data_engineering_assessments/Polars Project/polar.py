import numpy as np
import polars as pl

#q1 = (
    #pl.read_csv("https://j.mp/iriscsv")
    #.lazy()
    #.filter(pl.col("sepal_length") > 5)
    #.group_by("species")
    #.agg(pl.col("sepal_width").mean())
#)

#Reading and writing data (CSV)
import polars as pl

def read_and_print_csv(file_path):
    """
    Reads a CSV file into a DataFrame and prints it.
    Args:
    file_path (str): The path to the CSV file.
    """
    try:
        df = pl.read_csv(file_path)
        if df.shape[0] > 0:  # Check if the DataFrame is not empty
            print(df)
        else:
            print("No data found in the file.")
    except Exception as e:
        print(f"Failed to read the file: {e}")

#Read data parquet
loan_risk = pl.scan_parquet("https://tinyurl.com/5eduaare")  # Lazily read remote parquet file (compression: snappy)
#print(loan_risk.collect().shape)  # print shape
#print(loan_risk.collect().head(10))  # print the first 10 rows

#Filtering
non_debtors = loan_risk.filter(  # non-debtors
    pl.col('paid_amnt').eq(pl.col('funded_amnt'))
).collect()

#print(non_debtors)

paid_1h_3h = loan_risk.filter( # those who have made between 100.0 and 300.0 in loan repayments
    pl.col('paid_amnt').is_between(100.0, 300.0)
).collect()

#print(paid_1h_3h)

ca_debtors = loan_risk.filter( # debtors from California
    (pl.col('paid_amnt') < pl.col('funded_amnt')) & (pl.col('addr_state') == 'CA')
).collect()

#print(ca_debtors)


###Creating new columns
new_df = loan_risk.with_columns([
    pl.col('funded_amnt').mean().alias('avg_loan_amnt'),
    pl.col('paid_amnt').mean().alias('avg_paid_amnt')
]).collect()

#print(new_df)

###Groupby
# aggregates by state
groupby = loan_risk.group_by('addr_state', maintain_order=True).agg([
    pl.col('funded_amnt').mean().alias('avg_funded_amnt_by_state'),
    pl.col('funded_amnt').max().alias('max_funded_amnt_by_state'),
    pl.col('funded_amnt').min().alias('min_funded_amnt_by_state')
]).collect()

#print(groupby)

###Combining dataframes
import numpy as np
from datetime import datetime, timedelta

df = pl.LazyFrame({
    "a": np.arange(0, 8),
    "b": np.random.rand(8),
    "c": [datetime(2023, 3, 9) + timedelta(days=idx) for idx in range(8)],
    "d": [1, 2.0, np.NaN, np.NaN, 0, -5, -42, None]
}).collect()

df2 = pl.LazyFrame({
    "x": np.arange(0, 8),
    "y": ['A', 'A', 'A', 'B', 'B', 'C', 'X', 'X']
}).collect()

joined_df = df.join(df2, left_on='a', right_on='x')  # ~ join on 'a' == 'x'

#print(joined_df)


###SQLContext###

# Create an SQLContext from the "loan_risk" LazyFrame.
sql = pl.SQLContext(frame=loan_risk).execute(
    "SELECT funded_amnt FROM frame WHERE funded_amnt >= 10000"
).collect()

print(sql)

# It also supports CTEs, joins, aggregations etc.

sql2 = pl.SQLContext(frame=loan_risk).execute(
    """with tfa as ( -- total funded amount by state
          SELECT
              addr_state,
              CAST(SUM(funded_amnt) AS float) as total_funded_amnt
          FROM frame
          GROUP BY addr_state
      ),

      tpa as ( -- total paid amount by state
          SELECT
              addr_state,
              CAST(SUM(paid_amnt) AS float) as total_paid_amnt
          FROM frame
          GROUP BY addr_state
      )

    SELECT DISTINCT
        f.addr_state,
        tfa.total_funded_amnt,
        tpa.total_paid_amnt,
        tfa.total_funded_amnt - tpa.total_paid_amnt as total_outstanding
    FROM frame f
    JOIN
        tfa on f.addr_state = tfa.addr_state
    JOIN
        tpa on f.addr_state = tpa.addr_state
    ORDER BY total_outstanding DESC;
    """
).collect()

print(sql2)



