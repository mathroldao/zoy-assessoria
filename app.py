
import base64
from copy import deepcopy

import pandas as pd
import requests
import streamlit as st

st.set_page_config(page_title="Zoy Assessoria", page_icon="💜", layout="wide")

st.markdown("""
<style>

/* REMOVE HEADER PADRÃO DO STREAMLIT */
header {
    visibility: hidden;
    height: 0px;
}

/* REMOVE BARRA SUPERIOR */
[data-testid="stHeader"] {
    display: none;
}

/* REMOVE MENU SUPERIOR */
#MainMenu {
    visibility: hidden;
}

/* REMOVE FOOTER */
footer {
    visibility: hidden;
}

/* AJUSTA ESPAÇAMENTO DO TOPO */
.block-container {
    padding-top: 2rem;
}

</style>
""", unsafe_allow_html=True)

API_URL = "https://script.google.com/macros/s/AKfycbx9Qa_fRrUUAbRWomSoKFkwZqiLTzRlqUlvlBnxC9juMMcEmt9G_y4iKXM3okgB_3ZH/exec"

st.markdown("""
<style>
:root{
    --zoy-purple:#5E19D6;
    --zoy-deep:#16002E;
    --zoy-soft:#F7F3FF;
    --zoy-border:#E9DFFF;
    --zoy-muted:#7A7189;
}

.stApp{background:#fff;color:#1f1830}
.block-container{padding-top:2rem;padding-bottom:2rem;max-width:100%;padding-left:3.2rem;padding-right:3.2rem}

/* SIDEBAR */
section[data-testid="stSidebar"]{
    background:linear-gradient(180deg,#25004A 0%,#3A067D 55%,#5E19D6 100%);
}
section[data-testid="stSidebar"] *{color:white!important}
section[data-testid="stSidebar"] > div{padding-top:2.2rem}
.zoy-logo{font-size:42px;font-weight:950;letter-spacing:-2px;margin-bottom:-8px;color:white!important;line-height:.9}
.zoy-subtitle{font-size:11px;letter-spacing:4px;color:#DCCBFF!important;margin-bottom:32px;font-weight:800}
section[data-testid="stSidebar"] .stButton>button{
    background:transparent!important;
    color:rgba(255,255,255,.82)!important;
    border:0!important;
    border-radius:14px!important;
    font-weight:800!important;
    text-align:left!important;
    justify-content:flex-start!important;
    min-height:44px!important;
    padding:10px 14px!important;
    box-shadow:none!important;
}
section[data-testid="stSidebar"] .stButton>button:hover{
    background:rgba(255,255,255,.10)!important;
    color:#fff!important;
}
.sidebar-help{
    margin-top:34px;
    padding:14px 2px;
    color:#E9DDFF!important;
    font-size:13px;
    line-height:1.45;
}

/* HEADER */
.page-title{font-size:34px;font-weight:950;color:#17002E;letter-spacing:-1px;margin-bottom:4px;line-height:1}
.page-subtitle{color:#756B86;font-size:15px;margin-bottom:26px}
.section-title{font-size:18px;font-weight:900;color:#17002E;margin-bottom:12px}
.muted{color:#756B86;font-size:14px}

/* BOTÕES */
.stButton>button{
    border-radius:13px!important;
    font-weight:800!important;
    min-height:38px!important;
    border:1px solid #E9DFFF!important;
    background:#fff!important;
    color:#201533!important;
    box-shadow:none!important;
}
.stButton>button:hover{border-color:#C9ADFF!important;color:#5E19D6!important;background:#FBF8FF!important}
.stButton>button[kind="primary"]{
    background:#5E19D6!important;
    color:white!important;
    border:1px solid #5E19D6!important;
}
.stButton>button[kind="primary"]:hover{
    background:#4A0FB4!important;
    border-color:#4A0FB4!important;
    color:white!important;
}

/* INPUTS */
div[data-testid="stTextInput"] input,div[data-testid="stTextArea"] textarea{
    border-radius:13px!important;
    border:1px solid #E9DFFF!important;
    background:#FAFAFD!important;
}

/* LAYOUT */
.vertical-separator{
    width:1px;
    background:#EFE7FF;
    min-height:720px;
    margin:0 auto;
}
.profile-card{
    background:#fff;
    border:1px solid #E9DFFF;
    border-radius:24px;
    padding:22px;
    box-shadow:none;
    margin-bottom:14px;
}
.profile-actions{margin-top:4px;margin-bottom:20px}
.info-card{background:#fff;border:1px solid #E9DFFF;border-radius:18px;padding:20px;min-height:250px}

/* AVATAR */
.avatar{
    width:86px;height:86px;border-radius:50%;
    background:linear-gradient(135deg,#B98CFF,#6F2DE2);
    color:white;font-size:30px;font-weight:950;
    display:flex;align-items:center;justify-content:center;overflow:hidden;
}
.avatar img{width:86px;height:86px;object-fit:cover;border-radius:50%}
.profile-name{font-size:30px;font-weight:950;color:#17002E;letter-spacing:-.8px;margin-bottom:4px;line-height:1.05}
.profile-handle{color:#5E19D6;font-weight:900;font-size:14px;margin-bottom:6px}

.pill{display:inline-block;background:#EFE4FF;color:#6F2DE2;padding:7px 12px;border-radius:999px;font-size:12px;font-weight:900;margin-right:6px;margin-bottom:6px}
.field-label{color:#17002E;font-size:13px;font-weight:900;margin-bottom:2px}.field-value{color:#4F465D;font-size:14px;margin-bottom:14px}

/* LISTA DE INFLUENCIADORES */
.creator-count{font-size:13px;color:#7A7189;margin-top:12px}

/* TABS */
.stTabs [data-baseweb="tab-list"]{gap:18px;border-bottom:1px solid #EFE7FF;margin-top:14px}
.stTabs [data-baseweb="tab"]{color:#30273F;font-weight:800;padding-left:0;padding-right:0}
.stTabs [aria-selected="true"]{color:#5E19D6!important}
</style>
""", unsafe_allow_html=True)

