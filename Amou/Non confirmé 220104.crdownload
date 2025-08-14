import streamlit as st
import base64

st.set_page_config(page_title="Portfolio - Amadou BA", page_icon="📊", layout="wide")
st.markdown(
    """
    <style>
    .stApp {
        background-image: url("Data/Logo_2.jpg");
        background-size: cover;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }
    </style>
    """,
    unsafe_allow_html=True
)
# Barre latérale de navigation
menu = st.sidebar.selectbox(
    "📂 Navigation",
    ["À propos de Amadou BA", "Compétences", "Parcours académique", "Expérience professionnelle", "Contact"]
)
# Pages
if menu == "À propos de Amadou BA":
    st.title("👨‍💻 Présentation")
    st.markdown("""
    Je suis **Amadou BA**, Data Analyst diplômé d'un Master en Statistique et Informatique Décisionnelle 
    de l’Université Alioune Diop de Bambey. Passionné par l’analyse des données, 
    la modélisation et la visualisation, je dispose d’une solide expérience dans 
    le traitement de données médicales et la création de solutions analytiques adaptées.
    """)

    st.markdown("### Photo et Carte d'identité")

    col1, col2 = st.columns(2)

    with col1:
        st.image("Data/IMG_E0749.JPG", caption="Amadou BA", width=250)

    with col2:
        st.image("Data/IMG_E1404.JPG", caption="Identité", width=250)
elif menu == "Compétences":
    st.title("🛠️ Compétences techniques")
    st.markdown("""
    Durant mon parcours académique, j'ai acquis de solides connaissances en:
                
    - **Langages** : Python, R, SQL, C, C++, Java, HTML, CSS, Scala, Spark  
    - **Base de données** : MySQL, PostgreSQL, Excel  
    - **Data Science** : modélisation, échantillonnage, estimation, tests, ML, DL (CNN, RNN)  
    - **ETL / BI** : Talend Open Studio, Power BI, Tableau  
    - **Statistiques** : Analyse exploratoire, inférence, régression, analyse de survie  
    - **Outils** : Jupyter, Git, Streamlit
    """)

