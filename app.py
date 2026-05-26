import streamlit as st

st.set_page_config(
    page_title='Zoy Assessoria',
    page_icon='💜',
    layout='wide'
)

# ======================================================
# CSS
# ======================================================

st.markdown('''
<style>
    .stApp {
        background-color: #FFFFFF;
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

    .zoy-title {
        font-size: 42px;
        font-weight: 900;
        letter-spacing: -1px;
        color: white;
        margin-bottom: -8px;
    }

    .zoy-subtitle {
        font-size: 12px;
        letter-spacing: 4px;
        color: #DCCBFF;
        margin-bottom: 30px;
    }

    .page-title {
        font-size: 34px;
        font-weight: 900;
        color: #17002E;
        margin-bottom: 4px;
    }

    .page-subtitle {
        color: #6F6680;
        font-size: 15px;
        margin-bottom: 22px;
    }

    .section-title {
        font-size: 20px;
        font-weight: 850;
        color: #17002E;
        margin-bottom: 16px;
    }

    .card {
        background: #FFFFFF;
        border: 1px solid #E9DFFF;
        border-radius: 20px;
        padding: 20px;
        box-shadow: none;
        margin-bottom: 16px;
    }

    .profile-card {
        background: #FFFFFF;
        border: 1px solid #E9DFFF;
        border-radius: 24px;
        padding: 24px;
        box-shadow: none;
        margin-bottom: 16px;
    }

    .creator-list-card {
        background: #FFFFFF;
        border: 1px solid #E9DFFF;
        border-radius: 18px;
        padding: 14px;
        margin-bottom: 12px;
    }

    .creator-list-card-active {
        background: #F8F4FF;
        border: 1px solid #DCCBFF;
        border-radius: 18px;
        padding: 14px;
        margin-bottom: 12px;
    }

    .avatar {
        width: 78px;
        height: 78px;
        border-radius: 50%;
        background: linear-gradient(135deg, #B98CFF, #6F2DE2);
        color: white;
        font-size: 28px;
        font-weight: 900;
        display: flex;
        align-items: center;
        justify-content: center;
    }

    .avatar-small {
        width: 44px;
        height: 44px;
        border-radius: 50%;
        background: linear-gradient(135deg, #B98CFF, #6F2DE2);
        color: white;
        font-size: 15px;
        font-weight: 900;
        display: inline-flex;
        align-items: center;
        justify-content: center;
        margin-right: 10px;
        vertical-align: middle;
    }

    .profile-name {
        font-size: 30px;
        font-weight: 900;
        color: #17002E;
        margin-bottom: 3px;
    }

    .profile-handle {
        color: #6F2DE2;
        font-weight: 800;
        font-size: 15px;
        margin-bottom: 6px;
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
        font-weight: 850;
        display: inline-block;
    }

    .status-paused {
        background: #FFF3D8;
        color: #B96A00;
        padding: 7px 13px;
        border-radius: 999px;
        font-size: 12px;
        font-weight: 850;
        display: inline-block;
    }

    .metric-card {
        background: #FFFFFF;
        border: 1px solid #E9DFFF;
        border-radius: 18px;
        padding: 18px;
        text-align: center;
        min-height: 120px;
        box-shadow: none;
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
        font-weight: 800;
        margin-top: 6px;
    }

    .info-label {
        color: #30273F;
        font-size: 14px;
        font-weight: 850;
        margin-bottom: 2px;
    }

    .info-value {
        color: #6F6680;
        font-size: 14px;
        line-height: 1.45;
        margin-bottom: 14px;
        padding-bottom: 14px;
        border-bottom: 1px solid #EFEAF8;
    }

    .pill {
        display: inline-block;
        background: #EFE4FF;
        color: #6F2DE2;
        padding: 7px 12px;
        border-radius: 999px;
        font-size: 12px;
        font-weight: 800;
        margin-right: 6px;
        margin-bottom: 6px;
    }

    .badge-purple {
        background: #EFE4FF;
        color: #6F2DE2;
        padding: 7px 10px;
        border-radius: 999px;
        font-size: 12px;
        font-weight: 850;
        display: inline-block;
    }

    .badge-orange {
        background: #FFF1DD;
        color: #C76A00;
        padding: 7px 10px;
        border-radius: 999px;
        font-size: 12px;
        font-weight: 850;
        display: inline-block;
    }

    .badge-blue {
        background: #EAF0FF;
        color: #1746B3;
        padding: 7px 10px;
        border-radius: 999px;
        font-size: 12px;
        font-weight: 850;
        display: inline-block;
    }

    .campaign-table {
        width: 100%;
        border-collapse: collapse;
        font-size: 14px;
    }

    .campaign-table th {
        color: #7B6B8F;
        font-size: 13px;
        text-align: left;
        padding: 12px 8px;
        border-bottom: 1px solid #EFEAF8;
    }

    .campaign-table td {
        color: #30273F;
        padding: 14px 8px;
        border-bottom: 1px solid #EFEAF8;
        vertical-align: middle;
    }

    div[data-testid="stRadio"] > label {
        display: none;
    }

    .stButton > button {
        border-radius: 12px;
        border: 1px solid #6F2DE2;
        background: #6F2DE2;
        color: white;
        font-weight: 800;
        height: 44px;
    }

    div[data-testid="stTextInput"] input {
        border-radius: 12px;
        border: 1px solid #E9DFFF;
    }

    .stTabs [data-baseweb="tab-list"] {
        gap: 16px;
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
''', unsafe_allow_html=True)

