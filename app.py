import streamlit as st

# Colores
azul_oscuro = "#0D47A1"
azul_medio = "#1976D2"
azul_claro = "#42A5F5"
celeste = "#90CAF9"
celeste_suave = "#E3F2FD"
texto_color = "#0B3D91"

# CSS personalizado
st.markdown(
    f"""
    <style>
    .titulo-principal {{
        font-size: 2.8rem;
        font-weight: 900;
        background: linear-gradient(90deg, {azul_oscuro}, {azul_medio});
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
        margin-bottom: 1rem;
    }}
    .foto-perfil {{
        border-radius: 50%;
        border: 5px solid {celeste};
        box-shadow: 0 4px 12px rgba(25, 118, 210, 0.4);
        max-width: 140px;
        margin-bottom: 1rem;
        display: block;
    }}
    h2 {{
        color: {azul_medio} !important;
        font-weight: 700;
        margin-top: 2rem;
        margin-bottom: 1rem;
        border-bottom: 3px solid {celeste};
        padding-bottom: 0.3rem;
        display: flex;
        align-items: center;
        gap: 0.5rem;
    }}
    .seccion {{
        background: white;
        border-radius: 12px;
        box-shadow: 0 4px 10px rgba(25, 118, 210, 0.1);
        padding: 1.5rem 2rem;
        margin-bottom: 2rem;
    }}
    p, li {{
        color: {texto_color};
        font-size: 1.1rem;
        line-height: 1.5;
    }}
    footer {{
        text-align: center;
        color: {azul_medio};
        margin-top: 3rem;
        font-weight: 600;
    }}
    .galeria img {{
        border-radius: 12px;
        box-shadow: 0 6px 15px rgba(25, 118, 210, 0.2);
        margin-bottom: 15px;
        max-width: 100%;
        transition: transform 0.3s ease;
    }}
    .galeria img:hover {{
        transform: scale(1.05);
    }}
    .evento-timeline {{
        border-left: 4px solid {azul_medio};
        padding-left: 1rem;
        margin-bottom: 1.2rem;
    }}
    .evento-timeline h4 {{
        margin-bottom: 0.2rem;
        color: {azul_oscuro};
    }}
    a.logro-link {{
        color: {azul_medio};
        font-weight: 600;
        text-decoration: none;
        border-bottom: 2px solid {celeste};
    }}
    a.logro-link:hover {{
        color: {azul_oscuro};
        border-bottom-color: {azul_oscuro};
    }}
    .imagenes-logros {{
        display: flex;
        gap: 20px;
        flex-wrap: wrap;
        justify-content: center;
        margin-top: 1rem;
    }}
    .imagenes-logros img {{
        border-radius: 10px;
        max-width: 250px;
        box-shadow: 0 5px 15px rgba(25, 118, 210, 0.25);
        transition: transform 0.3s ease;
    }}
    .imagenes-logros img:hover {{
        transform: scale(1.07);
    }}
    </style>
    """,
    unsafe_allow_html=True,
)

# Información personal
info = {
    "Full_Name": "Grecia García Hoyos",
    "Intro": "Estudiante de Publicidad y apasionada por la comunicación creativa con impacto social",
    "About": """Hola, soy Grecia García Hoyos, estudiante de Publicidad en la PUCP. Me destaco por ser una persona productiva, puntual y con habilidades de liderazgo y organización. 
Siempre busco aprender, colaborar y crear impacto desde la comunicación.""",
    "Medium": "https://www.linkedin.com/in/grecia-garcia-hoyos-44997933a/",
    "City": "Lima, Perú",
    "Photo": "https://i.imgur.com/Noy3lNI.jpg",
    "Email": "a20234861@pucp.edu.pe"
}

endorsements = {
    "img1": "https://i.imgur.com/YQx2CP1.jpeg",
    "img2": "https://i.imgur.com/CmdHRw2.jpeg",
    "img3": "https://i.imgur.com/jakXIXZ.jpeg"
}

# Cabecera en columnas
st.markdown('<div class="seccion">', unsafe_allow_html=True)

col_foto, col_texto = st.columns([1, 3])

with col_foto:
    st.markdown(f'<img src="{info["Photo"]}" class="foto-perfil">', unsafe_allow_html=True)

