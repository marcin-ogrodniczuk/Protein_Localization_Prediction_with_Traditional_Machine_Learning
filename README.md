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

Protein sequence data were scraped from UniProt. The dataset includes amino acid sequences and annotated subcellular localization labels.

2. Feature Engineering

Each protein sequence was transformed into a feature vector capturing biochemical and biophysical properties including:
- Amino acid composition
- Sequence length
- Molecular weight
- Isoelectice point (pI)
- Aromaticity
- Hydrophobicity
- 
