import requests
import os
import zipfile  
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.style.use('ggplot')

#print(os.getcwd())  # it would print out the dir where this py is loaded
#print(os.listdir())
#FCNSLOC = '/Users/MacBookPro/Google Drive/myPython/CS599_Zeng/fcns/'
#DATALOC = '/Users/MacBookPro/Google Drive/myPython/CS599_Zeng/data/'
DATALOC = os.getcwd() + '/../data/'

def remove_data(filename, targetloc = DATALOC):
    ''' 
    filename: can be of any single file (string),
            or files (list or tuple of strings),
            or the keyword "all" (case insensitive).
            
            Filenames only. Not paths. Specify path in targetloc instead
    '''
    # validate the targetloc
    if not os.path.isdir(targetloc):
        print('The target location is invalid')
        return -1
    else:
        targetloc += '/'

    # validate the filename
    if  ( isinstance(filename,list) or isinstance(filename,tuple) ) and \
    all(isinstance(x,str) for x in filename):
        filelist = filename
    elif isinstance(filename,str):
        if filename.upper() == 'ALL':
            filelist = [ f for f in os.listdir(targetloc) ]       
        else:
            filelist = [filename]
    else:
        print('Input error: 1st input has to be a single string, or a list/tuple of strings')
        return -2
        
    # do the deletion
    if filelist == []:
        print('The data folder is already empty')
        return 0
    else:
        try:
            print('The following file(s) has been succesfully deleted:')
            for f in filelist:
                os.remove(targetloc + f)
                print(f)
        except:
            print('\n' + 'File remove failed...')
            return -3
        else:
            return 1
        
        
        
def download_if_needed(url, outfile):
    """
    Download data from url and save to outfile
    If outfile already exists, then do nothing
    """
    if os.path.exists(outfile):
        print('The same name file already exists. No more download.')
        return 0
    else:
        print('Downloading...')
        try:
            req = requests.get(url)
            assert req.status_code == 200
        except:
            print('Download error... Double check the url')
            return -1
        
        try:
            with open(outfile, 'wb') as f:
                f.write(req.content)
        except:
            print('Write error... Double check the path')
            return -1
        else:
            print('Downloaded.')
            return 1

def get_trip_data():
    url = 'https://s3.amazonaws.com/pronto-data/open_data_year_two.zip'
    outfile = DATALOC + 'pronto_data.zip'
    download_if_needed(url, outfile)
    zf = zipfile.ZipFile(outfile)
    return pd.read_csv(zf.open('2016_trip_data.csv'))

def get_bridge_data():
    url = 'https://data.seattle.gov/resource/4xy5-26gy.csv'
    outfile = DATALOC + 'bridge_data.csv'
    download_if_needed(url, outfile)
    return pd.read_csv(outfile)

def get_weather_data():
    url = 'https://raw.githubusercontent.com/UWSEDS/homework_data/master/weather_data.csv?token=AGL1-mlvl0B-0kLT86lRXBgcGha9E60Tks5Wn-cVwA%3D%3D'
    outfile = DATALOC + 'weather_data.csv'
    download_if_needed(url, outfile)
    return pd.read_csv(outfile)

def scatterplot_birthyear_duration(data, outfilename, xcol='tripduration', ycol='birthyear'):
    members = data[~np.isnan(data.birthyear)]
    try:
        x = members[xcol]
        y = members[ycol]
        plt.scatter(y, x);
        plt.savefig(outfilename + '.pdf')
        return 1
    except:
        return 0


def plot_daily_rides():
    """Plot ride count vs time for members and day users"""
    plt.style.use('ggplot')

    data = get_trip_data()
    start_time = pd.DatetimeIndex(pd.to_datetime(data.starttime,
                                                 infer_datetime_format=True))
    groups = data.groupby([start_time.date, 'usertype'])
    grouped_data = groups.trip_id.count().unstack()

    fig, ax = plt.subplots(2, figsize=(12, 6), sharex=True)
    grouped_data['Member'].plot(ax=ax[0])
    grouped_data['Short-Term Pass Holder'].plot(ax=ax[1])

    ax[0].set_title('Annual Members')
    ax[1].set_title('Short-term Pass Users')

    ax[0].set_ylabel('Number of riders')
    ax[1].set_ylabel('Number of riders')
    return 1
       







def plot_weather_data_old(fname):
    data=pd.read_csv(fname)
    dateInd=pd.DatetimeIndex(pd.to_datetime(data.DATE, format = "%Y%m%d"))
    
    data.index = dateInd
    fig, ax = plt.subplots(2, figsize=(15, 6), sharex=False)
    ax[0].plot(data.TMAX,'r-')
    ax[0].plot(data.TMIN,'b-')
    ax[1].plot(data.PRCP,'r-')

    ax[0].set_title('Max temperature (red) and Min temperature (blue)')
    ax[1].set_title('Precipitation')

    ax[0].set_ylabel('Celsius to tenth')
    ax[1].set_ylabel('mm to tenth')
    return data

def plot_bridge_data_old(fname):
    data=pd.read_csv(fname)
    data['totCount']=data['fremont_bridge_nb'] + data['fremont_bridge_sb']
    data.index= pd.DatetimeIndex(data['date'])
    
    dailydata=data.resample('D').sum()
    fig, ax = plt.subplots(1, figsize=(15, 6), sharex=False)
    ax.plot(dailydata.totCount,'r-')
    ax.set_title('Total number of counts crossing the bridge')
    return dailydata
