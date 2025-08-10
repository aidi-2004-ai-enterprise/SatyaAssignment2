from locust import HttpUser, task, between

class PenguinUser(HttpUser):
    wait_time = between(1, 3)  # wait between 1 to 3 seconds between tasks

    @task
    def predict(self):
        sample_data = {
            "island": 0,
            "bill_length_mm": 39.1,
            "bill_depth_mm": 18.7,
            "flipper_length_mm": 181.0,
            "body_mass_g": 3750.0,
            "sex": 1
        }
        self.client.post("/predict", json=sample_data)
