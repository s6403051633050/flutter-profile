f = open('d:\\work3.txt', 'r')
st = f.read()
k = (st.split(','))
f.close()
L = list()
print('ProID\t' 'ProName\t' 'Qty\t' 'Price/unit\t')
for p in range(0,len(k),4):
    print("%s\t %s\t %s\t %s\t "%(k[p],k[p+1],k[p+2],k[p+3]))