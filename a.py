import random
def get_int(msg,minimum,default):
    while True:
        try:
            line=input(msg)
            if not line and dafault is not None:
                return dafault
            i=int (line)
            if i<minimum:
                print ('must be >=',minimum)
            else:
                return i
        except ValueError as err:
            print(err)

rows=get_int('rows:',1,None)
columns=get_int('columns:',1,None)
minimum=get_int('minimum(on enter for 0):',-10000,0)

default=1000
if default<minimum:
    default=2*minimum
maximum=get_int('maximum(or enter for'+str(default)+'):',minimum,default)

row=0
while row<rows:
    line=''
    column=0
    while column<columns:
        i=random.randint(minimum,maximum)
        s=str(i)
        while len(s)<10:
            s=" "+s
        line+=s
        column+=1
    print(line)
    row+=1
