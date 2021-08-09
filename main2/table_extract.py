



# with open(r'output3_grayscale.txt','r') as file:
#     txt = file.read()


def clean_extract(txt):

    from fuzzywuzzy import fuzz
    Txt = txt.split('\n')
    # Cleaning the text
    bad_chars = ['=','\n','|\n','|','~~','_ ï¿½\n','-','ï¿½','_ ï¿½','\x0c','�','?','#','$',';','~','!','\\','""','(',')','“','|','[',']']

    clean = []
    for t in Txt:
        for i in bad_chars :
            t = t.replace(i,'')
        clean.append(t)

    # #print(clean)


    # Extracting the headings
    to_find = 'Description Qty Rate Amount'


    # highest = process.extractOne(to_find,clean)
    # print(highest)


    index  = 0
    for t in clean:
        if (fuzz.token_set_ratio(to_find.lower(),t.lower())) > 80:
            index = clean.index(t)

    ending = int(input("Enter the number of rows in the table"))
    op = []
    for i in range(index,(index+ending+1)):
        op.append(clean[i])

     
    return op
    # with open('something.txt','w') as file:
    #     for st in op:
    #         file.writelines(st+'\n') 
    # # header = op.pop(0)
# clean_extract(txt)