from pathlib import Path

code = '''import streamlit as st
import textwrap

st.set_page_config(
    page_title="Zoy Assessoria",
    page_icon="🟣",
    layout="wide"
)

def html(content: str):
    st.markdown(textwrap.dedent(content).strip(), unsafe_allow_html=True)

html("""
<style>
    .stApp { background-color: #FFFFFF; }

    .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
        max-width: 100%;
    }

    section[data-testid="stSidebar"] {
        background: linear-gradient(180deg, #2B005D 0%, #4B12B8 100%);
    }

    section[data-testid="stSidebar"] * {
        color: white !important;
    }

    .zoy-logo {
        font-size: 42px;
        font-weight: 900;
        color: white;
        margin-bottom: -6px;
    }

    .zoy-subtitle {
        font-size: 12px;
        letter-spacing: 4px;
        color: #D8C6FF;
        margin-bottom: 35px;
    }

    .main-title, .page-title {
        font-size: 34px;
        font-weight: 850;
        color: #17002E;
        margin-bottom: 4px;
    }

    .subtitle, .page-subtitle {
        color: #6F6680;
        font-size: 15px;
        margin-bottom: 24px;
    }

    .page-header {
        display: flex;
        justify-content: space-between;
        align-items: flex-start;
        margin-bottom: 26px;
    }

    .primary-btn {
        background: linear-gradient(135deg, #6F2DE2, #4B12B8);
        color: white;
        padding: 13px 20px;
        border-radius: 12px;
        font-weight: 800;
        text-align: center;
    }

    .panel, .panel-soft, .simple-card, .dashboard-card, .metric-card {
        background: #FFFFFF;
        border: 1px solid #E9DFFF;
        box-shadow: none;
    }

    .panel, .panel-soft {
        border-radius: 22px;
        padding: 22px;
    }

    .dashboard-card {
        border-radius: 20px;
        padding: 22px;
        min-height: 128px;
    }

    .dashboard-card-title {
        color: #7B6B8F;
        font-size: 14px;
        margin-bottom: 8px;
    }

    .dashboard-card-number {
        color: #17002E;
        font-size: 34px;
        font-weight: 900;
    }

    .simple-card {
        border-radius: 18px;
        padding: 18px;
        margin-bottom: 14px;
    }

    .section-title {
        color: #17002E;
        font-size: 20px;
        font-weight: 850;
        margin-bottom: 18px;
    }

    .muted {
        color: #6F6680;
        font-size: 14px;
    }

    .avatar {
        width: 92px;
        height: 92px;
        border-radius: 50%;
        background: linear-gradient(135deg, #B58CFF, #6F2DE2);
        display: flex;
        align-items: center;
        justify-content: center;
        color: white;
        font-size: 34px;
        font-weight: 900;
        flex-shrink: 0;
    }

    .avatar-small {
        width: 48px;
        height: 48px;
        border-radius: 50%;
        background: linear-gradient(135deg, #B58CFF, #6F2DE2);
        display: inline-flex;
        align-items: center;
        justify-content: center;
        color: white;
        font-size: 15px;
        font-weight: 900;
        margin-right: 12px;
        vertical-align: middle;
    }

    .creator-list-card {
        background: #F8F4FF;
        border: 1px solid #E9DFFF;
        border-radius: 18px;
        padding: 15px;
        margin-bottom: 12px;
    }

    .creator-list-card-light {
        background: #FFFFFF;
        border: 1px solid #EFEAF8;
        border-radius: 18px;
        padding: 15px;
        margin-bottom: 12px;
    }

    .profile-header {
        display: flex;
        align-items: center;
        gap: 24px;
    }

    .profile-name {
        font-size: 31px;
        font-weight: 900;
        color: #17002E;
        margin-bottom: 5px;
    }

    .profile-handle {
        color: #6F2DE2;
        font-size: 16px;
        font-weight: 800;
        margin-bottom: 8px;
    }

    .status-active {
        background: #E8F8ED;
        color: #148A42;
        padding: 7px 13px;
        border-radius: 999px;
        font-size: 12px;
        font-weight: 900;
    }

    .status-paused {
        background: #FFF3D8;
        color: #B96A00;
        padding: 7px 13px;
        border-radius: 999px;
        font-size: 12px;
        font-weight: 900;
    }

    .info-box {
        background: #FFFFFF;
        border: 1px solid #E9DFFF;
        border-radius: 16px;
        padding: 18px 20px;
        min-width: 128px;
        min-height: 86px;
    }

    .pill {
        display: inline-block;
        background: #F3EAFE;
        color: #6F2DE2;
        padding: 7px 13px;
        border-radius: 999px;
        font-size: 12px;
        font-weight: 800;
        margin-right: 8px;
        margin-bottom: 8px;
    }

    .info-row {
        display: grid;
        grid-template-columns: 26px 1fr;
        gap: 14px;
        padding: 14px 0;
        border-bottom: 1px solid #EFEAF8;
        align-items: start;
    }

    .info-row:last-child { border-bottom: none; }

    .info-icon {
        color: #6F2DE2;
        font-size: 17px;
        margin-top: 1px;
    }

    .info-label {
        font-weight: 800;
        color: #30273F;
        font-size: 14px;
        margin-bottom: 3px;
    }

    .info-value {
        color: #30273F;
        font-size: 14px;
        line-height: 1.45;
    }

    .metric-card {
        border-radius: 18px;
        padding: 20px 16px;
        text-align: center;
        min-height: 126px;
    }

    .metric-label {
        color: #7B6B8F;
        font-size: 13px;
        margin-bottom: 10px;
        font-weight: 600;
    }

    .metric-value {
        color: #17002E;
        font-size: 30px;
        font-weight: 900;
        margin-bottom: 4px;
    }

    .metric-growth {
        color: #12994F;
        font-size: 13px;
        font-weight: 800;
        margin-top: 4px;
    }

    .campaign-table {
        width: 100%;
        border-collapse: collapse;
        font-size: 14px;
    }

    .campaign-table th {
        color: #7B6B8F;
        text-align: left;
        font-size: 13px;
        padding: 13px 8px;
        border-bottom: 1px solid #EFEAF8;
    }

    .campaign-table td {
        color: #30273F;
        padding: 15px 8px;
        border-bottom: 1px solid #EFEAF8;
    }

    .badge-purple, .badge-orange, .badge-blue {
        padding: 7px 11px;
        border-radius: 999px;
        font-size: 12px;
        font-weight: 900;
        display: inline-block;
    }

    .badge-purple { background: #EFE4FF; color: #6F2DE2; }
    .badge-orange { background: #FFF1DD; color: #C76A00; }
    .badge-blue { background: #EAF0FF; color: #1746B3; }

    div[data-testid="stRadio"] > label { display: none; }

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
""")

html("""
<div class="zoy-logo">zoy</div>
<div class="zoy-subtitle">ASSESSORIA</div>
""")

menu = st.sidebar.radio(
    "Menu",
    ["Dashboard", "Influenciadores", "Planejamento", "Projetos"],
    label_visibility="collapsed"
)

st.sidebar.markdown("---")
st.sidebar.markdown("**Jean**")
st.sidebar.caption("Responsável")
st.sidebar.markdown("Sair")

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

if menu == "Dashboard":
    html('<div class="main-title">Olá, Jean.</div>')
    html('<div class="subtitle">Aqui está o panorama da assessoria hoje.</div>')

    c1, c2, c3, c4 = st.columns(4)

    cards = [
        ("Creators ativos", "12"),
        ("Parcerias em andamento", "9"),
        ("Conteúdos pendentes", "17"),
        ("Reuniões da semana", "6")
    ]

    for col, (title, number) in zip([c1, c2, c3, c4], cards):
        with col:
            html(f"""
            <div class="dashboard-card">
                <div class="dashboard-card-title">{title}</div>
                <div class="dashboard-card-number">{number}</div>
            </div>
            """)

    st.markdown("### Parcerias em andamento")
    p1, p2, p3 = st.columns(3)

    with p1:
        html('<div class="simple-card"><h4>FINI</h4><p class="muted">Campanha de Reels + Stories</p><span class="badge-blue">Negociação</span></div>')
    with p2:
        html('<div class="simple-card"><h4>Adidas</h4><p class="muted">Campanha Always On</p><span class="badge-purple">Produção</span></div>')
    with p3:
        html('<div class="simple-card"><h4>Lipton</h4><p class="muted">Stories + Reel</p><span class="badge-orange">Aprovação</span></div>')

elif menu == "Influenciadores":
    html("""
    <div class="page-header">
        <div>
            <div class="page-title">Influenciadores</div>
            <div class="page-subtitle">Gerencie seus influenciadores e acompanhe tudo em um só lugar.</div>
        </div>
        <div class="primary-btn">+ Novo influenciador</div>
    </div>
    """)

    left, right = st.columns([1.05, 3.55], gap="large")

    with left:
        html('<div class="panel-soft">')
        html('<div class="section-title">Influenciadores</div>')
        st.text_input("Buscar influenciador", placeholder="Buscar influenciador...", label_visibility="collapsed")

        selected_creator = st.radio("Influenciadores", list(creators_data.keys()), label_visibility="collapsed")

        for name, data in creators_data.items():
            card_class = "creator-list-card" if name == selected_creator else "creator-list-card-light"
            status_class = "status-active" if data["status"] == "Ativo" else "status-paused"

            html(f"""
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
            """)

        html(f'<div class="muted" style="margin-top:22px;">{len(creators_data)} influenciadores cadastrados</div>')
        html('</div>')

    creator = creators_data[selected_creator]

    with right:
        status_class = "status-active" if creator["status"] == "Ativo" else "status-paused"

        html(f"""
        <div class="panel">
            <div class="profile-header">
                <div class="avatar">{creator["initials"]}</div>
                <div style="flex:1;">
                    <div class="profile-name">{selected_creator}</div>
                    <div class="profile-handle">{creator["handle"]}</div>
                    <div class="muted">{creator["nicho"]}</div>
                    <div class="muted" style="margin-top:10px;">📍 {creator["cidade"]}</div>
                </div>
                <div class="info-box">
                    <div class="muted">Responsável</div>
                    <div style="margin-top:7px;"><b>Jean</b></div>
                </div>
                <div class="info-box">
                    <div class="muted">Status</div>
                    <div style="margin-top:9px;"><span class="{status_class}">{creator["status"]}</span></div>
                </div>
            </div>
        </div>
        """)

        tabs = st.tabs(["Visão geral", "Métricas", "Campanhas ativas", "Acompanhamento", "Histórico", "Documentos"])

        with tabs[0]:
            col_a, col_b = st.columns([1.1, 1.9], gap="large")

            with col_a:
                html(f"""
                <div class="panel">
                    <div class="section-title">Sobre o influenciador</div>

                    <div class="info-row"><div class="info-icon">✉</div><div><div class="info-label">E-mail</div><div class="info-value">{creator["email"]}</div></div></div>
                    <div class="info-row"><div class="info-icon">☎</div><div><div class="info-label">Telefone</div><div class="info-value">{creator["telefone"]}</div></div></div>
                    <div class="info-row"><div class="info-icon">◇</div><div><div class="info-label">Nicho</div><div class="info-value">{creator["nicho"]}</div></div></div>
                    <div class="info-row"><div class="info-icon">▣</div><div><div class="info-label">Aniversário</div><div class="info-value">{creator["aniversario"]}</div></div></div>
                    <div class="info-row"><div class="info-icon">☆</div><div><div class="info-label">Posicionamento</div><div class="info-value">{creator["posicionamento"]}</div></div></div>
                    <div class="info-row"><div class="info-icon">□</div><div><div class="info-label">Observações</div><div class="info-value">{creator["obs"]}</div></div></div>

                    <div style="margin-top:18px;">
                        <span class="pill">Lifestyle</span>
                        <span class="pill">Beleza</span>
                        <span class="pill">Humor</span>
                    </div>
                </div>
                """)

            with col_b:
                html("""
                <div class="panel">
                    <div style="display:flex; justify-content:space-between; align-items:center;">
                        <div class="section-title">Métricas principais</div>
                        <div style="color:#6F2DE2; font-weight:800; font-size:14px;">Ver todas as métricas</div>
                    </div>
                </div>
                """)

                m1, m2, m3, m4 = st.columns(4)

                metrics = [
                    ("Seguidores", creator["seguidores"], "↑ 2,3%"),
                    ("Alcance médio", creator["alcance"], "↑ 8,1%"),
                    ("Views Stories", creator["stories"], "↑ 5,2%"),
                    ("Engajamento", creator["engajamento"], "↑ 0,6%"),
                ]

                for col, (label, value, growth) in zip([m1, m2, m3, m4], metrics):
                    with col:
                        html(f"""
                        <div class="metric-card">
                            <div class="metric-label">{label}</div>
                            <div class="metric-value">{value}</div>
                            <div class="metric-growth">{growth}</div>
                            <div class="muted" style="font-size:12px;">vs mês anterior</div>
                        </div>
                        """)

                st.markdown("<br>", unsafe_allow_html=True)

                html("""
                <div class="panel">
                    <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:16px;">
                        <div class="section-title" style="margin-bottom:0;">Campanhas ativas</div>
                        <div style="color:#6F2DE2; font-weight:800; font-size:14px;">Ver todas</div>
                    </div>

                    <table class="campaign-table">
                        <thead>
                            <tr>
                                <th>Marca</th>
                                <th>Campanha</th>
                                <th>Entrega</th>
                                <th>Prazo</th>
                                <th>Status</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr><td><b>Adidas</b></td><td>Always On</td><td>3 Reels + 6 Stories</td><td>25/05</td><td><span class="badge-purple">Produção</span></td></tr>
                            <tr><td><b>Lipton</b></td><td>Verão 2025</td><td>2 Stories + 1 Reel</td><td>30/05</td><td><span class="badge-orange">Aprovação</span></td></tr>
                            <tr><td><b>FINI</b></td><td>Doces Momentos</td><td>2 Reels + 4 Stories</td><td>15/06</td><td><span class="badge-blue">Negociação</span></td></tr>
                        </tbody>
                    </table>
                </div>
                """)

        with tabs[1]:
            html('<div class="panel"><div class="section-title">Métricas completas</div><p class="muted">Aqui vamos registrar seguidores, alcance, impressões, views, engajamento e atualização manual das métricas.</p></div>')

        with tabs[2]:
            html('<div class="panel"><div class="section-title">Campanhas ativas</div><p class="muted">Aqui fica a visão completa de campanhas vinculadas ao influenciador.</p></div>')

        with tabs[3]:
            html('<div class="panel"><div class="section-title">Acompanhamento de postagem</div><p class="muted">Aqui vamos controlar entrega, data prevista, link, print, métricas e status.</p></div>')

        with tabs[4]:
            html('<div class="panel"><div class="section-title">Histórico</div><p class="muted">Timeline de reuniões, ajustes, retornos comerciais e observações internas.</p></div>')

        with tabs[5]:
            html('<div class="panel"><div class="section-title">Documentos</div><p class="muted">Contratos, mídia kit, dados bancários, NFs e arquivos importantes.</p></div>')

elif menu == "Planejamento":
    html('<div class="page-title">Planejamento</div>')
    html('<div class="page-subtitle">Organize metas, conteúdos e entregas mensais.</div>')
    st.markdown("<br>", unsafe_allow_html=True)

    st.selectbox("Influenciador", list(creators_data.keys()))
    st.text_input("Objetivo do mês", "Crescimento + Engajamento")
    st.text_area("Estratégia", "Foco em lifestyle espontâneo, rotina real e conteúdos mais conversados.")

    c1, c2, c3, c4 = st.columns(4)
    c1.number_input("Reels", value=4)
    c2.number_input("Stories", value=12)
    c3.number_input("Collabs", value=1)
    c4.number_input("Publis", value=1)

elif menu == "Projetos":
    html('<div class="page-title">Projetos</div>')
    html('<div class="page-subtitle">Acompanhe parcerias, campanhas e entregas comerciais.</div>')
    st.markdown("<br>", unsafe_allow_html=True)

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        html('<div class="panel"><div class="section-title">Briefing recebido</div><p>Sephora</p><p>C&A</p></div>')
    with c2:
        html('<div class="panel"><div class="section-title">Negociação</div><p>FINI</p><p>Amaro</p></div>')
    with c3:
        html('<div class="panel"><div class="section-title">Produção</div><p>Adidas</p><p>Lipton</p></div>')
    with c4:
        html('<div class="panel"><div class="section-title">Finalizado</div><p>Azul</p><p>Natura</p></div>')
'''

path = Path("/mnt/data/app_limpo.py")
path.write_text(code, encoding="utf-8")
path.as_posix()
