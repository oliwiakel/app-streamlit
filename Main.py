import streamlit as st
import pickle
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
import glob
import numpy as np 
import io
import webbrowser
import gdown
import plotly.express as px
import plotly.graph_objects as go
from rdkit import Chem
from rdkit.Chem import AllChem
from rdkit.Chem import Draw
from IPython.display import display
    
st.set_page_config(layout="wide")
@st.cache_data
@st.cache_data(ttl=1, show_spinner=False)
@st.cache_data(show_spinner=False)
def load_my_data():

    filename_0 = "Baza_Danych_FULL_names.pkl" 
    file_id0 = '1iT3NGplO2ikke8gopxvHLQD6TeI2zmfR'


    def download_file(file_id, output_name):
        url = f'https://drive.google.com/uc?id={file_id}'
        
        if os.path.exists(output_name):
            os.remove(output_name)
        try:
            # 
            gdown.download(url, output_name, quiet=False)
        except Exception as e:
            st.error(f"Błąd pobierania {output_name}: {e}")

        
    with st.spinner('Synchronizacja z Google Drive...'):
        download_file(file_id0, filename_0)
    try:
        data_0 = pd.read_pickle(filename_0)
        return data_0
    except Exception as e:
        st.error(f"Błąd wczytywania pkl: {e}")
        return pd.DataFrame(), pd.DataFrame()

# Wywołanie danych
df= load_my_data()

#%%---------------------------------------------------------------------------------------Title--------------------------------------------------------------------------------------------------------------------------------

col1, col2= st.columns([5, 5])

with col1:
    st.subheader("Baza danych")
    st.dataframe(df,height=590,use_container_width=True)

with col2:
    idx = st.slider("Wybierz indeks związku do wizualizacji", 1, 13499, 1)
    mol=df["Mol"][idx]
    m_2d = Chem.Mol(mol)
    m_2d = Chem.RemoveHs(m_2d)
    AllChem.Compute2DCoords(m_2d)
    img = Draw.MolToImage(m_2d, size=(500, 1000))
    img = img.rotate(90, expand=True)
    st.image(img, use_container_width=True)





                
