import json
d = ['MFR', 'QTY', 'FREE', 'DESCRIPTION', 'PKG', 'BATCH', 'EXP.', 'HSN', 'MRPs', 'RATE', 
'DIS%', 'VALUE', 'GST%', 'GST AMT.']
org = ['MFR', 'QTY', 'FREE', 'DESCRIPTION', 'PKG', 'BATCH', 'EXP.', 'HSN', 'MRPs', 'RATE', 
'DIS%', 'VALUE', 'GST%', 'GST AMT.']
op = ['MFR QTY  FREE  DESCRIPTION PKG BATCH  EXP.  HSN mrp  RATE pis%  vatue  est%  esr AMT',
 'GENER Il 0070  ABDOMINAL MOPS 11Xi—   TXT f74 ‘eri 3008 az a 24.68 0.0  2468.00 12.00 oad',
 'i SCHEM  3. 0 ACCUCHECK ACTIVE 100s 100s 24692131 03/20. 38220019  1,480.00 200 0.0 3600.00  12.00  432.00',
 'EQMWwOcK  25  0  DEX 5% 540ML  540ML 8A90270 06/21.  30049099  t 28.49 22.42  0.0  560.50  12.00 6726',
 'ty SCHEM 40 io 0  DEXONA INJ 2ML  2ML CHU1022 01/20.  30043913 5.98. 4.27 0.0 170.80  12.00 20.50 ',
 'WOCK  1% ll 0  540ML  540ML 8B90880  09/21  30049099 32.26 22.42  0.0 403.56  12.00 48.42 ',
 'apa CADIL 10% 0 GLOBACZ LIQUID 200ML 200ML cui 02/20  30045020 129.50/ 92.50 0.0 925.00 12.00 111.0 ',
 'WOCK 50 0  NS 540ML  540ML pene 11/21 30049099  29.44 22.42  0.0  1121.00  12.00 13852',
 'dOWwOCK 50 0.  RLS40ML 540ML 8D91104. 10/21  30049099 47.69 29.50 0.0 1475.00 12.00  177.00 .',
 ' CENTU 97 0  SINAREST DROP 15ML 15ML_ SBL1810. 10/21 3008  64.98. 46.42 0.0  417.78  12.00 50.14}',
 'CENTU 10 4 .@  SINAREST SYP 100ML 100ML SGL18109 09/21.  3004  82.82 59.16  0.0 591.60  12.00 71.00,',
 'a  GENER 25 0  SODIUM CHLORIDE NS 100ML 100ML 2818110  10/20. 30049099  17.00 11.25 0.0  281.25  12.00 3376',
 ' ALKEM  50 40.  TAXIM 1GM VAIL  VAIL 8184364  04/21 ons  36.06 25.76, 0.0  1288.00 12.00  154.56',
 '  CIPLA © 207 0  VOMISTOP TAB 10s  10s GI8VSA002” 03/20  30049039 ," 25.33 pana s. fit" 00:0  362.20  12.00  43.46',
 'GENER 10  Q  ZEEBEE ORAL SUSP 10ML.  10ML SHT0831  09/20,  30049099  16.70.  12.02 0.0 120.20  12.00  14.42',
 'GENER 25 0  DOMPY SUS 30ml.  30ml bees  06/20. 3004 S58 22.51 0.0  562.75  12.00 67.54']
def listToString(s): 
    str1 = " " 
    return (str1.join(s))

def rev_sentence(sentence): 
  
    words = sentence.split(' ') 
    reverse_sentence = ' '.join(reversed(words)) 
    return reverse_sentence 

for i in range(len(op)):
    h=op[i]
    h=h.replace("  "," ")
    a=h.split(" ")
    a = [string for string in a if string != ""]

    a.reverse()
    #rint(d)
    #print(a)

    n=len(d)
    m=len(a)
    i=0
    while i<m:
        if i==0:
            org[n-1]=a[i]
            i=i+1
        elif i==10:
            p=[]
            j=i
            while j<m:
                if a[j].isdigit():
                    j=j+1
                    break
                else:
                    p.append(a[j])
                    j=j+1
            #print(len(p))
            k=len(p)
            y=listToString(p)
            w=rev_sentence(y)
            #print(w)
            
            org[n-i-1]=w
            #print(org)
            #print(i)
            i=i+len(p)
        elif i>10:
            org[n-i+1]=a[i]
            i=i+1
        else:
            org[n-i-1] = a[i]
            i=i+1
    #print(org)

    dict_from_list = dict(zip(d, org))
    #print(dict_from_list)
    json_object = json.dumps(dict_from_list, indent = 4)  
    print(json_object)