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
        background: white;
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
    st.markdown('<div class="main-title">Olá, Time.</div>', unsafe_allow_html=True)
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
# Influenciadores
elif menu == "Influenciadores":

    st.markdown("""
    <style>
    .creator-card {
        background: white;
        border: 1px solid #ECE7F7;
        border-radius: 20px;
        padding: 20px;
        box-shadow: 0 8px 24px rgba(111,45,226,0.06);
    }

    .creator-item {
        background: white;
        border: 1px solid #ECE7F7;
        border-radius: 16px;
        padding: 14px;
        margin-bottom: 12px;
    }

    .metric-box {
        background: white;
        border: 1px solid #ECE7F7;
        border-radius: 18px;
        padding: 18px;
        text-align: center;
    }

    .metric-value {
        font-size: 30px;
        font-weight: 800;
        color: #17002E;
    }

    .metric-label {
        color: #7B6B8F;
        font-size: 13px;
    }

    .status-active {
        background: #E8F8ED;
        color: #1D8A46;
        padding: 6px 12px;
        border-radius: 20px;
        font-size: 12px;
        font-weight: 700;
    }
    </style>
    """, unsafe_allow_html=True)

    st.title("Influenciadores")
    st.caption("Gerencie seus influenciadores e acompanhe tudo em um só lugar.")

    left, right = st.columns([1, 3])

    with left:
        st.markdown("### Influenciadores")

        st.text_input("Buscar influenciador")

        creators = [
            "Jady Carvalho",
            "Malu Borges",
            "Vitória Guedes",
            "Laura Brito",
            "Giovana Fagundes"
        ]

        creator = st.radio(
            "Selecione",
            creators,
            label_visibility="collapsed"
        )

        st.button("+ Novo influenciador", use_container_width=True)

    with right:
        st.markdown(f"""
        <div class="creator-card">
            <h2>{creator}</h2>
            <p>@creatorhandle · Lifestyle · São Paulo</p>
            <br>
            <span class="status-active">ATIVO</span>
            <br><br>
            <b>Responsável:</b> Jean
        </div>
        """, unsafe_allow_html=True)

        tabs = st.tabs([
            "Visão geral",
            "Métricas",
            "Campanhas ativas",
            "Acompanhamento",
            "Histórico"
        ])

        with tabs[0]:
            c1, c2 = st.columns([1, 2])

            with c1:
                st.markdown("""
                <div class="creator-card">
                    <h4>Sobre o influenciador</h4>
                    <p><b>E-mail:</b> creator@email.com</p>
                    <p><b>Telefone:</b> (11) 99999-9999</p>
                    <p><b>Nicho:</b> Lifestyle / Beauty</p>
                    <p><b>Aniversário:</b> 12/03</p>
                    <p><b>Posicionamento:</b> Lifestyle real, rotina espontânea e humor.</p>
                    <p><b>Observações:</b> Forte entrega em reels.</p>
                </div>
                """, unsafe_allow_html=True)

            with c2:
                m1, m2, m3, m4 = st.columns(4)

                with m1:
                    st.markdown("""
                    <div class="metric-box">
                        <div class="metric-label">Seguidores</div>
                        <div class="metric-value">132K</div>
                    </div>
                    """, unsafe_allow_html=True)

                with m2:
                    st.markdown("""
                    <div class="metric-box">
                        <div class="metric-label">Alcance médio</div>
                        <div class="metric-value">48K</div>
                    </div>
                    """, unsafe_allow_html=True)

                with m3:
                    st.markdown("""
                    <div class="metric-box">
                        <div class="metric-label">Views Stories</div>
                        <div class="metric-value">18K</div>
                    </div>
                    """, unsafe_allow_html=True)

                with m4:
                    st.markdown("""
                    <div class="metric-box">
                        <div class="metric-label">Engajamento</div>
                        <div class="metric-value">4.2%</div>
                    </div>
                    """, unsafe_allow_html=True)

                st.markdown("### Campanhas ativas")

                campanhas = {
                    "Marca": ["Adidas", "Lipton", "FINI"],
                    "Campanha": ["Always On", "Verão 2025", "Doces Momentos"],
                    "Entrega": ["3 Reels + 6 Stories", "2 Stories + 1 Reel", "2 Reels + 4 Stories"],
                    "Prazo": ["25/05", "30/05", "15/06"],
                    "Status": ["Produção", "Aprovação", "Negociação"]
                }

                st.dataframe(campanhas, use_container_width=True)

        with tabs[1]:
            st.write("Métricas completas do influenciador.")

        with tabs[2]:
            st.write("Todas as campanhas ativas.")

        with tabs[3]:
            st.write("Acompanhamento de postagem.")

        with tabs[4]:
            st.write("Histórico de interações.")

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
