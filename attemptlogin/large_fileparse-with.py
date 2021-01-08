#!/usr/bin/python3

# parse keystone.common.wsgi and return number of failed login attempts
loginfail = 0 # counter for fails
loginsucess = 0 # counter for fails
# open the file for reading
with open("/home/student/mycode/attemptlogin/keystone.common.wsgi") as kfile:

    # loop over the file
    for line in kfile:
        # if this 'fail pattern' appears in the line...
        if "- - - - -] Authorization failed" in line:
            loginfail += 1
        elif "-] Authorization failed" in line:
            loginsucess += 1

print("the number of sucess log in attempts is", loginsucess)
print("the number of fail log in attempts is", loginfail)
