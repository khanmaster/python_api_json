import requests

response_bcc = requests.get("https://api.postcodes.io/postcodes/se120nb")

# def check_response_code():
#
#     if response_bcc:
#         return "Response successful"
#     elif response_bcc:
#          return " Sorry page not found"
#     else:
#           return "Opps some went wrong"
#
# print(check_response_code())

path = 'http://api.postcodes.io/postcodes/'
arguments = 'e147le'

url_target = path + arguments
print(url_target)

# # Make request and capture response
response = requests.get(url_target)
#
print(response)
print(type(response))

# Parsing or getting the dictionary out
print(response.json())
response_dictionary = response.json()

print(type(response_dictionary))

# for key in response_dictionary.keys():
#     print(key)

result_dictionary = response_dictionary['result']

print(result_dictionary)

for key in result_dictionary.keys():
    print(key, 'the value inside is', result_dictionary[key])