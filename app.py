import streamlit as st

st.set_page_config(
    page_title="Zoy Assessoria",
    page_icon="💜",
    layout="wide"
)

# CSS
st.markdown("""
<style>
    .stApp {
        background: #faf8ff;
    }

    section[data-testid="stSidebar"] {
        background: linear-gradient(180deg, #2B005D 0%, #6F2DE2 100%);
    }

    section[data-testid="stSidebar"] * {
        color: white !important;
    }

    .main-title {
        font-size: 34px;
        font-weight: 800;
        color: #17002E;
    }

    .subtitle {
        color: #7B6B8F;
        margin-bottom: 25px;
    }

    .card {
        background: white;
        padding: 20px;
        border-radius: 20px;
        border: 1px solid #E9DFFF;
        box-shadow: 0 8px 24px rgba(111, 45, 226, 0.08);
    }

    .metric-title {
        color: #7B6B8F;
        font-size: 14px;
    }

    .metric-number {
        font-size: 32px;
        font-weight: 800;
        color: #17002E;
    }

    .tag {
        background: #EFE4FF;
        color: #6F2DE2;
        padding: 6px 12px;
        border-radius: 20px;
        font-size: 12px;
        display: inline-block;
    }
</style>
""", unsafe_allow_html=True)

# Sidebar
st.sidebar.title("ZOY")
st.sidebar.caption("ASSESSORIA")

menu = st.sidebar.radio(
    "Menu",
    ["Dashboard", "Influenciadores", "Planejamento", "Projetos"],
    label_visibility="collapsed"
)

# Dashboard
if menu == "Dashboard":
    st.markdown('<div class="main-title">Olá, Bea.</div>', unsafe_allow_html=True)
    st.markdown('<div class="subtitle">Aqui está o panorama da assessoria hoje.</div>', unsafe_allow_html=True)

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        st.markdown("""
        <div class="card">
            <div class="metric-title">Creators ativos</div>
            <div class="metric-number">12</div>
        </div>
        """, unsafe_allow_html=True)

    with c2:
        st.markdown("""
        <div class="card">
            <div class="metric-title">Parcerias em andamento</div>
            <div class="metric-number">9</div>
        </div>
        """, unsafe_allow_html=True)

    with c3:
        st.markdown("""
        <div class="card">
            <div class="metric-title">Conteúdos pendentes</div>
            <div class="metric-number">17</div>
        </div>
        """, unsafe_allow_html=True)

    with c4:
        st.markdown("""
        <div class="card">
            <div class="metric-title">Reuniões da semana</div>
            <div class="metric-number">6</div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("## Parcerias em andamento")

    p1, p2, p3 = st.columns(3)

    with p1:
        st.markdown("""
        <div class="card">
            <h4>FINI</h4>
            <p>Campanha de Reels + Stories</p>
            <span class="tag">Negociação</span>
        </div>
        """, unsafe_allow_html=True)

    with p2:
        st.markdown("""
        <div class="card">
            <h4>Adidas</h4>
            <p>Campanha Always On</p>
            <span class="tag">Produção</span>
        </div>
        """, unsafe_allow_html=True)

    with p3:
        st.markdown("""
        <div class="card">
            <h4>Lipton</h4>
            <p>Stories + Reel</p>
            <span class="tag">Aprovação</span>
        </div>
        """, unsafe_allow_html=True)

# Influenciadores
elif menu == "Influenciadores":
    st.title("Influenciadores")

    creators = [
        "Jady Carvalho",
        "Malu Borges",
        "Vitória Guedes"
    ]

    creator = st.selectbox("Selecione o creator", creators)

    st.markdown(f"## {creator}")

    m1, m2, m3, m4 = st.columns(4)

    m1.metric("Seguidores", "132K", "+2.3%")
    m2.metric("Alcance", "48K", "+8.1%")
    m3.metric("Stories", "18K", "+5.2%")
    m4.metric("Engajamento", "4.2%", "+0.6%")

    st.markdown("""
    ### Posicionamento
    Lifestyle + Beauty + rotina espontânea + humor leve
    """)

# Planejamento
elif menu == "Planejamento":
    st.title("Planejamento")

    st.selectbox("Influenciador", ["Jady Carvalho", "Malu Borges"])

    st.text_input("Objetivo do mês", "Crescimento + Engajamento")

    st.text_area(
        "Estratégia",
        "Foco em lifestyle espontâneo, rotina real e conteúdos mais conversados."
    )

    c1, c2, c3, c4 = st.columns(4)

    c1.number_input("Reels", value=4)
    c2.number_input("Stories", value=12)
    c3.number_input("Collabs", value=1)
    c4.number_input("Publis", value=1)

# Projetos
elif menu == "Projetos":
    st.title("Projetos")

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        st.markdown("""
        <div class="card">
            <h4>Briefing recebido</h4>
            Sephora<br>
            C&A
        </div>
        """, unsafe_allow_html=True)

    with c2:
        st.markdown("""
        <div class="card">
            <h4>Negociação</h4>
            FINI<br>
            Amaro
        </div>
        """, unsafe_allow_html=True)

    with c3:
        st.markdown("""
        <div class="card">
            <h4>Produção</h4>
            Adidas<br>
            Lipton
        </div>
        """, unsafe_allow_html=True)

    with c4:
        st.markdown("""
        <div class="card">
            <h4>Finalizado</h4>
            Azul<br>
            Natura
        </div>
        """, unsafe_allow_html=True)
