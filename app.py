import streamlit as st

st.set_page_config(
    page_title="Zoy Assessoria",
    page_icon="💜",
    layout="wide"
)

# =========================
# CSS GLOBAL
# =========================
st.markdown("""
<style>
    .stApp {
        background: #FFFFFF;
    }

    .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
        max-width: 100%;
    }

    section[data-testid="stSidebar"] {
        background: linear-gradient(180deg, #2B005D 0%, #6F2DE2 100%);
    }

    section[data-testid="stSidebar"] * {
        color: white !important;
    }

    .main-title, .page-title {
        font-size: 34px;
        font-weight: 800;
        color: #17002E;
        margin-bottom: 6px;
    }

    .subtitle, .page-subtitle {
        color: #7B6B8F;
        margin-bottom: 25px;
        font-size: 15px;
    }

    .card, .panel, .metric-card, .creator-list-card, .creator-list-card-light, .info-box {
        background: white;
        border: 1px solid #E9DFFF;
        box-shadow: none;
    }

    .card {
        padding: 20px;
        border-radius: 20px;
    }

    .panel {
        border-radius: 22px;
        padding: 22px;
        margin-bottom: 18px;
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

    .tag, .pill {
        background: #EFE4FF;
        color: #6F2DE2;
        padding: 6px 12px;
        border-radius: 20px;
        font-size: 12px;
        font-weight: 700;
        display: inline-block;
        margin-right: 6px;
        margin-bottom: 6px;
    }

    .section-title {
        color: #17002E;
        font-size: 20px;
        font-weight: 800;
        margin-bottom: 16px;
    }

    .muted {
        color: #6F6680;
        font-size: 14px;
    }

    .avatar {
        width: 76px;
        height: 76px;
        border-radius: 50%;
        background: linear-gradient(135deg, #D8C6FF, #6F2DE2);
        display: flex;
        align-items: center;
        justify-content: center;
        color: white;
        font-size: 27px;
        font-weight: 800;
        flex-shrink: 0;
    }

    .avatar-small {
        width: 46px;
        height: 46px;
        border-radius: 50%;
        background: linear-gradient(135deg, #D8C6FF, #6F2DE2);
        display: inline-flex;
        align-items: center;
        justify-content: center;
        color: white;
        font-size: 15px;
        font-weight: 800;
        margin-right: 10px;
        vertical-align: middle;
    }

    .creator-list-card {
        background: #F8F4FF;
        border-radius: 18px;
        padding: 15px;
        margin-bottom: 12px;
    }

    .creator-list-card-light {
        background: #FFFFFF;
        border-radius: 18px;
        padding: 15px;
        margin-bottom: 12px;
    }

    .profile-header {
        display: flex;
        align-items: center;
        gap: 22px;
    }

    .profile-name {
        font-size: 30px;
        font-weight: 800;
        color: #17002E;
        margin-bottom: 4px;
    }

    .profile-handle {
        color: #6F2DE2;
        font-weight: 700;
        margin-bottom: 8px;
    }

    .status-active {
        background: #E8F8ED;
        color: #148A42;
        padding: 7px 13px;
        border-radius: 999px;
        font-size: 12px;
        font-weight: 800;
    }

    .status-paused {
        background: #FFF3D8;
        color: #B96A00;
        padding: 7px 13px;
        border-radius: 999px;
        font-size: 12px;
        font-weight: 800;
    }

    .info-box {
        background: #F8F4FF;
        border-radius: 16px;
        padding: 16px;
        min-height: 80px;
        min-width: 120px;
    }

    .metric-card {
        border-radius: 18px;
        padding: 20px;
        text-align: center;
        min-height: 120px;
    }

    .metric-label {
        color: #7B6B8F;
        font-size: 13px;
        margin-bottom: 8px;
    }

    .metric-value {
        color: #17002E;
        font-size: 30px;
        font-weight: 900;
    }

    .metric-growth {
        color: #12994F;
        font-size: 13px;
        font-weight: 700;
        margin-top: 6px;
    }

    .info-item {
        padding: 11px 0;
        border-bottom: 1px solid #EFEAF8;
    }

    .info-item:last-child {
        border-bottom: none;
    }

    .info-label {
        font-weight: 800;
        color: #30273F;
        font-size: 14px;
        margin-bottom: 3px;
    }

    .info-value {
        color: #6F6680;
        font-size: 14px;
        line-height: 1.45;
    }

    .campaign-row {
        display: grid;
        grid-template-columns: 1fr 1.4fr 1.5fr .8fr 1fr;
        gap: 12px;
        padding: 14px 0;
        border-bottom: 1px solid #EFEAF8;
        align-items: center;
        font-size: 14px;
    }

    .campaign-head {
        color: #7B6B8F;
        font-weight: 700;
        font-size: 13px;
    }

    .badge-purple, .badge-orange, .badge-blue {
        padding: 6px 10px;
        border-radius: 999px;
        font-size: 12px;
        font-weight: 800;
        text-align: center;
        display: inline-block;
    }

    .badge-purple {
        background: #EFE4FF;
        color: #6F2DE2;
    }

    .badge-orange {
        background: #FFF1DD;
        color: #C76A00;
    }

    .badge-blue {
        background: #EAF0FF;
        color: #1746B3;
    }

    div[data-testid="stRadio"] label {
        display: none;
    }

    div[data-testid="stRadio"] div[role="radiogroup"] {
        gap: 0px;
    }

    .stButton > button {
        border-radius: 12px;
        border: 1px solid #E9DFFF;
        font-weight: 700;
    }

    div[data-testid="stTextInput"] input {
        border-radius: 12px;
        border: 1px solid #E9DFFF;
    }

    .stTabs [data-baseweb="tab-list"] {
        gap: 18px;
        border-bottom: 1px solid #EFEAF8;
    }

    .stTabs [data-baseweb="tab"] {
        color: #30273F;
        font-weight: 700;
    }

    .stTabs [aria-selected="true"] {
        color: #6F2DE2 !important;
    }
</style>
""", unsafe_allow_html=True)

