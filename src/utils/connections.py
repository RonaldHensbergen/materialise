import pandas as pd
def GetPostgres(connection_string=None, object_name=None) -> pd.DataFrame:
    import psycopg2
    import os

    conn = psycopg2.connect( 
        host=os.getenv("POSTGRES_HOST"),
        port=os.getenv("POSTGRES_PORT"),
        database=os.getenv("POSTGRES_DB"),
        user=os.getenv("POSTGRES_USER"),
        password=os.getenv("POSTGRES_PASSWORD")
    )
    return pd.read_sql(f"SELECT * FROM {object_name}", conn)

def GetCSV(csv_file_path='data/source_data.csv') -> pd.DataFrame:

    return pd.read_csv(csv_file_path)

def GetCBSODATA(dataset_id='81486ned') -> pd.DataFrame:
    import cbsodata as cbso
    print('Getting data from CBSODATA with dataset_id:', dataset_id)
    if dataset_id == 'list':
        cbsodata = cbso.get_table_list()
    else:
        cbsodata = cbso.get_data(dataset_id)
    df = pd.DataFrame(cbsodata)

    return df