import requests

# API URL and Headers
url = "https://api.ragie.ai/documents"
headers = {
    "Accept": "application/json",
    "Authorization": "Bearer tnt_G6KCs4jcsXU_RF60y0Pak93TlvI0k7IqfEFcIlIN20r1FwigJ1Id7Ts"
}

# List of file paths
file_paths = [
    "C:/Users/Byhri/OneDrive/Desktop/ragie-python-ref-app/ragie-python-ref-app/documents_test/202056(b)4 Marital deduction valuation of interest passing to surviving spouse.pdf",
    "C:/Users/Byhri/OneDrive/Desktop/ragie-python-ref-app/ragie-python-ref-app/documents_test/Free Legal Services for Personal Tax and Estate Planning.pdf",
    "C:/Users/Byhri/OneDrive/Desktop/ragie-python-ref-app/ragie-python-ref-app/documents_test/THE NEW STATISTICS OF ESTATE PLANNING LIFETIME AND POST-MORTEM WILLS TRUSTS AND CHARITABLE PLANNING.pdf",
    "C:/Users/Byhri/OneDrive/Desktop/ragie-python-ref-app/ragie-python-ref-app/documents_test/Time as of which value of property is to be computed for purpose of inheritance succession or estate.pdf",
    "C:/Users/Byhri/OneDrive/Desktop/ragie-python-ref-app/ragie-python-ref-app/documents_test/Federal income tax charitable deductions property fair-market-value determinations.pdf"
]

# Loop through each file and upload separately
for file_path in file_paths:
    with open(file_path, "rb") as file:
        files = {"file": file}
        data = {"metadata": '{"scope": "estate_planning"}', "mode": "fast"}

        # Send POST request
        response = requests.post(url, headers=headers, files=files, data=data)

        # Print API response
        print(f"Uploaded {file_path}: {response.json()}")
