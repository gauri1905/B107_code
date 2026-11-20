#what is loop
#for loop
#while loop
for i in range(1,11,2):
  print(i)

while i in range(1,11,2):
  print(i)  

for i in range(20,0,-1):
  print(i)

#write a table of 4 using for loop
for i in range(1,11):
  print(i,"x",4,"=",i*4)

#for start patten 
for i in range(1,11):
  print(i* "*")

# continue , break , nad pass  
# ccontinue
for i in range(1,16):
  if i == 9:
    continue
  print(i)

#breack
for i in range(1,16):
  if i == 9:
    break
  print(i)

#pass
for i in range(1,16):
  if i == 9:
    pass
  print(i)  

#string
#print(len(String))
#print(String[4])
String = "hello gaurii how are uhh !!!!!"
result = " "
for i in range(20):
  if String[i] == " ":
    continue
  result += String[i].upper()
  print(result)

#listt
l = ["orange", " banana", "mango", "apple"]
#for i in range(len(l)):
  #print(l[i]+ " 1kg")

for fruit in l:
  print(fruit + "1kg ")

# in while loop 
i = 1
while i < 10:
  #i += 1
  print(i)
  i += 1

password =" "
while password != "1234567":
  password = input("enter your password : ")
print(" loginn successfully......")