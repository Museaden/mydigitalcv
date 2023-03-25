from pathlib import Path

import streamlit as st
from PIL import Image


# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "musa_cv.pdf"
profile_pic = current_dir / "assets" / "profile-pic.png"


# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital CV | Muse Aden Ahmed"
PAGE_ICON = ":wave:"
NAME = "Muse Aden Ahmed"
DESCRIPTION = """
I am skilled Data Scientist with problem-solving bussiness understanding, and communication skills. 
"""
EMAIL = "musexasan483@gmail.com"
SOCIAL_MEDIA = {
    "LinkedIn": "https://linkedin.com",
    "GitHub": "https://github.com",
    "Instagram": "https://www.instagram.com",
}
PROJECTS = {
    "🏆 COVID-19 World Vaccination - I went to know how the vaccination is going in my country and the rest world": "https://github.com/Museaden/COVID-19-World-Vaccination.git",
    "🏆 COVID-19 World Vaccination application ": "https://covid19musa-ooy0.onrender.com/",
    "🏆 Tomato Disease Prediction ": "https://github.com/Museaden/Tomato-Disease-Prediction.git",
    "🏆 Flight Price Prediction ": "https://github.com/Museaden/Flight-Price-Prediction-.git",
    "🏆 Crop Recommendation prediction ": "https://github.com/Museaden/Crop-Recommendation-Prediction.git",
    "🏆 Ecommerce textclassification ": "https://github.com/Museaden/end-end-project-ecommerce-text-classification.git",
    "🏆 Ecommerce textclassification Application ": "https://museaden-ecommerce-model-deployment-app-42emei.streamlit.app/",
    "🏆 used cars price prediction ": "https://github.com/Museaden/used-car-price-prediction.git",
    "🏆 used cars price prediction application ": "https://used-car-price-prediction.onrender.com/",
    "🏆 Loan prediction ": "https://github.com/Museaden/Loan-prediction.git",
    "🏆 Loan application ": "https://museaden-loan-streamlit-application-loan-app-iau981.streamlit.app/",
    "🏆 Climate Change: Earth Surface Temperature - I went to know how the earth's surface temperature changed from 1791 up to 2013": "https://github.com/Museaden/Climate-Change-Earth-Surface-Temperature-.git",
    "🏆 Epidemics on networks - comparing real and random networks":  "https://github.com/Museaden/Epidemics-on-networks.git",
    "🏆 height of male and female by country 2022":  "https://github.com/Museaden/Height-of-male-and-female.git",
}


st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)


# --- LOAD CSS, PDF & PROFIL PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)


# --- HERO SECTION ---
col1, col2 = st.columns(2) #gap="small")
with col1:
    st.image(profile_pic, width=230)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label=" 📄 Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    st.write("📫", EMAIL)


# --- SOCIAL LINKS ---
st.write('\n')
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")


# --- EXPERIENCE & QUALIFICATIONS ---
st.write('\n')
st.subheader("Experience & Qulifications")
st.write(
    """
- ✔️ 5 Years expereince 
- ✔️ Strong hands on experience and knowledge in Python and Excel, Data Studio, Kobo Toolbox and xlsform
- ✔️ Good understanding of statistics, Calculus, Probability and Linear aljebra 
- ✔️ Good problem solving 
"""
)


# --- SKILLS ---
st.write('\n')
st.subheader("Hard Skills")
st.write(
    """
- 👩‍💻 Programming: Python (Scikit-learn, Pandas, Dash, Numpy), SQL, R
- 📊 Data Visulization: Data Studio, MS Excel, Plotly, seaborn
- 📚 Modeling: Logistic regression, linear regression, decition trees, random forest, XGBoost etc
- 🗄️ Databases: Postgres, MySQL
"""
)


# --- WORK HISTORY ---
st.write('\n')
st.subheader("Work History")
st.write("---")

# --- JOB 1
st.write("🚧", "** Data Scientist | Delta consultant**")
st.write("07/2021 - up to know")
st.write(
    """
- ► Turn raw data into actionable insights
- ► Analyzing data using statistical techniques and proving report the organization
- ► Build models that are accurate and useful for predicting future outcomes.
- ► sharing organizations data report by using atractive dashboard in data studio, Power BI, Excel and Python.
"""
)

# --- JOB 2
st.write('\n')
st.write("🚧", "**Lecturer | New Generation University College**")
st.write("11/2019 - 03/2021")
st.write(
    """
- ► Evaluated processes and ensured appropriate learning process
- ► Participated in departmentmeetings and training programs
- ► Highly skilled in planning the strategies and applying them for the development of students
"""
)

# --- JOB 3
st.write('\n')
st.write("🚧", "**Graphic Designer | Asal Printing Price**")
st.write("09/2017 - 07/2018")
st.write(
    """
- ► Create the company logo, website and advertising graphics
- ► Design brochures, flyers, posters and other promotional materials
- ► Design print and digital advertisements
"""
)


# --- Projects & Accomplishments ---
st.write('\n')
st.subheader("Projects & Accomplishments")
st.write("---")
for project, link in PROJECTS.items():
    st.write(f"[{project}]({link})")