elif menu == "Parcours académique":
    st.title("🎓 Parcours académique")
    st.markdown("""
- **Certificat en Intelligence Artificielle pour tous** (2024–2025) — Force_N
""")
    st.header("📄 Cetificat en IA")
    if st.checkbox("📖 Afficher le Cetificat en IA"):
        with open("data/Certificat IA Amadou BA ForceN.pdf", "rb") as f:
            base64_pdf = base64.b64encode(f.read()).decode('utf-8')
            pdf_display = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="100%" height="500px" type="application/pdf"></iframe>'
            st.markdown(pdf_display, unsafe_allow_html=True)
    st.markdown("""
- **Certificat en Entreprenariat Numérique** (2024–2025) — Force_N (En cours)
- **Certificat en Commerce Digital** (2024–2025) — Force_N (En cours)
- **Certificat en Marketing Digital** (2024–2025) — Force_N (En cours)
- **Certificat en Informatique et internet** (2024–2025) — Force_N (En cours)        
- **Master 2** (2024–2025) — Statistique et Informatique Décisionnelle, UADB, Bambey  
""")

    st.markdown("""
- **Master 1** (2022–2023) — Statistique et Informatique Décisionnelle, UADB, Bambey
""")
    st.header("📄 Attestaion M1 SID")
    if st.checkbox("📖 Afficher l'Attestation de réussite", key="attestation_reussite"):
        with open("data/Attestation M1 AmadouBA.pdf", "rb") as f:
            base64_pdf = base64.b64encode(f.read()).decode('utf-8')
            pdf_display = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="100%" height="500px" type="application/pdf"></iframe>'
            st.markdown(pdf_display, unsafe_allow_html=True)

    st.markdown("""
- **Licence 3** (2021–2022) — Statistique et Informatique Décisionnelle, UADB, Bambey
""")
    st.header("📄 Attestaion L3 SID")
    if st.checkbox("📖 Afficher l'Attestation de réussite", key="attestation_reussite_L3"):
        with open("data/Attestation L3 Amadou BA.pdf", "rb") as f:
            base64_pdf = base64.b64encode(f.read()).decode('utf-8')
            pdf_display = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="100%" height="600px" type="application/pdf"></iframe>'
            st.markdown(pdf_display, unsafe_allow_html=True)

    st.markdown("""
- **Licence 2** (2021–2022) — Statistique et Informatique Décisionnelle, UADB, Bambey
""")
    st.header("📄 Attestaion L2 SID")
    if st.checkbox("📖 Afficher l'Attestation de réussite", key="attestation_reussite_L2"):
        with open("data/Attestation passage L2 Amadou BA.pdf", "rb") as f:
            base64_pdf = base64.b64encode(f.read()).decode('utf-8')
            pdf_display = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="100%" height="500px" type="application/pdf"></iframe>'
            st.markdown(pdf_display, unsafe_allow_html=True)

    st.markdown("""
- **Licence 1** (2021–2022) — Statistique et Informatique Décisionnelle, UADB, Bambey
""")
    st.header("📄 Attestaion L1 SID")
    if st.checkbox("📖 Afficher l'Attestation de réussite", key="attestation_reussite_L1"):
        with open("data/Attestation passage L1 Amadou BA.pdf", "rb") as f:
            base64_pdf = base64.b64encode(f.read()).decode('utf-8')
            pdf_display = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="100%" height="500px" type="application/pdf"></iframe>'
            st.markdown(pdf_display, unsafe_allow_html=True)

    st.markdown("""
- **BAC S2** (2018) — Sciences experimentales, Lycée de Latmingue
""")
    st.header("📄 Attestaion BAC S2")
    if st.checkbox("📖 Afficher l'Attestation de réussite", key="attestation_reussite_BAC"):
        with open("data/Attestation du BAC.pdf", "rb") as f:
            base64_pdf = base64.b64encode(f.read()).decode('utf-8')
            pdf_display = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="100%" height="600px" type="application/pdf"></iframe>'
            st.markdown(pdf_display, unsafe_allow_html=True)
    
# Expérience professionnelle
elif menu == "Expérience professionnelle":
    st.title("💼 Expérience professionnelle")

    st.subheader("🔹 Data Analyst - Hôpital Le Dantec (Dakar)")
    st.write("📅 Depuis décembre 2024")
    st.markdown("""
    - Analyse statistique et modélisation de données médicales  
    - Visualisation et reporting santé  
    - Utilisation de SQL et Excel sur des bases de données cliniques
    """)

    st.subheader("🔹 Data Analyste & Technicien informatique - Hôpital régional de Kaolack")
    st.write("📅 Août – Novembre 2021")
    st.markdown("""
    - Traitement & analyse de données  
    - Réseaux & télécommunications  
    - Maintenance informatique  
    - Création d'une application pour l’analyse de survie en cancérologie  
    - Relations fournisseurs
    """)
elif menu == "Contact":
    st.title("📞 Contact")
    st.write("📧 Email : amadou8.ba@uadb.edu.sn / ba945218@gmail.com")
    st.write("📱 Téléphone 1 : (+221) 78 558 65 84 / 76 328 14 01")
    st.write("[🔗 LinkedIn](https://www.linkedin.com/in/amadou-ba-b7b78625a)")

    st.header("📄 CV")
    if st.checkbox("📖 Afficher le CV"):
        with open("data/CV_Amadou_BA.pdf", "rb") as f:
            base64_pdf = base64.b64encode(f.read()).decode('utf-8')
            pdf_display = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="100%" height="800px" type="application/pdf"></iframe>'
            st.markdown(pdf_display, unsafe_allow_html=True)

    st.header("📄 Lettre de motivation")
    if st.checkbox("📖 Afficher la lettre de motivation dans la page"):
        with open("data/LM Amadou BA.pdf", "rb") as f:
            base64_pdf = base64.b64encode(f.read()).decode('utf-8')
            pdf_display = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="100%" height="800px" type="application/pdf"></iframe>'
            st.markdown(pdf_display, unsafe_allow_html=True)