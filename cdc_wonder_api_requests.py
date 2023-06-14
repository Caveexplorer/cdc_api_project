import requests

# Load the XML file
with open('req.xml', 'r') as file:
    xml_data = file.read()

# Set the URL for the database you are querying
url = 'https://wonder.cdc.gov/controller/datarequest/D76'  # Replace 'D76' with your database ID if different

# Send the POST request
response = requests.post(url, data={'request_xml': xml_data, 'accept_datause_restrictions': 'true'})

# Check the response
if response.status_code == 200:
    print('Request successful')
    # print('Response XML: ', response.text)
    with open('response.xml', 'w') as file:
        file.write(response.text)
else:
    print('Request failed. Status code: ', response.status_code)

print(response)