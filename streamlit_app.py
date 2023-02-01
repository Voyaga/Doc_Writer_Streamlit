import streamlit as st
import numpy as np
import pandas as pd
from st_aggrid import AgGrid
import plost
from PIL import Image




seattle_weather = pd.read_csv('wallets.csv', parse_dates=['Name'])

#st.set_page_config(layout="wide")
def print_this():
    st.write('HOLY SHIT BALLS BATMAN2.0')
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

st.header('Materials and Methods')

st.subheader('Semper viverra nam libero')
st.markdown('''
Ut consequat semper viverra nam libero. Arcu vitae elementum curabitur vitae [2]. Neque convallis a cras semper auctor neque vitae tempus. Tempus quam pellentesque nec nam aliquam. Libero nunc consequat interdum varius sit amet mattis vulputate. Nibh tortor id aliquet lectus. Netus et malesuada fames ac turpis egestas. Euismod in pellentesque massa placerat duis ultricies. Amet volutpat consequat mauris nunc congue nisi. Vulputate eu scelerisque felis imperdiet proin.
''')

st.subheader('Arcu non sodales')
st.markdown('''
Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua [4]. Nibh tortor id aliquet lectus proin nibh nisl condimentum id. Laoreet id donec ultrices tincidunt [5]. In ornare quam viverra orci sagittis eu volutpat odio facilisis. Cursus turpis massa tincidunt dui ut ornare lectus sit. Quis vel eros donec ac odio tempor. Quis auctor elit sed vulputate mi. Feugiat sed lectus vestibulum mattis. Sed vulputate odio ut enim blandit volutpat. Aliquam eleifend mi in nulla. Egestas sed tempus urna et. Nisl vel pretium lectus quam id leo. Quam elementum pulvinar etiam non quam lacus suspendisse. Lectus magna fringilla urna porttitor rhoncus. Vitae tempus quam pellentesque nec nam aliquam sem et. Mauris in aliquam sem fringilla ut morbi tincidunt augue interdum.
''')

st.header('Acknowledgements')
st.warning('''
Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Nulla facilisi nullam vehicula ipsum a. Nunc faucibus a pellentesque sit amet porttitor eget dolor. Nunc sed velit dignissim sodales ut eu sem integer vitae. Vel facilisis volutpat est velit. Auctor eu augue ut lectus arcu. Habitant morbi tristique senectus et netus. Quisque sagittis purus sit amet volutpat consequat mauris nunc. Libero justo laoreet sit amet cursus sit. Sed faucibus turpis in eu. Ac orci phasellus egestas tellus rutrum. Malesuada proin libero nunc consequat. Nascetur ridiculus mus mauris vitae ultricies leo integer malesuada. Facilisi morbi tempus iaculis urna id volutpat. Mi bibendum neque egestas congue quisque egestas diam in. Nunc lobortis mattis aliquam faucibus.
''')


