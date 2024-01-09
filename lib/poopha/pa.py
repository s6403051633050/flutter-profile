import os

flag = 0
key = 0
while(key!=4):
    f = open('d:\\work3.txt', 'r')
    st = f.read()
    k = (st.split(','))

    f.close()
    L = list()
    for j in range(0,len(k),4):
        L.append([k[j],k[j+1],k[j+2],k[j+3]])
    print(L)
    os.system('cls')
    print('1:)Show Product')
    print('2:)Search by ID')
    print('3:)Insert Data')
    print('4:)Exit')
    key = int(input('Enter Number: '))

    if key == 1 :
        print('ProID\t' 'ProName\t' 'Qty\t' 'Price/unit\t')
        for p in range(0,len(k),4):
            print("%s\t %s\t %s\t %s\t "%(k[p],k[p+1],k[p+2],k[p+3]))
        print()
        input('\nPress any key _ _ _')
    
    if key == 2 :
        
        ProID = input('\nEnter Product ID:')
        
        for i in L:
            if ProID in i  :
                print('ProID\t''ProName\t''Qty\t''Price/unit\t')
                print("%s\t %s\t %s\t %s\t "%(i[0],i[1],i[2],i[3]))
                flag = 1
                break
        if flag != 1 :
            print('Not found')

        input('\nPress any key _ _ _')

    if key == 3 :
        f = open('d:\\work3.txt', 'a')
        I = input('Enter ID: ')
        I2 = input('Enter Poduct Name: ')
        I3 = input('Enter Qty: ')
        I4 = input('Enter Price/unit: ')
        L2=[I,I2,I3,I4]
        f.write(','+I+','+I2+','+I3+ ','+I4 )      
        input('\nPress any key _ _ _')