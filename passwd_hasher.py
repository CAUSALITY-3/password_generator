# y=[]
# z=[]
h='''~`{[}]|!()_-+=\:;"@#$%^&*'<,>.?/qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM012345678901234567890123456789'''

k='''~`! @#$%^&*()_-+={[}]|\:;"'<,>.?/'''
l="abcdefghijklmnopqrstuvwxyz"
m="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
n="0123456789"
print(f"k= {len(k)}")

# try:
#    site = input("pass hasher ; ")
#    if site == "":
#     print("type anything that you remember")

while True:
   try:

      site=input("pass hasher ; ")
      if site!='':
         break
      print("enter a valid value")


   except Exception as e:
    print(e)

n=0
for i in site:
   n+=ord(i)
   print(n)
print(str(n)[-1:-7:-1])
x=str(ord(chr(int(str(n)[-1:-7:-1])))**(.18))
if float(x)<=1:
   
   x=str(ord(chr(int(str(n))))**(.18))
print(f"x= {x}")
y=(x[2:10])
print(f"y=  {y}")
# print(len(h))
ad=0
pss=""
s=0
# kl=0
for i in y:
   print(f"s= {s}")
   # if s>:
   #    s=0
   kl=int(i) + 9 
   ad=(s+kl)
   print(f"ad= {ad}")
   if ad>113:
      ad=0
   pss+=h[ad]
   print(pss)
   s+=kl
print(len(pss))
print(pss[7])
print(f"type == {type(pss)}")

# p=x[-1:-9:-1]
# print(p[7])
# print(f"type p == {type(p)}")
# pwd=""
# z=0
# for i in p:
#    i=int(i)
#    if len(pss)==1 | len(pss) == 2:
#       i=int(0)
#    elif (len(pss)-1)<int(i):
#       i=int(abs(int(i)-int(i)%len(pss)-int(i)//len(pss)))
#       print(type(i))
   

#    pwd[z]=list(pss[int(i)])
#    pss.replace(pss[i],'')
#    z+=1
# print(pwd)





# lis="29457367"
# print(pss[int(lis[0])])






# e=""  
# for i in str(sorted(pss)):
#    e+=str(i)
# print(e)



# y= str(int(x*10**8))
# print(y[5])
# x=1
# for i in site:
#    if x<10000000:
   
#       x*=ord(i)
# # if x<100000000:











# for i in x:
# j="5"
# print(ord(j+"3"))
# for i in range(65,91):
#     j=(j)+chr(i)
# print(j)


#     y.append(ord(i))
# print(sorted(x))
# # print(chr(32))
# a=32,48
# b=48,58  #int
# c=58,65
# d=65,91  #caps
# e=91,97
# f=97,123  #small
# g=123,127

# lis=[a,b,c,d,e,f,g]
# for i in lis:
#     for j in range(lis[1][0],lis[1][1]):
#      print(f"{j}={chr(j)}")


