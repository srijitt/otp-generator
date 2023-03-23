import random
import math

digits= '0123456789'

otp= ''
for i in range(0,4):
    otp+=digits[math.floor(random.random()*10)]

print(otp)