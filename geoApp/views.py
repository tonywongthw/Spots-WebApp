from django.shortcuts import render, redirect
import os
import folium
import pandas as pd


# Create your views here.
def home(request):
    shp_dir = os.path.join(os.getcwd(), 'media', 'shp')
    # folium
    """m = folium.Map(location=[-16.22, -71.59], zoom_start=10)
    # style
    style_basin = {'fillColor': '#228B22', 'color': '#228B22'}
    style_rivers = {'color': 'blue'}
    # adding to view
    folium.GeoJson(os.path.join(shp_dir, 'basin.geojson'), name='basin', style_function=lambda x: style_basin).add_to(m)
    folium.GeoJson(os.path.join(shp_dir, 'rivers.geojson'), name='rivers',
                   style_function=lambda x: style_rivers).add_to(m)
    folium.LayerControl().add_to(m)"""

    cities = pd.read_csv(os.path.join(shp_dir, 'cities.csv'))
    m = folium.Map(
        location=[13.14, 16.10],
        zoom_start=2)
    for _, city in cities.iterrows():
        folium.Marker(
            location=[city['latitude'], city['longitude']],
            tooltip=city['name']
        ).add_to(m)

    # exporting
    m = m._repr_html_()
    context = {'my_map': m}
    # rendering
    return render(request, 'geoApp/home.html', context)
