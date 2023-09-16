import sys
import re

def readFile(namefile):
    out=open(namefile,'r')
    alpha = out.readline().replace("\n","")
    alpha=alpha.replace(" ","")
    alpha=alpha.split("OR")
    length_kb = int(out.readline().replace("\n",""))
    kb=[]
    temp=[]
    for i in range(length_kb):
        temp=out.readline().replace("\n","")
        temp=temp.replace(" ","")
        temp=temp.split("OR")
        temp=sorted(temp)
        kb.append(temp)
    out.close()
    return alpha, length_kb, kb
#AvBv-B => xóa đi
def checkTrue(s):
    for i in s:
        if(('-'+i) in s):
            return True
    return False
def remove(s1, name):
    s=s1[:]
    s.remove(name)
    t=s
    return t
def resolve(ci, cj):
#ex: ci,cj=['A', 'B']<=> AvB
    clauses = []
    new=[]
    t=[]
    for di in ci:
        for dj in cj:
            new=[]
            t=[]
            if(di==("-"+dj) or ("-"+di)==dj):
                t=remove(ci,di)
                if(len(t)!=0):
                    new.extend(t)
                t=remove(cj,dj)
                if(len(t)!=0):
                    new.extend(t)
                new=set(new)
                new=list(new)
                if(len(new)==0):
                    new.append("{}")
                if(checkTrue(new)==False):# đảm bảo không có Bv-B. Vì không giá trị
                    clauses.extend(new)
    clauses=sorted(clauses)
    return clauses
def checkAll(new, clauses):
    for i in new:
        if(i not in clauses):
            return False
    return True
def Not(alpha):
    if(len(alpha)==2):
        return alpha[1]
    return "-"+alpha
def NotAll(alpha):
    temp=[]
    for i in alpha:
        temp.append([Not(i)])
    return temp
def Sort(s):
    t=s[:]
    t=set(s)
    r=[]
    for i in t:
        r.append(i)
    return r
def resolution(kb, alpha, nameFile):
    clauses=kb[:]
    clauses.extend(NotAll(alpha))
    if "{}" in clauses: return True
    n = len(clauses)
    new = []
    res_count = 0
    round = 0
    out=open(nameFile, 'w')
    while True:
        round += 1
        n=len(clauses)
        l=len(new)
        pairs = [(clauses[i], clauses[j])
                 for i in range(n) for j in range(i+1, n)]
        for (ci, cj) in pairs:
            resolvents = resolve(ci, cj)
            res_count += 1
            if "{}" in resolvents:#chứa mệnh đề trống
                new.append(resolvents)
                if(l<len(new)):
                    out.write(str(len(new)-l)+'\n')
                for i in range(l,len(new)):
                    for j in new[i]:
                        out.write(j)
                        if(j!=new[i][len(new[i])-1]):
                            out.write(" OR ")
                    out.write('\n')
                out.write("YES")
                out.close()
                return True
            if(resolvents not in new and len(resolvents)!=0 and resolvents not in clauses):
                new.append(resolvents)
        if(l<len(new)):
            out.write(str(len(new)-l)+'\n')
            for i in range(l,len(new)):
                for j in new[i]:
                    out.write(j)
                    if(j!=new[i][len(new[i])-1]):
                        out.write(" OR ")
                out.write('\n')
        if (checkAll(new, clauses)):
            out.write("0")
            out.write("\nNO")
            out.close()
            return False
        for i in new:
            if(i not in clauses):
                clauses.append(i)
#1
alpha, length_kb, kb=readFile("in1.txt")
resolution(kb,alpha,"out1.txt")
#2
alpha, length_kb, kb=readFile("in2.txt")
resolution(kb,alpha,"out2.txt")
#3
alpha, length_kb, kb=readFile("in3.txt")
resolution(kb,alpha,"out3.txt")
#4
alpha, length_kb, kb=readFile("in4.txt")
resolution(kb,alpha,"out4.txt")
#5
alpha, length_kb, kb=readFile("in5.txt")
resolution(kb,alpha,"out5.txt")

                
    
    
