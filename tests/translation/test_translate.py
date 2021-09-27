from flask import url_for


def test_translate_word(flask_client):
    r = flask_client.post(
        url_for("app2.home"),
        data={
            "word": "abandoned industrial site",
        },
        follow_redirects=True
    )
    assert r.status == "200 OK"
