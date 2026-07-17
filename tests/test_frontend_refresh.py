from pathlib import Path


def test_signup_refreshes_activity_list_after_success():
    app_js_path = Path(__file__).resolve().parents[1] / "src/static/app.js"
    app_js = app_js_path.read_text()

    assert "activitySelect.innerHTML" in app_js
    assert "signupForm.reset();" in app_js
    assert "fetchActivities();" in app_js
