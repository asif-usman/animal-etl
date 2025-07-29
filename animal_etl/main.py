from .etl.client import AnimalAPIClient
from .etl.transform import transform_animal, transform_animal_for_upload
from .etl.loader import load_animals_in_batches

def main():
    client = AnimalAPIClient()
    all_animals = []

    mock_animals = [
        {
            "id": 1,
            "name": "Tiger",
            "friends": "Lion, Panther",
            "born_at": "2022-03-05T08:00:00-05:00"
        },
        {
            "id": 2,
            "name": "Elephant",
            "friends": "Rhino, Hippo",
            "born_at": "2020-06-12T11:30:00+02:00"
        },
        {
            "id": 3,
            "name": "Eagle",
            "friends": "Hawk, Falcon",
            "born_at": "2021-12-25T14:00:00+01:00"
        },
        {
            "id": 4,
            "name": "Penguin",
            "friends": ""
        }
    ]

    for raw in mock_animals:
        cleaned = transform_animal(raw)
        upload_ready = transform_animal_for_upload(cleaned)
        all_animals.append(upload_ready)

    print(f"Prepared {len(all_animals)} animals.")
    load_animals_in_batches(client, all_animals)

if __name__ == "__main__":
    main()
#     print("Getting animal listings...")
#     for animal_id in client.get_all_animal_ids():
#         details = client.get_animal_details(animal_id)
#         if details:
#             transformed = transform_animal(details)
#             upload_ready = transform_animal_for_upload(transformed)
#             all_animals.append(upload_ready)

#     print(f"Get and transformed {len(all_animals)} animals.")
#     load_animals_in_batches(client, all_animals)

# if __name__ == "__main__":
#     main()