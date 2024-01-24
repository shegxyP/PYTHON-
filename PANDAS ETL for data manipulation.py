import pandas as pd

# Sample Extract function - Simulates extracting data from a source
def extract_data():
    # Replace this with your actual data source or extraction logic
    data = {
        'ID': [1, 2, 3],
        'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [25, 30, 22]
    }
    return pd.DataFrame(data)

# Sample Transform function - Simulates transforming data
def transform_data(raw_data):
    # Replace this with your actual data transformation logic
    transformed_data = raw_data.copy()
    transformed_data['Age'] = transformed_data['Age'] + 5
    return transformed_data

# Sample Load function - Simulates loading data to a destination
def load_data(processed_data):
    # Replace this with your actual data loading logic
    print("Data loaded successfully:")
    print(processed_data)

# ETL Process
def etl_process():
    # Extract
    raw_data = extract_data()

    # Transform
    transformed_data = transform_data(raw_data)

    # Load
    load_data(transformed_data)

# Run the ETL process
etl_process()
