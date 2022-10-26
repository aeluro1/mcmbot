import requests

def main():
    auth = {"Username": "john924xps@gmail.com", "Password": "mcmapitest"}
    response = -1
    try:
        response = requests.post("https://api.mcmaster.com/v1/login", json = auth)
    except requests.exceptions.RequestException as err:
        print(err)
    print(response)
    

if __name__ == "__main__":
    main()