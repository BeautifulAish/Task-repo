# API
# Request library
import requests

# Make GET,POST,PUT,PATCH AND DELETE and Verify
# HTTP Methods

def main():
    # GET - Need Url and method
    response_body = requests.get("https://restful-booker.herokuapp.com/booking/428")
    print(response_body.text)
    print(response_body.status_code)
    print(response_body.json())
    if response_body.status_code  == 200:
        print("TC#1 - GET request is successfully")

    else:
           print("TC#1 - GET request is not successfully")


if __name__ == "__main__":
    main()
# To make an API request     Req
# Url,Auth,headers,Cookies,data (payload), json file

#Validate in API testing
# Response,headers, statuscode,responsetime,JSON,Schema validation