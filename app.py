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
img_base64 = get_base64_img("Amou/oip2.webp")

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
            pdf_bytes = f.read()
        st.download_button("📄 Télécharger le PDF", data=pdf_bytes, file_name=os.path.basename(path), mime="application/pdf")
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
        if os.path.exists("Amou/img_e0749.JPG"):
            st.image("Amou/img_e0749.JPG", caption="Amadou BA", width=250)
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
        afficher_pdf("Amou/examen_data_maning_ngom_dapsa.pdf")
        
    st.header("📄 Projet Modèles Linéaires Généralisés (GLM) sur Données Réelles")
    if st.checkbox("📖 Afficher le document du Projet", key="DPMLG"):
        afficher_pdf("Amou/examen_mlg_amadou_ba.pdf")

    st.header("📄 Projet Intégration de Données Applications aux entrepôts de données")
    if st.checkbox("📖 Afficher le document du Projet", key="DPI"):
        afficher_pdf("Amou/projet_examen_integration_de_donnees.pdf")

    st.header("📄 Projet Séries temporelles")
    if st.checkbox("📖 Afficher le document du Projet", key="DPST"):
        afficher_pdf("Amou/serie_temporelle_aba_diop.pdf")
        
    st.header("📄 Projet Mesure et probabilité")
    if st.checkbox("📖 Afficher le document du Projet", key="DPMP"):
        afficher_pdf("Amou/projet_mesure_et_probabilite.pdf")
    
    st.header("📄 Projet Methode classification")
    if st.checkbox("📖 Afficher le document du Projet", key="DPMC"):
        afficher_pdf("Amou/projet_methode_classification.pdf")

    st.header("📄 Projet Linux et Reseau")
    if st.checkbox("📖 Afficher le document du Projet", key="DPLR"):
        afficher_pdf("Amou/document_presentation_linux_reseau_amadou_ba.pdf")

# Section : Parcours académique
elif menu == "Parcours académique":
    st.title("🎓 Parcours académique")
    ("- Certification en Entreprenariat Numerique (En cours)"),
    ("- Certification en Informatique et internet (En cours)"),
    ("- Certification en Markting Digital (En cours)"),
    ("- Certification en Commerce Digital (En cours)"),
    certificats = [
        ("Ceritficat d'inscription M2 SID", "Amou/Certificat_inscription_m2sid_amadou_ba.pdf", "cert_m2"),
        ("Certificat en Intelligence Artificielle pour tous", "Amou/certificat_ia_amadou_ba_forcen.pdf", "cert_ia"),
        ("Attestaion M1 SID", "Amou/attestation_m1_amadou_ba.pdf", "att_m1"),
        ("Attestaion L3 SID", "Amou/attestation_l3_amadou_ba.pdf", "att_l3"),
        ("Attestaion L2 SID", "Amou/attestation_passage_l2_amadou_ba.pdf", "att_l2"),
        ("Attestaion L1 SID", "Amou/attestation_passage_l1_amadou_ba.pdf", "att_l1"),
        ("Attestaion BAC S2", "Amou/attestation_du_bac.pdf", "att_bac")
    ]
    for titre, path, key in certificats:
        st.header(f"📄 {titre}")
        if st.checkbox(f"📖 Afficher : {titre}", key=key):
            afficher_pdf(path)
# Section : Expérience professionnelle
elif menu == "Expérience professionnelle":
    st.title("💼 Expérience professionnelle")
    st.subheader("🔹 Data Analyst - Hôpital Dakar")
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
        afficher_pdf("Amou/memoire_de_licence_de_amadou_ba.pdf")
# Section : Contact
elif menu == "Contact":
    st.title("📞 Contact")
    st.write("📧 Email : amadou8.ba@uadb.edu.sn / ba945218@gmail.com")
    st.write("📱 Téléphone : (+221) 78 558 65 84 / 76 328 14 01")
    st.write("[🔗 LinkedIn](https://www.linkedin.com/in/amadou-ba-b7b78625a)")
    st.header("📄 CV")
    if st.checkbox("📖 Afficher le CV", key="cv"):
        afficher_pdf("Amou/cv_amadou_ba.pdf")
    st.header("📄 Lettre de motivation")
    if st.checkbox("📖 Afficher la lettre de motivation", key="lm"):
        afficher_pdf("Amou/lm_amadou_ba.pdf")
