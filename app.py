import streamlit as st
import pandas as pd
import random

st.set_page_config(layout="wide")

st.markdown("""
<style>
.big-font {
    font-size:32px !important;
    color:red !important;
}
.big {
    font-size:32px !important;
}
p{
    display:inline-block;
}

</style>
""", unsafe_allow_html=True)


st.title('WordBook')
data = pd.read_excel('./data.xlsx')


def select_new():
    index = random.randint(0, len(data))
    row = data.iloc[index]
    # print(data.head())
    print(row)
    wordlist = row["Word"].split('=')
    sentence = row['Sentence'].strip().capitalize()
    word = wordlist[0].strip().capitalize()
    meaning = wordlist[1].strip().capitalize()
    st.markdown(f'<p class ="big">Word: </p> <p class="big-font">{word}<p>', unsafe_allow_html=True)  # word
    st.markdown((f'Meaning: :red[{meaning}]'))   # meaning
    st.text('Sentence : '+sentence)


st.button("Next", on_click=select_new())
st.info('Data are scrapped from a Book, Any inconsistency is remissible', icon="ℹ️")