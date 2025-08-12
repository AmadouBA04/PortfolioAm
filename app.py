import streamlit as st
import base64
import os

# Fonction pour convertir une image → base64
def get_base64_img(img_path):
    if os.path.exists(img_path):
        with open(img_path, "rb") as f:
            return base64.b64encode(f.read()).decode()
    else:
        st.error(f"❌ Image introuvable : {img_path}")
        return None

st.set_page_config(page_title="Portfolio - Amadou BA", page_icon="📊", layout="wide")

# Charger l'image depuis le dossier Amou
img_base64 = get_base64_img("Amou/OIP2.webp")

# Appliquer en arrière-plan uniquement si l'image est trouvée
if img_base64:
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("data:image/webp;base64,{img_base64}");
            background-size: cover;
            background-repeat: no-repeat;
            background-attachment: fixed;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )
# Fonction affichage PDF
def afficher_pdf(path):
    if os.path.exists(path):
        with open(path, "rb") as f:
            base64_pdf = base64.b64encode(f.read()).decode('utf-8')
            pdf_display = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="100%" height="500px"></iframe>'
            st.markdown(pdf_display, unsafe_allow_html=True)
    else:
        st.warning(f"Fichier non trouvé : {path}")
# Navigation
menu = st.sidebar.selectbox(
    "📂 Navigation",
    ["À propos de Amadou BA", "Compétences", "Parcours académique", "Expérience professionnelle", "Contact"]
)
# Section : À propos
if menu == "À propos de Amadou BA":
    st.title("👨‍💻 Présentation")
    st.markdown("""
    Je suis **Amadou BA**, Data Analyst titulaire d’un Master en Statistique et Informatique Décisionnelle de l’Université Alioune Diop de Bambey.
Fort d’une solide formation académique allant de la Licence en Mathématiques, Physique, Chimie et Informatique au Master 2, j’ai acquis une expertise approfondie en analyse statistique, modélisation et data science.
Mon parcours m’a permis de maîtriser la conception et la gestion d’entrepôts de données avec Talend Open Studio, ainsi que l’utilisation des SGBD relationnels tels que MySQL, PostgreSQL et Excel.
Je possède de solides compétences en interrogation de données (SQL) et en visualisation à travers des outils comme Power BI et Tableau.
Je maîtrise également les techniques statistiques avancées, l’apprentissage automatique (Machine Learning) et le Deep Learning (CNN, RNN).
Mes compétences en programmation incluent Python, R, Java, HTML, CSS, PHP et Scala, me permettant de concevoir des solutions analytiques complètes.
J’ai une expérience notable dans le traitement et l’analyse de données médicales, notamment à l’Hôpital Le Dantec et à l’Hôpital Régional de Kaolack.
J’ai travaillé sur des projets de visualisation et reporting santé, ainsi que sur la mise en place d’applications analytiques spécialisées.
Mon approche allie rigueur scientifique, esprit analytique et souci de l’efficacité opérationnelle.
Passionné par la transformation des données en informations stratégiques, je m’engage à fournir des analyses claires et des solutions adaptées aux besoins métiers.
    """)
    st.markdown("### Photo")
    col1, col2 = st.columns(2)
    with col1:
        if os.path.exists("Amou/IMG_E0749.jpg"):
            st.image("Amou/IMG_E0749.jpg", caption="Amadou BA", width=250)