# =========================
# SIDEBAR
# =========================
st.sidebar.title("ZOY")
st.sidebar.caption("ASSESSORIA")

menu = st.sidebar.radio(
    "Menu",
    ["Dashboard", "Influenciadores", "Planejamento", "Projetos"],
    label_visibility="collapsed"
)

st.sidebar.markdown("---")
st.sidebar.markdown("**Jean**")
st.sidebar.caption("Responsável")

# =========================
# DADOS MOCKADOS
# =========================
creators_data = {
    "Jady Carvalho": {
        "initials": "JC",
        "handle": "@jadycarvalho",
        "nicho": "Lifestyle • Beleza • Humor",
        "cidade": "São Paulo, SP",
        "status": "Ativo",
        "email": "jadycarvalho@gmail.com",
        "telefone": "(11) 99999-9999",
        "aniversario": "12/03",
        "posicionamento": "Lifestyle real, rotina espontânea, beleza leve e humor do dia a dia.",
        "obs": "Tem ótima entrega em Reels. Público jovem e muito engajado.",
        "seguidores": "132K",
        "alcance": "48K",
        "stories": "18K",
        "engajamento": "4,2%"
    },
    "Malu Borges": {
        "initials": "MB",
        "handle": "@maluborges",
        "nicho": "Fashion • Lifestyle",
        "cidade": "São Paulo, SP",
        "status": "Ativo",
        "email": "malu@email.com",
        "telefone": "(11) 98888-8888",
        "aniversario": "04/08",
        "posicionamento": "Moda urbana, lifestyle aspiracional e rotina criativa.",
        "obs": "Boa aderência para marcas de moda e beleza.",
        "seguidores": "89K",
        "alcance": "31K",
        "stories": "12K",
        "engajamento": "3,8%"
    },
    "Vitória Guedes": {
        "initials": "VG",
        "handle": "@vitoriaguedes",
        "nicho": "Beauty • Skincare",
        "cidade": "Rio de Janeiro, RJ",
        "status": "Ativo",
        "email": "vitoria@email.com",
        "telefone": "(21) 97777-7777",
        "aniversario": "22/01",
        "posicionamento": "Beleza acessível, skincare e rotina feminina.",
        "obs": "Boa entrega em stories e reviews.",
        "seguidores": "76K",
        "alcance": "22K",
        "stories": "9K",
        "engajamento": "3,1%"
    }
}

