import pandas as pd
import matplotlib
import numpy

data = pd.read_csv('Car2goOD.csv')
data.head()

df = pd.DataFrame(data)
times = pd.DatetimeIndex(df['otime'])
times.minute
# Choose the data on the hour
a=df[times.minute==0]

# Choose the data by the CarID
df.set_index(['id'])
b = df[(df['id'] == 'AXG5761')]
b.head()

# Input the data to ArcGIS
import arcpy
import arcpy.mapping 
import xlrd
# Set the working environment
path = "c:/Users/student/Destop/O"
arcpy.env.workspace = path

# Get the map document
mxd = arcpy.mapping.MapDocument("CURRENT")
# Get the data frame named 0
df = arcpy.mapping.ListDataFrames(mxd,"*")[0]
# Create a new layer named block
arcpy.MakeFeatureLayer_management('c:\Users\student\Desktop\O\kc_block_10.shp','block')
# Add the layer to the map at the bottom of the TOC in data frame 0
# arcpy.mapping.AddLayer(df, block,"BOTTOM")

# Import the excel file and convert it to table file, which is read by ArcMap
inputExcel = r'c:\Users\student\Desktop\O\Car2goOD.xls'
sheetName = "Sheet1"
memoryTable = "in_memory" + "\\" + "memoryTable"
arcpy.Delete_management(memoryTable)
arcpy.ExcelToTable_conversion(inputExcel, memoryTable,sheetName)
# arcpy.MakeXYEventLayer_management("memoryTable", "olon", "olat", "ocar_layer",r"Coordinate Systems\Geographic Coordinate System\North America\Nad 1983","")


# Display the x,y coordinates for the origin cars
try:
    # Set the local variables
    in_Table = "memoryTable.dbf"
    x_coords = "olon"
    y_coords = "olat"
    z_coords = ""
    out_Layer = "ocar_layer"
    saved_Layer = r"c:\Users\student\Desktop\O\ocar.lyr"
 
    # Set the spatial reference GCS_North_American_1983
    spRef = r"Coordinate Systems\Geographic Coordinate System\North America\Nad 1983"
 
    # Make the XY event layer
    arcpy.MakeXYEventLayer_management(in_Table, x_coords, y_coords, out_Layer, spRef, z_coords)
 
    # Print the total rows
    print(arcpy.GetCount_management(out_Layer))
 
    # Save to a layer file
    arcpy.SaveToLayerFile_management(out_Layer, saved_Layer)
 
except Exception as err:
    print(err.args[0])

# Select blocks and create a new layer by selection
# The layer that is created by the tool is temporary
arcpy.MakeFeatureLayer_management('block', 'block_lyr') 
arcpy.SelectLayerByLocation_management('block_lyr', 'intersect', 'ocar_layer')

# If features matched criteria write them to a new feature class
matchcount = int(arcpy.GetCount_management('block_lyr')[0]) 
if matchcount == 0:
    print('No Car2Go data falls in the census block')
else:
    arcpy.CopyFeatures_management('block_lyr', 'SelectedBlocks')
    print('{0} blocks have the Car2Go data written to {0}'.format(matchcount, SelectedBlocks))

arcpy.MakeFeatureLayer_management('ocar_layer', 'ocar_lyr') 
arcpy.SelectLayerByLocation_management('ocar_lyr', 'intersect', 'SelectedBlocks')
matchcount = int(arcpy.GetCount_management('block_lyr')[0]) 
if matchcount == 0:
    print('No Car2Go data falls in the census block')
else:
    arcpy.CopyFeatures_management('ocar_lyr', 'SelectedOcars')
    print('{0} blocks have the Car2Go data written to {0}'.format(matchcount, SelectedOcars))

# Join the 2 data sets
try:
    inFeatures = ["SelectedOcars","SelectedBlocks"]
    intersectOutput = "Oblock"
    # clusterTolerance = 1.5    
    arcpy.Intersect_analysis(inFeatures, intersectOutput, "ALL", "", "INPUT")

except Exception as err:
    print(err.args[0])


# arcpy.MakeXYEventLayer_management("memoryTable", "dlon", "dlat", "dcar_layer",r"Coordinate Systems\Geographic Coordinate System\North America\Nad 1983","")
# Display the x,y coordinates for the destination cars
try:
    in_Table = "memoryTable.dbf"
    x_coords = "dlon"
    y_coords = "dlat"
    z_coords = ""
    out_Layer = "dcar_layer"
    saved_Layer = r"c:\Users\student\Desktop\O\dcar.lyr"
    spRef = r"Coordinate Systems\Geographic Coordinate System\North America\Nad 1983"
    arcpy.MakeXYEventLayer_management(in_Table, x_coords, y_coords, out_Layer, spRef, z_coords)
    print(arcpy.GetCount_management(out_Layer))
    arcpy.SaveToLayerFile_management(out_Layer, saved_Layer)
except Exception as err:
    print(err.args[0])

arcpy.MakeFeatureLayer_management('block', 'block_lyr') 
arcpy.SelectLayerByLocation_management('block_lyr', 'intersect', 'dcar_layer')
matchcount = int(arcpy.GetCount_management('block_lyr')[0]) 
if matchcount == 0:
    print('No Car2Go data falls in the census block')
else:
    arcpy.CopyFeatures_management('block_lyr', 'SelectedBlocks2')
    print('{0} blocks have the Car2Go data written to {0}'.format(matchcount, SelectedBlocks))

arcpy.MakeFeatureLayer_management('dcar_layer', 'dcar_lyr') 
arcpy.SelectLayerByLocation_management('dcar_lyr', 'intersect', 'SelectedBlocks2')
matchcount = int(arcpy.GetCount_management('block_lyr')[0]) 
if matchcount == 0:
    print('No Car2Go data falls in the census block')
else:
    arcpy.CopyFeatures_management('dcar_lyr', 'SelectedDcars2')
    print('{0} blocks have the Car2Go data written to {0}'.format(matchcount, SelectedDcars2))

try:
    inFeatures = ["SelectedDcars","SelectedBlocks2"]
    intersectOutput = "dblock"
    # clusterTolerance = 1.5    
    arcpy.Intersect_analysis(inFeatures, intersectOutput, "ALL", "", "INPUT")
except Exception as err:
    print(err.args[0])


