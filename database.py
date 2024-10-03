import vector_store_func as vsf



database_path="./store_database"
store_csv_path="DMart.csv"

store_data = vsf.load_store_csv(store_csv_path)

vsf.create_store_database(store_data,database_path) 