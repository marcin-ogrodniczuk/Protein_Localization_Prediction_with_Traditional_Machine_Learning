# Protein_Localization_Prediction_with_Traditional_Machine_Learning
This project predicts the subcellular localization of proteins based on their amino acid sequences and biochemical traits using traditional machine learning methods and deploys an interactive Streamlit dashboard for predictions. 


# What problem does this project address?
Proteins are functional workhorses of the cell, participating in nearly every biological process. Each protein's function is closely related to where it localizes in the cell, however determining a protein's subcellular location through wet-lab experimentation is costly, time consuming, and often incomplete. This project leverages machine learning to predict a protein's subcellular location directly from its amino acid sequence and biochemical properties, providing a faster and scalable alternative to wet-lab experimentation. 

# Motivation 
Understanding protein localization is crucial for:
- Drug Development: mislocalized proteins can alter drug targeting.
- Disease Modeling: localization shifts often drive cancer and neurodegenerative diseases.
- Bioinformatic automation: speeds up annotation of newly sequenced proteins.

# Data Pipeline
1. Data Collection 

Protein sequence data were scraped from [UniProt](https://www.uniprot.org/uniprotkb?facets=reviewed%3Atrue&query=*), the dataset includes amino acid sequences and annotated subcellular localization labels.

2. Feature Engineering

Each protein sequence was transformed into a feature vector capturing biochemical and biophysical properties including:
- Amino acid composition
- Sequence length
- Molecular weight
- Isoelectice point (pI)
- Aromaticity
- Hydrophobicity

3. Preprocessing
- Numeric features were standardized using StandardScaler.
- Localization categories were encoded using LabelEncoder.
- Data were split into training (80%) and testing (20%) sets.

# Models Tested 
| Model                | Accuracy | F1 (Macro) |
| -------------------- | -------- | ---------- |
| Logistic Regression  | 0.55     | 0.41       |
| Random Forest        | 0.63     | 0.51       |
| **XGBoost**          | **0.78** | **0.66**   |
| HistGradientBoosting | 0.78     | 0.67       |


# Deployment 

An interactive Streamlit app lets users:
- Paste a protein sequence
- Predict localization class
- Visualize model confidence and feature importance

# Tech Stack 
- Python (Pandas, NumPy, Scikit-learn, Biopython, XGBoost)
- Streamlit for dashboard
- Matplotlib/Seaborn for visualization 
- Joblib for model serialization

# Repository Structure 
protein_localization_prediction_ML/
│
├── app.py                     # Streamlit dashboard
├── protein_localization.ipynb # Full training + preprocessing workflow
├── xgboost_protein_localization.pkl  # Trained model
├── scaler.pkl                 # Scaler for app
├── label_encoder.pkl          # Label encoder
├── README.md                  # Project documentation
└── data/
    ├── uniprot_sprot.fasta.gz
    └── uniprot_data.tsv

# Author 
Marcin Ogrodniczuk
Data Science Master's Student 
