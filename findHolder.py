def findHolder(n,time):
      forward=True
      person=1

      while time>0:
            if forward:
                person+=1
                if person==n:
                     forward=False
            else:
                person-=1
                if person==1:
                    forward=True

                time-=1

            return person
n=4
time=5
print(findHolder(n,time))
#output : 2


           