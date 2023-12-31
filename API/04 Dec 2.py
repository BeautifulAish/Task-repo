import requests
import pytest
response_body = requests.get("https://restful-booker.herokuapp.com/booking/3899")
print(response_body.text)
print(response_body.headers)


# Assertions -- To verify ER with Actual Result
# Stactus code ER - 200
# AR - 200
# if id = 2020 doesn't exist
# AR- 404 - ER - 404

def main():


    PASS

response_body = requests.get("https://restful-booker.herokuapp.com/booking/428")
assert response_body.status_code == 200
# If SC != 200 give error, else it will not give error

if __name__ == "__main__":
    main()