DEFAULT_OPPORTUNITIES = [
    {"Creator":"", "Marca":"", "Valor":"", "Fee Zoy":"", "Status":"Lead recebido", "Data":"", "Observações":""}
]
DEFAULT_METRICS_HISTORY = pd.DataFrame([
    {"Mês":"Jan","Seguidores":"","Alcance":"","Stories":"","Engajamento":""},
    {"Mês":"Fev","Seguidores":"","Alcance":"","Stories":"","Engajamento":""},
    {"Mês":"Mar","Seguidores":"","Alcance":"","Stories":"","Engajamento":""},
])
DEFAULT_PLANNING = pd.DataFrame([
    {"Creator":"","Objetivo":"","Pilar":"","Ideia":"","Status":"Pendente","Prioridade":"Média"}
])

def initials_from_name(name):
    parts = [p for p in str(name).strip().split() if p]
    if not parts:
        return "CR"
    if len(parts) == 1:
        return parts[0][:2].upper()
    return (parts[0][0] + parts[-1][0]).upper()

def safe_value(value):
    if value is None:
        return ""
    value = str(value)
    if value.lower() in ["nan", "none"]:
        return ""
    return value

def creator_from_sheet_item(item):
    nome = safe_value(item.get("nome_completo") or item.get("nome") or "Sem nome")
    nicho = safe_value(item.get("nicho"))
    return {
        "nome": nome,
        "nome_artistico": safe_value(item.get("nome_artistico") or nome),
        "initials": initials_from_name(nome),
        "handle": safe_value(item.get("instagram")),
        "nicho": nicho,
        "cidade": safe_value(item.get("cidade")),
        "status": safe_value(item.get("status") or "Ativo"),
        "email": safe_value(item.get("email")),
        "telefone": safe_value(item.get("telefone")),
        "aniversario": safe_value(item.get("aniversario")),
        "cpf_cnpj": safe_value(item.get("cpf_cnpj")),
        "endereco": safe_value(item.get("endereco")),
        "pix": safe_value(item.get("pix")),
        "banco": safe_value(item.get("banco")),
        "agencia": safe_value(item.get("agencia")),
        "conta": safe_value(item.get("conta")),
        "responsavel": safe_value(item.get("responsavel")),
        "foto": safe_value(item.get("foto")),
        "bio": safe_value(item.get("bio")),
        "posicionamento": safe_value(item.get("posicionamento")),
        "tom_voz": safe_value(item.get("tom_voz")),
        "marcas_sonho": safe_value(item.get("marcas_sonho")),
        "marcas_no_fit": safe_value(item.get("marcas_no_fit")),
        "obs": safe_value(item.get("obs")),
        "seguidores": safe_value(item.get("seguidores")),
        "alcance": safe_value(item.get("alcance")),
        "impressoes": safe_value(item.get("impressoes")),
        "stories": safe_value(item.get("stories")),
        "engajamento": safe_value(item.get("engajamento")),
        "crescimento": safe_value(item.get("crescimento")),
        "tags": [tag.strip() for tag in nicho.replace("•", ",").split(",") if tag.strip()],
    }

