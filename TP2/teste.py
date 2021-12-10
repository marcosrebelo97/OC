    # -*- coding: utf-8 -*-

dicio_assembly = {

    'ADD':'1000',
    'SHR':'1001',
    'SHL':'1010',
    'NOT':'1011',
    'AND':'1100',
    'OR':'1101',
    'XOR':'1110',
    'CMP':'1111',
    'LD':'0000',
    'ST':'0001',
    'DATA':'001000',
    'JMPR':'0011',
    'JMP':'01000000',
    'J':'0101',
    'C':'1',
    'A':'1',
    'E':'1',
    'Z':'1',
    'CLF':'01100000',
    'R0':'00',
    'R1':'01',
    'R2':'10',
    'R3':'11' 
}

assembly = []
binary = []
hexadecimal = []

def dir_1():
    global dir1
    dir1 = "/home/marcos/Documentos/OC/TP2/assembly/teste2.txt"
           #Alterar diretório
           
def read_Arquivo():
    reader = open(dir1, 'r')

    with open (dir1, 'r', encoding="utf-8-sig") as reader:
        for l in reader:       
            res = re.split(" ", l.rstrip())
            if (res[0]) in dicio_assembly.keys():

                inst_data(res)
                inst_shr(res)
                inst_shl(res)
                inst_not(res)
                inst_add(res)
                inst_and(res)
                inst_or(res)
                inst_xor(res)
                inst_cmp(res)
                inst_ld(res)
                inst_st(res)
                inst_jmpr(res)
                inst_jmp(res)
                inst_clf(res)
                #print(res)
                
            elif(res[0][0] == 'J'):
                inst_jcaez(res, len(res[0]))
            assembly.append(res)  
        print(binary)
    reader.close();

def inst_add (list):
    if(list[0] == 'ADD'):
        print (list[0] + " = " + dicio_assembly.get(list[0]))
        print(dicio_assembly.get(list[0]) + dicio_assembly.get(list[1]) + dicio_assembly.get(list[2]))
        binary.append(dicio_assembly.get(list[0]) + dicio_assembly.get(list[1]) + dicio_assembly.get(list[2]))

def inst_shr (list):
    if(list[0] == 'SHR'):
        print (list[0] + " = " + dicio_assembly.get(list[0]))
        if(len(list) == 2):
            print(dicio_assembly.get(list[0]) + dicio_assembly.get(list[1]) + dicio_assembly.get(list[1]))
            binary.append(dicio_assembly.get(list[0]) + dicio_assembly.get(list[1]) + dicio_assembly.get(list[1]))
        elif (len(list) == 3):
            print(dicio_assembly.get(list[0]) + dicio_assembly.get(list[1]) + dicio_assembly.get(list[2]))
            binary.append(dicio_assembly.get(list[0]) + dicio_assembly.get(list[1]) + dicio_assembly.get(list[2]))  
def inst_shl (list):
    if(list[0] == 'SHL'):
        print (list[0] + " = " + dicio_assembly.get(list[0]))
        if(len(list) == 2):
            print(dicio_assembly.get(list[0]) + dicio_assembly.get(list[1]) + dicio_assembly.get(list[1]))
            binary.append(dicio_assembly.get(list[0]) + dicio_assembly.get(list[1]) + dicio_assembly.get(list[1]))
        elif (len(list) == 3):
            print(dicio_assembly.get(list[0]) + dicio_assembly.get(list[1]) + dicio_assembly.get(list[2]))
            binary.append(dicio_assembly.get(list[0]) + dicio_assembly.get(list[1]) + dicio_assembly.get(list[2]))

def inst_not (list):
    if(list[0] == 'NOT'):
        print (list[0] + " = " + dicio_assembly.get(list[0]))
        print(dicio_assembly.get(list[0]) + dicio_assembly.get(list[1]) + dicio_assembly.get(list[2]))
        binary.append(dicio_assembly.get(list[0]) + dicio_assembly.get(list[1]) + dicio_assembly.get(list[2]))

def inst_and (list):
    if(list[0] == 'AND'):
        print (list[0] + " = " + dicio_assembly.get(list[0]))
        print(dicio_assembly.get(list[0]) + dicio_assembly.get(list[1]) + dicio_assembly.get(list[2]))
        binary.append(dicio_assembly.get(list[0]) + dicio_assembly.get(list[1]) + dicio_assembly.get(list[2]))

def inst_or (list):
    if(list[0] == 'OR'):
        print (list[0] + " = " + dicio_assembly.get(list[0]))
        print(dicio_assembly.get(list[0]) + dicio_assembly.get(list[1]) + dicio_assembly.get(list[2]))
        binary.append(dicio_assembly.get(list[0]) + dicio_assembly.get(list[1]) + dicio_assembly.get(list[2]))

def inst_xor (list):
    if(list[0] == 'XOR'):
        print (list[0] + " = " + dicio_assembly.get(list[0]))
        print(dicio_assembly.get(list[0]) + dicio_assembly.get(list[1]) + dicio_assembly.get(list[2]))
        binary.append(dicio_assembly.get(list[0]) + dicio_assembly.get(list[1]) + dicio_assembly.get(list[2]))

