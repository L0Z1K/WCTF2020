from random import *

instruction = []
global cnt
cnt = 0
jmp_table = {"add":0,"Loop9":24, "Done9":157, "Loop1":388, "Loop2":429, "Done2":569, "Done1":590, "Loop3":764, "Loop4":816, "Done4":992, "Done3":1013, "Loop5":1076, "Loop6":1092, "Done6":1152, "Done5":1173, "Loop7":1180, "Done7":1243, "Loop8":1250, "Done8":1337,"my_error":1539}
cnt2 = 0
def random():
    return randint(0x11111111,0x7fffffff)

def push(reg):
    instruction.append(13)
    instruction.append(reg)
    global cnt
    cnt +=1

def pop(reg):
    instruction.append(14)
    instruction.append(reg)
    global cnt
    cnt +=1

def mov_const(const):
    instruction.append(20)
    instruction.append(const)
    global cnt
    cnt +=1

def mov_reg(reg):
    instruction.append(0)
    instruction.append(reg)
    global cnt
    cnt +=1

def mov_to_0(reg):
    instruction.append(21)
    instruction.append(reg)
    global cnt
    cnt +=1

def sub(reg):
    instruction.append(1)
    instruction.append(reg)
    global cnt
    cnt +=1

def rbp24():
    instruction.append(24)
    instruction.append(random())
    global cnt
    cnt +=1
    
def rbp25():
    instruction.append(25)
    instruction.append(random())
    global cnt
    cnt +=1
    
def heap17():
    instruction.append(27)
    instruction.append(random())
    global cnt
    cnt +=1
    
def heap20():
    instruction.append(26)
    instruction.append(random())
    global cnt
    cnt +=1
    
def cmp10(value):
    instruction.append(10)
    instruction.append(value)
    global cnt
    cnt +=1
    
def mod(reg):
    instruction.append(8)
    instruction.append(reg)
    global cnt
    cnt +=1
    
def shl(value):
    instruction.append(12)
    instruction.append(value)
    global cnt
    cnt +=1
    
def add(reg):
    instruction.append(2)
    instruction.append(reg)
    global cnt
    cnt +=1
    
def xor(reg):
    instruction.append(5)
    instruction.append(reg)
    global cnt
    cnt +=1
    
def mul(reg):
    instruction.append(3)
    instruction.append(reg)
    global cnt
    cnt +=1
    
def div(reg):
    instruction.append(4)
    instruction.append(reg)
    global cnt
    cnt +=1
    
def putc(reg):
    instruction.append(17)
    instruction.append(reg)
    global cnt
    cnt += 1

def jmp(arg):
    instruction.append(22)
    instruction.append(arg)
    global cnt
    cnt += 1

def jmp2(arg):
    instruction.append(23)
    instruction.append(arg)
    global cnt
    cnt += 1

def exit_():
    instruction.append(19)
    instruction.append(random())
    global cnt
    cnt += 1

def gt(value):
    instruction.append(11)
    instruction.append(value)
    global cnt
    cnt += 1

def heap28():
    instruction.append(28)
    instruction.append(random())
    global cnt
    cnt += 1

def heap29():
    instruction.append(29)
    instruction.append(random())
    global cnt
    cnt += 1

f = open("asm.asm","r")
fb = f.read()
f.close()

inst = fb.split("\n")



