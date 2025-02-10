import requests

# API URL
url = "https://api.ragie.ai/retrievals"

# Headers with API Key
headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer tnt_G6KCs4jcsXU_RF60y0Pak93TlvI0k7IqfEFcIlIN20r1FwigJ1Id7Ts"
}

# Query Payload
payload = {
    "query": "steps to draft a legally valid will in estate planning",
    "rerank": True,
    "filter": {"scope": "estate_planning"}
}

# Send POST request
response = requests.post(url, headers=headers, json=payload)

# Process Response
if response.status_code == 200:
    result = response.json()
    print("Retrieved Chunks:\n", result)
else:
    print(f"Error {response.status_code}: {response.text}")
