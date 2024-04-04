import sqlite3
import pandas as pd

# Database connection
db_connection = sqlite3.connect('PBS.db')
cursor = db_connection.cursor()

# Create tables
create_builder_proposer_tx_table = """
CREATE TABLE IF NOT EXISTS builder_proposer_tx (
    hash TEXT,
    nonce INTEGER,
    transaction_index INTEGER,
    from_address TEXT,
    to_address TEXT,
    value INTEGER,
    gas INTEGER,
    gas_price INTEGER,
    input TEXT,
    receipt_cumulative_gas_used INTEGER,
    receipt_gas_used INTEGER,
    receipt_contract_address TEXT,
    receipt_root TEXT,
    receipt_status INTEGER,
    block_timestamp TEXT,
    block_number INTEGER,
    block_hash TEXT,
    max_fee_per_gas INTEGER,
    max_priority_fee_per_gas INTEGER,
    transaction_type INTEGER,
    receipt_effective_gas_price INTEGER
);
"""

create_relay_data_table = """
CREATE TABLE IF NOT EXISTS relay_data (
    relay TEXT,
    slot INTEGER,
    block_hash TEXT,
    builder_pubkey TEXT,
    value INTEGER,
    gas_used INTEGER,
    gas_limit INTEGER,
    block_number INTEGER
);
"""

cursor.execute(create_builder_proposer_tx_table)
cursor.execute(create_relay_data_table)


def insert_data_from_csv(table_name, csv_file):
    # Check if table already has data
    cursor.execute(f"SELECT COUNT(*) FROM {table_name}")
    if cursor.fetchone()[0] == 0:  # If no data, insert new data
        df = pd.read_csv(csv_file)
        df.to_sql(table_name, db_connection, if_exists='append', index=False)
        print(f"Data inserted into {table_name}")
    else:
        print(f"{table_name} already has data. No new data inserted.")


# File paths
builder_proposer_tx_csv = 'data_0404/BigQueryData.csv'
relay_data_csv = 'data_from_relays/merged_file.csv'

# Insert data
insert_data_from_csv('builder_proposer_tx', builder_proposer_tx_csv)
insert_data_from_csv('relay_data', relay_data_csv)

# Close the database connection
db_connection.close()