for i in inst:
    if len(i) == 0:
        continue
    if i[0] == "#":
        if "mov [rbp" in i:
            offset = int(i.split("-")[1].split("]")[0])
            if ", eax" in i:
                push(0)
                mov_const(offset)
                mov_reg(1)
                mov_to_0(3)
                sub(1)
                mov_reg(1)
                pop(0)
                rbp24()
            else:
                value = int(i.split(", ")[1])
                mov_const(offset)
                mov_reg(1)
                mov_to_0(3)
                sub(1)
                mov_reg(1)
                mov_const(value)
                rbp24()
        elif "mov eax, [rbp-" in i :
            offset = int(i.split("-")[1].split("]")[0])
            mov_const(offset)
            mov_reg(1)
            mov_to_0(3)
            sub(1)
            mov_reg(1)
            rbp25()
        elif "mov eax, [eax]" in i:
            mov_reg(1)
            if "HEAP2" in i:
                heap28()
            elif "HEAP" in i:
                heap17()
            else:
                rbp25()

        elif "mov eax, [" in i:
            offset = int(i.split("[")[1].split("]")[0])
            mov_const(offset)
            mov_reg(1)
            if "HEAP2" in i:
                heap28()
            else:
                #print(i)
                heap17()
        elif "mov eax, rsp" in i:
            mov_to_0(4)
        elif "mov eax, rbp-" in i:
            offset = int(i.split("-")[1])
            mov_const(offset)
            mov_reg(1)
            mov_to_0(3)
            sub(1)
        elif "mov eax, ecx" in i:
            mov_to_0(2)
        elif "mov eax, ebx" in i:
            mov_to_0(1)
        elif "mov eax, rbp" in i:
            mov_to_0(3)
        elif "mov eax, " in i:
            value = int(i.split(", ")[1])
            mov_const(value)
        elif "mov ebx, rbp-" in i:
            offset = int(i.split("-")[1])
            mov_const(offset)
            mov_reg(1)
            mov_to_0(3)
            sub(1)
            mov_reg(1)
        elif "mov ebx, eax" in i:
            mov_reg(1)
        elif "mov ebx, " in i:
            value = int(i.split(", ")[1])
            mov_const(value)
            mov_reg(1)
        elif "mov ecx, eax" in i:
            mov_reg(2)
        elif "mov [ebx], eax" in i:
            if "HEAP2" in i:
                heap29()
            elif "HEAP" in i:
                heap20()
            else:
                rbp24()
        elif "mov rbp, eax" in i:
            mov_reg(3)
        elif "mov rbp, " in i:
            value = int(i.split(", ")[1])
            #if value == 30000:
            #    print(cnt)
            mov_const(value)
            mov_reg(3)
        elif "mov rsp, eax" in i:
            mov_reg(4)
        elif "mov rsp, " in i:
            value = int(i.split(", ")[1])
            mov_const(value)
            mov_reg(4)
        elif "cmp eax, " in i:
            value = int(i.split(", ")[1])
            cmp10(value)
        elif "% eax, ebx" in i:
            mod(1)
        elif "% eax, " in i:
            value = int(i.split(", ")[1])
            push(0)
            mov_const(value)
            mov_reg(1)
            pop(0)
            mod(1)
        elif "shl eax, " in i:
            value = int(i.split(", ")[1])
            shl(value)
        elif "push eax" in i:
            push(0)
        elif "push ebx" in i:
            push(1)
        elif "push ecx" in i:
            push(2)
        elif "push rbp" in i:
            push(3)
        elif "pop eax" in i:
            pop(0)
        elif "pop ebx" in i:
            pop(1)
        elif "pop rbp" in i:
            pop(3)
        elif "add eax, ebx" in i:
            add(1)
        elif "xor eax, ebx" in i:
            xor(1)
        elif "mul eax, ebx" in i:
            mul(1)
        elif "div eax, ebx" in i:
            div(1)
        elif "sub eax, ebx" in i:
            sub(1)
        elif "sub rsp, " in i:
            value = int(i.split(", ")[1])
            mov_const(value)
            mov_reg(1)
            mov_to_0(4)
            sub(1)
            mov_reg(4)
        elif "putc rbp-" in i:
            offset = int(i.split("-")[1])
            mov_const(offset)
            mov_reg(1)
            mov_to_0(3)
            sub(1)
            push(0)
            pop(1)
            rbp25()
            putc(0)
        elif "putc " in i:
            char = ord(i.split("putc ")[1][0])
            mov_const(char)
            putc(0)
        elif "j " in i:
            label = i.split("j ")[1]
            mov_const(0)
            if "ra" in label:
                jmp(1131)
            else:
                jmp(jmp_table[label])
            #if label == "add":
            #   print(cnt)
        elif "jz " in i:
            label = i.split("jz ")[1]
            jmp(jmp_table[label])
        elif "exit" in i:
            exit_()
            #print(cnt)
        elif "gt eax, " in i:
            value = int(i.split(", ")[1])
            gt(value)



    '''
    if "Loop" in i:
        if ":" in i:
            print(i + str(cnt) + ","),
    if "Done" in i:
        if ":" in i:
            print(i + str(cnt) + ","),
    '''

print(instruction)
#print(cnt)




            

