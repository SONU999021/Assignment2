# 'a' -------> 5 times

# #counter variable
# while (test expr.)
#     statement
#     increment / decrement


# #counter variable


x='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ@0123456789'
#signup form
while True:
    username=input('Enter Username: ')
    password=input('Enter your password: ')

    if not password:
        print('Password cannot be empty')
        continue

    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special= '@' in password or '#' in password
    
    

    # if has_upper and has_lower and has_digit >= 3:
    if has_upper and has_lower and has_digit and has_special<=3:
        print(
        'You have successfully signup'
    ) 
        break
    else:
        print('Choose password one uppercase,@, one lower case and atlese 3 number ')

#login form
# 
while True:
    username1=input('Enter login username: ')
    password1=input('Enter your login password: ')
    if username1==username and password1==password:
        print('You have successfully login')
        break

    else:
        print('Try Again!')