# =========================
# DASHBOARD
# =========================
if menu == "Dashboard":
    st.markdown('<div class="main-title">Olá, Jean.</div>', unsafe_allow_html=True)
    st.markdown('<div class="subtitle">Aqui está o panorama da assessoria hoje.</div>', unsafe_allow_html=True)

    c1, c2, c3, c4 = st.columns(4)

    dashboard_cards = [
        ("Creators ativos", "12"),
        ("Parcerias em andamento", "9"),
        ("Conteúdos pendentes", "17"),
        ("Reuniões da semana", "6")
    ]

    for col, (title, number) in zip([c1, c2, c3, c4], dashboard_cards):
        with col:
            st.markdown(f"""
            <div class="card">
                <div class="metric-title">{title}</div>
                <div class="metric-number">{number}</div>
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

# =========================
# INFLUENCIADORES
# =========================
elif menu == "Influenciadores":

    title_col, btn_col = st.columns([5, 1])

with title_col:
    st.markdown('<div class="page-title">Influenciadores</div>', unsafe_allow_html=True)
    st.markdown('<div class="page-subtitle">Gerencie seus influenciadores e acompanhe tudo em um só lugar.</div>', unsafe_allow_html=True)

with btn_col:
    st.button("+ Novo influenciador", use_container_width=True)

    left, right = st.columns([1.05, 3.4], gap="large")

    with left:
        st.markdown('<div class="section-title">Influenciadores</div>', unsafe_allow_html=True)
        st.text_input("Buscar influenciador", placeholder="Buscar influenciador...", label_visibility="collapsed")

        selected_creator = "Jady Carvalho"

        for name, data in creators_data.items():
            card_class = "creator-list-card" if name == selected_creator else "creator-list-card-light"
            status_class = "status-active" if data["status"] == "Ativo" else "status-paused"

            st.markdown(f"""
            <div class="{card_class}">
                <span class="avatar-small">{data["initials"]}</span>
                <div style="display:inline-block; vertical-align:middle;">
                    <b>{name}</b><br>
                    <span class="muted">{data["handle"]}</span>
                </div>
                <div style="float:right; margin-top:8px;">
                    <span class="{status_class}">{data["status"]}</span>
                </div>
            </div>
            """, unsafe_allow_html=True)

        st.markdown(
            f'<div class="muted" style="margin-top:22px;">{len(creators_data)} influenciadores cadastrados</div>',
            unsafe_allow_html=True
        )

    creator = creators_data[selected_creator]

    with right:
        status_class = "status-active" if creator["status"] == "Ativo" else "status-paused"

        st.markdown(f"""
        <div class="panel">
            <div class="profile-header">
                <div class="avatar">{creator["initials"]}</div>
                <div style="flex:1;">
                    <div class="profile-name">{selected_creator}</div>
                    <div class="profile-handle">{creator["handle"]}</div>
                    <div class="muted">{creator["nicho"]}</div>
                    <div class="muted" style="margin-top:8px;">📍 {creator["cidade"]}</div>
                </div>
                <div class="info-box">
                    <div class="muted">Responsável</div>
                    <b>Jean</b>
                </div>
                <div class="info-box">
                    <div class="muted">Status</div>
                    <span class="{status_class}">{creator["status"]}</span>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)

        tabs = st.tabs(["Visão geral", "Métricas", "Campanhas ativas", "Acompanhamento", "Histórico", "Documentos"])

        with tabs[0]:
            col_a, col_b = st.columns([1.1, 1.7], gap="large")

            with col_a:
                st.markdown(f"""
                <div class="panel">
                    <div class="section-title">Sobre o influenciador</div>

                    <div class="info-item">
                        <div class="info-label">E-mail</div>
                        <div class="info-value">{creator["email"]}</div>
                    </div>

                    <div class="info-item">
                        <div class="info-label">Telefone</div>
                        <div class="info-value">{creator["telefone"]}</div>
                    </div>

                    <div class="info-item">
                        <div class="info-label">Nicho</div>
                        <div class="info-value">{creator["nicho"]}</div>
                    </div>

                    <div class="info-item">
                        <div class="info-label">Aniversário</div>
                        <div class="info-value">{creator["aniversario"]}</div>
                    </div>

                    <div class="info-item">
                        <div class="info-label">Posicionamento</div>
                        <div class="info-value">{creator["posicionamento"]}</div>
                    </div>

                    <div class="info-item">
                        <div class="info-label">Observações</div>
                        <div class="info-value">{creator["obs"]}</div>
                    </div>

                    <div style="margin-top:15px;">
                        <span class="pill">Lifestyle</span>
                        <span class="pill">Beleza</span>
                        <span class="pill">Humor</span>
                    </div>
                </div>
                """, unsafe_allow_html=True)

            with col_b:
                st.markdown("""
                <div class="panel">
                    <div class="section-title">Métricas principais</div>
                </div>
                """, unsafe_allow_html=True)

                m1, m2, m3, m4 = st.columns(4)

                metrics = [
                    ("Seguidores", creator["seguidores"], "↑ 2,3%"),
                    ("Alcance médio", creator["alcance"], "↑ 8,1%"),
                    ("Views Stories", creator["stories"], "↑ 5,2%"),
                    ("Engajamento", creator["engajamento"], "↑ 0,6%"),
                ]

                for col, (label, value, growth) in zip([m1, m2, m3, m4], metrics):
                    with col:
                        st.markdown(f"""
                        <div class="metric-card">
                            <div class="metric-label">{label}</div>
                            <div class="metric-value">{value}</div>
                            <div class="metric-growth">{growth}</div>
                        </div>
                        """, unsafe_allow_html=True)

                st.markdown("<br>", unsafe_allow_html=True)

                st.markdown("""
                <div class="panel">
                    <div class="section-title">Campanhas ativas</div>

                    <div class="campaign-row campaign-head">
                        <div>Marca</div>
                        <div>Campanha</div>
                        <div>Entrega</div>
                        <div>Prazo</div>
                        <div>Status</div>
                    </div>

                    <div class="campaign-row">
                        <div><b>Adidas</b></div>
                        <div>Always On</div>
                        <div>3 Reels + 6 Stories</div>
                        <div>25/05</div>
                        <div><span class="badge-purple">Produção</span></div>
                    </div>

                    <div class="campaign-row">
                        <div><b>Lipton</b></div>
                        <div>Verão 2025</div>
                        <div>2 Stories + 1 Reel</div>
                        <div>30/05</div>
                        <div><span class="badge-orange">Aprovação</span></div>
                    </div>

                    <div class="campaign-row">
                        <div><b>FINI</b></div>
                        <div>Doces Momentos</div>
                        <div>2 Reels + 4 Stories</div>
                        <div>15/06</div>
                        <div><span class="badge-blue">Negociação</span></div>
                    </div>
                </div>
                """, unsafe_allow_html=True)

        with tabs[1]:
            st.markdown("""
            <div class="panel">
                <div class="section-title">Métricas completas</div>
                <p class="muted">Aqui entram seguidores, alcance, impressões, views, engajamento e atualização manual das métricas.</p>
            </div>
            """, unsafe_allow_html=True)

        with tabs[2]:
            st.markdown("""
            <div class="panel">
                <div class="section-title">Campanhas ativas</div>
                <p class="muted">Aqui fica a visão completa de campanhas vinculadas ao influenciador.</p>
            </div>
            """, unsafe_allow_html=True)

        with tabs[3]:
            st.markdown("""
            <div class="panel">
                <div class="section-title">Acompanhamento de postagem</div>
                <p class="muted">Aqui vamos controlar entrega, data prevista, link, print, métricas e status.</p>
            </div>
            """, unsafe_allow_html=True)

        with tabs[4]:
            st.markdown("""
            <div class="panel">
                <div class="section-title">Histórico</div>
                <p class="muted">Timeline de reuniões, ajustes, retornos comerciais e observações internas.</p>
            </div>
            """, unsafe_allow_html=True)

        with tabs[5]:
            st.markdown("""
            <div class="panel">
                <div class="section-title">Documentos</div>
                <p class="muted">Contratos, mídia kit, dados bancários, NFs e arquivos importantes.</p>
            </div>
            """, unsafe_allow_html=True)

# =========================
# PLANEJAMENTO
# =========================
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

# =========================
# PROJETOS
# =========================
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
