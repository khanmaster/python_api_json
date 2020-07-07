import requests
import json
post_codes_req = requests.get("https://api.postcodes.io/postcodes/se120nb")
# print(post_codes_req.status_code)
# print(post_codes_req.content)
# print(type(post_codes_req.content))
# print(post_codes_req.headers)
# print(type(post_codes_req.headers))

#print(post_codes_req.json())

json_data = post_codes_req.json()
# storing data from json()
print(type(json_data))

for key in json_data:
    print(key)

print(json_data)












# # Why should we use built in packages
# # first iteration
# if post_codes_req.status_code == 200:
#     print(" success ")
# elif post_codes_req.status_code == 404:
#     print(" Sorry page available ")

# Second iteration
# Why should we use built in packages/modules
# #
# if post_codes_req.status_code:
#     print(" success ")
# elif post_codes_req.status_code:
#       print(" Sorry page available ")


# 3rd iteration create same functionality with OOP - class and a
# create a method called check_status_code():
# create a class live_web_status_code:
# out put should be the same as we achieved without OOP.




# class Live_Web_Status:
#
#     def check_web_status(self):
#         if post_codes_req.status_code:
#             return " success "
#         elif post_codes_req.status_code:
#             return " Sorry page available "

# web_status_code = Live_Web_Status()

# print(web_status_code.check_web_status())

#
# print(post_codes_req.headers)
# print(post_codes_req.content)
# print(post_codes_req.json())
# type_json = post_codes_req.json()
# print(type(type_json))

# for key in type_json:
  #  if requests.status_codes:
   #  print(str(post_codes_req.status_code) + " current status code with live " + key)
