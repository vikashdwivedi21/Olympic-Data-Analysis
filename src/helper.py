import pandas as pd
import numpy as np

# def medal_tally(df):
#     medal_tally = df.drop_duplicates(subset=['Team', 'NOC', 'Games','Year','City','Sport','Event','Medal'])
#     medal_tally = medal_tally.groupby('region').sum()[['Gold','Silver','Bronze']].sort_values('Gold', ascending=False).reset_index()
#     medal_tally['Total'] = medal_tally['Gold']+ medal_tally['Silver']+ medal_tally['Bronze']

#     medal_tally['Gold'] = medal_tally['Gold'].astype('int')
#     medal_tally['Silver'] = medal_tally['Silver'].astype('int')
#     medal_tally['Bronze'] = medal_tally['Bronze'].astype('int')
#     medal_tally['Total'] = medal_tally['Total'].astype('int')

 
#     return medal_tally


def fetch_medal_tally(df,year,country):

    medal_df = df.drop_duplicates(subset=['Team', 'NOC', 'Games', 'Year', 'City', 'Sport', 'Event', 'Medal'])
    flag= 0
    if year == 'overall' and country=='overall':
        temp_df = medal_df

    if year == 'overall' and country != 'overall':
        flag =1
        temp_df = medal_df[medal_df['region']==country]

    if year != 'overall' and country == 'overall':
        temp_df = medal_df[medal_df['Year']==int(year)]

    if year != 'overall' and country != 'overall':
        temp_df = medal_df[(medal_df['Year']==int(year)) & (medal_df['region']==country)]

    if flag == 1:
        x = temp_df.groupby('Year').sum()[['Gold','Silver','Bronze']].sort_values('Year').reset_index()

    else :

         x = temp_df.groupby('region').sum()[['Gold','Silver','Bronze']].sort_values('Gold', ascending=False).reset_index()

    
    x['Total'] = x['Gold'] + x['Silver'] + x['Bronze']

    medal_tally['Gold'] = medal_tally['Gold'].astype('int')
    medal_tally['Silver'] = medal_tally['Silver'].astype('int')
    medal_tally['Bronze'] = medal_tally['Bronze'].astype('int')
    medal_tally['Total'] = medal_tally['Total'].astype('int')

    return x


def country_year_list(df):
    years = df['Year'].unique().tolist()
    years.sort()
    years.insert(0,'overall')

    country = df['region'].dropna().unique().tolist()
    country.sort()
    country.insert(0,'overall')

    return years,country






