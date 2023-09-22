import pytest
import requests

# Define the base URL for the Pet Store API
BASE_URL = "https://petstore.swagger.io/v2"


# Test case 1: Get "available" pets and assert expected result
def test_get_available_pets():
    response = requests.get(f"{BASE_URL}/pet/findByStatus?status=available")
    assert response.status_code == 200
    pets = response.json()
    assert all(pet['status'] == 'available' for pet in pets)


# Test case 2: Post a new available pet and assert new pet added
def test_post_new_available_pet():
    new_pet_data = {
        "id": 12345,  # Replace with a unique ID
        "name": "NewPet",
        "status": "available"
    }
    response = requests.post(f"{BASE_URL}/pet", json=new_pet_data)
    assert response.status_code == 200

    # Check if the added pet exists
    response = requests.get(f"{BASE_URL}/pet/{new_pet_data['id']}")
    assert response.status_code == 200
    pet = response.json()
    assert pet['name'] == new_pet_data['name']
    assert pet['status'] == new_pet_data['status']


# Test case 3: Update the pet status to "sold" and assert status updated
def test_update_pet_status_to_sold():
    pet_id = 12345  # Replace with the ID of the pet added in test case 2
    updated_status = "sold"
    response = requests.post(
        f"{BASE_URL}/pet/{pet_id}",
        json={"status": updated_status}
    )
    assert response.status_code == 200

    # Check if the status is updated
    response = requests.get(f"{BASE_URL}/pet/{pet_id}")
    assert response.status_code == 200
    pet = response.json()
    assert pet['status'] == updated_status


# Test case 4: Delete the pet and assert deletion
def test_delete_pet():
    pet_id = 12345  # Replace with the ID of the pet added in test case 2
    response = requests.delete(f"{BASE_URL}/pet/{pet_id}")
    assert response.status_code == 200

    # Check if the pet is deleted
    response = requests.get(f"{BASE_URL}/pet/{pet_id}")
    assert response.status_code == 404  # Pet should not be found


if __name__ == "__main__":
    pytest.main()
