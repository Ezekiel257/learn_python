import pandas as pd
import polars as pl

flight_data = 'https://github.com/ianmcook/dplyr-examples/raw/master/data/flights.parquet'
try:
    # Load data using pandas
    pa_df = pd.read_parquet(flight_data)
    # Load data using polars
    pl_df = pl.read_parquet(flight_data)
except Exception as e:
    print(f"An error occurred: {e}")

##pandas
%%timeit
aggs2 = pl_df.group_by('carrier').agg(
    [
        pl.col('dep_delay').min().alias('dep_delay_min'),
        pl.col('dep_delay').mean().alias('dep_delay_mean'),
        pl.col('dep_delay').max().alias('dep_delay_max'),
        pl.col('arr_delay').min().alias('arr_delay_min'),
        pl.col('arr_delay').mean().alias('arr_delay_mean'),
        pl.col('arr_delay').max().alias('arr_delay_max')
    ]
)