def carregar_influenciadores():
    try:
        response = requests.get(API_URL, timeout=15)
        if response.status_code != 200:
            return {}
        dados = response.json()
        if not isinstance(dados, list) or not dados:
            return {}
        creators = {}
        for item in dados:
            if not isinstance(item, dict):
                continue
            nome = safe_value(item.get("nome_completo") or item.get("nome"))
            if nome:
                creators[nome] = creator_from_sheet_item(item)
        return creators
    except Exception:
        return {}

def salvar_influenciador_sheets(dados):
    try:
        response = requests.post(API_URL, json=dados, timeout=15)
        return response.status_code == 200
    except Exception:
        return False

def atualizar_influenciador_sheets(nome_original, dados):
    try:
        payload = {
            "action": "update",
            "nome_original": nome_original,
            **dados
        }

        response = requests.post(API_URL, json=payload, timeout=15)
        return response.status_code == 200
    except Exception:
        return False

def excluir_influenciador_sheets(nome_original):
    try:
        payload = {
            "action": "delete",
            "nome_original": nome_original
        }

        response = requests.post(API_URL, json=payload, timeout=15)
        return response.status_code == 200
    except Exception:
        return False

def refresh_creators():
    st.session_state.creators = carregar_influenciadores()
    names = list(st.session_state.creators.keys())
    if names:
        if st.session_state.selected_creator not in names:
            st.session_state.selected_creator = names[0]
    else:
        st.session_state.selected_creator = None

def get_creator_names():
    return list(st.session_state.creators.keys())

def render_status(status):
    status = status or "Ativo"
    if status == "Ativo":
        st.success("Ativo")
    elif status == "Pausado":
        st.warning("Pausado")
    else:
        st.info(status)

def field(label, value):
    st.markdown(f'<div class="field-label">{label}</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="field-value">{safe_value(value)}</div>', unsafe_allow_html=True)

def image_to_data_url(uploaded_file):
    if uploaded_file is None:
        return ""
    encoded = base64.b64encode(uploaded_file.getvalue()).decode()
    return f"data:{uploaded_file.type};base64,{encoded}"

def avatar_html(data):
    foto = data.get("foto", "")
    initials = data.get("initials", "CR")
    if foto:
        return f'<div class="avatar"><img src="{foto}"></div>'
    return f'<div class="avatar">{initials}</div>'

if "creators" not in st.session_state:
    st.session_state.creators = carregar_influenciadores()
if "opportunities" not in st.session_state:
    st.session_state.opportunities = deepcopy(DEFAULT_OPPORTUNITIES)
if "metrics_history" not in st.session_state:
    st.session_state.metrics_history = DEFAULT_METRICS_HISTORY.copy()
if "planning" not in st.session_state:
    st.session_state.planning = DEFAULT_PLANNING.copy()
if "selected_creator" not in st.session_state:
    st.session_state.selected_creator = next(iter(st.session_state.creators), None)
if "show_new_creator" not in st.session_state:
    st.session_state.show_new_creator = False
if "editing_creator" not in st.session_state:
    st.session_state.editing_creator = None
if "deleting_creator" not in st.session_state:
    st.session_state.deleting_creator = None
if "menu" not in st.session_state:
    st.session_state.menu = "Influenciadores"

st.sidebar.markdown('<div class="zoy-logo">zoy</div>', unsafe_allow_html=True)
st.sidebar.markdown('<div class="zoy-subtitle">ASSESSORIA</div>', unsafe_allow_html=True)

