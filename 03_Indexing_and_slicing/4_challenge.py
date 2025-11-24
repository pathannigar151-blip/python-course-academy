# Input an email address
email = input("Enter Your Email: ")

# Username before '@'
username = email.split('@')[0]

# Remove first and last character of username
trimmed = username[1:-1]

# Print both
print("Original username:", username)
print("Trimmed username:", trimmed)
