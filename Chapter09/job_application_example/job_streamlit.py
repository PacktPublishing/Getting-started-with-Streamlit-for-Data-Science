import streamlit as st
from streamlit_lottie import st_lottie
import pandas as pd
import requests

password_attempt = st.text_input('Please Enter The Password')
if password_attempt != 'example_password':
	st.write('Incorrect Password!')
	st.stop()

def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_airplane = load_lottieurl('https://assets4.lottiefiles.com/packages/lf20_jhu1lqdz.json')
st_lottie(lottie_airplane, speed=1, height=200, key="initial")

st.title('Major US Airline Job Application')
st.write('by Tyler Richards')
st.subheader('Question 1: Airport Distance')
'''
The first exercise asks us 'Given the table of airports and 
locations (in latitude and longitude) below, 
write a function that takes an airport code as input and 
returns the airports listed from nearest to furthest from 
the input airport.' There are three steps here:

1. Load Data
2. Implement Distance Algorithm
3. Apply distance formula across all airports other than the input
4. Return sorted list of airports Distance
'''

airport_distance_df = pd.read_csv('airport_location.csv')

with st.echo():
	#load necessary data
	airport_distance_df = pd.read_csv('airport_location.csv')

'''
From some quick googling, I found that the haversine distance is 
a good approximation for distance. At least good enough to get the 
distance between airports! Haversine distances can be off by up to .5%, 
because the earth is not actually a sphere. It looks like the latitudes 
and longitudes are in degrees, so I'll make sure to have a way to account 
for that as well. The haversine distance formula is labeled below, 
followed by an implementation in python
'''
st.image('haversine.png')


