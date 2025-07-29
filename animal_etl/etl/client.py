import requests
from ..utils.retry import retry_request

class AnimalAPIClient:
    BASE_URL = "http://localhost:3123/animals/v1"

    def get_all_animal_ids(self):
        ids = []
        page = 1

        while True:
            response = requests.get(f"{self.BASE_URL}/animals/v1/animals?page={page}")
            if response.status_code != 200:
                break

            data = response.json()
            animals = data.get("animals") or data
            if not animals:
                break
            for animal in animals:
                ids.append(animal["id"])
            page += 1

        return ids

    def get_animal_details(self, animal_id):
        url = f"{self.BASE_URL}/animals/{animal_id}"

        def request_func():
            return requests.get(url)

        response = retry_request(request_func)
        if response.status_code == 200:
            return response.json()
        return None

    def post_animals_home(self, animals_batch):
        url = f"{self.BASE_URL}/home"

        def request_func():
            return requests.post(url, json=animals_batch)

        response = retry_request(request_func)
        return response
