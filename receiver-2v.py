import os
import requests

def download_file(url, save_path):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            with open(save_path, 'wb') as file:
                file.write(response.content)
            print(f"File downloaded successfully and saved as {save_path}")
        else:
            print(f"Error downloading file from {url}. Status code: {response.status_code}")
    except Exception as e:
        print(f"An error occurred while downloading {url}: {e}")

def display_file_urls(file_urls):
    for i, url in enumerate(file_urls, start=1):
        print(f"{i}. {url}")

def get_user_selection():
    try:
        selection = input("Enter the number(s) of the file(s) you want to download (comma-separated): ")
        selected_numbers = [int(num.strip()) for num in selection.split(",")]
        return selected_numbers
    except ValueError:
        print("Invalid input. Please enter valid numbers separated by commas.")
        return get_user_selection()

# List of file URLs
file_urls = [
    "https://catfish-relaxing-supposedly.ngrok-free.app/web-dd/eco-tourist.html",
    "https://catfish-relaxing-supposedly.ngrok-free.app/web-dd/destinations.html",
    "https://catfish-relaxing-supposedly.ngrok-free.app/web-dd/t-combine.png",
    "https://catfish-relaxing-supposedly.ngrok-free.app/web-dd/t1.png",
    "https://catfish-relaxing-supposedly.ngrok-free.app/web-dd/t2.png",
    "https://catfish-relaxing-supposedly.ngrok-free.app/web-dd/t3.png",
    "https://catfish-relaxing-supposedly.ngrok-free.app/web-dd/t1.mp4",
    "https://catfish-relaxing-supposedly.ngrok-free.app/web-dd/t2.mp4",
    "https://catfish-relaxing-supposedly.ngrok-free.app/web-dd/t3.mp4"
]

# Specify the local directory where you want to save the files
local_directory = "home-server-v2"

# Create the directory if it doesn't exist
os.makedirs(local_directory, exist_ok=True)

# Display file URLs and get user selection
display_file_urls(file_urls)
user_selection = get_user_selection()

# Download selected files
for num in user_selection:
    if 1 <= num <= len(file_urls):
        url = file_urls[num - 1]
        filename = os.path.basename(url)
        local_path = os.path.join(local_directory, filename)
        download_file(url, local_path)
    else:
        print(f"Invalid selection: {num}. Please choose a valid number.")
