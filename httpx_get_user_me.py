import httpx


login_payload = {
    "email": "user998@example.com",
    "password": "string"
}

login_response = httpx.post("http://localhost:8000/api/v1/authentication/login", json=login_payload)
login_response_data = login_response.json()

token = {
    "Authorization": f"Bearer {login_response_data['token']['accessToken']}"
}


user_response = httpx.get("http://localhost:8000/api/v1/users/me", headers=token )
user_data = user_response.json()

print("User response:", user_data)
print("Status Code:", user_response.status_code)