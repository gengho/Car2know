
# coding: utf-8

#
#
# # data processing and produce the images
# input:
# shape data which contain the block informaiton (.shp)
# car data (.csv)
#
# output:
# heat map
# point map
#
# The images conbined the 0-23 hours of flux in / flux out and the sensor block data
#
# You may need first install geopandas package by clone it on github
# pip install geopandas
# or
# git clone https://github.com/geopandas/geopandas.git
# cd geopandas
# python setup.py install
#
# This script is written by Yuxuan Cheng
# yxcheng@uw.edu

# # imprort all the packages

#import the packages
import shapely
import geopandas as gpd

import pandas as pd
import numpy as np

import matplotlib
import matplotlib.pyplot as plt
get_ipython().magic(u'matplotlib inline')
#plt.style.use('ggplot')

import pysal
from scipy import ndimage

#read the shape file
boros = gpd.GeoDataFrame.from_file('../../data/SelectedBlocks.shp')
#boros = gpd.GeoDataFrame.from_file('project/Output/OwithBG.shp')
#boros.plot()

boros.head()

# # These data have the polygon 'geometry' informaiton

#show the plot of geopandas
boros.geometry[1245]

#read and rename the car data
flux = pd.read_csv('../../data/influxmap.csv')
#flux1 = pd.read_csv('project/Output/influxmap_blockgroup.csv')
flux = flux.rename(columns={'Unnamed: 0':'OBJECTID'})

#show data
flux.head()

# # merge the car2go data with the block data

#split the data - flux in vs flux out
flux_in = flux.where(flux>0,0)
flux_out = -flux.where(flux<0,0)

#transplant the ID
flux_out['OBJECTID'] = flux['OBJECTID']
flux_out.head()

#merge the data by OBJECTID
flux_map = pd.merge(boros, flux, on=['OBJECTID'])

#continue to merge
flux_map_in = pd.merge(boros, flux_in, on=['OBJECTID'])
flux_map_out = pd.merge(boros, flux_out, on=['OBJECTID'])

#this function used for plotting the map
def plot_flux(hour,size,flux_map,direction):
    """
    plot the map and save the images to current folder
    direction 'in' or 'out'
    hour range (0-23)
    size 60,80 can be used
    flux_map should be geopanda data
    """
    if direction == 'out':
        cmapstr = 'Reds'
        filename1 = 'fluxmapOut'
    else:
        if direction == 'in':
            cmapstr = 'Blues'
            filename1 = 'fluxmapIn'

    fig2 = flux_map.plot(column=str(hour), cmap=cmapstr,figsize=(size))#viridis

    filename = filename1 + str(hour) + '.png'
    plt.savefig(filename)
    plt.show()


flux_map.columns


#fig1 = flux_map_in.plot(column='0', cmap='Blues',figsize=(40,50))
#plt.show()


# # ploting

#write the image files by a loop (0-23 hours)
for i in range(0,24):
    plot_flux(i,(80,100),flux_map_in,'in')

#write the image files
for i in range(0,24):
    plot_flux(i,(80,100),flux_map_out,'out')

#plot the histogram of one block
#plt.style.use('ggplot')
flux.loc[0].plot.bar(legend=False,figsize=(10,6))

#fig1 = flux_map_out.plot(column='0', cmap='Reds',figsize=(40,50))
#plt.show()

#try to draw the map
temp_shp = gpd.GeoDataFrame.from_file('project/kc_bg_10.shp')

temp_shp.plot(figsize=(50,60))

#waiting for further research
#call the google map package
#to be continue
#import gmaps
#import gmaps.datasets
#gmaps.configure(api_key=AIzaSyBTiCtthOgV4O-ZY2T5bYlqOaH_5he4YnM)

#data = gmaps.datasets.load_dataset('taxi_rides')


#m = gmaps.Map()
#m.add_layer(gmaps.Heatmap(data=data))
#m
