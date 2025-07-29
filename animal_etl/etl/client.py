import requests

class AnimalAPIClient:
    BASE_URL = "http://localhost:3123/animals/v1"

    def get_all_animal_ids(self):
        page = 1
        ids = []
        while True:
            response = retry_request(lambda: requests.get(f"{self.BASE_URL}/animals?page={page}"))
            if response.status_code != 200:
                break
            data = response.json()
            if not data:
                break
            ids.extend([animal['id'] for animal in data])
            page += 1
        return ids

    def get_animal_details(self, animal_id):
        url = f"{self.BASE_URL}/animals/{animal_id}"
        response = retry_request(lambda: requests.get(url))
        if response.status_code == 200:
            return response.json()
        return None

    def post_animals_home(self, animals_batch):
        url = f"{self.BASE_URL}/home"
        response = retry_request(lambda: requests.post(url, json=animals_batch))
        return response
