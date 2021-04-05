
from netCDF4 import Dataset
f= Dataset("Mercator.nc")

import json
g= open ("C:/www/projecto/static/leaflet/novo.json")
a=json.loads(g.read())
g.close()

u=f["uo"][:]
u[0][0][:]
u[0][0].tolist()
a[0]["data"]=u[0][0].tolist()

v=f["vo"][:]
v[0][0][:]
v[0][0].tolist()
a[1]["data"]=v[0][0].tolist()

v=f["so"][:]
v[0][0][:]
v[0][0].tolist()
a[1]["data"]=v[0][0].tolist()

v=f["thetao"][:]
v[0][0][:]
v[0][0].tolist()
a[1]["data"]=v[0][0].tolist()

h=open ("novo.json", "w")
json.dump(a, h)
h.close()