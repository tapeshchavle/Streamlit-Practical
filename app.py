import streamlit as st

# Page config
st.set_page_config(page_title="Tapesh Portfolio", page_icon="💻", layout="wide")

# Inject custom CSS
st.markdown("""
    <style>
        body {
            font-family: 'Poppins', sans-serif;
            background-color: #f9fafb;
            color: #333;
        }

        /* Navbar */
        .nav {
            position: fixed;
            top: 0; left: 0; right: 0;
            background: white;
            border-bottom: 1px solid #eee;
            padding: 15px 40px;
            display: flex;
            justify-content: space-between;
            align-items: center;
            z-index: 999;
            box-shadow: 0 2px 8px rgba(0,0,0,0.05);
        }
        .nav a {
            margin: 0 15px;
            font-weight: 600;
            text-decoration: none;
            color: #444;
            transition: 0.3s;
        }
        .nav a:hover {
            color: #2563eb;
        }

        /* Hero */
        .hero {
            height: 100vh;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            background: linear-gradient(135deg,#fdfbfb,#ebedee);
            text-align: center;
        }
        .hero h1 {
            font-size: 56px;
            font-weight: 800;
            margin-bottom: 10px;
        }
        .gradient-text {
            background: linear-gradient(90deg,#a855f7,#ec4899,#ef4444);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }
        .hero p {
            font-size: 20px;
            color: #555;
            margin-bottom: 30px;
        }
        .btn {
            display: inline-block;
            padding: 12px 24px;
            border-radius: 30px;
            background: #2563eb;
            color: white;
            font-weight: 600;
            text-decoration: none;
            transition: 0.3s;
            margin: 10px;
        }
        .btn:hover {
            background: #1e40af;
            transform: translateY(-3px);
        }

        /* Sections */
        .section {
            padding: 100px 50px;
        }
        .section h2 {
            text-align: center;
            margin-bottom: 50px;
            font-size: 36px;
            font-weight: 700;
        }

        /* Cards */
        .card {
            padding: 25px;
            border-radius: 15px;
            background: #fff;
            border: 1px solid #eee;
            box-shadow: 0 4px 12px rgba(0,0,0,0.06);
            transition: 0.3s;
            margin-bottom: 30px;
        }
        .card:hover {
            transform: translateY(-6px);
            box-shadow: 0 10px 20px rgba(0,0,0,0.12);
        }

        /* Skill Chips */
        .skill-chip {
            display:inline-block;
            padding:8px 16px;
            border-radius:25px;
            background: #e0f2fe;
            color:#0369a1;
            font-size: 14px;
            font-weight: 500;
            margin:4px;
            transition: 0.3s;
        }
        .skill-chip:hover {
            background:#0369a1;
            color:white;
        }

        /* Footer */
        .footer {
            padding: 30px;
            text-align: center;
            background: #f1f5f9;
            margin-top: 80px;
            color:#666;
            font-size: 14px;
        }
    </style>
""", unsafe_allow_html=True)

# Navbar
st.markdown("""
<div class="nav">
  <div style="font-weight:700;font-size:22px">💻 Tapesh Chavle</div>
  <div>
    <a href="#home">Home</a>
    <a href="#about">About</a>
    <a href="#skills">Skills</a>
    <a href="#projects">Projects</a>
    <a href="#contact">Contact</a>
  </div>
</div>
""", unsafe_allow_html=True)

# Hero Section
st.markdown("""
<div id="home" class="hero">
  <h1>Hi, I'm <span class="gradient-text">Tapesh Chavle</span></h1>
  <p>🚀 Full Stack SpringBoot Developer & UI/UX Designer</p>
  <a class="btn" href="#projects">View My Work</a>
  <a class="btn" href="#contact">Contact Me</a>
</div>
""", unsafe_allow_html=True)

# About Section
st.markdown('<div id="about" class="section">', unsafe_allow_html=True)
st.markdown("<h2>📖 About Me</h2>", unsafe_allow_html=True)
col1, col2 = st.columns([1,2])
with col1:
    st.image("RA.png", use_column_width=True)
