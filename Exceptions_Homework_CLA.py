#Read the following code and change it so that it treats 
# the possible exceptions that might arise.

a = 12
s = "hello"
try:
    print(a+s)
except TypeError:
    print("can't preform such operation")
except:
    print("can't preform such operation")