for option in ["Dashboard", "Influenciadores", "Planejamento", "Oportunidades", "Documentos"]:
    label = "→ " + option if st.session_state.menu == option else option
    if st.sidebar.button(label, key=f"menu_{option}", use_container_width=True):
        st.session_state.menu = option
        if option == "Influenciadores":
            st.session_state.show_new_creator = False
        st.rerun()

menu = st.session_state.menu

st.sidebar.markdown(
    '<div class="sidebar-help">Sistema interno de gestão da assessoria.</div>',
    unsafe_allow_html=True
)

if menu == "Dashboard":
    st.markdown('<div class="page-title">Dashboard</div>', unsafe_allow_html=True)
    st.markdown('<div class="page-subtitle">Panorama da assessoria.</div>', unsafe_allow_html=True)
    open_opps = len([o for o in st.session_state.opportunities if o.get("Status") not in ["Pago", "Perdido"]])
    closed_opps = len([o for o in st.session_state.opportunities if o.get("Status") == "Fechado"])
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Creators ativos", len(st.session_state.creators))
    c2.metric("Oportunidades abertas", open_opps)
    c3.metric("Fechamentos do mês", closed_opps)
    c4.metric("Reuniões da semana", 0)
    ca, cb = st.columns([1.5, 1], gap="large")
    with ca:
        st.markdown("### Oportunidades recentes")
        st.dataframe(pd.DataFrame(st.session_state.opportunities), use_container_width=True, hide_index=True)
    with cb:
        st.markdown("### Alertas")
        st.info("Cadastre e atualize os influenciadores pelo sistema.")

