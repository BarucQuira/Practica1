import re 
patron=re.compile(r'\W')
def bus_anchura(E,ni,V):
    nodos={'a':0,'b':1,'c':2,'d':3,'e':4,'f':5,'g':6,'h':7}
    vi=nodos[ni]
    V=patron.split(V)

    v1=V[vi]
    Vp=[v1]

    Ep=[]
    S = [v1]
    while True:
        bandera = True
        V_S=[]
        for x in S:
            Vdiff = [z for z in V if z not in Vp]
            print(Vdiff)
            for y in Vdiff:
                if ((x,y) in E):
                    vk=(x,y)                    
                    Ep.append(vk)
                    Vp.append(y)
                    V_S.append(y)
                    
                    bandera = False
        if bandera==True:
            print("Anchura resuelto",Ep)
            return Ep
        S = V_S         
        
vi='g'
V=('a b c d e f g h')


E={('a','b'),('a','c'),('a','g'),('b','a'),('b','d'),('b','g'),('c','a'),('c','d'),('c','e'),
    ('d','b'),('d','c'),('d','f'),('e','c'),('e','f'),('e','g'),('f','d'),('f','e'),('f','h'),
    ('g','a'),('g','b'),('g','e'),('h','f')} 
bus_anchura(E,vi,V)
