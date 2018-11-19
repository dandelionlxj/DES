s=[[14, 4, 13,  1,  2, 15, 11,  8,  3, 10,  6, 12,  5,  9,  0,  7],
     [0, 15,  7,  4, 14,  2, 13,  1, 10,  6, 12, 11,  9,  5,  3,  8],
     [4,  1, 14,  8, 13,  6,  2, 11, 15, 12,  9,  7,  3, 10,  5,  0],    
     [15, 12,  8,  2,  4,  9,  1,  7,  5, 11,  3, 14, 10,  0,  6, 13]]

def functions(key):
    '''
    s盒代替
    '''
    return_list=''
    row=int( str(key[0])+str(key[5]),2)
    raw=int(str( key[1])+str(key[2])+str(key[3])+str(key[4]),2)
    return_list+=changtos(s[row][raw],4)
    return return_list

def changtos(o,lens):
    '''
    二进制转换
    '''
    return_code=''
    for i in range(lens):
        return_code=str(o>>i &1)+return_code
    return return_code

def codeyihuo(code,key):
    '''
    异或运算
    '''
    code_len=len(key)
    return_list=''
    for i in range(code_len):
        if code[i]==key[i]:
            return_list+='0'
        else:
            return_list+='1'
    return return_list


b=''
d=''
a=[]
c=[]
for i in range(64):
    b+=str(functions(str('{:06b}'.format(i))))
    d+=str(functions(str(codeyihuo('{:06b}'.format(i),'000001'))))
    #print('b['+str(i+1)+']:'+b)
    #print('d['+str(i+1)+']:'+d)
    a.append(str(codeyihuo(b[i*4:i*4+4],d[i*4:i*4+4])))
    #print('a:'+str(a))

for i in range(16):
    number=0
    c.append(str('{:04b}'.format(i)))
    for j in range(len(a)):
        if a[j]==c[i]:
            number+=1
    print('输出差分'+str(c[i])+'数量为'+str(number)+'个')


