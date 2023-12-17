import string

password = "sjhwaAHG%%&@232jADF123@#$"  # input

"it checks for each character in password if it present then 1 else 0"
upper_case = any([1 if c in string.ascii_uppercase else 0 for c in password])
lower_case = any([1 if c in string.ascii_lowercase else 0 for c in password])
special = any([1 if c in string.punctuation else 0 for c in password])
digits = any([1 if c in string.digits else 0 for c in password])

characters = [upper_case, lower_case, special, digits]
length = len(password)

score = 0

"it will open the file and checks the password"
with open('common.txt', 'r') as f:
    common = f.read().splitlines()

if password in common:
    print("Password found in the Data Breach Score=0")
    exit()

if length > 8:
    score += 1
if length > 12:
    score += 1
if length > 14:
    score += 1
if length > 17:
    score += 1
if length > 20:
    score += 1

"it will show the password length"
print(f"Password Length is {str(length)}, adding {str(score)} points!")

if sum(characters) > 1:
    score += 1
if sum(characters) > 2:
    score += 1
if sum(characters) > 3:
    score += 1

print(f"Password has {str(sum(characters))} different character type, adding {str(sum(characters) - 1)} points!")

if score < 4:
    print(f"Your password is weak Score: {str(score)}")
elif score == 4:
    print(f"The password is medium Score: {str(score)} points ")
elif 4 <= score < 6:
    print(f"The password is Pretty Good Score: {str(score)} points ")
elif score > 6:
    print(f"The password is strong Score: {str(score)} points ")
