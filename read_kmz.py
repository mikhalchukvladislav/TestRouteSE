import zipfile
import pandas as pd
from bs4 import BeautifulSoup

# filename=r'C:/Users/Vladislav/Desktop/Диск/Мои доки/Личное/PYTHON/Test_Route_SE/Test_Route_SE/task_2_sensor.kml'

def read_file(filename):
    """read raw kml/kmz file"""
    if filename.upper().endswith('.KML'):    
        with open(filename, "r") as f:
            data = f.read()

    if filename.upper().endswith('.KMZ'):
        with zipfile.ZipFile(filename, "r") as f:
            data = f.read(f.namelist()[0])

    
    soup = BeautifulSoup(data,'html.parser')
    placemarks = soup.find_all('placemark')


    for x in (placemarks[0].select_one('coordinates')):
        coordinates_list = x.split()

        latitude = []
        longtitude = []

        for x in coordinates_list:
            lat = x.split(',')[1]
            long = x.split(',')[0]
            latitude.append(float(lat))
            longtitude.append(float(long))


    df = pd.DataFrame({'latitude':latitude, 'longtitude': longtitude})


    return(df)
