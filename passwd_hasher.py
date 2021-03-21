# Letters, symbols and digits taken
h='''~`{[}]|!()_-+=\:;"@#$%^&*'<,>.?/qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM012345678901234567890123456789'''


# Taking input from user
while True:

   try:
      site=input("Enter any text to hash : ")
      if site!='':
         break
      print("enter a valid value")

   except Exception as e:
    print(e)



# Hashing algorithm
n=0
for i in site:
   n+=ord(i)
x=str(ord(chr(int(str(n)[-1:-7:-1])))**(.18))

if float(x)<=1:  
   x=str(ord(chr(int(str(n))))**(.18))
y=(x[2:10])
ad=0
pss=""
s=0
for i in y:
   kl=int(i) + 9 
   ad=(s+kl)
   if ad>113:
      ad=0
   pss+=h[ad]
   s+=kl

print(f"Your hashed password : {pss}")


