
**DEMO PET STORE**



For these automated basic CRUD the used page is [Swagger Pet Store](https://petstore.swagger.io/v2). Using Python and pytest, 
you'll need to use the `requests` library to send HTTP requests and pytest 
for test assertions. Make sure you have both libraries installed 
(`requests` and `pytest`) before running the tests. 
You can install them using `pip` if you haven't already:


```bash
pip install requests pytest
```

Please note the following:

1. Replace the `id` value in `test_post_new_available_pet` with a unique ID.
2. In `test_update_pet_status_to_sold` and `test_delete_pet`, you need to specify the pet ID you want to update and delete. Make sure it matches the ID used in `test_post_new_available_pet`.

To run these tests, save the code to a Python file (e.g., `test_pet_store.py`) and run it using `pytest`:

```bash
pytest test_pet_store.py
```
