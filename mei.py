import random, os

os.system('clear')
os.system('figlet -f smslant "NYe-NYe "')
kontol="Result : "+input("STRING: ")
memek = {'a':'i','e':'i','u':'i','o':'i','A':'i','E':'i','U':'i','O':'i'}
for x,y in memek.items():
   kontol = kontol.replace(x,y)
#print(a)

print(f"\n{kontol}")
