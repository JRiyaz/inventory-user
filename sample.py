from enum import Enum

import bcrypt

# password = "riyaz".encode()
# # Hash a password for the first time, with a randomly-generated salt
# hashed = bcrypt.hashpw(password, bcrypt.gensalt())
# print(hashed)
# # Check that an unhashed password matches one that has previously been
# # hashed
# if bcrypt.checkpw(password, hashed):
#     print("It Matches!")
# else:
#     print("It Does not Match :(")


class Season(Enum):
    SPRING = 1
    SUMMER = 2
    AUTUMN = 3
    WINTER = 4


print(Season.AUTUMN)
print(Season)
print(Season.AUTUMN.name)
print(Season.AUTUMN.value)