with col2:
    st.markdown("""
    I'm a dedicated Full Stack Java Developer with focus on **Spring Boot**.  
    Currently pursuing my B.Tech (3rd Year) with hands-on real-world projects.  

    ✅ 2 years Java experience  
    ✅ 1+ year building REST APIs with Spring Boot  
    ✅ Strong database + frontend knowledge  
    """)
    st.download_button("📄 Download Resume", "resume.pdf", file_name="Tapesh_Chavle_Resume.pdf")
st.markdown('</div>', unsafe_allow_html=True)

# Skills Section
st.markdown('<div id="skills" class="section">', unsafe_allow_html=True)
st.markdown("<h2>🛠 My Skills</h2>", unsafe_allow_html=True)

skills = {
    "Programming Languages": ["Java", "JEE", "C/C++", "JavaScript"],
    "Frontend Development": ["React", "Tailwind CSS", "HTML/CSS", "Bootstrap"],
    "Backend Development": ["Spring Boot", "Microservices", "REST API", "MySQL", "MongoDB"],
    "UI/UX Design": ["Figma", "Responsive Design"],
    "Tools & Methods": ["Git", "Docker", "Postman", "Maven"],
    "Soft Skills": ["Communication", "Teamwork", "Problem Solving"]
}
cols = st.columns(3)
i = 0
for category, sks in skills.items():
    with cols[i % 3]:
        st.markdown(f"<div class='card'><h4>{category}</h4>" + "".join([f"<span class='skill-chip'>{s}</span>" for s in sks]) + "</div>", unsafe_allow_html=True)
    i+=1
st.markdown('</div>', unsafe_allow_html=True)

# Projects Section
st.markdown('<div id="projects" class="section">', unsafe_allow_html=True)
st.markdown("<h2>✨ My Projects</h2>", unsafe_allow_html=True)
projects = [
    {
        "title":"Foodingo",
        "desc":"Food delivery + restaurant discovery app inspired by Zomato.",
        "tags":["React","SpringBoot","MongoDB"],
        "image":"RA.png",
        "github":"https://github.com/tapeshchavle/foodingo",
        "demo":"https://foodingo.netlify.app/"
    },
    {
        "title":"Background Remover",
        "desc":"Cloud SaaS app for removing image backgrounds.",
        "tags":["React","Spring Boot","MySql"],
        "image":"RA.png",
        "github":"https://github.com/tapeshchavle/background-remover",
        "demo":"https://backg-remover.netlify.app/"
    }
]
cols = st.columns(2)
for i, p in enumerate(projects):
    with cols[i % 2]:
        st.markdown(f"""
        <div class='card'>
            <img src='{p["image"]}' style='width:100%;border-radius:12px;margin-bottom:15px'/>
            <h4>{p["title"]}</h4>
            <p>{p["desc"]}</p>
            {''.join([f"<span class='skill-chip'>{t}</span>" for t in p["tags"]])}
            <br><br>
            <a href='{p["github"]}' target='_blank'>🔗 Code</a> | 
            <a href='{p["demo"]}' target='_blank'>🚀 Live</a>
        </div>
        """, unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# Contact Section
st.markdown('<div id="contact" class="section">', unsafe_allow_html=True)
st.markdown("<h2>📩 Get in Touch</h2>", unsafe_allow_html=True)
col1, col2 = st.columns(2)
with col1:
    with st.form("contact_form"):
        name = st.text_input("Your Name")
        email = st.text_input("Your Email")
        message = st.text_area("Message")
        submit = st.form_submit_button("Send Message")
        if submit:
            st.success(f"Thanks {name}, I'll reach out to you at {email}!")
with col2:
    st.markdown("""
    <div class='card'>
        <h4>Contact Info</h4>
        📧 tapeshchawle@gmail.com  
        🔗 <a href="https://linkedin.com/in/tapesh-chavle-48656b23a" target="_blank">LinkedIn</a>  
        💻 <a href="https://github.com/tapeshchavle" target="_blank">GitHub</a>  
    </div>
    """, unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# Footer
st.markdown(f"<div class='footer'>© {2025} Tapesh Chavle. All rights reserved.</div>", unsafe_allow_html=True)

