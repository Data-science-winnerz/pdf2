
def head_extract2(a):
    original_contents = ['MFR','QTY','FREE','DESCRIPTION','PKG','BATCH','EXP.',
    'HSN','MRPs','RATE','DIS%','VALUE','GST%', 'GST AMT.']


    # a = 'MFR QTY  FREE DESCRIPTION  PKG BATCH EXP.  HSN MRPs RATE DIS % VALUE  GST%  GST AMT.'
    s = a.split(" ")
    c=[]

    d = []
    for string in s:
        if (string != ""):
            d.append(string)

    #print(d)
    '''Here I have joined it like this 
     but u check the special character if it is present 
     append it with the before elem'''
    d[10 : 12] = [''.join(d[10 : 12])]
    #print(d)


    for i in range(len(d)-1):
        if d[i] not in original_contents:
            q=d[i]+" "+d[i+1]
            if q not in original_contents:
                q=q+" "+d[i+2]
                if q not in original_contents:
                    q=q+" "+d[i+3]
                else:
                    c.append(q)
            else:
                c.append(q)
        else:
            c.append(d[i])
    return c