elif menu == "Influenciadores":
    header_left, header_right = st.columns([5, 1.4])
    with header_left:
        st.markdown('<div class="page-title">Influenciadores</div>', unsafe_allow_html=True)
        st.markdown('<div class="page-subtitle">Cadastro, métricas, posicionamento e histórico dos creators.</div>', unsafe_allow_html=True)
    with header_right:
        if st.button("+ Novo influenciador", type="primary", use_container_width=True):
            st.session_state.show_new_creator = True

    if st.session_state.show_new_creator:
        with st.expander("Cadastrar novo influenciador", expanded=True):
            with st.form("form_new_creator"):
                col1, col2, col3 = st.columns(3)
                with col1:
                    nome = st.text_input("Nome completo")
                    nome_artistico = st.text_input("Nome artístico")
                    handle = st.text_input("@ Instagram")
                    email = st.text_input("E-mail")
                    telefone = st.text_input("Telefone")
                with col2:
                    cidade = st.text_input("Cidade")
                    nicho = st.text_input("Nicho")
                    aniversario = st.text_input("Aniversário")
                    cpf_cnpj = st.text_input("CPF/CNPJ")
                    status = st.selectbox("Status", ["Ativo", "Pausado", "Encerrado"])
                with col3:
                    pix = st.text_input("Chave Pix")
                    banco = st.text_input("Banco")
                    agencia = st.text_input("Agência")
                    conta = st.text_input("Conta")
                    endereco = st.text_input("Endereço")
                bio = st.text_area("Bio estratégica")
                posicionamento = st.text_area("Posicionamento")
                tom_voz = st.text_area("Tom de voz")
                obs = st.text_area("Observações internas")

                if st.form_submit_button("Salvar influenciador"):
                    if not nome:
                        st.error("Preencha o nome do influenciador.")
                    else:
                        novo = {
                            "nome_completo": nome,
                            "nome_artistico": nome_artistico or nome,
                            "instagram": handle,
                            "email": email,
                            "telefone": telefone,
                            "cidade": cidade,
                            "nicho": nicho,
                            "aniversario": aniversario,
                            "cpf_cnpj": cpf_cnpj,
                            "pix": pix,
                            "banco": banco,
                            "agencia": agencia,
                            "conta": conta,
                            "bio": bio,
                            "posicionamento": posicionamento,
                            "status": status,
                            "foto": "",
                        }
                        ok = salvar_influenciador_sheets(novo)
                        if ok:
                            refresh_creators()
                            st.session_state.selected_creator = nome
                            st.session_state.show_new_creator = False
                            st.success("Influenciador salvo.")
                            st.rerun()
                        else:
                            st.error("Não consegui salvar no Google Sheets. Verifique a implantação do Apps Script.")

    left, sep, right = st.columns([0.92, 0.06, 3.72], gap="large")
    names = get_creator_names()

    with sep:
        st.markdown('<div class="vertical-separator"></div>', unsafe_allow_html=True)

    with left:
        st.markdown('<div class="section-title">Influenciadores</div>', unsafe_allow_html=True)
        query = st.text_input("Buscar influenciador", placeholder="Buscar influenciador...", label_visibility="collapsed").lower()
        if not names:
            st.info("Nenhum influenciador cadastrado ainda.")
        else:
            shown = [n for n in names if query in n.lower() or query in st.session_state.creators[n].get("handle", "").lower()]
            for name in shown:
                data = st.session_state.creators[name]
                prefix = "→ " if name == st.session_state.selected_creator else ""
                handle_label = data.get("handle", "")
                if st.button(f"{prefix}{name}  ·  {handle_label}", key=f"select_{name}", use_container_width=True):
                    st.session_state.selected_creator = name
                    st.rerun()
            st.markdown(f'<div class="creator-count">{len(st.session_state.creators)} influenciadores cadastrados</div>', unsafe_allow_html=True)

    if not names:
        with right:
            st.warning("Cadastre o primeiro influenciador usando o botão '+ Novo influenciador'.")
        st.stop()

    if st.session_state.selected_creator not in names:
        st.session_state.selected_creator = names[0]

    selected = st.session_state.selected_creator
    creator = st.session_state.creators[selected]

    with right:
        st.markdown('<div class="profile-card">', unsafe_allow_html=True)
        h1, h2, h3 = st.columns([0.7, 3.2, 1.1])
        with h1:
            st.markdown(avatar_html(creator), unsafe_allow_html=True)
        with h2:
            st.markdown(f'<div class="profile-name">{selected}</div>', unsafe_allow_html=True)
            st.markdown(f'<div class="profile-handle">{creator.get("handle", "")}</div>', unsafe_allow_html=True)
            st.caption(creator.get("nicho", ""))
            st.caption(f"📍 {creator.get('cidade', '')}")
        with h3:
            st.markdown("**Status**")
            render_status(creator.get("status", "Ativo"))
        st.markdown("</div>", unsafe_allow_html=True)

        st.markdown('<div class="profile-actions">', unsafe_allow_html=True)
        a1, a2, a3 = st.columns([1, 1, 4])
        with a1:
            if st.button("Editar dados", use_container_width=True):
                st.session_state.editing_creator = selected
        with a2:
            if st.button("Excluir", use_container_width=True):
                st.session_state.deleting_creator = selected
        st.markdown('</div>', unsafe_allow_html=True)

        if st.session_state.deleting_creator == selected:
            st.warning("Tem certeza que deseja excluir este influenciador?")

            cdel1, cdel2 = st.columns(2)

            with cdel1:
                if st.button("Confirmar exclusão", use_container_width=True):
                    ok = excluir_influenciador_sheets(selected)

                    if ok:
                        refresh_creators()
                        st.session_state.deleting_creator = None
                        st.success("Influenciador excluído.")
                        st.rerun()
                    else:
                        st.error("Erro ao excluir influenciador.")

            with cdel2:
                if st.button("Cancelar exclusão", use_container_width=True):
                    st.session_state.deleting_creator = None
                    st.rerun()

        if st.session_state.editing_creator == selected:
            with st.expander("Editar dados do influenciador", expanded=True):
                st.info("Por enquanto, a edição permanente deve ser feita direto no Google Sheets. Nesta tela a edição fica apenas na sessão atual.")
                with st.form("form_edit_creator"):
                    col1, col2, col3 = st.columns(3)
                    with col1:
                        enome = st.text_input("Nome completo", value=creator.get("nome", selected))
                        enomeart = st.text_input("Nome artístico", value=creator.get("nome_artistico", selected))
                        ehandle = st.text_input("@ Instagram", value=creator.get("handle", ""))
                        eemail = st.text_input("E-mail", value=creator.get("email", ""))
                        etel = st.text_input("Telefone", value=creator.get("telefone", ""))
                    with col2:
                        ecid = st.text_input("Cidade", value=creator.get("cidade", ""))
                        enicho = st.text_input("Nicho", value=creator.get("nicho", ""))
                        eani = st.text_input("Aniversário", value=creator.get("aniversario", ""))
                        ecpf = st.text_input("CPF/CNPJ", value=creator.get("cpf_cnpj", ""))
                        opts = ["Ativo", "Pausado", "Encerrado"]
                        cur = creator.get("status", "Ativo")
                        cur = cur if cur in opts else "Ativo"
                        estatus = st.selectbox("Status", opts, index=opts.index(cur))
                    with col3:
                        epix = st.text_input("Chave Pix", value=creator.get("pix", ""))
                        ebanco = st.text_input("Banco", value=creator.get("banco", ""))
                        eag = st.text_input("Agência", value=creator.get("agencia", ""))
                        econta = st.text_input("Conta", value=creator.get("conta", ""))
                        eend = st.text_input("Endereço", value=creator.get("endereco", ""))
                    ebio = st.text_area("Bio estratégica", value=creator.get("bio", ""))
                    epos = st.text_area("Posicionamento", value=creator.get("posicionamento", ""))
                    etom = st.text_area("Tom de voz", value=creator.get("tom_voz", ""))
                    ems = st.text_area("Marcas dos sonhos", value=creator.get("marcas_sonho", ""))
                    enf = st.text_area("Marcas no-fit", value=creator.get("marcas_no_fit", ""))
                    eobs = st.text_area("Observações internas", value=creator.get("obs", ""))

                    s1, s2 = st.columns([1, 1])
                    save = s1.form_submit_button("Salvar alterações")
                    cancel = s2.form_submit_button("Cancelar")
                    if save:
                        payload = {
                            "nome_completo": enome,
                            "nome_artistico": enomeart,
                            "instagram": ehandle,
                            "email": eemail,
                            "telefone": etel,
                            "cidade": ecid,
                            "nicho": enicho,
                            "aniversario": eani,
                            "cpf_cnpj": ecpf,
                            "pix": epix,
                            "banco": ebanco,
                            "agencia": eag,
                            "conta": econta,
                            "bio": ebio,
                            "posicionamento": epos,
                            "status": estatus,
                            "foto": creator.get("foto", "")
                        }

                        ok = atualizar_influenciador_sheets(selected, payload)

                        if ok:
                            refresh_creators()
                            st.session_state.selected_creator = enome
                            st.session_state.editing_creator = None
                            st.success("Influenciador atualizado.")
                            st.rerun()
                        else:
                            st.error("Erro ao atualizar influenciador.")
                    if cancel:
                        st.session_state.editing_creator = None
                        st.rerun()

        tabs = st.tabs(["Dados gerais", "Posicionamento", "Métricas", "Histórico", "Arquivos"])
        with tabs[0]:
            ca, cb, cc = st.columns(3)
            with ca:
                st.markdown("### Contato")
                field("Nome completo", creator.get("nome", ""))
                field("Nome artístico", creator.get("nome_artistico", ""))
                field("Instagram", creator.get("handle", ""))
                field("E-mail", creator.get("email", ""))
                field("Telefone", creator.get("telefone", ""))
            with cb:
                st.markdown("### Dados pessoais")
                field("Cidade", creator.get("cidade", ""))
                field("Endereço", creator.get("endereco", ""))
                field("Aniversário", creator.get("aniversario", ""))
                field("CPF/CNPJ", creator.get("cpf_cnpj", ""))
            with cc:
                st.markdown("### Dados bancários")
                field("Pix", creator.get("pix", ""))
                field("Banco", creator.get("banco", ""))
                field("Agência", creator.get("agencia", ""))
                field("Conta", creator.get("conta", ""))

        with tabs[1]:
            st.markdown("### Posicionamento")
            field("Nicho", creator.get("nicho", ""))
            field("Bio estratégica", creator.get("bio", ""))
            field("Posicionamento", creator.get("posicionamento", ""))
            field("Tom de voz", creator.get("tom_voz", ""))
            field("Marcas dos sonhos", creator.get("marcas_sonho", ""))
            field("Marcas no-fit", creator.get("marcas_no_fit", ""))
            field("Observações internas", creator.get("obs", ""))
            tags_html = "".join([f'<span class="pill">{t}</span>' for t in creator.get("tags", [])])
            st.markdown(tags_html, unsafe_allow_html=True)

        with tabs[2]:
            st.markdown("### Métricas principais")

            mc1, mc2, mc3 = st.columns(3)
            mc4, mc5, mc6 = st.columns(3)

            edit_seguidores = mc1.text_input("Seguidores", value=creator.get("seguidores", ""), key=f"met_seguidores_{selected}")
            edit_alcance = mc2.text_input("Alcance", value=creator.get("alcance", ""), key=f"met_alcance_{selected}")
            edit_impressoes = mc3.text_input("Impressões", value=creator.get("impressoes", ""), key=f"met_impressoes_{selected}")
            edit_stories = mc4.text_input("Stories", value=creator.get("stories", ""), key=f"met_stories_{selected}")
            edit_engajamento = mc5.text_input("Engajamento", value=creator.get("engajamento", ""), key=f"met_engajamento_{selected}")
            edit_crescimento = mc6.text_input("Crescimento", value=creator.get("crescimento", ""), key=f"met_crescimento_{selected}")

            if st.button("Salvar métricas", use_container_width=True):
                payload = {
                    "nome_completo": creator.get("nome", selected),
                    "nome_artistico": creator.get("nome_artistico", selected),
                    "instagram": creator.get("handle", ""),
                    "email": creator.get("email", ""),
                    "telefone": creator.get("telefone", ""),
                    "cidade": creator.get("cidade", ""),
                    "nicho": creator.get("nicho", ""),
                    "aniversario": creator.get("aniversario", ""),
                    "cpf_cnpj": creator.get("cpf_cnpj", ""),
                    "pix": creator.get("pix", ""),
                    "banco": creator.get("banco", ""),
                    "agencia": creator.get("agencia", ""),
                    "conta": creator.get("conta", ""),
                    "bio": creator.get("bio", ""),
                    "posicionamento": creator.get("posicionamento", ""),
                    "status": creator.get("status", "Ativo"),
                    "foto": creator.get("foto", ""),
                    "seguidores": edit_seguidores,
                    "alcance": edit_alcance,
                    "impressoes": edit_impressoes,
                    "stories": edit_stories,
                    "engajamento": edit_engajamento,
                    "crescimento": edit_crescimento
                }

                ok = atualizar_influenciador_sheets(selected, payload)

                if ok:
                    refresh_creators()
                    st.success("Métricas atualizadas.")
                    st.rerun()
                else:
                    st.error("Erro ao salvar métricas no Google Sheets.")

            st.markdown("### Histórico mensal")
            st.caption("O histórico mensal ainda será conectado a uma aba própria de métricas. Por enquanto, esta tabela é apenas visual.")
            st.dataframe(st.session_state.metrics_history, use_container_width=True, hide_index=True)

        with tabs[3]:
            st.markdown("### Histórico")
            st.write("18/05 — Reunião mensal realizada")
            st.write("15/05 — Proposta enviada para marca")
            st.write("10/05 — Ajuste de posicionamento aprovado")
            st.write("02/05 — Atualização de métricas realizada")

        with tabs[4]:
            st.markdown("### Arquivos")
            st.file_uploader("Mídia kit", type=["pdf", "pptx", "docx"])
            st.file_uploader("Contrato", type=["pdf", "docx"])
            st.file_uploader("Documentos pessoais", type=["pdf", "jpg", "png"])
            st.file_uploader("Comprovante bancário", type=["pdf", "jpg", "png"])
            st.file_uploader("Notas fiscais", type=["pdf", "xml"])

