import requests

# Note details to be added
note = {
    "date": "2024-12-01",  # You can use today's date
    "title": "Sunday Insights",  # Title of the note
    "highlight": "Reviewed Python projects and brainstormed for new ideas."  # Brief highlight
}

# API endpoint for the Flask app
url = "http://127.0.0.1:5000/add"

# Make the POST request to add the note
try:
    response = requests.post(url, json=note)
    if response.status_code == 200:
        print("Note added successfully!")
        print("Server Response:", response.json())
    else:
        print(f"Failed to add note. Status Code: {response.status_code}")
        print("Error:", response.text)
except requests.exceptions.RequestException as e:
    print("Error connecting to the server:", e)
