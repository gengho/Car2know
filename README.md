# Organization of the project
The project has the following structure:
```
Car2know/
  |- Car2know/
     |- __init__.py
     |- analysis/
     	|- ...
     |- tests/
        |- ...
  |- docs/
     |- DataSet.md
     |- Tech Rev.pptx
     |- Presentation Ver3.pptx
  |- data/
     |- ...
  |- examples/
     |- ...
  |- .gitignore
  |- LICENSE
  |- Project Overview.md
  |- README.md
  |- setup.py
  ```

# Packages

## Package introduction

### Urllib2

#### About this package:
* The urllib2 module defines functions and classes which help in opening URLs (mostly HTTP) from car2go’s api
* Using Request, urlopen function to fetch data
* Storing the data in a txt file named the data’s date

#### Dependencies (Required Packages):
* pandas
* numpy

#### Using the package:
```
from urllib2 import Request, urlopen, URLError
request = Request("http://www.car2go.com/api/v2.1/vehicles?loc=" + city + "&oauth_consumer_key=" key "&format=json")
response = urlopen(request)
response.read()
```

### Arcpy

#### About this package:
Perform geographic data analysis, data conversion, data management, and map automation with Python. Gives us the ability to quickly prototype and test scripts in an interactive environment while still being powerful enough to support the writing of large applications.

#### Dependencies (Required Packages):
* Python
* ArcGIS

#### Using the package:
```
import arcpy
import arcpy.mapping
arcpy.env.workspace = 'C:/...'

```

### GepPandas

#### About this package:
An open source project to make working with geospatial
data in python easier. GeoPandas extends the datatypes used by pandas. A GeoDataFrame is a tabular data structure that contains a GeoSeries. Always has one GeoSeries column that holds a special status. This GeoSeries is referred to as the Geo DataFrame‘s
“geometry”

#### Dependencies (Required Packages):
fiona

#### Using the package:
```
pip install fiona
git clone https://github.com/geopandas/geopandas.git
cd geopandas
pip install 

import shapely
import geopandas 
import pysal from scipy import ndimage
```

## How to install
Here are how to install packages:
1. Download miniconda and install it on your system and use the conda command-line tool to update your package listing and install the IPython notebook

2. Update conda's listing of packages for your system:
$ conda update conda

3. Install IPython notebook and all its requirements
$ conda install ipython-notebook

4. Install Python's Data Science packages
$ conda install numpy pandas matplotlib

5. Specfic Package
	1. If you are already an Anaconda user, you can simply run the command:```conda install fiona```. This will install the most recent published fiona release from the related repository, along with all dependencies.

	2. Alternatively, it is possible to install from PyPI using pip:```pip install fiona```.

## License
This project utilizes the MIT license.