# ======================================================
# SIDEBAR
# ======================================================

st.sidebar.markdown('<div class="zoy-title">zoy</div>', unsafe_allow_html=True)
st.sidebar.markdown('<div class="zoy-subtitle">ASSESSORIA</div>', unsafe_allow_html=True)

menu = st.sidebar.radio(
    'Menu',
    ['Dashboard', 'Influenciadores', 'Planejamento', 'Projetos'],
    label_visibility='collapsed'
)

st.sidebar.markdown('---')
st.sidebar.markdown('**Jean**')
st.sidebar.caption('Responsável')

# ======================================================
# DADOS MOCKADOS
# ======================================================

creators_data = {
    'Jady Carvalho': {
        'initials': 'JC',
        'handle': '@jadycarvalho',
        'nicho': 'Lifestyle • Beleza • Humor',
        'cidade': 'São Paulo, SP',
        'status': 'Ativo',
        'email': 'jadycarvalho@gmail.com',
        'telefone': '(11) 99999-9999',
        'aniversario': '12/03',
        'posicionamento': 'Lifestyle real, rotina espontânea, beleza leve e humor do dia a dia.',
        'obs': 'Tem ótima entrega em Reels. Público jovem e muito engajado.',
        'seguidores': '132K',
        'alcance': '48K',
        'stories': '18K',
        'engajamento': '4,2%',
        'tags': ['Lifestyle', 'Beleza', 'Humor']
    },
    'Malu Borges': {
        'initials': 'MB',
        'handle': '@maluborges',
        'nicho': 'Fashion • Lifestyle',
        'cidade': 'São Paulo, SP',
        'status': 'Ativo',
        'email': 'malu@email.com',
        'telefone': '(11) 98888-8888',
        'aniversario': '04/08',
        'posicionamento': 'Moda urbana, lifestyle aspiracional e rotina criativa.',
        'obs': 'Boa aderência para marcas de moda e beleza.',
        'seguidores': '89K',
        'alcance': '31K',
        'stories': '12K',
        'engajamento': '3,8%',
        'tags': ['Moda', 'Lifestyle', 'Beauty']
    },
    'Vitória Guedes': {
        'initials': 'VG',
        'handle': '@vitoriaguedes',
        'nicho': 'Beauty • Skincare',
        'cidade': 'Rio de Janeiro, RJ',
        'status': 'Ativo',
        'email': 'vitoria@email.com',
        'telefone': '(21) 97777-7777',
        'aniversario': '22/01',
        'posicionamento': 'Beleza acessível, skincare e rotina feminina.',
        'obs': 'Boa entrega em stories e reviews.',
        'seguidores': '76K',
        'alcance': '22K',
        'stories': '9K',
        'engajamento': '3,1%',
        'tags': ['Beauty', 'Skincare', 'Review']
    }
}

