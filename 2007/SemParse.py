file = open('relation-1-train.txt','r+')

nfile = open('data1.txt','w')

for line in file:
    x = line.split(' ')
    #print(x[0])
    #filtering process for extracting the sentence
    if x[0] == 'Comment:':
        continue
    elif x[0] == 'WordNet(e1)':
        print(x[8])
        if x[8] == '\"true\",':
            nfile.write('\t0\n')
        else:
            nfile.write('\t1\n')
    elif x[0] == '\n':
        continue
    else:
        y = line.split(' ',1)
        #print(y[0])
        nfile.write(y[1].strip().replace('<e1>','').replace('</e1>','').replace('<e2>',' ').replace('</e2>',''))
nfile.close()
file.close()