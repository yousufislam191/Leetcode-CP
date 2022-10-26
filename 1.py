# ip = str(input())
# regex =

# import re
# address = str(input())
# pat = re.compile(
#     "^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$")
# test = pat.match(address)
# if test:
#     print('\"'+address.replace(".", "[.]")+'\"')
# else:
#     print("Unacceptable ip address")


import re
address = str(input())
pat = re.compile(
    "^([\"])(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])([\"])$")
test = pat.match(address)
if test:
    print(address.replace(".", "[.]"))
else:
    print("Unacceptable ip address")
