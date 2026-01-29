from locust import HttpUser, task, between
import random

class MyEventsUser(HttpUser):
    wait_time = between(0.5, 1)   # faster requests = better stress test

    @task
    def view_my_events(self):
        user = f"user{random.randint(1, 50)}"

        self.client.get(
            f"/my-events?user={user}",
            name="/my-events"     # clean endpoint name in Locust UI
        )
