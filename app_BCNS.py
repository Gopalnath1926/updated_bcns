import sys
import numpy as np
import pandas as pd
import pickle
import streamlit as st
import sklearn

st.write("Python:", sys.version)
st.write("streamlit:", st.__version__)
st.write("numpy:", np.__version__)
st.write("pandas:", pd.__version__)
st.write("sklearn:", sklearn.__version__)

# load model AFTER version prints
with open("model.pkl", "rb") as f:
    model = pickle.load(f)
