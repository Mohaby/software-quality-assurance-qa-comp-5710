import hvac
import csv

# Setup Vault client
vault_url = 'http://127.0.0.1:8200'
vault_token = 'hvs.MCHSm79asqQvGQQmqSB3h48z'
client = hvac.Client(url=vault_url, token=vault_token)

#to store secrets in Vault
def store_secrets(csv_path):
    with open(csv_path, mode='r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            path = f"secret/{row['Variable']}"  
            data = {row['Variable']: row['Value']}
            # Store the secret in Vault
            client.secrets.kv.v2.create_or_update_secret(path=path, secret=data)
            print(f"Secret stored at {path} with data {data}")

# Path to the CSV file
csv_file_path = '/Users/mbeyo/Downloads/secrets.csv'

# Store secrets in Vault
store_secrets(csv_file_path)
