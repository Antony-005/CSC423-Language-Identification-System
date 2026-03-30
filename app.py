
import streamlit as st
import joblib
import os

# ── Page config ──────────────────────────────────────────────
st.set_page_config(
    page_title="Language Identifier",
    page_icon="🌍",
    layout="centered"
)

# ── Load model ───────────────────────────────────────────────
@st.cache_resource
def load_model():
    return joblib.load("language_id_model.pkl")

model = load_model()

# ── Language flag emoji map ───────────────────────────────────
LANG_INFO = {
    "Swahili": ("🇰🇪", "#2E86AB", "Kiswahili — Widely spoken in East Africa"),
    "English": ("🇬🇧", "#A23B72", "English — International language"),
    "Sheng":   ("🏙️", "#F18F01", "Sheng — Nairobi urban slang (Swahili + English)"),
    "Luo":     ("🌊", "#C73E1D", "Dholuo — Spoken by the Luo people of Kenya & Uganda"),
}

# ── UI Layout ─────────────────────────────────────────────────
st.title("🌍 Language Identification System")
st.markdown("### Detect Swahili · English · Sheng · Luo")
st.markdown("---")

st.markdown(
    "Enter a short sentence (1–2 sentences) and click **Identify Language**."
)

user_input = st.text_area(
    "📝 Enter your text here:",
    placeholder="e.g.  Habari yako leo? / How are you? / Wacha tuende base / An gi tich matek",
    height=120
)

st.markdown("---")
predict_btn = st.button("🔍 Identify Language", use_container_width=True)

if predict_btn:
    if not user_input.strip():
        st.warning("⚠️  Please enter some text first.")
    else:
        predicted_lang = model.predict([user_input.strip()])[0]
        flag, color, description = LANG_INFO.get(
            predicted_lang, ("❓", "#888888", "Unknown language")
        )

        st.markdown("---")
        st.markdown("### 🎯 Prediction Result")

        st.markdown(
            f"""
            <div style="
                background-color:{color}22;
                border-left: 6px solid {color};
                border-radius: 8px;
                padding: 20px 24px;
                margin-top: 10px;
            ">
                <h2 style="color:{color}; margin:0">{flag} {predicted_lang}</h2>
                <p style="color:#555; margin-top:6px; font-size:15px">{description}</p>
            </div>
            """,
            unsafe_allow_html=True
        )

        st.markdown("---")
        st.markdown("**You entered:**")
        st.info(f"*{user_input.strip()}*")

st.markdown("---")
st.markdown(
    "<small style=\'color:gray\'>CSC423 NLP Term Project — Language Identification System</small>",
    unsafe_allow_html=True
)
