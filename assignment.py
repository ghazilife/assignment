import os
import csv

# Function to create a new table
def create_table(table_name, columns):
    # Create a metadata file for table columns
    with open(f"{table_name}_metadata.csv", "w", newline="") as metadata_file:
        writer = csv.writer(metadata_file)
        writer.writerow(["Column Name", "Data Type"])
        for column in columns:
            writer.writerow(column)

    # Create a data file for the table
    with open(f"{table_name}.csv", "w", newline="") as data_file:
        pass

    print(f"Table '{table_name}' created successfully.")

# Function to insert data into a table
def insert_into_table(table_name, values):
    # Check if the table exists
    if not os.path.exists(f"{table_name}.csv"):
        print(f"Table '{table_name}' does not exist.")
        return

    # Load the metadata to get the column names and data types
    metadata = {}
    with open(f"{table_name}_metadata.csv", "r") as metadata_file:
        reader = csv.DictReader(metadata_file)
        for row in reader:
            metadata[row["Column Name"]] = row["Data Type"]

    # Check if the provided values match the table schema
    if len(values) != len(metadata):
        print("Number of values does not match the table schema.")
        return

    # Insert the values into the table
    with open(f"{table_name}.csv", "a", newline="") as data_file:
        writer = csv.writer(data_file)
        writer.writerow(values)

    print("Data inserted successfully.")

# Example usage
create_table("my_table", [("col1", "INTEGER"), ("col2", "STRING")])
insert_into_table("my_table", [1, "Hello"])