with col_texto:
    st.markdown(f'<h1 class="titulo-principal">Portafolio de {info["Full_Name"]}</h1>', unsafe_allow_html=True)
    st.markdown(f'<h3 style="color:{azul_oscuro}; margin-top:0;">{info["Intro"]}</h3>', unsafe_allow_html=True)
    st.markdown(f'<p style="max-width:700px;">{info["About"]}</p>', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

# Sección Contacto
st.markdown('<div class="seccion">', unsafe_allow_html=True)
st.markdown('📬 <h2>Contacto</h2>', unsafe_allow_html=True)
st.markdown(f'📧 {info["Email"]}  \n📍 {info["City"]}  \n[🔗 LinkedIn]({info["Medium"]})')
st.markdown('</div>', unsafe_allow_html=True)

# Galería ordenada
st.markdown('<div class="seccion galeria">', unsafe_allow_html=True)
st.markdown('📸 <h2>Galería</h2>', unsafe_allow_html=True)

gal_col1, gal_col2, gal_col3 = st.columns(3)
with gal_col1:
    st.image(endorsements["img1"], width=250)
with gal_col2:
    st.image(endorsements["img2"], width=250)
with gal_col3:
    st.image(endorsements["img3"], width=250)

st.markdown('</div>', unsafe_allow_html=True)

# Sobre Grecia
st.markdown('<div class="seccion">', unsafe_allow_html=True)
st.markdown('🌟 <h2>Sobre Grecia</h2>', unsafe_allow_html=True)
st.markdown('Grecia García Hoyos es estudiante de Publicidad en la PUCP, apasionada por la comunicación creativa con impacto social. Se destaca por ser productiva, puntual y poseer habilidades de liderazgo y organización.')
st.markdown('</div>', unsafe_allow_html=True)

# Experiencia y Metas
col1, col2 = st.columns(2)

with col1:
    st.markdown('<div class="seccion">', unsafe_allow_html=True)
    st.markdown('💼 <h2>Experiencia de trabajo</h2>', unsafe_allow_html=True)
    st.markdown("""
    - Voluntariado ambiental en el colegio  
    - Coordinadora de redes sociales en Huellitas PUCP  
    - Fortaleció creatividad, comunicación digital y trabajo en equipo
    """)
    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="seccion">', unsafe_allow_html=True)
    st.markdown('🎯 <h2>Metas de carrera</h2>', unsafe_allow_html=True)
    st.markdown("Desarrollarse profesionalmente en comunicación y publicidad, creando proyectos con impacto social.")
    st.markdown('</div>', unsafe_allow_html=True)

# Habilidades y Certificaciones
col3, col4 = st.columns(2)

with col3:
    st.markdown('<div class="seccion">', unsafe_allow_html=True)
    st.markdown('🛠️ <h2>Habilidades</h2>', unsafe_allow_html=True)
    st.markdown("""
    - Edición de video (CapCut)  
    - Diseño gráfico (Canva)  
    - Comunicación digital  
    - Liderazgo y trabajo en equipo  
    - Creatividad  
    - Inglés C1 (PUCP)
    """)
    st.markdown('</div>', unsafe_allow_html=True)

with col4:
    st.markdown('<div class="seccion">', unsafe_allow_html=True)
    st.markdown('📜 <h2>Certificaciones</h2>', unsafe_allow_html=True)
    st.markdown("Inglés nivel C1 certificado por Idiomas PUCP.")
    st.markdown('</div>', unsafe_allow_html=True)

# Logros
st.markdown('<div class="seccion">', unsafe_allow_html=True)
st.markdown('🏆 <h2>Logros</h2>', unsafe_allow_html=True)
st.markdown("""
Ganadora del Concurso de Investigación Académica 2024-1:  
[🔗 Monografía publicada](https://estudios-generales-letras.pucp.edu.pe/investigacion-academica-2024-1-monografias-ganadoras/)
""")

st.markdown("""
<div class="imagenes-logros">
    <img src="https://i.imgur.com/YQx2CP1.jpeg" alt="Logro 1">
    <img src="https://i.imgur.com/OvFF2iU.jpeg" alt="Logro 2">
</div>
""", unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# Línea de tiempo
st.markdown('<div class="seccion">', unsafe_allow_html=True)
st.markdown('🕒 <h2>Mi trayectoria</h2>', unsafe_allow_html=True)

timeline_events = [
    {"year": "2022", "title": "Egresé del colegio", "description": "Terminé mis estudios en el Colegio Cristo Rey."},
    {"year": "2023", "title": "Inicio en CATO", "description": "Empecé Publicidad en la PUCP. Primer puesto desde entonces."},
    {"year": "2024", "title": "Diseñadora en Huellitas PUCP", "description": "Diseño audiovisual en voluntariado animalista."},
    {"year": "2025", "title": "Coordinadora de Huellitas PUCP", "description": "Lideré redes sociales y campañas digitales."},
    {"year": "2025", "title": "Ganadora del Concurso", "description": "Mi monografía fue publicada por EE.GG.LL PUCP."}
]

for event in timeline_events:
    st.markdown(f'''
        <div class="evento-timeline">
            <h4>{event["year"]} - {event["title"]}</h4>
            <p>{event["description"]}</p>
        </div>
    ''', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

# Footer personalizado
st.markdown('<footer>✨ Grecia García Hoyos | Este portafolio es un reflejo de mi camino y creatividad ✨</footer>', unsafe_allow_html=True)
