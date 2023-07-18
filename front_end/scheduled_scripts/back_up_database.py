import sqlite3
import sys

# sys.path.append('/app/server')
# from content import *
# from helper import *

in_file_path = sys.argv[1]
out_file_path = sys.argv[2]

# main_content = Content(in_file_path)
# backup_content = Content(out_file_path)

# I tried VACUUM INTO, but it runs out of memory.

# Connect to the source database file
source_conn = sqlite3.connect(in_file_path)
destination_conn = sqlite3.connect(out_file_path)

source_cursor = source_conn.cursor()
sql = "SELECT name FROM sqlite_master WHERE type='table'"
source_cursor.execute(sql)

table_names = []
for row in source_cursor.fetchall():
    table_names.append(row[0])

source_cursor.close()

for table_name in table_names:
    if table_name == "sqlite_sequence":
        continue

    print(table_name)

    # Connect to the destination database file
    source_cursor = source_conn.cursor()
    destination_cursor = destination_conn.cursor()

    # Get the CREATE TABLE statement for the table
    source_cursor.execute(f"SELECT sql FROM sqlite_master WHERE name='{table_name}'")
    create_table_sql = source_cursor.fetchone()[0]

    # Create the table in the destination database
    destination_cursor.execute(create_table_sql)

    # Copy the data from the source table to the destination table
    source_cursor.execute(f"SELECT * FROM {table_name}")
    rows = source_cursor.fetchall()

    if len(rows) > 0:
        destination_cursor.executemany(f"INSERT INTO {table_name} VALUES ({', '.join(['?'] * len(rows[0]))})", rows)

    # Commit the changes and close the connections
    destination_conn.commit()

destination_conn.close()
source_conn.close()