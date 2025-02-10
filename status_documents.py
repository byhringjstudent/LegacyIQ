import requests

# API URL and Headers
base_url = "https://api.ragie.ai/documents"
headers = {
    "Accept": "application/json",
    "Authorization": "Bearer tnt_G6KCs4jcsXU_RF60y0Pak93TlvI0k7IqfEFcIlIN20r1FwigJ1Id7Ts"
}

# List of document IDs from previous uploads
# Replace with actual IDs from previous uploads
document_ids = [
    "6246a4b5-ae74-4e31-a770-4a2d99a9877d",
    "3ecceb49-aba2-40b2-92bc-7a26e4855eb7",
    "57e3242e-87cc-481e-bb45-70fa8fa77cc7",  # Replace with actual IDs
    "98504e92-425a-4017-91fe-a371ce8d66be",
    "61bb7beb-9611-4986-a2d2-fefdbd222715"
]

# Loop through document IDs and check their status
for doc_id in document_ids:
    response = requests.get(f"{base_url}/{doc_id}", headers=headers)
    
    if response.status_code == 200:
        print(f"Document {doc_id} Status:", response.json()["status"])
    else:
        print(f"Error fetching document {doc_id}: {response.status_code} - {response.text}")
