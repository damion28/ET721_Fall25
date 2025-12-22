import pytest
from app import create_app
from app.models import db, Fruit

@pytest.fixture
def app():
    """
    Create and configure a new app instance for each test.
    """
    app = create_app({"TESTING": True, "SQLALCHEMY_DATABASE_URI": "sqlite:///:memory:"})
    with app.app_context():
        db.create_all()
        # Add initial fruits
        fruits = [
            Fruit(name="Apple", quantity=10, variety="Gala", season="Winter"),
            Fruit(name="Banana", quantity=20, variety="Cavendish", season="All"),
        ]
        db.session.bulk_save_objects(fruits)
        db.session.commit()
    yield app

@pytest.fixture
def client(app):
    """
    Provide a Flask test client for the tests.
    """
    return app.test_client()

def test_get_all_fruits(client):
    response = client.get('/api/fruits')
    data = response.get_json()
    assert response.status_code == 200
    assert len(data) == 2
    assert data[0]['name'] == 'Apple'

def test_add_fruit(client):
    new_fruit = {"name": "Orange", "quantity": 5, "variety": "Navel", "season": "Winter"}
    response = client.post('/api/fruits', json=new_fruit)
    data = response.get_json()
    assert response.status_code == 201
    assert data['message'] == 'Fruit added successfully'
    assert 'id' in data

def test_get_fruit_by_name(client):
    response = client.get('/api/fruits/Apple')  # match API route
    data = response.get_json()
    assert response.status_code == 200
    assert data["name"] == "Apple"
    assert data["quantity"] == 10

def test_get_nonexistent_fruit(client):
    response = client.get('/api/fruits/Pear')  # match API route
    data = response.get_json()
    assert response.status_code == 404
    assert "error" in data
