import streamlit as st
import plotly.express as px
from utils import upload_data, artist_filter, frequency_calculator, pie_graph_artist, music_fq, most_played_songs, most_popular_album

df = upload_data()

st.title('Most played songs on Spotify')
artist = st.selectbox('Choose an artist:', df['artist'].unique(), placeholder='Artist', index=None)

artist_data = artist_filter(df, artist)
artist_fq, all_fq = frequency_calculator(df, artist)

if artist!= None:
    st.write(f'Analysis of {artist}:')

    pie_graph = pie_graph_artist(artist, artist_fq, all_fq)
    fig = px.pie(pie_graph, names='Artist', title='Artist Presence in Spotify’s Top 1000', values='All', hole=0.3)
    st.plotly_chart(fig)

    num_music = music_fq(df, artist)
    st.write(f'The artist {artist} has {num_music} musics on the top 1000 most played in spotify')
    mps = most_played_songs(df, artist)
    st.dataframe(mps, hide_index=True)

    mpa = most_popular_album(df, artist)
    st.write(f'Most popular album of {artist}: {mpa}')

