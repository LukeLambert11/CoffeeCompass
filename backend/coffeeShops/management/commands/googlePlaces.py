import requests

#API_KEY =
endpoint_url = "https://places.googleapis.com/v1/places:searchNearby"

# Define the payload as a dictionary
payload = {
    "includedTypes": ["coffee_shop"],
    "maxResultCount": 20,
    "locationRestriction": {
        "circle": {
            "center": {
                "latitude": 36.155060,
                "longitude": -95.984470
            },
            "radius": 50000.0
        }
    },
    "rankPreference": "DISTANCE"

}

# Define the headers
headers = {
    "Content-Type": "application/json",
    "X-Goog-Api-Key": API_KEY,
    "X-Goog-FieldMask": "*"
}

# Make the POST request
response = requests.post(endpoint_url, json=payload, headers=headers)

# Check the response status code
if response.status_code == 200:
    # Parse the response JSON
    results = response.json()
    for place in results.get('places', []):
        # print(f"Name: {place.get('displayName')}")
        # print(f"Address: {place.get('formattedAddress')}")
        # print(f"Types: {', '.join(place.get('types', []))}")
        # print(f"Website: {place.get('websiteUri')}")
        # print('---')
        print(place)
        print("______________")
else:
    print(f"Error: {response.status_code}, {response.text}")