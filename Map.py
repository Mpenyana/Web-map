import folium
import pandas


data = pandas.read_csv('Volcanoes_USA.txt')

lat = list(data['LAT'])
lon = list(data['LON'])
el = list(data['ELEV'])



map = folium.Map(location=[-26.418217, 27.872459], zoom_start=5, tiles='Mapbox Control Room')

def color_producer(elevation):
    if elevation < 1000:
        return 'blue'
    elif 1000 <= elevation < 3000:
        return 'orange'
    else:
        return 'red'

fgv = folium.FeatureGroup(name="Volcanoes")
fgl = folium.FeatureGroup(name="Me")
# fgp = folium.FeatureGroup(name="Population")

locations = [[-26.415846, 27.864953]]

for lat, lon, el in zip(lat,lon, el):
    fgv.add_child(folium.CircleMarker(radius=7, location=[lat,lon], popup=str(el), color='pink', fill_color=color_producer(el), weight=1, fillOpacity=0.7))

for me in locations:
    fgl.add_child(folium.CircleMarker(location=(me), radius=20, tooltip='My Circle'))

# fgp.add_child(folium.GeoJson(data=open('world.json', 'r', encoding='utf-8-sig').read(),
#                             style_function=lambda x: {'fillColor':'red' if x['properties']['POP2005'] < 10000000 else 'green' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'brown' }))

map.add_child(fgv)
# map.add_child(fgp)
map.add_child(fgl)

map.add_child(folium.LayerControl())
map.save('Map.html')

