
import androidhelper
from datetime import datetime
droid=androidhelper.Android()
import time
from math import sin, cos, sqrt, atan2, radians 
 
def distance(p1, p2): 
    # Raio aproximado da terra 
    R = 6371.0 
 
    lat1 = radians(p1[0]) 
    lon1 = radians(p1[1]) 
    lat2 = radians(p2[0]) 
    lon2 = radians(p2[1]) 
 
    dlon = lon2 - lon1 
    dlat = lat2 - lat1 
 
    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2 
    c = 2 * atan2(sqrt(a), sqrt(1 - a)) 
 
    distance = R * c 
 
    return distance 

    
def localizacao(hlat,hlon):
    #opt=droid.dialogGetInput('','')
    #droid = android.Android()
    droid.startLocating()
    #event = droid.eventWait(1000).result
    time.sleep(15)
    loc = droid.readLocation().result

    droid.stopLocating() 
 
    vfonte='gps'
    if 'gps' in loc:
        vfonte='gps'
    else:
        vfonte='network'
    vlat=loc[vfonte]['latitude']
    vlong=loc[vfonte]['longitude']
    dt = datetime.today()
    mes="{:02d}".format(dt.month)
    dia="{:02d}".format(dt.day)
    hora="{:02d}".format(dt.hour)
    minuto="{:02d}".format(dt.minute)
    segundo="{:02d}".format(dt.second)
    print(time.strftime("%I %M %p on %A, %B %e, %Y"))
    result=(time.strftime("%Y")+mes+dia+hora+minuto+segundo)
    
    print(vlat)
    print(vlong)

    vresult=droid.geocode(vlat,vlong)
    
    p1=[hlat,hlon]
    p2=[vlat,vlong]
    dir1=""
    dir2=""
    if (hlat>vlat):
        dir1="N"
    else:
        dir1="S"
    if (hlon>vlong):
        dir2="E"
    else:
        dir2="W"
    
    distancia='{:.3f}'.format(distance(p1,p2))
    ndist=dir1+dir2+distancia
    droid.makeToast(ndist)
    print('dist:'+ndist)

file = open('../Log/LocIn.txt','r')
lido=file.read()
print('ler')
print(lido)
latPin=float(lido.split(',')[0])
LongPin=float(lido.split(',')[1])
print(latPin)
print(LongPin)
while(True):
 
 try:
    localizacao(latPin,LongPin)
    time.sleep(20)
 except Exception as e:
    # código que será executado se uma exceção for gerada
    print(f"Erro: {e}")
  #finally:
    # código que será executado independentemente de uma exceção ser gerada
    #print("Fim do programa")
