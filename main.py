# List  of alphabets
lower = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', " ", ",", "."]

# List of the code of alphabets
lower_code = ['owrsdf' , 'hjconags' , 'iufrx' , 'jkaw' , 'jdfgth' , 'biuwab' , 'vtasdw' , 'edfjr' , 'lwsk' , 'djfav' , 'offdnr' , 'uhgta' , 'urhxwe' , 'jfpo' , 'ihjkpw' , 'etcv' , 'jjhkmh' , 'rhjkgi' , 'oksfd' , 'jhng' , 'akkje', 'ogihw' , 'ioenv' , 'rjioerj' , 'pqxow' , 'epfojepifo','sassdK' ,'Jhfk' ,'jsdhkf' ,'jbnjdgJ' ,'kSKj' ,'fdhka' ,'jshfksk' ,'hhoxiOU' ,'bGowje' ,'comjwp' ,'eojrcn' ,'erowie' ,'ujoij' ,'iNIJo' ,'kisjO' ,'Jofn' ,'ijewoci' ,'nCenrp' ,'owej' ,'pdASo','sdsdask','jhdflsk','kdhfl','kijefs','ksdhlfj','ksdjfl', "afhjk","jfkddf","yrgeuuf"]

#Dictionarie Formation of Code and Decode
code_dict = dict(zip(lower,lower_code))
decode_dict = dict(zip(lower_code, lower))

initial = []
i = 0 

mode = int(input("Select operation mode \nFor Code :- 1 \nFor Decode :- 2 \n"))

if mode == 1 :
    print ("Code mode selected")
elif mode == 2:
    print ("Decode mode selected")
else : 
    print("mode error")

sent = input("Enter a String :- ")

def code(se):

    for item in se:
        print(code_dict[item], end = '')
    return " "    

def decoder(main,new):
    for i in main:
        if i.startswith(sent[0:4]):
            new.append(i)

def shorting_the_list(new_list,sent,i):
    word = new_list[i]
    sent = sent.replace(word, "",1)
    return sent

if mode == 1 :
    print("Coded Text :- ")
    print (code(sent))
else : 
    while len(sent) > 0 :
        decoder(lower_code, initial)
        sent = shorting_the_list(initial,sent,i)
        i = i+1
        value_list = [decode_dict[key] for key in initial]
    decoded_sen = "".join(value_list)
    print("Decoded Text :- ",decoded_sen)
print("Programm Ended !!")