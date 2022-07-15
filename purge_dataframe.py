from distance import distance


def purge_df(df):
    
    index_for_drop = []
    latitude_for_drop = []
    longtitude_for_drop = []

    for i in range(len(df)):
        if df.loc[i]['distance'] > 30:
            index_for_drop.append(i)
            latitude_for_drop.append(df.loc[i]['latitude'])
            longtitude_for_drop.append(df.loc[i]['longtitude'])
    
    purified_df = df.drop(index_for_drop)
    purified_df = purified_df.reset_index(drop=True)
    
    for i in range(len(latitude_for_drop)):
        purified_df_lat = purified_df[purified_df['latitude'] == latitude_for_drop[i]]
        purified_df_long = purified_df_lat[purified_df_lat['longtitude'] == longtitude_for_drop[i]]
        purified_df = purified_df.drop(purified_df_long.index)
    
    purified_df = purified_df.reset_index(drop=True)
    
    purified_df = purified_df.drop(columns=['distance'])
    purified_df = purified_df.drop_duplicates(subset=['latitude', 'longtitude'], keep='last')
    purified_df = purified_df.reset_index(drop=True)
    
    dist = []

    for i in range(len(purified_df)):
        try:
            dist.append(distance(purified_df.loc[i-1]['latitude'], purified_df.loc[i-1]['longtitude'], purified_df.loc[i]['latitude'], purified_df.loc[i]['longtitude']))
        except:
            dist.append(0.0)
    
    purified_df.insert(2, 'distance', dist)
    
    for i in dist:
        if i > 30:
            purge_df(purified_df)
        else:
            return(purified_df)