elif menu == "Planejamento":
    st.markdown('<div class="page-title">Planejamento</div>', unsafe_allow_html=True)
    st.markdown('<div class="page-subtitle">Gestão estratégica mensal dos creators assessorados.</div>', unsafe_allow_html=True)
    names = get_creator_names()
    col1, col2 = st.columns([1, 2])
    with col1:
        if names:
            st.selectbox("Influenciador", names)
        else:
            st.info("Cadastre influenciadores para planejar.")
        st.selectbox("Objetivo do mês", ["Crescimento", "Monetização", "Posicionamento", "Autoridade", "Relacionamento com marcas", "Awareness"])
        st.multiselect("Pilares editoriais", ["Lifestyle", "Beleza", "Skincare", "Humor", "Moda", "Viagem", "Fitness", "Gastronomia"], default=["Lifestyle"])
        st.checkbox("Reunião realizada")
        st.checkbox("Planejamento aprovado")
        st.checkbox("Creator alinhado")
        st.checkbox("Execução iniciada")
    with col2:
        st.markdown("### Plano do mês")
        st.text_area("Estratégia do mês", "Descrever a estratégia geral do creator para o mês.")
        st.text_area("Conteúdos orgânicos sugeridos", "Ideia 1\\nIdeia 2\\nIdeia 3")
        st.text_area("Collabs sugeridas", "Creator X — objetivo\\nCreator Y — objetivo")
        st.text_area("Marcas alvo", "Marca 1 — motivo fit\\nMarca 2 — abordagem")
        st.text_area("Datas importantes", "Eventos, sazonalidades e datas relevantes.")
    st.markdown("### Planejamentos em andamento")
    st.dataframe(st.session_state.planning, use_container_width=True, hide_index=True)

