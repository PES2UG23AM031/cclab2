from locust import HttpUser, task, between
import random

class EventsUser(HttpUser):
    wait_time = between(0.5, 1)   # faster users = better stress test

    @task
    def view_events(self):
        user = f"user{random.randint(1, 50)}"

        self.client.get(
            f"/events?user={user}",
            name="/events"     # clean endpoint name in Locust UI
        )
