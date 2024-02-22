import os
import syscall from syscalls; 

print("id,t", end=',')
i = 0
for sys in syscall:
   if i == 497:
       print(sys)
   else:
       print(sys, end=',')
   i+=1
i=0
id = 0
for _, _, arquivos in os.walk('./wordpress/exec/'):
    for arquivo in arquivos:
        with open(f'./wordpress/exec/{arquivo}', "r") as f:
            lines = f.readlines()

        # Trecho para contar o numero de chamadas de cada syscall
        for line in lines:
            linhaAux = line.split(' ')
            call = linhaAux[0]
            syscall[call] += 1
        print(f'{id},0', end=',')
        id += 1
        for sys in syscall.values():
            if i == 497:
                print(sys/2)
            else:
                print(sys/2, end=',')
            i+=1
        i=0
        for sys in syscall:
            syscall[sys] = 0
        
for _, _, arquivos in os.walk('./wordpress/normal/'):
    for arquivo in arquivos:
        with open(f'./wordpress/normal/{arquivo}', "r") as f:
            lines = f.readlines()

        # Trecho para contar o numero de chamadas de cada syscall
        for line in lines:
            linhaAux = line.split(' ')
            call = linhaAux[0]
            syscall[call] += 1
        print(f'{id},1', end=',')
        id += 1
        for sys in syscall.values():
            if i == 497:
                print(sys/2)
            else:
                print(sys/2, end=',')
            i+=1
        i=0
                
        for sys in syscall:
            syscall[sys] = 0
