import requests
import json

def get_friends(user_id):
    url = f"https://friends.roblox.com/v1/users/{user_id}/friends"
    response = requests.get(url)
    
    if response.status_code != 200:
        print("Failed to retrieve friends. Check the user ID and try again.")
        return []
    
    data = response.json()
    friends = [friend["name"] for friend in data.get("data", [])]
    return friends

def save_to_file(friends, filename="roblox_friends.txt"):
    with open(filename, "a", encoding="utf-8") as file:  # Open in append mode
        for friend in friends:
            file.write(friend + "\n")
    print(f"Saved {len(friends)} friends to {filename}")

def main():
    user_id = input("⚠️ Enter the Roblox user ID: ")
    friends = get_friends(user_id)
    if friends:
        save_to_file(friends)
    else:
        print("No friends found or failed to retrieve data.")
    input("🛑 Press Enter to exit 🛑")

if __name__ == "__main__":
    main()
