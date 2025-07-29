import time
import json

def load_animals_in_batches(client, animals, batch_size=100):
    batch_number = 1
    for start in range(0, len(animals), batch_size):
        batch = animals[start:start + batch_size]
        print(f"Uploading batch {batch_number}...")
        print(json.dumps(batch, indent=2))

        response = client.post_animals_home(batch)

        if response.status_code == 200:
            print(f"Batch {batch_number} uploaded successfully.")
        else:
            print(f"Batch {batch_number} failed with status code {response.status_code}.")

        batch_number += 1
        time.sleep(1)

