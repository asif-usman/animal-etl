from etl.client import AnimalAPIClient
from etl.transform import transform_animal

def main():
    client = AnimalAPIClient()
    all_animals = []

    print("Fetching animal listings...")
    for animal_id in client.get_all_animal_ids():
        details = client.get_animal_details(animal_id)
        if details:
            transformed = transform_animal(details)
            all_animals.append(transformed)

    print(f"Fetched and transformed {len(all_animals)} animals.")
    load_animals_in_batches(client, all_animals)

if __name__ == "__main__":
    main()