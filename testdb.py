import pandas as pd
from db import client 

def insert_csv_to_mongodb(csv_file, database_name, collection_name):
    db = client[database_name]
    collection = db[collection_name]

   
    data = pd.read_csv(csv_file)

   
    data_dict = data.to_dict(orient='records')

   
    collection.insert_many(data_dict)

if __name__ == "__main__":
    csv_file_path = "sigma_v_1.csv"  # Update with your CSV file path
    database_name = "Problems"  # Update with your database name
    collection_name = "Sigma"  # Update with your collection name

    insert_csv_to_mongodb(csv_file_path, database_name, collection_name)
