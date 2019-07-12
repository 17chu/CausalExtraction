file = open('SemevalTrain.txt', 'r+')

nfile = open('data.txt','w')

#nfile.write('<data>\n')
"""x = file.read()
print(x)
"""
#"""
#METHOD1
for line in file:
    x = line.strip() #extractline
    #check line for number
    if x.find('\t') != -1: ##if you find tab, this is a dataline
        xlist = x.split('\t')
        #split on tab
        #print(xlist[1])
        #xlist[1] is the sentence after the tab, raw data we want
        a = xlist[1].replace('<e1>','').replace('</e1>','').replace('<e2>','').replace('</e2>','')
        nfile.write(a) ##writeline to file
    elif (x.find('Comment:') != -1 or line == "\n"):
        continue
    elif (x.find('Cause-Effect') != -1):
        #print('1\n')
        nfile.write('\t1\n')
    else:
        #print('0\n')
        nfile.write('\t0\n')
    
    #print(x)
    
#"""
#METHOD2
"""
ml = file.readline()
while ml != "":
    ml = file.readline()
    print(ml)
"""
file.close()
nfile.close()