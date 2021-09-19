from django.shortcuts import render, redirect
from .forms import CustomerForm
import os
import folium
import pandas as pd


# Create your views here.
def home(request):
    form = CustomerForm()


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

    m = folium.Map(
        location=[13.133932, 16.1039387],
        zoom_start=2)

    a=1
    if request.method == 'POST' and a==1:
        print(request.POST)
        cities = pd.read_csv(os.path.join(shp_dir, 'cities1.csv'))
        m = folium.Map(
            location=[43.6561, -79.3801],
            zoom_start=14)
        for _, city in cities.iterrows():
            folium.Marker(
                location=[city['latitude'], city['longitude']],
                tooltip=city['name']
            ).add_to(m)
    elif request.method == 'POST' and a==2:
        cities = pd.read_csv(os.path.join(shp_dir, 'cities2.csv'))
        m = folium.Map(
            location=[22.28967, 114.171144327727],
            zoom_start=13)
        for _, city in cities.iterrows():
            folium.Marker(
                location=[city['latitude'], city['longitude']],
                tooltip=city['name']
            ).add_to(m)
    else:
        m = folium.Map(
            location=[13.133932, 16.1039387],
            zoom_start=2)

    # exporting
    m = m._repr_html_()
    context = {'my_map': m, 'form': form}
    # rendering context=context ?
    return render(request, 'geoApp/home.html', context)
