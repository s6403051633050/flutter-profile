Prod = [[10001, 'pen', 100, 10], [10002, 'book', 200, 20], [10003, 'glass', 50, 25], [10004, 'eraser', 500, 10]]
f = open('d:\\work3.txt', 'w') 
for k in range(len(Prod)):
    f.write(str(Prod[k][0]) + ',' + str(Prod[k][1]) +','+ str(Prod[k][2])+','+str(Prod[k][3]))
    if k != len(Prod) - 1:
        f.write(',')