campaigns = [
    {
        'marca': 'Adidas',
        'campanha': 'Always On',
        'entrega': '3 Reels + 6 Stories',
        'prazo': '25/05',
        'status': 'Produção',
        'badge': 'badge-purple'
    },
    {
        'marca': 'Lipton',
        'campanha': 'Verão 2025',
        'entrega': '2 Stories + 1 Reel',
        'prazo': '30/05',
        'status': 'Aprovação',
        'badge': 'badge-orange'
    },
    {
        'marca': 'FINI',
        'campanha': 'Doces Momentos',
        'entrega': '2 Reels + 4 Stories',
        'prazo': '15/06',
        'status': 'Negociação',
        'badge': 'badge-blue'
    }
]

# ======================================================
# DASHBOARD
# ======================================================

if menu == 'Dashboard':
    st.markdown('<div class="page-title">Olá, Jean.</div>', unsafe_allow_html=True)
    st.markdown('<div class="page-subtitle">Aqui está o panorama da assessoria hoje.</div>', unsafe_allow_html=True)

    col1, col2, col3, col4 = st.columns(4)

    dashboard_cards = [
        ('Creators ativos', '12'),
        ('Parcerias em andamento', '9'),
        ('Conteúdos pendentes', '17'),
        ('Reuniões da semana', '6')
    ]

    for col, (title, number) in zip([col1, col2, col3, col4], dashboard_cards):
        with col:
            st.markdown(
                f'''
                <div class="card">
                    <div class="metric-label">{title}</div>
                    <div class="metric-value">{number}</div>
                </div>
                ''',
                unsafe_allow_html=True
            )

    st.markdown('### Parcerias em andamento')

    p1, p2, p3 = st.columns(3)

    with p1:
        st.markdown(
            '''
            <div class="card">
                <h4>FINI</h4>
                <p class="muted">Campanha de Reels + Stories</p>
                <span class="badge-blue">Negociação</span>
            </div>
            ''',
            unsafe_allow_html=True
        )

    with p2:
        st.markdown(
            '''
            <div class="card">
                <h4>Adidas</h4>
                <p class="muted">Campanha Always On</p>
                <span class="badge-purple">Produção</span>
            </div>
            ''',
            unsafe_allow_html=True
        )

    with p3:
        st.markdown(
            '''
            <div class="card">
                <h4>Lipton</h4>
                <p class="muted">Stories + Reel</p>
                <span class="badge-orange">Aprovação</span>
            </div>
            ''',
            unsafe_allow_html=True
        )

# ======================================================
# INFLUENCIADORES
# ======================================================

