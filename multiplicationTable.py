class tables:
    def tables(self, nValue):
        for x in range(2, nValue + 1):
            print("/n","TABLE OF",x,"/n")
            for y in range(1,11):
                print(x,"X",y,"=",x*y)
        
nValue=int(input("Enter a value: "))       
f=tables()
f.tables(nValue)