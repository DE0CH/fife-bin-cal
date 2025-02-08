import argparse
import requests
import json

def main(postcode, address):
    authorization = get_authorization()
    addresses = get_addresses(postcode, authorization)
    address_object = find_value_by_label(addresses, address)
    uprn = get_uprn(address_object, authorization)
    return get_calendar(uprn, authorization)


def get_addresses(postcode, authorization):
    url = 'https://www.fife.gov.uk/api/widget'
    params = {
        "action": "propertysearch",
        "actionedby": "ps_3SHSN93",
        "loadform": "true",
        "access": "citizen",
        "locale": "en"
    }
    
    headers = {
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "Authorization": authorization,
        "Content-Type": "application/json"
    }

    payload = {
        "name": "bin_calendar",
        "data": {
            "postcode": postcode
        },
        "email": "",
        "caseid": "",
        "xref": "",
        "xref1": "",
        "xref2": ""
    }
    
    response = requests.post(
        url,
        params=params,
        headers=headers,
        json=payload
    )

    return response.json()

def get_authorization():
    url = "https://www.fife.gov.uk/api/citizen"
    
    # The same query parameters: preview=false and locale=en
    params = {
        "preview": "false",
        "locale": "en"
    }
    
    response = requests.get(url, params=params)
    authorization = response.headers['Authorization']
    return authorization

def get_uprn(object_id, authorization):
    url = "https://www.fife.gov.uk/api/getobjectdata"
    params = {
        "objecttype": "property",
        "objectid": object_id
    }
    headers = {
        "Accept": "*/*",
        "Authorization": authorization
    }
    
    # Perform the POST request
    response = requests.post(url, params=params, headers=headers)
    return response.json()['profileData']['property-UPRN']

def get_calendar(uprn, authorizaiton):
    url = 'https://www.fife.gov.uk/api/custom'
    
    params = {
        'action': 'powersuite_bin_calendar_collections',
        'actionedby': 'bin_calendar',
        'loadform': 'true',
        'access': 'citizen',
        'locale': 'en'
    }
    
    # Headers, including your Authorization token
    headers = {
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Authorization': authorizaiton,
        'Content-Type': 'application/json'
    }
    
    # JSON body
    payload = {
        "name": "bin_calendar",
        "data": {
            "uprn": uprn
        },
        "email": "",
        "caseid": "",
        "xref": "",
        "xref1": "",
        "xref2": ""
    }
    response = requests.post(url, params=params, headers=headers, json=payload)
    return response.json()

def find_value_by_label(data_dict, search_label):
    # Access the list of items under "data"
    items = data_dict["data"]
    
    for item in items:
        label = item["label"]
        
        if search_label in label:
            return item["value"]
    raise ValueError('Address not found')
    
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("postcode", help="The postcode of the address")
    parser.add_argument("address", help="The address (usually just the street number) to get the bin calendar for")
    args = parser.parse_args()
    print(json.dumps(main(args.postcode, args.address), indent=2))
