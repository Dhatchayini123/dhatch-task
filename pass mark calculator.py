mark=input("enter the students marks:")
R=mark.split(',')
result=[]
for i in R:
    if int(i)>35:
        result.append("pass")
    else:
        result.append("fail")

print(",".join(result))