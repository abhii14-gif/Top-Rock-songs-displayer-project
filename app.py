import pandas as pd
import streamlit as st

# 1. Title and description
st.title("🎸 The 100 Great Rock Songs Explorer!")
st.write("Filter through a curated list of 100 timeless rock anthems.")

# 2. Load your new rock spreadsheet
df = pd.read_csv("songs.csv")

# 3. Create interactive sidebar filters
decade_choice = st.sidebar.selectbox("Choose a Rock Era:", ["1970s", "1980s", "1990s"])
energy_choice = st.sidebar.selectbox("Choose Energy Level:", ["High", "Low"])

# 4. Filter the spreadsheet based on BOTH choices
filtered_songs = df[(df["Decade"] == decade_choice) & (df["Energy"] == energy_choice)]

# 5. Display the matching classic tracks!
st.subheader(f"⚡ Recommended {decade_choice} Rock Tracks ({energy_choice} Energy):")
st.dataframe(filtered_songs[["Title", "Artist"]])