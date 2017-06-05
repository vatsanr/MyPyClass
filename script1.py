import folium
import pandas

df=pandas.read_csv("Volcanoes-USA.txt")

map=folium.Map(location=[df['LAT'].mean(),df['LON'].mean()],zoom_start=6,tiles='Stamen Terrain')

def color(elev):
    if elev in range(0,1000):
        col = "Green"
    elif elev in range(1000,3000):
        col = "Orange"
    else:
        col = "Red"
    return col

fg=folium.FeatureGroup(name='Volcano Locations')

for lat,lon,name,elev in zip(df['LAT'],df['LON'],df['NAME'],df['ELEV']):
    fg.add_child(folium.Marker(location=[lat,lon],popup=name,icon=folium.Icon(color=color(elev))))
map.add_child(fg)
map.add_child(folium.LayerControl())
map.save(outfile='test.html')
