#Assertion - Using Assert
# Using Pytest library
Import pytest
def main():
Url = "https://restful-booker.herokuapp.com/booking/"
id = "163"
full_Url = Url + id
    print(full_url)
    response_body = requests.get(full_url)
    assert response_body.status_code == 200

# if status code != 200 it will give error else it will not give error
# Conversion data - json
data = response_body.json()
print(type(data))

# assertions
# Verification of keys  #Assume data is a dictionary
assert 'firstname' in data, "Incorrect firstname"
assert 'lastname' in data, "lastname key is present"

print(data)

# Verification of data
assert data["firstname"] == "Jim", "Incorrect firstname is Jim"
assert data["lastname"] == "Brown", "Incorrect lastname"
checkin_data["bookingdates"]["checkin"] == "2018-01-01", "Incorrect Message "