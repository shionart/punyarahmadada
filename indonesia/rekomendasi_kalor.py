
def calculate_beban_unit(lambda_coef, a,b):
    return round((lambda_coef-b)/(2*a))

def calculate_beban_each_unit(koef_lambda, koef_ic):
    P=[]
    for koefisien in koef_ic:
        a,b,c=koefisien
        #print(f'a:{a} b:{b} c:{c}')
        bebanunit = calculate_beban_unit(koef_lambda, a, b)
        P.append(bebanunit)
        #print(f'koef lambda: {koef_lambda} beban unit:{bebanunit}')
    return P
def delta_P_unit(P_beban,Punit):
    dP=P_beban
    for v in Punit:
        dP=dP-v
    return dP

def delta_lambda(deltaPunit,koef_ic):
    pembagi=0
    for koef in koef_ic:
        a,b,c = koef
        pembagi += 1/(2*a)
        #print(f'a:{a}, {1/(2*a)}')
    return (deltaPunit/pembagi)

def cek_kesesuaian_beban(P, min_dn, max_dn):
    for idx,v in enumerate(P):
        #print(f'{idx},{v}')
        if v < min_dn:
            P[idx]= min_dn   #dn: daya unit
        #elif v> max_dn:
        #    P[idx]= max_dn
        else:
            P[idx]=v
    return P

def printP(P):
    for v in P:
        print(v)

def optimasi_beban_unit(koef_ic,Preq,min_dn,max_dn):
    koef_lambda = 400000
    loop = True
    iterasike=0;
    while loop:
        P = calculate_beban_each_unit(koef_lambda, koef_ic)
        dP= delta_P_unit(Preq,P)
        print(f'dP:{dP}')
        print(f'P: {P}')
        P = cek_kesesuaian_beban(P, min_dn, max_dn)
        print(f'P penyesuaian:{P}')
        dP = delta_P_unit(Preq, P)
        print(f'dP:{dP}')
        if (dP == 0) :
            break
        koef_lambda = koef_lambda + delta_lambda(dP,koef_ic)
        print(f'koefisien lamda:{koef_lambda}')
        iterasike +=1
        print(f'iterasi ke{iterasike}')
    return P

def hitungCost(P,koef):
    costApp = []
    for idx,v in enumerate(P):
        costs = calculatecost(v,idx,koef)
        costApp.append(costs)
    return costApp

def calculatecost(p,i,koef):
    for idx, koefisien in enumerate(koef):
        a, b, c = koefisien
        if i == idx:
            costss = calculateunitcost(p, a, b,c)
    return costss

def calculateunitcost(p, a, b, c):
    return (a*(p*p))+(b*(p))+c

def hitungnphrunit(P,C,beban):
    nphrunit =[]
    for idx,v in enumerate(P):
        nphr = hitungperunit(v,C,idx,beban)
        nphrunit.append(nphr)
    return nphrunit

def hitungperunit(p,css,i,bebaninput):
    for idx, cs in enumerate(css):
        if i == idx:
            un = (cs/(p*1000*bebaninput))
    return un

def hitungbiayaprod(P,C):
    biaya = []
    for idx,v in enumerate(P):
        b = calculatebiaya(v,C,idx)
        biaya.append(b)
    return biaya

def calculatebiaya(p,cu,i):
    for idx, cuu in enumerate(cu):
        if i == idx:
            biayaprod = round(cuu/(p*1000))
    return biayaprod

def nilairekomendasikalor(P,U):
    nilai = []
    for idx,v in enumerate(P):
        n = calculatenilai(v,U,idx)
        nilai.append(n)
    return nilai

def calculatenilai(p,unit,i):
    for idx, cuu in enumerate(unit):
        if i == idx:
            nilairekom = calculateperunit(p,cuu,i)
    return nilairekom

def calculateperunit(p,nphr,i):
    if i == 0:
        return 2443.743 + (0.457 * p) + (0.806 * nphr)
    elif i == 1:
        return 2486.969 + (1.351 * p) + (0.695 * nphr)
    else:
        return 3370.328 + (0.645 * p) + (0.414 * nphr)

def calculatefixrekomendasikalor(N):
    total = 0
    for nr in N:
        total += nr
    nrf = total/3
    return nrf

import csv

with open('koefisien.csv', newline='') as f:
    reader = csv.reader(f)
    #data = [tuple((map(float,row))) for row in reader]

Preq=700
inputanbeban = 0.1687234
coef_pembebanan =[(15.59,443872.57,8854230.19),(432.52,228835.28,26186478.79),(928.68,-130876.67,81788363.85)]
#coef_pembebanan = data
min_dn = 200
max_dn = 315
P = optimasi_beban_unit(coef_pembebanan,Preq,min_dn,max_dn)
C = hitungCost(P,coef_pembebanan)
U = hitungnphrunit(P,C,inputanbeban)
B = hitungbiayaprod(P,C)
N = nilairekomendasikalor(P,U)
NR = calculatefixrekomendasikalor(N)

for idx, v in enumerate(P):
    print(f'P({idx}): {v}')

for idx,c in enumerate(C):
    print(f'C({idx}): {c}')

for idx, u in enumerate(U):
    print(f'U({idx}): {u}')

for idx, b in enumerate(B):
    print(f'B({idx}): {b}')

for idx, n in enumerate(N):
    print(f'N({idx}): {n}')

print("NILAI REKOMENDASI KALOR",NR)

# for idx, v in enumerate(P):
#     print(f'P({idx}): {v}')
