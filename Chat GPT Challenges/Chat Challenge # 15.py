# 15
# API Integration Challenge:
# Fetch and display information about a specific user from the JSONPlaceholder API.

 # api
import requests

def main():

    # Fetch user data
    response = requests.get("https://jsonplaceholder.typicode.com/users/1")
    user = response.json()

    # Display user data
    print(f"Name: {user['name']}")
    print(f"Username: {user['username']}")
    print(f"Email: {user['email']}")
    print(f"Phone: {user['phone']}")
    print(f"Website: {user['website']}")

if __name__ == "__main__":
    main()