# Section : Compétences
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
    st.markdown("# Projets réalises")
    
    st.header("📄 Projet Traitement des donnees, DATA Mining, Econometrie et Actuariat")
    if st.checkbox("📖 Afficher le document du Projet", key="DPTDMEA"):
        afficher_pdf("Amou/Examen DATA Maning NGOM DAPSA Groupe 3.pdf")
        
    st.header("📄 Projet Modèles Linéaires Généralisés (GLM) sur Données Réelles")
    if st.checkbox("📖 Afficher le document du Projet", key="DPMLG"):
        afficher_pdf("Amou/Examen MLG Amadou BA.pdf")

    st.header("📄 Projet Intégration de Données Applications aux entrepôts de données")
    if st.checkbox("📖 Afficher le document du Projet", key="DPI"):
        afficher_pdf("Amou/Projet Examen Integration de Données #.pdf")

    st.header("📄 Projet Séries temporelles")
    if st.checkbox("📖 Afficher le document du Projet", key="DPST"):
        afficher_pdf("Amou/SerieTemporelleAbaDIOP BA.pdf")
        
    st.header("📄 Projet Mesure et probabilité")
    if st.checkbox("📖 Afficher le document du Projet", key="DPMP"):
        afficher_pdf("Amou/Projet Mesure et probabilité.pdf")
    
    st.header("📄 Projet Methode classification")
    if st.checkbox("📖 Afficher le document du Projet", key="DPMC"):
        afficher_pdf("Amou/PROJET FINAL METHODES DE CLASSIFICATION.pdf")

    st.header("📄 Projet Linux et Reseau")
    if st.checkbox("📖 Afficher le document du Projet", key="DPLR"):
        afficher_pdf("Amou/Document presentation linux reseau Amadou BA et Mahmoud SIDIBE.pdf")

# Section : Parcours académique
elif menu == "Parcours académique":
    st.title("🎓 Parcours académique")
    certificats = [
        ("Certificat en Intelligence Artificielle pour tous", "Amou/Certificat IA Amadou BA ForceN.pdf", "cert_ia"),
        ("Attestaion M1 SID", "Amou/Attestation M1 AmadouBA.pdf", "att_m1"),
        ("Attestaion L3 SID", "Amou/Attestation L3 Amadou BA.pdf", "att_l3"),
        ("Attestaion L2 SID", "Amou/Attestation passage L2 Amadou BA.pdf", "att_l2"),
        ("Attestaion L1 SID", "Amou/Attestation passage L1 Amadou BA.pdf", "att_l1"),
        ("Attestaion BAC S2", "Amou/Attestation du BAC.pdf", "att_bac")
    ]
    for titre, path, key in certificats:
        st.header(f"📄 {titre}")
        if st.checkbox(f"📖 Afficher : {titre}", key=key):
            afficher_pdf(path)
# Section : Expérience professionnelle
elif menu == "Expérience professionnelle":
    st.title("💼 Expérience professionnelle")
    st.subheader("🔹 Data Analyst - Hôpital Le Dantec (Dakar)")
    st.write("🗓️ Depuis décembre 2024")
    st.markdown("""
    - Analyse statistique et modélisation de données médicales  
    - Visualisation et reporting santé  
    - Utilisation de SQL et Excel sur des bases de données cliniques
    """)
    st.subheader("🔹 Data Analyste & Technicien informatique - Hôpital régional de Kaolack")
    st.write("🗓️ Août – Novembre 2021")
    st.markdown("""
    - Traitement & analyse de données  
    - Réseaux & télécommunications  
    - Maintenance informatique    
    - Relations fournisseurs
    """)
    st.header("📄 Memoire Licence L3 SID")
    if st.checkbox("📖 Afficher le rapport de memoire ", key="mrs"):
        afficher_pdf("Amou/Memoire de licence de Amadou BA.pdf")
# Section : Contact
elif menu == "Contact":
    st.title("📞 Contact")
    st.write("📧 Email : amadou8.ba@uadb.edu.sn / ba945218@gmail.com")
    st.write("📱 Téléphone : (+221) 78 558 65 84 / 76 328 14 01")
    st.write("[🔗 LinkedIn](https://www.linkedin.com/in/amadou-ba-b7b78625a)")
    st.header("📄 CV")
    if st.checkbox("📖 Afficher le CV", key="cv"):
        afficher_pdf("Amou/CV_Amadou_BA.pdf")
    st.header("📄 Lettre de motivation")
    if st.checkbox("📖 Afficher la lettre de motivation", key="lm"):
        afficher_pdf("Amou/LM Amadou BA.pdf")
