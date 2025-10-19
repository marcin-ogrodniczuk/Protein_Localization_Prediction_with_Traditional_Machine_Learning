import streamlit as st 
import pandas as pd 
import numpy as np 
import joblib
import pickle 
from Bio.SeqUtils.ProtParam import ProteinAnalysis

model = joblib.load('xgboost_protein_localization.pkl')
scaler = joblib.load("scaler.pkl")
encoder = joblib.load("label_encoder.pkl")

valid_aa = set ("ACDEFGHIKLMNPQRSTVWY")

def clean_sequence(seq):
    return "".join([aa for aa in seq.upper() if aa in valid_aa])

def sequence_features(seq):
    seq = clean_sequence(seq)
    if len(seq) == 0:
        return [0]*30  # placeholder for missing
    pa = ProteinAnalysis(seq)
    amino_acids = list("ACDEFGHIKLMNPQRSTVWY")
    aa_comp = [seq.count(aa)/len(seq) for aa in amino_acids]
    length = len(seq)
    molecular_weight = pa.molecular_weight()
    isoelectric_point = pa.isoelectric_point()
    aromaticity = pa.aromaticity()
    instability_index = pa.instability_index()
    gravy = pa.gravy()
    polar = sum(seq.count(aa) for aa in "DEKRQN") / length
    nonpolar = sum(seq.count(aa) for aa in "AVLIFMW") / length
    charged = sum(seq.count(aa) for aa in "DEKR") / length
    hydrophobic = sum(seq.count(aa) for aa in "AILMFWV") / length
    return aa_comp + [length, molecular_weight, isoelectric_point,
                      aromaticity, instability_index, gravy,
                      polar, nonpolar, charged, hydrophobic]

# Streamlit UI
st.title("Protein Localization Predictor (XGBoost)")


# create tabs

tab1, tab2, tab3 = st.tabs(["Predict", "Model Performance", "Feature Importance"])

#  tab 1: Prediction
with tab1:
    st.markdown("### Predict Protein Localization")
    seq_input = st.text_area("Paste protein sequence here:")

    if st.button("Predict Localization"):
        if not seq_input:
            st.warning("Please paste a protein sequence first!")
        else:
            # compute sequence features and scale
            features = np.array(sequence_features(seq_input)).reshape(1, -1)
            features_scaled = scaler.transform(features)

            # make prediction
            pred_class = model.predict(features_scaled)[0]
            pred_category = encoder.inverse_transform([pred_class])[0]

            # show main prediction result
            st.success(f"Predicted localization category: **{pred_category}**")

            # add dynamic confidence visualization
            try:
                pred_proba = model.predict_proba(features_scaled)[0]
                confidence_df = pd.DataFrame({
                    'Localization Category': encoder.classes_,
                    'Probability': pred_proba
                }).sort_values('Probability', ascending=False)

                st.markdown("#### Prediction Confidence by Class for this Sequence")
                st.bar_chart(confidence_df.set_index('Localization Category'))

            except Exception as e:
                st.warning(f"Probability estimates not available: {e}")

# tab 2: Model Performance 
with tab2:
    st.markdown("### Model Performance Metrics")
    st.metric("Accuracy", "0.78")
    st.metric("F1 Score (Macro)", "0.66")
    # Optionally display confusion matrix if you saved it
    # st.image("confusion_matrix.png")

#  tab 3: Feature Importance 
with tab3:
    st.markdown("### Feature Importance")
    try:
        importances = model.feature_importances_

        # define feature names in the same order as your sequence_features() output
        feature_names = [
            "A_freq", "C_freq", "D_freq", "E_freq", "F_freq", "G_freq", "H_freq", "I_freq", "K_freq", "L_freq",
            "M_freq", "N_freq", "P_freq", "Q_freq", "R_freq", "S_freq", "T_freq", "V_freq", "W_freq", "Y_freq",
            "length", "molecular_weight", "isoelectric_point", "aromaticity", "instability_index",
            "gravy", "polar", "nonpolar", "charged", "hydrophobic"
        ]

        # match feature importances to names
        importance_df = pd.DataFrame({
            'Feature': feature_names[:len(importances)],  
            'Importance': importances
        }).sort_values('Importance', ascending=False)

        st.bar_chart(importance_df.set_index('Feature'))

        # show top 10 features as a table
        st.markdown("#### Top 10 Most Important Features")
        st.dataframe(importance_df.head(10))

    except AttributeError:
        st.warning("Feature importance not available for this model.")

