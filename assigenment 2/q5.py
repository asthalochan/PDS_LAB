ch=input(" Enter a character")
if(ch>='A' and ch<='Z') or (ch>='a' and ch<='z'):
    print("Its a alphabet")
    ch=ch.lower()
    if (ch =='a') or (ch =='e') or (ch == 'i') or (ch=='o') or (ch=='u'):
        print("the alphabet is vowel")
    else:
        print("The alphabat is consonet")
elif(ch>='0') and (ch<='9'):
    print("its a number")
else:
    print("special character")