'''
Definition of names:
- collection: The name of the data source to connect to (e.g., 'Postgres', 'CBSODATA', 'CSV'). 
  Later this will be used as the schema or folder to write4 out.
- object: The name of the table, file or dataset_id. This will be the table name or file name to write out.
- connection_string: This can be a connection string, file path or dataset_id depending on the collection type. 
'''
import argparse
from unittest import case
import utils.connections as connections
from dotenv import load_dotenv

def ConnectSource(collection, object, connection_string):
    # With credentials and/or connection string to the source as parameters
    # Connect to the source and return the data as a DataFrame

    switch = {
        'Postgres': lambda: connections.GetPostgres(connection_string, object),
        'CBSODATA': lambda: connections.GetCBSODATA(object),
        'CSV': lambda: connections.GetCSV(connection_string)
    }
    return switch.get(collection, lambda: None)()

def WritetoTarget(source, target_type, target, connection_string=None):
    match target_type:
        case 'CSV':
            source.to_csv(target, index=False)
        case 'Postgres':
            source.to_sql(target, con=connections.GetPostgres(connection_string), if_exists='replace', index=False)
        case 'JSON':
            source.to_json(target, orient='records', lines=True)
        case _: print(f"Unsupported target type: {target_type}")

def main():
    import os

    load_dotenv()
    parser = argparse.ArgumentParser(description='Fetch data from a source and write to target CSV')
    parser.add_argument('--collection', '-c', default='CBSODATA', help='Source collection type (Postgres, CBSODATA, CSV)')
    parser.add_argument('--object', '-o', default='81486ned', help='Object name (table name or file name without extension)')
    parser.add_argument('--connection_string', '-s', default=None, help='Connection string, file path or dataset id for the source')
    args = parser.parse_args()

    # Connect to the source using provided parameters
    dfSource = ConnectSource(args.collection, args.object, args.connection_string)

    # By default we write out as CSV into the project data folder
    data_dir = f'{os.getenv('DATA_DIR', './data')}/{args.collection}'
    target_type = os.getenv('DEFAULT_TARGET_TYPE','~/')

    if not os.path.isdir(data_dir):
        os.makedirs(data_dir)
    target_path = f'{data_dir}/{args.object}.{target_type.lower()}'
 
    WritetoTarget(dfSource, target_type, target_path, args.connection_string)

if __name__ == "__main__":
    main()
