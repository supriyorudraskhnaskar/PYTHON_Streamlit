import streamlit as st
st.header('Supriyo')
games = st.radio(
     "What's your favorite movie game?",
     ('Cricket', 'Football', 'Hockey'))

if games == 'Cricket':
    st.write('You selected cricket.')
elif games == 'Football':
    st.write('You selected football.')
elif games == 'Hockey':
    st.write('You selected football.')
else:
    st.write("You didn't select any.")

st.header('Select from the following:')
st.subheader('Are you satisfied with the service?')
disagree = st.checkbox('Disagree')
if disagree:
    st.write('Sorry for the inconvenience!')
Neutral = st.checkbox('Neutral')
if Neutral:
    st.write('Okay how we can improve')
Agree = st.checkbox('Agree')
if Agree:
    st.write('Thank you')

name = st.text_input('Name',)