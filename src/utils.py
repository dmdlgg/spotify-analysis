import pandas as pd

def upload_data():
    df = pd.read_csv(r'.\data\spotify_tracks.csv')
    df = df.sort_values(by='artist')
    return df

def artist_filter(df, artist):
    artist_data = df.loc[df['artist'] == artist]
    artist_data = artist_data[['track_name', 'album']]
    artist_data = artist_data.rename(columns={'track_name': 'Music', 'album': 'Album'})
    return artist_data

def frequency_calculator(df, artist):
    artist_fq = df.loc[df['artist']==artist]
    artist_fq = artist_fq.value_counts('artist').sum()

    all_fq = df.loc[df['artist']!=artist]
    all_fq = all_fq.value_counts('artist').sum()

    return artist_fq, all_fq

def pie_graph_artist(artist, artist_fq, all_fq):
    pie_df = pd.DataFrame({
        'Artist': [artist, 'Others Artists'],
        'All': [artist_fq, all_fq - artist_fq]
    })
    return pie_df

def music_fq(df, artist):
    return df[df['artist'] == artist].shape[0]


def most_played_songs(df, artist):
    mps = df.loc[df['artist']==artist]
    mps = mps.rename(columns={'track_name': 'Most popular songs:'})
    mps = mps.sort_values(by='popularity', ascending=False)
    mps = mps['Most popular songs:']
    return mps

def most_popular_album(df, artist):
    mpa = df.loc[df['artist']==artist]
    mpa = mpa.sort_values(by='popularity', ascending=False).iloc[0]['album']
    return mpa