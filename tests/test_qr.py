
def test_form_exists(client):
    rv = client.get('/')
    assert '<form action="" method="POST">'.encode() in rv.data


def test_post_to_index(client):
    rv = client.post('/', data=dict(
        ssid="FreeWifi",
        password="supersecret"
    ))
    assert rv.status_code == 200
