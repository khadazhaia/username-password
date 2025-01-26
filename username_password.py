import re

# Print statement, Initialize any needed variables

print('''To sign up, enter a username and password.
      
The username must start with a lowercase letter, and only contain letters, numbers, and underscores.
      
The passowrd must be at least 8 characters long, contain at least one uppercase letter, contain at least one lowercase letter, contain at least one digit, contain at least one special character: !,?,@,#,$,^,&,*,_,-, and not have any spaces.\n''')

username, password = " ", " "

reprompt_username, reprompt_password = " ", " "

taken_username = ["admin", "admin123", "superuser", "superuser123"]

error_message = ["Username Taken.", "Invalid Username.", "Invalid Password.", "Incorrect Username or Password."]

special_character = ["!", "?", "@", "#", "$", "^", "&", "*", "_", "-"]

# Get username and password from user. Compare user entries with system username and password. Do they match? 
   # Initialize loop to prompt user, Not a taken username, Give error messages

while True:
   username = input("Username: ")
   username = username.strip()

   password = input("Password: ")
   password = password.strip()
  
   if username not in taken_username:
       pass
   else:
       print(error_message[0],"\n")
       continue
   
# Incorrect username or password  
   # Testing Username: starts with a lowercase letter and only contain letters, numbers and underscore 

   if username[0].islower() and username.isidentifier():
       pass
   else:
       print(error_message[1],"\n")
       continue

   # Testing password: at least 8 characters long, contain at least one uppercase letter, contain at least one lowercase letter, contain at least one digit, contain at least one special character, and not have any spaces

   if (len(password) >= 8) and (any(p.isupper() for p in password)) and (any(p.islower() for p in password)) and (re.search(r'\d', password)) and ([p for p in password if p in special_character]) and (not re.search(r'\s', password)):
       print("Sign up Successful.\n")
       break
   else:
       print(error_message[2],"\n")
       continue
          
# Login Successful! 
   # Handling Successful Login: Reprompt user

print("Please log in, using your username and password.\n")
while True:
   reprompt_username = input("Username: ")
   reprompt_username = reprompt_username.strip()
   
   reprompt_password = input("Password: ")
   reprompt_password = reprompt_password.strip()
   
   if (username == reprompt_username) and (password == reprompt_password):
        print(f"Login Successful.")
        break
   else:
        print(error_message[3],"\n")
        continue
 

