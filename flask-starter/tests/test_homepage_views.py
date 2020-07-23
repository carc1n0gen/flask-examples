

def test_index_should_return_200(client):
    rv = client.get('/')
    assert rv.status_code == 200


def test_about_should_return_200(client):
    rv = client.get('/about')
    assert rv.status_code == 200
