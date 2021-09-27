import pytest

from mywebsite import create_app
from mywebsite.config import config


@pytest.fixture
def flask_client():
    app = create_app(config['dev'])

    # use in-memory database
    app.config["TESTING"] = True

    client = app.test_client()

    with app.app_context():
        yield client
