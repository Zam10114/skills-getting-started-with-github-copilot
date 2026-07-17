import copy

from fastapi.testclient import TestClient

import src.app as app_module


client = TestClient(app_module.app)


def reset_activities():
    app_module.activities = {
        "Chess Club": {
            "description": "Learn strategies and compete in chess tournaments",
            "schedule": "Fridays, 3:30 PM - 5:00 PM",
            "max_participants": 12,
            "participants": ["michael@mergington.edu", "daniel@mergington.edu"],
        },
        "Programming Class": {
            "description": "Learn programming fundamentals and build software projects",
            "schedule": "Tuesdays and Thursdays, 3:30 PM - 4:30 PM",
            "max_participants": 20,
            "participants": ["emma@mergington.edu", "sophia@mergington.edu"],
        },
    }


def test_unregister_participant_removes_email_from_activity():
    reset_activities()

    signup_response = client.post(
        "/activities/Chess Club/signup?email=student@mergington.edu"
    )
    assert signup_response.status_code == 200

    delete_response = client.delete(
        "/activities/Chess Club/participants?email=student@mergington.edu"
    )

    assert delete_response.status_code == 200
    assert "student@mergington.edu" not in app_module.activities["Chess Club"]["participants"]
