"""
Script creado el 16/07/2018
La funcion principal es dibujar un mapa de Argentina
con los SHAPEFILES que se pueden descargar desde
la pagina del IGN:
http://www.ign.gob.ar/NuestrasActividades/InformacionGeoespacial/CapasSIG

y compararlo con los limites que vienen por default en python

El script esta basado en los apuntes que aparecen en el siguiente blog:

http://www.datadependence.com/2016/06/creating-map-visualisations-in-python/
"""

import matplotlib.pyplot as plt
import matplotlib.cm

from mpl_toolkits.basemap import Basemap
from matplotlib.patches import Polygon
from matplotlib.collections import PatchCollection
from matplotlib.colors import Normalize

# Mapa con datos default en BASEMAP
fig, ax = plt.subplots(figsize=(10,20))
resol = ['c', 'l', 'i', 'h', 'f']
for i_x, rs in enumerate(resol):
    m = Basemap(resolution=rs, # c, l, i, h, f or None
                projection='merc',
                lat_0=-38.45, lon_0=-63.68,
                llcrnrlon=-76.74, llcrnrlat=-55.88,
                urcrnrlon=-51.43, urcrnrlat=-21.02)

    m.drawmapboundary(fill_color='#46bcec')
    m.fillcontinents(color='#f2f2f2',lake_color='#46bcec')
    m.drawcoastlines()
    m.drawcountries()
    plt.savefig('./' + str(i_x) + 'mapa_test_' + rs + '.jpg')
    plt.clf()
    del(m)
# Mapa con datos de Shapefile IGN
sh_fold = './shapefiles/'
fig1, ax1 = plt.subplots(figsize=(10,20))
m = Basemap(resolution='c', # c, l, i, h, f or None
            projection='merc',
            lat_0=-38.45, lon_0=-63.68,
            llcrnrlon=-76.74, llcrnrlat=-55.88,
            urcrnrlon=-51.43, urcrnrlat=-21.02)
m.readshapefile(sh_fold + 'Pais', 'pais')
plt.savefig('./0_shapefile_mapa_test.jpg')
plt.clf()

# Mapa con Provincias y Departamentos de Argentina
m.readshapefile(sh_fold + 'Provincias', 'prov')
m.readshapefile(sh_fold + 'Departamentos', 'dptos')
plt.savefig('./1_shapefile_mapa_test.jpg')
plt.clf()
