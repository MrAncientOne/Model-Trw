from itertools import combinations
from popd import popu
from request import request
from optimize import opt
from calculate import assign
import copy
#def temp(av):
final=popu()
#final=av
pop_dict=final[0]
places=final[1]
pop_dict=(sorted(pop_dict,key=lambda item: int(item[1])))
#print(pop_dict)
places.remove(pop_dict[-1][0])
places_stop=list(combinations(places,4))
places_stop_final=[(pop_dict[-1][0],) + combo for combo in places_stop]
#print(*places_stop_final,sep='\n')

length=len(places_stop_final)
routes=[]

for i in range(length):
    routes.append(request(places_stop_final[i][0],places_stop_final[i][1],places_stop_final[i][2],places_stop_final[i][3],places_stop_final[i][4]))
routes=(sorted(routes,key=lambda item: int(item[1])))
#print(*routes,sep='\n')
#print(routes)
optim=opt(routes)
feed=copy.deepcopy(optim)
#print(feed)
assi=assign(pop_dict,feed)
#for i in range (len(optim)):
#    print(optim[i])
#for i in range (len(assi)):
#print(optim)
#print(assi)
#print(pop_dict)
with open("output.txt", "w") as out:
    out.write(str(pop_dict))
    out.write('\n')
    out.write(str(optim))
    out.write('\n')
    out.write(str(assi))


'''if __name__ == "__main__":
   av= [[['Ponmar', '117042'], ['Chromepet', '68956'], ['Kelambakkam', '3930'], ['Alwarpet', '140682'], ['Royapuram', '96472'], ['Kaaranai', '3199'], ['Gopalapuram', '130046'], ['Manapakkam', '53957'], ['Nungambakkam', '122440'], ['Mahabalipuram', '25958']], ['Ponmar', 'Chromepet', 'Kelambakkam', 'Alwarpet', 'Royapuram', 'Kaaranai', 'Gopalapuram', 'Manapakkam', 'Nungambakkam', 'Mahabalipuram']]
   temp(av)'''
   