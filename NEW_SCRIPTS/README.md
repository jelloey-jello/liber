# 🧪 Chemical Reaction Web App

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

## 🧩 GitHub Setup & Auto Push (Optional)
To automatically push your changes to GitHub every time your code updates:

1. Clone your GitHub repo locally

If you haven’t already:

```bash
git clone https://github.com/YOUR_USERNAME/YOUR_REPO.git
cd YOUR_REPO
```

2. Set the upstream and default branch

```bash
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO.git
git pull origin main  # optional, if the remote already has code
```

3. Add the auto-push script

```python
import os
import time

FOLDER_TO_WATCH = '.'  # or the path to your project
POLL_INTERVAL = 5  # seconds

def has_changes():
    return os.system('git diff --quiet') != 0

def push_changes():
    os.system('git add .')
    os.system('git commit -m "Auto update from local changes"')
    os.system('git push')

print("Watching for changes... Press Ctrl+C to stop.")
try:
    while True:
        if has_changes():
            push_changes()
        time.sleep(POLL_INTERVAL)
except KeyboardInterrupt:
    print("Stopped watching.")
```

Then run the script in the background:
```bash
python auto_push_on_change.py
```

✅ Now any change you make and save will automatically push to your GitHub repo!