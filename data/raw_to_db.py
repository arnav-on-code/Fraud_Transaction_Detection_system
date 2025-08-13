import pandas as pd
import sqlite3

# Load data from CSV
df = pd.read_csv('data/raw/creditcard.csv')

# Connect to (or create) SQLite database
conn = sqlite3.connect('data/processed/fraud.db')

# Write DataFrame to SQL table
df.to_sql('transactions', conn, index=False, if_exists='replace')

# Query a subset for analysis
# df_subset = pd.read_sql_query("SELECT * FROM transactions WHERE Amount > 500", conn)

conn.close()
