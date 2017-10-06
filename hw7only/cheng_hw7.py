
# coding: utf-8

# before use this script, you should have the following packages
# you can install GeoPandas git clone https://github.com/kjordahl/geopandas 
# and then install it with 
# <pre><code>
#     python setup.py install
#     conda install fiona
#     conda install pysal
# </code></pre>
# 
# yxcheng@uw.edu
# Yuxuan Cheng
# https://sites.google.com/view/ycheng

# In[1]:

import shapely
import geopandas as gpd


# In[2]:

import pandas as pd
import numpy as np

import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns
#from matplotlib import interactive
#interactive(True)
#%matplotlib inline


# In[3]:

import pysal
from scipy import ndimage
#p1 = shapely.geometry.Polygon([(0, 0), (1, 0), (1, 1)])
#p2 = shapely.geometry.Polygon([(0, 0), (1, 0), (1, 1), (0, 1)])
#p3 = shapely.geometry.Polygon([(2, 0), (3, 0), (3, 1), (2, 1)])
#g = gpd.GeoSeries([p1,p2,p3])
#g.area
#g.plot()
#matplotlib.pyplot.show()


# In[4]:

#road the data
boros = gpd.GeoDataFrame.from_file('project/Output/SelectedBlocks.shp')


# In[ ]:

#show the first data frame
boros.ix[0]
#boros.blocks


# In[ ]:

#plot the dataframe
boros.plot()
matplotlib.pyplot.show()


# In[ ]:

#get the data(future will read antother dataset)
boros['InCount'] = boros['OBJECTID'].mod(255)


# In[ ]:

#show the range of OBJECCTID
boros['OBJECTID'].max()


# In[ ]:

#show the name of the “geometry” column of gpd
boros.geometry.name


# In[ ]:

#create the centroid of each block (point data)
boros['centroid_column'] = boros.centroid


# In[ ]:

#show the data
boros.head()


# In[ ]:

#change the name of column
boros.rename(columns={'centroid_column': 'centroid_XY'})


# In[ ]:

#plot the blocks and "In Count"
#%matplotlib qt
fig1 = boros.plot(column='InCount', cmap='viridis')
#fig1.colorbar()
plt.show()
plt.colorbar
plt.savefig('map2.pdf')


# In[ ]:

#the hel
def heatmap(d, bins=(100,100), smoothing=1.3, cmap='viridis'):
    """
    plot the heat map
    This function takes a GeoDataFrame with point geometries and shows a matplotlib plot of heatmap density 
    """
    def getx(pt):
        return pt.coords[0][0]

    def gety(pt):
        return pt.coords[0][1]

    x = list(d.geometry.apply(getx))
    y = list(d.geometry.apply(gety))
    heatmap, xedges, yedges = np.histogram2d(y, x, bins=bins)
    extent = [yedges[0], yedges[-1], xedges[-1], xedges[0]]
    
    #using numpy's 2D histogram binning with smoothing from scipy
    logheatmap = np.log(heatmap)
    logheatmap[np.isneginf(logheatmap)] = 0
    logheatmap = ndimage.filters.gaussian_filter(logheatmap, smoothing, mode='nearest')
    
    plt.imshow(logheatmap, cmap=cmap, extent=extent)
    plt.colorbar()
    plt.gca().invert_yaxis()
    plt.show()


# In[ ]:

#create a new data whose “geometry” column is the center of blocks (point geometries)
boros_point = boros.set_geometry('centroid_column')


# In[ ]:

#plot the piont data
boros_point.plot()
plt.show()


# In[ ]:

#plot the heat map
heatmap(boros_point, bins=50, smoothing=1.5)


# In[ ]:



