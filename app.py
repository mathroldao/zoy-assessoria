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
elif menu == "Influenciadores":

    st.markdown("""
    <style>
        .block-container {
            padding-top: 2rem;
            padding-bottom: 2rem;
        }

        .page-header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 28px;
        }

        .page-title {
            font-size: 34px;
            font-weight: 800;
            color: #17002E;
            margin-bottom: 6px;
        }

        .page-subtitle {
            color: #6F6680;
            font-size: 15px;
        }

        .primary-btn {
            background: linear-gradient(135deg, #6F2DE2, #4B12B8);
            color: white;
            padding: 13px 20px;
            border-radius: 12px;
            font-weight: 700;
            text-align: center;
            box-shadow: 0 8px 20px rgba(111,45,226,0.25);
        }

        .panel {
            background: #FFFFFF;
            border: 1px solid #E9DFFF;
            border-radius: 22px;
            padding: 20px;
            box-shadow: 0 10px 30px rgba(111,45,226,0.07);
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

        .avatar {
            width: 72px;
            height: 72px;
            border-radius: 50%;
            background: linear-gradient(135deg, #D8C6FF, #6F2DE2);
            display: flex;
            align-items: center;
            justify-content: center;
            color: white;
            font-size: 26px;
            font-weight: 800;
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

        .muted {
            color: #6F6680;
            font-size: 14px;
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
            border: 1px solid #E9DFFF;
            border-radius: 16px;
            padding: 16px;
            min-height: 80px;
        }

        .metric-card {
            background: #FFFFFF;
            border: 1px solid #E9DFFF;
            border-radius: 18px;
            padding: 20px;
            text-align: center;
            box-shadow: 0 8px 22px rgba(111,45,226,0.05);
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

        .section-title {
            color: #17002E;
            font-size: 20px;
            font-weight: 800;
            margin-bottom: 16px;
        }

        .pill {
            display: inline-block;
            background: #EFE4FF;
            color: #6F2DE2;
            padding: 7px 12px;
            border-radius: 999px;
            font-size: 12px;
            font-weight: 700;
            margin-right: 6px;
            margin-bottom: 6px;
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

        .badge-purple {
            background: #EFE4FF;
            color: #6F2DE2;
            padding: 6px 10px;
            border-radius: 999px;
            font-size: 12px;
            font-weight: 800;
            text-align: center;
        }

        .badge-orange {
            background: #FFF1DD;
            color: #C76A00;
            padding: 6px 10px;
            border-radius: 999px;
            font-size: 12px;
            font-weight: 800;
            text-align: center;
        }

        .badge-blue {
            background: #EAF0FF;
            color: #1746B3;
            padding: 6px 10px;
            border-radius: 999px;
            font-size: 12px;
            font-weight: 800;
            text-align: center;
        }

        div[data-testid="stRadio"] label {
            display: none;
        }

        div[data-testid="stRadio"] div[role="radiogroup"] {
            gap: 0px;
        }
    </style>
    """, unsafe_allow_html=True)

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

    st.markdown("""
    <div class="page-header">
        <div>
            <div class="page-title">Influenciadores</div>
            <div class="page-subtitle">Gerencie seus influenciadores e acompanhe tudo em um só lugar.</div>
        </div>
        <div class="primary-btn">+ Novo influenciador</div>
    </div>
    """, unsafe_allow_html=True)

    left, right = st.columns([1.05, 3.4], gap="large")

    with left:
        st.markdown('<div class="panel">', unsafe_allow_html=True)
        st.markdown('<div class="section-title">Influenciadores</div>', unsafe_allow_html=True)
        st.text_input("Buscar influenciador", placeholder="Buscar influenciador...", label_visibility="collapsed")

        selected_creator = st.radio(
            "Influenciadores",
            list(creators_data.keys()),
            label_visibility="collapsed"
        )

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

        st.markdown('<div class="muted" style="margin-top:22px;">3 influenciadores cadastrados</div>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

    creator = creators_data[selected_creator]

    with right:
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
                    <span class="status-active">{creator["status"]}</span>
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

                    <p><b>E-mail</b><br><span class="muted">{creator["email"]}</span></p>
                    <p><b>Telefone</b><br><span class="muted">{creator["telefone"]}</span></p>
                    <p><b>Nicho</b><br><span class="muted">{creator["nicho"]}</span></p>
                    <p><b>Aniversário</b><br><span class="muted">{creator["aniversario"]}</span></p>
                    <p><b>Posicionamento</b><br><span class="muted">{creator["posicionamento"]}</span></p>
                    <p><b>Observações</b><br><span class="muted">{creator["obs"]}</span></p>

                    <div style="margin-top:15px;">
                        <span class="pill">Lifestyle</span>
                        <span class="pill">Beleza</span>
                        <span class="pill">Humor</span>
                    </div>
                </div>
                """, unsafe_allow_html=True)

            with col_b:
                st.markdown('<div class="panel">', unsafe_allow_html=True)
                st.markdown('<div class="section-title">Métricas principais</div>', unsafe_allow_html=True)

                m1, m2, m3, m4 = st.columns(4)
                with m1:
                    st.markdown(f"""
                    <div class="metric-card">
                        <div class="metric-label">Seguidores</div>
                        <div class="metric-value">{creator["seguidores"]}</div>
                        <div class="metric-growth">↑ 2,3%</div>
                    </div>
                    """, unsafe_allow_html=True)
                with m2:
                    st.markdown(f"""
                    <div class="metric-card">
                        <div class="metric-label">Alcance médio</div>
                        <div class="metric-value">{creator["alcance"]}</div>
                        <div class="metric-growth">↑ 8,1%</div>
                    </div>
                    """, unsafe_allow_html=True)
                with m3:
                    st.markdown(f"""
                    <div class="metric-card">
                        <div class="metric-label">Views Stories</div>
                        <div class="metric-value">{creator["stories"]}</div>
                        <div class="metric-growth">↑ 5,2%</div>
                    </div>
                    """, unsafe_allow_html=True)
                with m4:
                    st.markdown(f"""
                    <div class="metric-card">
                        <div class="metric-label">Engajamento</div>
                        <div class="metric-value">{creator["engajamento"]}</div>
                        <div class="metric-growth">↑ 0,6%</div>
                    </div>
                    """, unsafe_allow_html=True)

                st.markdown("<br>", unsafe_allow_html=True)
                st.markdown('<div class="section-title">Campanhas ativas</div>', unsafe_allow_html=True)

                st.markdown("""
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
                """, unsafe_allow_html=True)

                st.markdown('</div>', unsafe_allow_html=True)

        with tabs[1]:
            st.markdown('<div class="panel"><div class="section-title">Métricas completas</div><p class="muted">Aqui entram seguidores, alcance, impressões, views, engajamento e atualização manual das métricas.</p></div>', unsafe_allow_html=True)

        with tabs[2]:
            st.markdown('<div class="panel"><div class="section-title">Campanhas ativas</div><p class="muted">Aqui fica a visão completa de campanhas vinculadas ao influenciador.</p></div>', unsafe_allow_html=True)

        with tabs[3]:
            st.markdown('<div class="panel"><div class="section-title">Acompanhamento de postagem</div><p class="muted">Aqui vamos controlar entrega, data prevista, link, print, métricas e status.</p></div>', unsafe_allow_html=True)

        with tabs[4]:
            st.markdown('<div class="panel"><div class="section-title">Histórico</div><p class="muted">Timeline de reuniões, ajustes, retornos comerciais e observações internas.</p></div>', unsafe_allow_html=True)

        with tabs[5]:
            st.markdown('<div class="panel"><div class="section-title">Documentos</div><p class="muted">Contratos, mídia kit, dados bancários, NFs e arquivos importantes.</p></div>', unsafe_allow_html=True)

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
