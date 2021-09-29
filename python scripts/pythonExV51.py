import random
import string

list_of_domains = ['supersqa.com','gmail.com','outlook.com','yahoo.com','msn.com']

emails=[]

for i in list_of_domains:
    for j in range(20):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for k in range(5))
        email=random_string+"@"+i
        emails.append(email)
print(len(emails))
#print(emails)

with open("v51.csv", 'w') as f:
    for i in emails:
        f.write(i)
        f.write("\n")

emails1=[]
letters = string.ascii_lowercase

# print((emails1))

with open("v52.csv", 'w') as f:
    for i in range(100):
        random_string = ''.join(random.choice(letters) for x in range(5))
        email = random.choice(list_of_domains)
        emails1 =f'{random_string}@{email}'

        f.write((emails1+',\n'))
        #f.write("\n")