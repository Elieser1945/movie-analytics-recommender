import streamlit as st
import pandas as pd
import joblib
import os
from sklearn.metrics.pairwise import cosine_similarity # Tambahan library baru

# --- 1. PAGE CONFIGURATION ---
st.set_page_config(
    page_title="Movie Intelligence & Recommender Hub",
    page_icon="🎬",
    layout="wide"
)

# --- 2. CUSTOM CSS (VIVID GRADIENT + ABSTRACT WAVES + READABILITY FIXES) ---
st.markdown("""
    <style>
    .stApp {
        background: 
            url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 1440 320'%3E%3Cpath fill='none' stroke='rgba(255,255,255,0.15)' stroke-width='3' d='M0,160L48,144C96,128,192,96,288,106.7C384,117,480,171,576,165.3C672,160,768,96,864,90.7C960,85,1056,139,1152,154.7C1248,171,1344,149,1392,138.7L1440,128'/%3E%3Cpath fill='none' stroke='rgba(255,255,255,0.08)' stroke-width='2' d='M0,224L48,229.3C96,235,192,245,288,218.7C384,192,480,128,576,133.3C672,139,768,213,864,229.3C960,245,1056,203,1152,181.3C1248,160,1344,160,1392,160L1440,160'/%3E%3Cpath fill='none' stroke='rgba(255,255,255,0.05)' stroke-width='4' d='M0,64L80,85.3C160,107,320,149,480,144C640,139,800,85,960,74.7C1120,64,1280,96,1360,112L1440,128'/%3E%3C/svg%3E"),
            linear-gradient(135deg, #4338ca 0%, #6d28d9 30%, #0284c7 70%, #06b6d4 100%);
        background-size: cover;
        background-attachment: fixed;
        color: #ffffff;
    }
    [data-testid="stSidebar"] {
        background-color: rgba(30, 27, 75, 0.95);
        border-right: 1px solid rgba(255, 255, 255, 0.1);
    }
    div.stContainer {
        background: rgba(255, 255, 255, 0.08);
        padding: 15px;
        border-radius: 10px;
        border: 1px solid rgba(255, 255, 255, 0.15);
        margin-bottom: 10px;
        backdrop-filter: blur(10px);
    }
    </style>
""", unsafe_allow_html=True)

def custom_alert(text, alert_type="success"):
    color = "#22c55e" if alert_type == "success" else ("#eab308" if alert_type == "warning" else "#3b82f6")
    st.markdown(f"""
        <div style="padding:15px; background-color:rgba(0,0,0,0.4); border-left: 5px solid {color}; border-radius: 5px; color: white; margin-bottom: 1rem; font-size: 16px;">
            {text}
        </div>
    """, unsafe_allow_html=True)

# --- 3. LOAD MODELS & ON-THE-FLY COMPUTATION ---
@st.cache_resource
def load_data_and_models():
    # Hanya me-load dataframe dan vectorizer yang ringan
    df = joblib.load('df_model.pkl')
    tfidf = joblib.load('tfidf_vectorizer.pkl')
    
    # Membangun matriks sparse secara dinamis di server (ukurannya sangat kecil di memori)
    tfidf_matrix = tfidf.transform(df['soup'])
    return df, tfidf_matrix

try:
    df_model, tfidf_matrix = load_data_and_models()
except FileNotFoundError:
    st.error("Model files not found! Make sure `df_model.pkl` and `tfidf_vectorizer.pkl` are in the folder.")
    st.stop()

# --- 4. SIDEBAR: CREATOR PROFILE & CONTACT LINKS ---
with st.sidebar:
    st.markdown("### 👨‍💻 Portfolio Creator")
    st.markdown("**Elieser Pasaribu**")
    st.markdown("<p style='color: #38bdf8; font-size: 14px; margin-top: -15px;'>Data Analyst | Data Science | Machine Learning</p>", unsafe_allow_html=True)
    st.markdown("---")
    st.markdown("### 📬 Connect With Me:")
    st.markdown("🔗 [LinkedIn Profile](https://www.linkedin.com/in/elieser-pasaribu/)")
    st.markdown("📧 [Send Email](mailto:elieserpasaribu15@gmail.com)")
    st.markdown("📂 [GitHub Repository](https://github.com/Elieser1945)")
    st.markdown("---")
    st.info("💡 **About App:** Built as an end-to-end data product combining exploratory business analytics and machine learning.")