elif menu == 'Influenciadores':

    header_left, header_right = st.columns([5, 1.2])

    with header_left:
        st.markdown('<div class="page-title">Influenciadores</div>', unsafe_allow_html=True)
        st.markdown(
            '<div class="page-subtitle">Gerencie seus influenciadores e acompanhe tudo em um só lugar.</div>',
            unsafe_allow_html=True
        )

    with header_right:
        st.button('+ Novo influenciador', use_container_width=True)

    left, right = st.columns([1.05, 3.4], gap='large')

    with left:
        st.markdown('<div class="section-title">Influenciadores</div>', unsafe_allow_html=True)
        st.text_input(
            'Buscar influenciador',
            placeholder='Buscar influenciador...',
            label_visibility='collapsed'
        )

        selected_creator = st.radio(
            'Influenciadores',
            list(creators_data.keys()),
            label_visibility='collapsed'
        )

        for name, data in creators_data.items():
            card_class = 'creator-list-card-active' if name == selected_creator else 'creator-list-card'
            status_class = 'status-active' if data['status'] == 'Ativo' else 'status-paused'

            st.markdown(
                f'''
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
                ''',
                unsafe_allow_html=True
            )

        st.markdown(
            f'<div class="muted" style="margin-top:22px;">{len(creators_data)} influenciadores cadastrados</div>',
            unsafe_allow_html=True
        )

    creator = creators_data[selected_creator]

    with right:
        status_class = 'status-active' if creator['status'] == 'Ativo' else 'status-paused'

        profile_col_1, profile_col_2 = st.columns([4, 1.2])

        with profile_col_1:
            st.markdown(
                f'''
                <div class="profile-card">
                    <div style="display:flex; align-items:center; gap:22px;">
                        <div class="avatar">{creator["initials"]}</div>
                        <div>
                            <div class="profile-name">{selected_creator}</div>
                            <div class="profile-handle">{creator["handle"]}</div>
                            <div class="muted">{creator["nicho"]}</div>
                            <div class="muted" style="margin-top:8px;">📍 {creator["cidade"]}</div>
                        </div>
                    </div>
                </div>
                ''',
                unsafe_allow_html=True
            )

        with profile_col_2:
            st.markdown(
                f'''
                <div class="profile-card">
                    <div class="muted">Responsável</div>
                    <b>Jean</b>
                    <br><br>
                    <div class="muted">Status</div>
                    <span class="{status_class}">{creator["status"]}</span>
                </div>
                ''',
                unsafe_allow_html=True
            )

        tabs = st.tabs([
            'Visão geral',
            'Métricas',
            'Campanhas ativas',
            'Acompanhamento',
            'Histórico',
            'Documentos'
        ])

        with tabs[0]:
            col_a, col_b = st.columns([1.1, 1.9], gap='large')

            with col_a:
                st.markdown(
                    f'''
                    <div class="card">
                        <div class="section-title">Sobre o influenciador</div>

                        <div class="info-label">E-mail</div>
                        <div class="info-value">{creator["email"]}</div>

                        <div class="info-label">Telefone</div>
                        <div class="info-value">{creator["telefone"]}</div>

                        <div class="info-label">Nicho</div>
                        <div class="info-value">{creator["nicho"]}</div>

                        <div class="info-label">Aniversário</div>
                        <div class="info-value">{creator["aniversario"]}</div>

                        <div class="info-label">Posicionamento</div>
                        <div class="info-value">{creator["posicionamento"]}</div>

                        <div class="info-label">Observações</div>
                        <div class="info-value">{creator["obs"]}</div>
                    </div>
                    ''',
                    unsafe_allow_html=True
                )

                tag_html = ''.join([f'<span class="pill">{tag}</span>' for tag in creator['tags']])
                st.markdown(
                    f'<div style="margin-top:-8px;">{tag_html}</div>',
                    unsafe_allow_html=True
                )

            with col_b:
                st.markdown('<div class="section-title">Métricas principais</div>', unsafe_allow_html=True)

                m1, m2, m3, m4 = st.columns(4)

                metric_items = [
                    ('Seguidores', creator['seguidores'], '↑ 2,3%'),
                    ('Alcance médio', creator['alcance'], '↑ 8,1%'),
                    ('Views Stories', creator['stories'], '↑ 5,2%'),
                    ('Engajamento', creator['engajamento'], '↑ 0,6%')
                ]

                for col, (label, value, growth) in zip([m1, m2, m3, m4], metric_items):
                    with col:
                        st.markdown(
                            f'''
                            <div class="metric-card">
                                <div class="metric-label">{label}</div>
                                <div class="metric-value">{value}</div>
                                <div class="metric-growth">{growth}</div>
                                <div class="muted" style="font-size:12px;">vs mês anterior</div>
                            </div>
                            ''',
                            unsafe_allow_html=True
                        )

                st.markdown('<br>', unsafe_allow_html=True)
                st.markdown('<div class="section-title">Campanhas ativas</div>', unsafe_allow_html=True)

                rows = ''
                for item in campaigns:
                    rows += f'''
                    <tr>
                        <td><b>{item["marca"]}</b></td>
                        <td>{item["campanha"]}</td>
                        <td>{item["entrega"]}</td>
                        <td>{item["prazo"]}</td>
                        <td><span class="{item["badge"]}">{item["status"]}</span></td>
                    </tr>
                    '''

                st.markdown(
                    f'''
                    <div class="card">
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
                                {rows}
                            </tbody>
                        </table>
                    </div>
                    ''',
                    unsafe_allow_html=True
                )

        with tabs[1]:
            st.markdown(
                '''
                <div class="card">
                    <div class="section-title">Métricas completas</div>
                    <p class="muted">Aqui vamos registrar seguidores, alcance, impressões, views, engajamento e atualização manual das métricas.</p>
                </div>
                ''',
                unsafe_allow_html=True
            )

        with tabs[2]:
            st.markdown(
                '''
                <div class="card">
                    <div class="section-title">Campanhas ativas</div>
                    <p class="muted">Aqui fica a visão completa de campanhas vinculadas ao influenciador.</p>
                </div>
                ''',
                unsafe_allow_html=True
            )

        with tabs[3]:
            st.markdown(
                '''
                <div class="card">
                    <div class="section-title">Acompanhamento de postagem</div>
                    <p class="muted">Aqui vamos controlar entrega, data prevista, link, print, métricas e status.</p>
                </div>
                ''',
                unsafe_allow_html=True
            )

        with tabs[4]:
            st.markdown(
                '''
                <div class="card">
                    <div class="section-title">Histórico</div>
                    <p class="muted">Timeline de reuniões, ajustes, retornos comerciais e observações internas.</p>
                </div>
                ''',
                unsafe_allow_html=True
            )

        with tabs[5]:
            st.markdown(
                '''
                <div class="card">
                    <div class="section-title">Documentos</div>
                    <p class="muted">Contratos, mídia kit, dados bancários, NFs e arquivos importantes.</p>
                </div>
                ''',
                unsafe_allow_html=True
            )

