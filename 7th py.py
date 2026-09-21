'''1.petrol pump fuel filing
vehicles arrive one by one at a petrol station.record fuel filled for each
vechile untill the total fuel sold reaches 500 liters.'''

'''reverse=500
res=[]
while reverse>0:
    fuel=int(input('enter the fuel:'))
    reverse-=fuel
    if reverse>=0:
        res.append(fuel)
print(res)'''


'''2.hospital patient temperature check
a hospital records temperatures of patients entering the emergency ward.
stop when a patient with temperature above 104f is found and display the
patient count checked before that.'''


'''temp=int(input('enter the temp:'))
count=0
while temp<104:
    temp=int(input('enter the temp:'))
    count+=1
print(count)'''



'''3.wap to check whether number is prime or not.'''


'''n=int(input('enter the number'))
i=2
count=0
while i<n:
    if n%i==0:
        count+=1
    i+=1
if count>=1:
    print('nonprime')
else:
    print('prime')'''



'''4.website login attempt system
a user has only 3 attempts to enter the correct password.
display"access granted"if correct,othewise block the account.'''



'''psd='@Qspider123'
for i in range(3):
    pd=input('enter the password:')
    if pd==psd:
        print('access granted')
        break
    else:
        print('login failed')'''


'''5.wap to find a specified element from the list'''
'''l=[4,2,4,58,5,8,2,58,5,54]
value=int(input('enter the number:'))
for i in l:
    if i==value:
        print('found')
        break
    print('thankyou')'''


'''6.wap to print numbers from 1-30 but without multiples of 3'''


'''for i in range(1,31):
    if i%3==0:
        continue
    print(i)'''


'''7.wap to find the hcf of two numbers'''


'''n1=int(input('enter n1:'))
n1=int(input('enter n1:'))
smallest=n1 if n1<n2 else n2
for i in range(1,smallest+1):
    if n1%i==0 and n2%i==0:
        hcf=i
print(hcf)'''


































