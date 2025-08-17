import requests



def make_http_request(url):
    try:
        response = requests.get(url)
        print(f"Request to {url} successful")
        print(f"Status Code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Error making request to {url}: {e}")


input_value = "https://" + input("What is the url?")
make_http_request(input_value)