# ======================================================
# PLANEJAMENTO
# ======================================================

elif menu == 'Planejamento':
    st.markdown('<div class="page-title">Planejamento</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="page-subtitle">Organize metas, conteúdos e entregas mensais.</div>',
        unsafe_allow_html=True
    )

    st.selectbox('Influenciador', list(creators_data.keys()))
    st.text_input('Objetivo do mês', 'Crescimento + Engajamento')

    st.text_area(
        'Estratégia',
        'Foco em lifestyle espontâneo, rotina real e conteúdos mais conversados.'
    )

    c1, c2, c3, c4 = st.columns(4)

    c1.number_input('Reels', value=4)
    c2.number_input('Stories', value=12)
    c3.number_input('Collabs', value=1)
    c4.number_input('Publis', value=1)

# ======================================================
# PROJETOS
# ======================================================

elif menu == 'Projetos':
    st.markdown('<div class="page-title">Projetos</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="page-subtitle">Acompanhe parcerias, campanhas e entregas comerciais.</div>',
        unsafe_allow_html=True
    )

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        st.markdown(
            '''
            <div class="card">
                <div class="section-title">Briefing recebido</div>
                <p>Sephora</p>
                <p>C&A</p>
            </div>
            ''',
            unsafe_allow_html=True
        )

    with c2:
        st.markdown(
            '''
            <div class="card">
                <div class="section-title">Negociação</div>
                <p>FINI</p>
                <p>Amaro</p>
            </div>
            ''',
            unsafe_allow_html=True
        )

    with c3:
        st.markdown(
            '''
            <div class="card">
                <div class="section-title">Produção</div>
                <p>Adidas</p>
                <p>Lipton</p>
            </div>
            ''',
            unsafe_allow_html=True
        )

    with c4:
        st.markdown(
            '''
            <div class="card">
                <div class="section-title">Finalizado</div>
                <p>Azul</p>
                <p>Natura</p>
            </div>
            ''',
            unsafe_allow_html=True
        )