elif menu == "Oportunidades":
    st.markdown('<div class="page-title">Oportunidades</div>', unsafe_allow_html=True)
    st.markdown('<div class="page-subtitle">Pipeline comercial da assessoria por creator.</div>', unsafe_allow_html=True)
    names = get_creator_names()
    with st.expander("+ Nova oportunidade"):
        with st.form("new_opportunity"):
            c1, c2, c3 = st.columns(3)
            with c1:
                if names:
                    op_creator = st.selectbox("Creator", names)
                else:
                    op_creator = ""
                    st.info("Cadastre influenciadores primeiro.")
                op_marca = st.text_input("Marca")
                op_status = st.selectbox("Status", ["Lead recebido", "Abordagem", "Negociação", "Contrato", "Fechado", "Perdido", "Pago"])
            with c2:
                op_valor = st.text_input("Valor")
                op_fee = st.text_input("Fee Zoy")
                op_data = st.text_input("Data")
            with c3:
                op_obs = st.text_area("Observações")
            if st.form_submit_button("Salvar oportunidade"):
                if op_creator:
                    st.session_state.opportunities.append({"Creator": op_creator, "Marca": op_marca, "Valor": op_valor, "Fee Zoy": op_fee, "Status": op_status, "Data": op_data, "Observações": op_obs})
                    st.rerun()
                else:
                    st.error("Cadastre pelo menos um influenciador antes.")
    statuses = ["Lead recebido", "Abordagem", "Negociação", "Contrato", "Fechado", "Pago"]
    cols = st.columns(len(statuses))
    for col, status in zip(cols, statuses):
        with col:
            st.markdown(f"### {status}")
            filtered = [o for o in st.session_state.opportunities if o.get("Status") == status]
            if not filtered:
                st.caption("Sem oportunidades")
            for opp in filtered:
                st.markdown(f"**{opp.get('Marca','')}**")
                st.caption(opp.get("Creator", ""))
                st.write(opp.get("Valor", ""))
                st.caption(f"Fee Zoy: {opp.get('Fee Zoy', '')}")
                st.markdown("---")
    st.markdown("### Base completa")
    st.dataframe(pd.DataFrame(st.session_state.opportunities), use_container_width=True, hide_index=True)

elif menu == "Documentos":
    st.markdown('<div class="page-title">Documentos</div>', unsafe_allow_html=True)
    st.markdown('<div class="page-subtitle">Central de arquivos dos influenciadores.</div>', unsafe_allow_html=True)
    names = get_creator_names()
    if names:
        st.selectbox("Influenciador", names)
    else:
        st.info("Cadastre influenciadores primeiro.")
    st.markdown("### Uploads")
    st.file_uploader("Mídia kit", type=["pdf", "pptx", "docx"])
    st.file_uploader("Contrato", type=["pdf", "docx"])
    st.file_uploader("Documentos pessoais", type=["pdf", "jpg", "png"])
    st.file_uploader("Comprovante bancário", type=["pdf", "jpg", "png"])
    st.file_uploader("Notas fiscais", type=["pdf", "xml"])
    st.info("Na próxima etapa conectamos esses arquivos ao Google Drive ou banco de dados.")
