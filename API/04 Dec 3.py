import requests


def main():
    response_body = requests.get("https://restful-booker.herokuapp.com/booking/2914")
    assert response_body.status_code == 200


# If SC != 200 give error, else it will not give error

if __name__ == "__main__":
  main()
