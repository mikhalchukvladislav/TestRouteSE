from read_kmz import read_file
from distance import distance
from purge_dataframe import purge_df
import pandas as pd
pd.set_option('display.max_rows', None)
import matplotlib.pyplot as plt

if __name__ == "__main__":
    filename = input('Enter the path to the kmz file: ')
    # for example: C:/Users/Vladislav/Desktop/PYTHON/Test_Route_SE/Test_Route_SE/task_2_sensor.kml

    df = read_file(filename)

    dist = []

    for i in range(len(df)):
        try:
            dist.append(distance(df.loc[i-1]['latitude'], df.loc[i-1]['longtitude'], df.loc[i]['latitude'], df.loc[i]['longtitude']))
        except:
            dist.append(0.0)
            
    df.insert(2, 'distance', dist)

    purified_df = purge_df(df)
    distance_total = purified_df['distance'].sum() / 1000

    print(f'Total distance: {distance_total.round(2)} kilometres.')

    plt.figure(figsize=(50, 25))
    plt.scatter(purified_df['longtitude'], purified_df['latitude'])
    plt.show()