# --- 5. MAIN HEADER & APP PURPOSE ---
st.title("🎬 Movie Intelligence & Recommender Hub")
st.markdown("""
**AI-Powered Film Analytics & Recommendation Platform**  
This interactive web application bridges **Financial & Business Analysis (Data Analytics)** with **Machine Learning Recommender Systems (Data Science)**. 
It is designed to evaluate the commercial performance of films (budget, revenue, and ROI) while seamlessly generating personalized content-based recommendations.
""")
st.markdown("---")

# --- 6. USER CONTROL PANEL (MOVIE SELECTION) ---
st.subheader("🔍 Select a Movie to Analyze")
movie_list = sorted(df_model['title'].dropna().unique())
selected_movie = st.selectbox("Type or select a movie title:", movie_list)

movie_data = df_model[df_model['title'].str.lower() == selected_movie.lower()].iloc[0]

# --- 7. BUSINESS & FINANCIAL ANALYSIS ---
st.markdown("---")
st.header(f"💡 Business & Financial Analysis — *{movie_data['title']}*")

budget = movie_data['budget'] if pd.notnull(movie_data['budget']) else 0
revenue = movie_data['revenue'] if pd.notnull(movie_data['revenue']) else 0

if budget > 0:
    roi = ((revenue - budget) / budget) * 100
    roi_str = f"{roi:.2f}%"
else:
    roi_str = "N/A (Budget 0)"

col1, col2, col3, col4 = st.columns(4)
col1.metric("Production Budget", f"${budget:,.0f}" if budget > 0 else "N/A")
col2.metric("Box Office Revenue", f"${revenue:,.0f}" if revenue > 0 else "N/A")
col3.metric("Estimated ROI", roi_str)
col4.metric("Audience Rating", f"{movie_data['vote_average']} / 10 ({int(movie_data['vote_count'])} votes)")

st.markdown("### 💡 Executive Summary & Financial Health:")
if budget > 0 and revenue > 0:
    if revenue > budget * 2:
        custom_alert(f"<b>Box Office Hit!</b> <i>{movie_data['title']}</i> demonstrated strong commercial performance, generating revenue far above its production budget.", "success")
    elif revenue >= budget:
        custom_alert(f"<b>Break-Even / Profitable:</b> The film successfully covered its production costs and yielded a positive return.", "success")
    else:
        custom_alert(f"<b>Underperformed:</b> Box office revenue has not fully covered the total production budget.", "warning")
else:
    custom_alert("Detailed financial data (budget/revenue) is not fully recorded for this title in the dataset.", "info")

st.markdown("### 📖 Synopsis & Plot Details")
st.write(movie_data['overview'] if pd.notnull(movie_data['overview']) else "Synopsis not available.")

# --- 8. AI-POWERED RECOMMENDER SYSTEM ---
st.markdown("---")
st.header(f"✨ AI Movie Recommendations")
st.markdown(f"Based on content similarity analysis (genres, *cast*, director, and *overview*), here are recommended films if you like **{selected_movie}**:")

top_n = st.slider("Number of Recommendations:", min_value=3, max_value=10, value=5, key="slider_reco")

try:
    idx = df_model[df_model['title'].str.lower() == selected_movie.lower()].index[0]
    
    # [TEKNIK BARU] Hitung Cosine Similarity HANYA untuk film yang dipilih terhadap semua film lainnya
    sim_scores = cosine_similarity(tfidf_matrix[idx], tfidf_matrix).flatten()
    
    # Urutkan berdasarkan skor tertinggi
    sim_scores_list = list(enumerate(sim_scores))
    sim_scores_list = sorted(sim_scores_list, key=lambda x: x[1], reverse=True)
    sim_scores_list = sim_scores_list[1:top_n+1]
    
    movie_indices = [i[0] for i in sim_scores_list]
    rec_df = df_model.iloc[movie_indices][['title', 'vote_average', 'vote_count', 'release_year', 'revenue']].reset_index(drop=True)
    
    for i, row in rec_df.iterrows():
        with st.container():
            col_a, col_b, col_c = st.columns([3, 1, 1])
            with col_a:
                st.subheader(f"{i+1}. {row['title']} ({int(row['release_year']) if pd.notnull(row['release_year']) else 'N/A'})")
            with col_b:
                st.metric("Rating", f"{row['vote_average']} / 10")
            with col_c:
                rev = row['revenue'] if pd.notnull(row['revenue']) else 0
                st.metric("Revenue", f"${rev/1e6:.1f}M" if rev > 0 else "N/A")
            st.markdown("---")
            
except Exception as e:
    st.error(f"An error occurred while processing recommendations: {e}")