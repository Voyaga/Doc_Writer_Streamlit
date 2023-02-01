import streamlit as st
import numpy as np
import pandas as pd
from st_aggrid import AgGrid
import plost
from PIL import Image




seattle_weather = pd.read_csv('wallets.csv', parse_dates=['Name'])

#st.set_page_config(layout="wide")
def print_this():
    st.write('HOLY SHIT BALLS BATMAN2.001')
    my_file = open("wallets.txt", "w")

    item = 'HOLY SHIT BALLS BATMAN'

    my_file.write(item)


st.button('Say helloo', on_click=print_this)


st.write('Hello, *World!* :sunglasses:')
######################################################
st.markdown('*CTHub News Mate Yeah Good On Ya*')
image = Image.open('ct_top_image.PNG')

st.image(image, caption='---------------------------------------------------------------------------', width=1000)
st.markdown("<h1 style='text-align: center; color: grey;'>Crown Therapy</h1>", unsafe_allow_html=True)

st.markdown('''
**GeniDee and NeoCortex**

*Neo 'White Hat, YouTube channel, www.youtube.com/watch?v=dcqkHwC6FNQ*

''')



# "<h1 style='text-align: center; color: grey;'>'**Table 1.** Current CTHub Ledger Accounts.'</h1>", unsafe_allow_html=True
st.caption("<h3 style='text-align: center; color: grey;'>Table 1. Current CTHub Ledger Accounts.</h1>", unsafe_allow_html=True)
AgGrid(seattle_weather, height=300,)

st.header('Who are we?')
st.info('''
We are a Private Membership by Association community. Crown Therapy is a private, membership-based unincorporated organisation that operates by referral only. To access more information you must be personally referred by an existing member.
''')

#st.markdown('**Keywords:** *Streamlit*, *machine learning*, *data science*, *Python*')

st.header('Notice')
st.warning('''
Crown Therapy is a private, membership-based organisation and is functioning for humanitarian purposes and to improve the lives in our local communities. No information shared or discussed should be considered as legal or health advice. By visiting and entering this website or any of its entertainment libraries in any way you hereby agree that you entered into a private domain subject to the private membership terms of  Crown Therapy.
Crown Therapy reserves all rights and are not responsible for individual use by the Users and/or Visitors to this site. This site is proprietary in nature and controlled under special private agreement. Obtaining any material including but not limited to downloads, recording, copying of any kind, cut and paste, hand written, etc., from this site by any and all parties without express permission from Crown Therapy, is expressly forbidden. All State and Federal public entities, legal persons, offices, officers, agencies or agents are barred from extracting content from this site under any presumption of law without express permission by the Crown Therapy. All state and federal persons and offices will be held liable in their private and public capacities for any breach of these conditions. Assumed and presumed public statutory authority over the private proprietary property of Crown Therapy, contained and maintained on this site is hereby rebutted and denied without a valid quo warranto, express contract or express agreement.
  
Notice to agent is notice to principle. Notice to principle is notice to agent.
''')
video_file = open('“Until Proven Otherwise” —Two of the Top Cardiologists in the World.mp4', 'rb')
video_bytes = video_file.read()

st.video(video_bytes)

