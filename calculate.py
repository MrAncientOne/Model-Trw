
def assign(diction,routes):
    total_buses=8000
    sums=0
    #for i in range(len(diction)):
    #    sums+=int(diction[i][1])
   
    temp=0
    diction=dict( (k[0], k[1]) for k in diction)
    for i in range(len(routes)):
        for j in routes[i][0]:
            sums+=int(diction[j])

    for i in range(len(routes)):
        for j in routes[i][0]:
            temp+=int(diction[j])
        routes[i][1]=(temp/sums)*total_buses
        temp=0
    return routes


if __name__ == "__main__" :
    ab=[['Ponmar', '117042'], ['Chromepet', '68956'], ['Kelambakkam', '3930'], ['Alwarpet', '140682'], ['Royapuram', '96472'], ['Kaaranai', '3199'], ['Gopalapuram', '130046'], ['Manapakkam', '53957'], ['Nungambakkam', '122440'], ['Mahabalipuram', '25958']]
    cd=[[['Alwarpet', 'Royapuram', 'Gopalapuram', 'Nungambakkam', 'Mahabalipuram'], '3130'], [['Alwarpet', 'Ponmar', 'Chromepet', 'Kelambakkam', 'Kaaranai'], '7461']]
    print(assign(ab,cd))

