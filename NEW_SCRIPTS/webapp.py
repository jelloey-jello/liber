"""
Aromatic Compound Explorer Web App

This Streamlit app performs the following:
1. Scrapes aromatic compound names from Wikipedia.
2. Retrieves molecular data from PubChem and calculates additional properties using RDKit.
3. Displays the data in a searchable table.
4. Visualizes basic statistics via matplotlib.
5. Displays 2D and 3D molecular structures using RDKit and py3Dmol.
6. Performs similarity search for structurally similar compounds.
7. Simulates chemical interactions via a mock T5Chem/ChemCrow-style checker.
8. Allows data export to CSV and JSON.

In case you get import warnings: pip install streamlit requests bs4 pandas matplotlib rdkit py3Dmol json

To run: 'streamlit run "NEW SCRIPTS/webapp.py"' in the terminal

To stop once code runs: CTRL + C

fun note: running "pwd" in the terminal will show you the current working directory

Path: "cd /Users/josiahe.thompson/Library/Mobile\ Documents/com~apple~CloudDocs/G2RETRO"

To push changes from VS Code: git push -u origin main --force
(if it's still in a BLANK, run 'git rebase --continue')

Ensuring code is pushed to GitHub:

git init
git remote add origin https://github.com/jelloey-jello/https://github.com/jelloey-jello/liber.git
git branch -M main
git add .
git commit -m "Initial commit"
git push -u origin main
"""

import streamlit as st
import requests
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt
from rdkit import Chem
from rdkit.Chem import Draw, Descriptors
import py3Dmol
import time
import json

# -------------------------------
# Step 1: Scrape compound names
# -------------------------------
def get_aromatic_compound_names():
    url = "https://en.wikipedia.org/wiki/Category:Aromatic_compounds"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    items = soup.select('div#mw-pages li a')
    compound_names = [item.get_text() for item in items]
    return compound_names

# ----------------------------------------------------------
# Step 2: Get SMILES from PubChem and calculate properties
# ----------------------------------------------------------
def get_pubchem_data(name):
    base_url = f"https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/name/{name}/property/CanonicalSMILES/JSON"
    response = requests.get(base_url)
    if response.status_code == 200:
        try:
            data = response.json()['PropertyTable']['Properties'][0]
            smiles = data.get("CanonicalSMILES")
            mol = Chem.MolFromSmiles(smiles)
            if mol:
                return {
                    "Name": name,
                    "SMILES": smiles,
                    "MolecularWeight": Descriptors.MolWt(mol),
                    "LogP": Descriptors.MolLogP(mol),
                    "TPSA": Descriptors.TPSA(mol)
                }
        except (KeyError, IndexError):
            return None
    return None

# ----------------------------
# Step 3: Get Similar Compounds
# ----------------------------
def get_similar_compounds(smiles):
    url = f"https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/similarity/smiles/{smiles}/JSON?Threshold=90&MaxRecords=5"
    response = requests.get(url)
    if response.status_code == 200:
        try:
            cids = response.json()['IdentifierList']['CID']
            names = []
            for cid in cids:
                name_url = f"https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/cid/{cid}/property/IUPACName/JSON"
                name_response = requests.get(name_url)
                if name_response.status_code == 200:
                    name = name_response.json()['PropertyTable']['Properties'][0]['IUPACName']
                    names.append(name)
            return names
        except:
            return []
    return []

"""

# ----------------------------
# Step 4: Visualization helpers
# ----------------------------
def display_structure_image(smiles):
    mol = Chem.MolFromSmiles(smiles)
    if mol:
        st.image(Draw.MolToImage(mol, size=(300, 300)), caption="2D Structure")

def display_3d_structure(smiles):
    mol = Chem.MolFromSmiles(smiles)
    if mol:
        mblock = Chem.MolToMolBlock(Chem.AddHs(mol))
        viewer = py3Dmol.view(width=400, height=300)
        viewer.addModel(mblock, "mol")
        viewer.setStyle({"stick": {}})
        viewer.zoomTo()
        st.components.v1.html(viewer._make_html(), height=300)

# --------------------------------
# Step 5: Simulate Chemical Interaction
# --------------------------------
def simulate_interaction(smiles_list):
    # Simulated knowledge base
    if len(smiles_list) < 2:
        return "Please select at least 2 compounds."
    simulated_output = "Mixing these compounds may result in a high-energy aromatic reaction. Check thermochemistry and toxicity!"
    return simulated_output

# ----------------------
# Step 6: Streamlit App
# ----------------------
st.title("🧪 Aromatic Compound Explorer")

with st.spinner("Scraping and fetching compound data (may take ~1 min)..."):
    names = get_aromatic_compound_names()
    data = []
    for name in names:
        d = get_pubchem_data(name)
        if d and d['SMILES']:  # only include valid entries
            data.append(d)
        time.sleep(0.3)  # respectful delay
    df = pd.DataFrame(data)

st.success(f"Loaded {len(df)} compounds!")

# Display compound table
st.dataframe(df)

# Export section
st.subheader("💾 Download Data")
st.download_button("Download as CSV", df.to_csv(index=False), "compounds.csv")
st.download_button("Download as JSON", json.dumps(df.to_dict(orient="records")), "compounds.json")

# Histogram visualization
st.subheader("📊 Compound Molecular Weight Distribution")
fig, ax = plt.subplots()
df['MolecularWeight'].dropna().plot(kind='hist', bins=20, ax=ax)
ax.set_xlabel("Molecular Weight")
st.pyplot(fig)

# Select a compound
st.subheader("🔍 Explore a Compound")
selected = st.selectbox("Select a compound:", df['Name'])
compound = df[df['Name'] == selected].iloc[0]

st.write(f"**Name:** {compound['Name']}")
st.write(f"**SMILES:** {compound['SMILES']}")
st.write(f"**Molecular Weight:** {compound['MolecularWeight']:.2f}")
st.write(f"**LogP:** {compound['LogP']:.2f}")
st.write(f"**TPSA:** {compound['TPSA']:.2f}")

display_structure_image(compound['SMILES'])
display_3d_structure(compound['SMILES'])

# Similar compounds
st.subheader("🔗 Similar Compounds (90%+ similarity)")
similar = get_similar_compounds(compound['SMILES'])
if similar:
    for s in similar:
        st.write("-", s)
else:
    st.write("No similar compounds found.")

# Interaction checker
st.subheader("🧠 Simulate Chemical Interaction")
selected_names = st.multiselect("Choose compounds to mix:", df['Name'])
selected_smiles = df[df['Name'].isin(selected_names)]['SMILES'].tolist()
if st.button("Check Interaction"):
    result = simulate_interaction(selected_smiles)
    st.info(result)

"""