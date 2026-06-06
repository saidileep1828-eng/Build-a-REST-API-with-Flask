# Flask REST API

## Objective
Build a REST API to manage user data using Flask.

## Features
- GET all users
- GET single user
- POST new user
- PUT update user
- DELETE user

## Tools Used
- Python
- Flask
- Postman

## Run
```bash
pip install -r requirements.txt
python app.py
```

## Endpoints
- `GET /users` - list all users
- `GET /users/<user_id>` - get one user
- `POST /users` - create a user
- `PUT /users/<user_id>` - update a user
- `DELETE /users/<user_id>` - delete a user

## Example Request Body
```json
{
  "name": "David",
  "age": 28
}
```

## Notes
This implementation uses an in-memory dictionary and is suitable for learning and testing.
