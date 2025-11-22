
import pandas as pd

# Path to CSV (change this if your file is on Drive)


df =pd.read_csv("C:\\Users\\terah\\Downloads\\housing_quick_sale.csv")
df.head()


# Select ONLY the major predictors requested
FEATURES = ["size_sqft","bedrooms","bathrooms","has_pool","land_size_acres"]
TARGET = "sold_quickly"

X = df[FEATURES].copy()
y = df[TARGET].astype(int)

X.head(), y.head()


from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_auc_score, classification_report
import joblib
from pathlib import Path

X_tr, X_te, y_tr, y_te = train_test_split(X, y, test_size=0.25, random_state=42, stratify=y)

# Use a higher max_iter to avoid convergence warnings
model = LogisticRegression(max_iter=1000, class_weight="balanced")
model.fit(X_tr, y_tr)

probs = model.predict_proba(X_te)[:,1]
auc = roc_auc_score(y_te, probs)
print("Validation ROC AUC:", round(auc, 3))
print(classification_report(y_te, (probs>=0.5).astype(int)))

# Save model + features together
Path("models").mkdir(exist_ok=True, parents=True)
joblib.dump({"model": model, "features": FEATURES}, "models/classifier.pkl")
print("Saved → models/classifier.pkl")

!pip -q install streamlit pyngrok
!pip -q install pyngrok streamlit
!pip -q install streamlit cloudflared

%%writefile app.py
# app.py — Streamlit frontend for housing quick-sale prediction
import streamlit as st
import pandas as pd
import joblib
from pathlib import Path

st.set_page_config(page_title="🏠 Will My Home Sell Quickly?", layout="centered")

BUNDLE_PATH = Path("models/classifier.pkl")
if not BUNDLE_PATH.exists():
    st.error("Model file not found. Run the training cells above.")
    st.stop()

bundle = joblib.load(BUNDLE_PATH)
model = bundle["model"]
FEATURES = bundle["features"]

st.markdown(
    """
    <div style="background-color:yellow;padding:13px">
      <h1 style="color:black;text-align:center;">Predict How Fast Your Home Would Sell</h1>
    </div>
    """,
    unsafe_allow_html=True
)

col1, col2 = st.columns(2)
with col1:
    size_sqft = st.number_input("Home Size (sqft)", min_value=300, max_value=10000, value=2200, step=50)
    bedrooms = st.selectbox("Bedrooms", [1,2,3,4,5,6], index=2)
with col2:
    bathrooms = st.selectbox("Bathrooms", [1.0,1.5,2.0,2.5,3.0,3.5,4.0], index=2)
    has_pool_txt = st.radio("Pool?", ["No","Yes"], index=0)

land_size_acres = st.number_input(
    "Land Size (acres)",
    min_value=0.01,
    max_value=5.0,
    value=0.20,
    step=0.01,
    format="%.2f"
)

if st.button("Check"):
    row = pd.DataFrame([{
        "size_sqft": int(size_sqft),
        "bedrooms": int(bedrooms),
        "bathrooms": float(bathrooms),
        "has_pool": 1 if has_pool_txt == "Yes" else 0,
        "land_size_acres": float(land_size_acres)
    }])[FEATURES]

    proba = float(model.predict_proba(row)[0, 1])
    label = "Will Sell Quickly (≤ 30 days)" if proba >= 0.5 else "May Take Longer"

    st.metric("Probability (Sell Quickly)", f"{proba:.2%}")
    if proba >= 0.5:
        st.success(f"Prediction: {label}")
    else:
        st.warning(f"Prediction: {label}")

# running the app

!streamlit run app.py 

#!streamlit run app.py &>/dev/null&