def inst_cmp (list):
    if(list[0] == 'CMP'):
        print (list[0] + " = " + dicio_assembly.get(list[0]))
        print(dicio_assembly.get(list[0]) + dicio_assembly.get(list[1]) + dicio_assembly.get(list[2]))
        binary.append(dicio_assembly.get(list[0]) + dicio_assembly.get(list[1]) + dicio_assembly.get(list[2]))

def inst_ld (list):
    if(list[0] == 'LD'):
        print (list[0] + " = " + dicio_assembly.get(list[0]))
        print(dicio_assembly.get(list[0]) + dicio_assembly.get(list[1]) + dicio_assembly.get(list[2]))
        binary.append(dicio_assembly.get(list[0]) + dicio_assembly.get(list[1]) + dicio_assembly.get(list[2]))

def inst_st (list):
    if(list[0] == 'ST'):
        print (list[0] + " = " + dicio_assembly.get(list[0]))
        print(dicio_assembly.get(list[0]) + dicio_assembly.get(list[1]) + dicio_assembly.get(list[2]))
        binary.append(dicio_assembly.get(list[0]) + dicio_assembly.get(list[1]) + dicio_assembly.get(list[2]))

def inst_data (list):
    if(list[0] == 'DATA'):
        print (list[0] + " = " + dicio_assembly.get(list[0]))
        print(dicio_assembly.get(list[0]) + dicio_assembly.get(list[1]))
        binary.append(dicio_assembly.get(list[0]) + dicio_assembly.get(list[1]))

        an_integer = int(list[2], 16)
        num_of_bits = 8
        bin_value = bin(an_integer)[2:].zfill(num_of_bits)
        print(bin_value)
        binary.append(bin_value)

def inst_jmpr (list):
    if(list[0] == 'JMPR'):
        print (list[0] + " = " + dicio_assembly.get(list[0]))
        print(dicio_assembly.get(list[0]) + dicio_assembly.get(list[1]))
        binary.append(dicio_assembly.get(list[0]) + dicio_assembly.get(list[1]))

def inst_jmp (list):
    if(list[0] == 'JMP'):
        print (list[0] + " = " + dicio_assembly.get(list[0]))
        print(dicio_assembly.get(list[0]))
        binary.append(dicio_assembly.get(list[0]))

        an_integer = int(list[1], 16)
        num_of_bits = 8
        bin_value = bin(an_integer)[2:].zfill(num_of_bits)
        print(bin_value)
        binary.append(bin_value)

def inst_jcaez (list, wordLenght):
    i=1
    c='0'
    a='0'
    e='0'
    z='0'
    
    while i<wordLenght:
        if(list[0][i] == 'C'):
            c = dicio_assembly.get(list[0][i])
        elif(list[0][i] == 'A'):
            a = dicio_assembly.get(list[0][i])
        elif(list[0][i] == 'E'):
            e = dicio_assembly.get(list[0][i])
        elif(list[0][i] == 'Z'):
            z = dicio_assembly.get(list[0][i])

        i+=1

    caezCode = '{0}{1}{2}{3}'.format(c, a, e, z)
    print (list[0] + " = " + dicio_assembly.get(list[0][0]))
    print(dicio_assembly.get(list[0][0])+caezCode)
    binary.append(dicio_assembly.get(list[0][0])+caezCode)
  
    an_integer = int(list[1], 16)
    num_of_bits = 8
    bin_value = bin(an_integer)[2:].zfill(num_of_bits)
    print(bin_value)
    binary.append(bin_value)

def inst_clf (list):
    if(list[0] == 'CLF'):
        print (list[0] + " = " + dicio_assembly.get(list[0]))
        print(dicio_assembly.get(list[0]))
        binary.append(dicio_assembly.get(list[0]))

#Executa o dir_2 pra criação do arquivo txt
def dir_2(): 
    global dir2
    dir2 = "/home/marcos/Documentos/OC/TP2/binario.txt" 
            #Alterar diretório

def dir_3():
    global dir3
    dir3 = "/home/marcos/Documentos/OC/TP2/hexadecimal.txt"
            #Alterar diretório

 #Gera um arquivo txt com o título especificado            
def gerar_Txt():
    fo = open(dir2, "wt")
    fo.write("")
    for l in binary:
        fo.write(l + '\n')

    fo.close()

def convert_hexa():
    for n in binary:

        integer = int(n, 2)
        valor = hex(integer)[2:]
        hexadecimal.append(valor)
        print(valor)

def gerar_Txt_hexa():
    cont = 0
    fo = open(dir3, "r+")
    fo.write("v3.0 hex words addressed \n")
    for x in hexadecimal:
        if cont % 16 == 0:
            fo.write('\n')
            fo.write('{0:02x}'.format(cont))
            fo.write(':')
       #fo.write(' '+x)
        if len(x) == 1:
            fo.write(' 0'+x)
        else: 
            fo.write(' '+x)
        cont+=1        
    fo.close()


#Principal
import re
import os
os.system('cls')

#Funções
dir_1()
read_Arquivo()
dir_2()  
dir_3()
gerar_Txt()
convert_hexa()
gerar_Txt_hexa()