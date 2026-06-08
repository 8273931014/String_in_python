letter = '''
Dear <|Name|>,
You are selected!
<|Date|>
'''

name = input("Enter Your Name : ")
date = input("Enter the date")

print(letter.replace("<|Name|>",name).replace("<|Date|>",date))