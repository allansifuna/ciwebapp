import pytest

from mywebsite import create_app


@pytest.fixture
def flask_client():
    app = create_app()

    # use in-memory database
    app.config["TESTING"] = True

    client = app.test_client()

    with app.app_context():
        yield client
