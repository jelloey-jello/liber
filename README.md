# liber

This is a **Streamlit-based web app** that allows users to explore aromatic compounds scraped from Wikipedia. The app fetches molecular data from **PubChem**, displays **2D and 3D structures**, and offers basic visualization and similarity search features. It’s a great starting point for chemical informatics and SMILES-based applications.

---

## 🚀 Features

1. **Wikipedia Scraper**  
   Scrapes compound names from [Wikipedia’s Aromatic Compounds category](https://en.wikipedia.org/wiki/Category:Aromatic_compounds).

2. **PubChem Integration**  
   Retrieves chemical properties such as:
   - SMILES
   - Molecular Weight
   - Boiling Point
   - Melting Point

3. **Searchable Table & Filtering**  
   Displays chemical info in a clean Pandas DataFrame.

4. **2D + 3D Visualization**  
   - **2D** structure using **RDKit**  
   - **3D** interactive viewer using **py3Dmol**

5. **Similarity Search**  
   Finds structurally similar molecules (90%+ Tanimoto similarity) using the PubChem similarity endpoint.

6. **Interactive HashMap**  
   Converts English compound names into SMILES strings.

7. **“What Happens if These Mix?” (Simulated)**  
   Simulates logic from models like **T5Chem** or **ChemCrow** to hypothetically explore reactions or hazards between selected SMILES compounds.

8. **Data Export**  
   Export results to **CSV** or **JSON** with one click.

---

## ⚙️ Setup Instructions

### ✅ Recommended (pip-based)
Install dependencies from the pip requirements file:
```bash
pip install -r requirements-pip.txt
```

### 🧪 Alternate (if using Conda/Miniconda)
Recommended for RDKit and py3Dmol:
```bash
conda install --file requirements-conda.txt -c conda-forge
```

Alternatively, you can run the following:

```bash
pip install streamlit requests bs4 pandas matplotlib rdkit py3Dmol json
```

---

## 💻 How to Run the App

1. Save the script as `app.py`  
2. Open terminal and run:
```bash
streamlit run app.py
```

---

## 📂 Requirements Files

- [`requirements-pip.txt`](./requirements-pip.txt) — For pip-based installs
- [`requirements-conda.txt`](./requirements-conda.txt) — For conda-based installs

---

## 📝 Notes

- Make sure you have **Python 3.8–3.12** installed.
- You’ll need a **stable internet connection** to fetch data from Wikipedia and PubChem.
- Some compound names may not have SMILES strings; these are skipped automatically.
