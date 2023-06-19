#use of break
for i in range (0,10):
    if i==3:
        break
    else:
        print(i)
print("\n")
#use of continue and for with else
for k in range (0,3):
    if k%2==1:
        continue
    else:
        print(k)
else:
    print("else part executed")
print("\n")
#use of pass and while with else
h=1
while h<=10: 
    h+=1
    for l in range(0,5):
        if i%2==0:           
            pass
        else:
            print(l)
else:
    print("else part executed")
