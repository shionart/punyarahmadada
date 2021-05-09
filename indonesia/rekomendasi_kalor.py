
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






Preq=700
coef_pembebanan =[(15.59,443872.57,8854230.19),(432.52,228835.28,26186478.79),(928.68,-130876.67,81788363.85)]
min_dn = 200
max_dn = 315
P= optimasi_beban_unit(coef_pembebanan,Preq,min_dn,max_dn)


for idx, v in enumerate(P):
    print(f'P({idx}): {v}')
