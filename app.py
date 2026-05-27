
import streamlit as st
import pandas as pd
from copy import deepcopy

st.set_page_config(page_title="Zoy Assessoria", page_icon="💜", layout="wide")

st.markdown("""
<style>
.stApp { background:#FFFFFF; }
.block-container { padding-top:2rem; padding-bottom:2rem; max-width:100%; }
section[data-testid="stSidebar"] { background:linear-gradient(180deg,#2B005D 0%,#6F2DE2 100%); }
section[data-testid="stSidebar"] * { color:white !important; }
.page-title { font-size:34px; font-weight:900; color:#17002E; margin-bottom:4px; }
.page-subtitle { color:#6F6680; font-size:15px; margin-bottom:22px; }
.zoy-title { font-size:42px; font-weight:900; color:white; margin-bottom:-8px; }
.zoy-subtitle { font-size:12px; letter-spacing:4px; color:#DCCBFF; margin-bottom:30px; }
.pill { display:inline-block; background:#EFE4FF; color:#6F2DE2; padding:7px 12px; border-radius:999px; font-size:12px; font-weight:800; margin-right:6px; margin-bottom:6px; }
.avatar { width:70px; height:70px; border-radius:50%; background:linear-gradient(135deg,#B98CFF,#6F2DE2); color:white; font-size:26px; font-weight:900; display:flex; align-items:center; justify-content:center; }
.avatar-small { width:40px; height:40px; border-radius:50%; background:linear-gradient(135deg,#B98CFF,#6F2DE2); color:white; font-size:14px; font-weight:900; display:flex; align-items:center; justify-content:center; }
.creator-card { border:1px solid #E9DFFF; border-radius:16px; padding:12px; margin-bottom:10px; }
.creator-card-active { border:1px solid #DCCBFF; background:#F8F4FF; border-radius:16px; padding:12px; margin-bottom:10px; }
.profile-box { border:1px solid #E9DFFF; border-radius:22px; padding:22px; margin-bottom:18px; }
.stButton > button { border-radius:12px; font-weight:700; min-height:38px; }
</style>
""", unsafe_allow_html=True)

DEFAULT_CREATORS = {
    "Jady Carvalho": {
        "nome": "Jady Carvalho",
        "nome_artistico": "Jady Carvalho",
        "initials": "JC",
        "handle": "@jadycarvalho",
        "nicho": "Lifestyle • Beleza • Humor",
        "cidade": "São Paulo, SP",
        "status": "Ativo",
        "email": "jadycarvalho@gmail.com",
        "telefone": "(11) 99999-9999",
        "aniversario": "12/03",
        "cpf_cnpj": "000.000.000-00",
        "endereco": "São Paulo, SP",
        "pix": "jadycarvalho@gmail.com",
        "banco": "Itaú",
        "agencia": "0001",
        "conta": "00000-0",
        "responsavel": "Jean",
        "bio": "Creator de lifestyle, beleza e humor com linguagem espontânea.",
        "posicionamento": "Lifestyle real, rotina espontânea, beleza leve e humor do dia a dia.",
        "tom_voz": "Espontâneo, leve, bem-humorado e próximo.",
        "marcas_sonho": "Adidas, Sephora, Sallve, Natura",
        "marcas_no_fit": "Marcas sem fit com beleza, lifestyle ou humor.",
        "obs": "Tem ótima entrega em Reels. Público jovem e muito engajado.",
        "seguidores": "132K",
        "alcance": "48K",
        "impressoes": "68K",
        "stories": "18K",
        "engajamento": "4,2%",
        "crescimento": "2,3%",
        "tags": ["Lifestyle", "Beleza", "Humor"],
    },
    "Malu Borges": {
        "nome": "Malu Borges",
        "nome_artistico": "Malu Borges",
        "initials": "MB",
        "handle": "@maluborges",
        "nicho": "Fashion • Lifestyle",
        "cidade": "São Paulo, SP",
        "status": "Ativo",
        "email": "malu@email.com",
        "telefone": "(11) 98888-8888",
        "aniversario": "04/08",
        "cpf_cnpj": "000.000.000-00",
        "endereco": "São Paulo, SP",
        "pix": "malu@email.com",
        "banco": "C6",
        "agencia": "0001",
        "conta": "00000-0",
        "responsavel": "Jean",
        "bio": "Creator de moda e lifestyle urbano.",
        "posicionamento": "Moda urbana, lifestyle aspiracional e rotina criativa.",
        "tom_voz": "Fashion, urbano, aspiracional e direto.",
        "marcas_sonho": "C&A, Amaro, Adidas, Arezzo",
        "marcas_no_fit": "Marcas fora do universo fashion/lifestyle.",
        "obs": "Boa aderência para marcas de moda e beleza.",
        "seguidores": "89K",
        "alcance": "31K",
        "impressoes": "44K",
        "stories": "12K",
        "engajamento": "3,8%",
        "crescimento": "1,8%",
        "tags": ["Moda", "Lifestyle", "Beauty"],
    },
    "Vitória Guedes": {
        "nome": "Vitória Guedes",
        "nome_artistico": "Vitória Guedes",
        "initials": "VG",
        "handle": "@vitoriaguedes",
        "nicho": "Beauty • Skincare",
        "cidade": "Rio de Janeiro, RJ",
        "status": "Ativo",
        "email": "vitoria@email.com",
        "telefone": "(21) 97777-7777",
        "aniversario": "22/01",
        "cpf_cnpj": "000.000.000-00",
        "endereco": "Rio de Janeiro, RJ",
        "pix": "vitoria@email.com",
        "banco": "Nubank",
        "agencia": "0001",
        "conta": "00000-0",
        "responsavel": "Jean",
        "bio": "Creator focada em beleza, skincare e rotina.",
        "posicionamento": "Beleza acessível, skincare e rotina feminina.",
        "tom_voz": "Educativo, próximo e leve.",
        "marcas_sonho": "Sallve, Creamy, Natura, Sephora",
        "marcas_no_fit": "Marcas sem conexão com beleza ou rotina.",
        "obs": "Boa entrega em stories e reviews.",
        "seguidores": "76K",
        "alcance": "22K",
        "impressoes": "29K",
        "stories": "9K",
        "engajamento": "3,1%",
        "crescimento": "1,1%",
        "tags": ["Beauty", "Skincare", "Review"],
    },
}

DEFAULT_OPPORTUNITIES = [
    {"Creator": "Jady Carvalho", "Marca": "Adidas", "Valor": "R$ 12.000", "Fee Zoy": "R$ 2.400", "Status": "Negociação", "Data": "27/05", "Observações": "Cliente pediu proposta."},
    {"Creator": "Malu Borges", "Marca": "C&A", "Valor": "R$ 8.000", "Fee Zoy": "R$ 1.600", "Status": "Lead recebido", "Data": "26/05", "Observações": "Mapear fit de conteúdo."},
    {"Creator": "Vitória Guedes", "Marca": "Sallve", "Valor": "R$ 6.500", "Fee Zoy": "R$ 1.300", "Status": "Fechado", "Data": "25/05", "Observações": "Contrato em andamento."},
]

DEFAULT_METRICS_HISTORY = pd.DataFrame([
    {"Mês": "Jan", "Seguidores": "120K", "Alcance": "38K", "Stories": "14K", "Engajamento": "3,7%"},
    {"Mês": "Fev", "Seguidores": "124K", "Alcance": "41K", "Stories": "15K", "Engajamento": "3,9%"},
    {"Mês": "Mar", "Seguidores": "128K", "Alcance": "44K", "Stories": "16K", "Engajamento": "4,0%"},
    {"Mês": "Abr", "Seguidores": "132K", "Alcance": "48K", "Stories": "18K", "Engajamento": "4,2%"},
])

DEFAULT_PLANNING = pd.DataFrame([
    {"Creator": "Jady Carvalho", "Objetivo": "Crescimento + Monetização", "Pilar": "Lifestyle / Humor", "Ideia": "Rotina real dirigindo e conversando", "Status": "Em planejamento", "Prioridade": "Alta"},
    {"Creator": "Malu Borges", "Objetivo": "Posicionamento Fashion", "Pilar": "Moda", "Ideia": "Looks de trabalho + rotina urbana", "Status": "Pendente", "Prioridade": "Média"},
    {"Creator": "Vitória Guedes", "Objetivo": "Autoridade em skincare", "Pilar": "Beleza", "Ideia": "Review sincero de produtos favoritos", "Status": "Aprovado", "Prioridade": "Alta"},
])

if "creators" not in st.session_state:
    st.session_state.creators = deepcopy(DEFAULT_CREATORS)
if "opportunities" not in st.session_state:
    st.session_state.opportunities = deepcopy(DEFAULT_OPPORTUNITIES)
if "metrics_history" not in st.session_state:
    st.session_state.metrics_history = DEFAULT_METRICS_HISTORY.copy()
if "planning" not in st.session_state:
    st.session_state.planning = DEFAULT_PLANNING.copy()
if "selected_creator" not in st.session_state:
    st.session_state.selected_creator = next(iter(st.session_state.creators))
if "show_new_creator" not in st.session_state:
    st.session_state.show_new_creator = False
if "editing_creator" not in st.session_state:
    st.session_state.editing_creator = None
if "deleting_creator" not in st.session_state:
    st.session_state.deleting_creator = None

def initials_from_name(name):
    parts = [p for p in name.strip().split() if p]
    if not parts:
        return "CR"
    if len(parts) == 1:
        return parts[0][:2].upper()
    return (parts[0][0] + parts[-1][0]).upper()

def get_creator_names():
    return list(st.session_state.creators.keys())

def render_status(status):
    if status == "Ativo":
        st.success("Ativo")
    elif status == "Pausado":
        st.warning("Pausado")
    else:
        st.info(status)

st.sidebar.markdown('<div class="zoy-title">zoy</div>', unsafe_allow_html=True)
st.sidebar.markdown('<div class="zoy-subtitle">ASSESSORIA</div>', unsafe_allow_html=True)
menu = st.sidebar.radio(
    "Menu",
    ["Dashboard", "Influenciadores", "Planejamento", "Oportunidades", "Documentos"],
    label_visibility="collapsed"
)
st.sidebar.markdown("---")
st.sidebar.markdown("**Jean**")
st.sidebar.caption("Responsável")

if menu == "Dashboard":
    st.markdown('<div class="page-title">Olá, Jean.</div>', unsafe_allow_html=True)
    st.markdown('<div class="page-subtitle">Aqui está o panorama da assessoria hoje.</div>', unsafe_allow_html=True)

    open_opps = len([o for o in st.session_state.opportunities if o["Status"] not in ["Pago", "Perdido"]])
    closed_opps = len([o for o in st.session_state.opportunities if o["Status"] == "Fechado"])

    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Creators ativos", len(st.session_state.creators))
    c2.metric("Oportunidades abertas", open_opps)
    c3.metric("Fechamentos do mês", closed_opps)
    c4.metric("Reuniões da semana", 6)

    ca, cb = st.columns([1.5, 1], gap="large")
    with ca:
        st.markdown("### Oportunidades recentes")
        st.dataframe(pd.DataFrame(st.session_state.opportunities), use_container_width=True, hide_index=True)
    with cb:
        st.markdown("### Alertas")
        st.info("Jady Carvalho: reunião mensal pendente.")
        st.info("Malu Borges: atualizar métricas do mês.")
        st.info("Vitória Guedes: revisar marcas alvo.")

elif menu == "Influenciadores":
    header_left, header_right = st.columns([5, 1.4])
    with header_left:
        st.markdown('<div class="page-title">Influenciadores</div>', unsafe_allow_html=True)
        st.markdown('<div class="page-subtitle">Cadastro, métricas, posicionamento e histórico dos creators.</div>', unsafe_allow_html=True)
    with header_right:
        if st.button("+ Novo influenciador", use_container_width=True):
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
                    elif nome in st.session_state.creators:
                        st.error("Já existe um influenciador com esse nome.")
                    else:
                        st.session_state.creators[nome] = {
                            "nome": nome,
                            "nome_artistico": nome_artistico or nome,
                            "initials": initials_from_name(nome),
                            "handle": handle,
                            "nicho": nicho,
                            "cidade": cidade,
                            "status": status,
                            "email": email,
                            "telefone": telefone,
                            "aniversario": aniversario,
                            "cpf_cnpj": cpf_cnpj,
                            "endereco": endereco,
                            "pix": pix,
                            "banco": banco,
                            "agencia": agencia,
                            "conta": conta,
                            "responsavel": "Jean",
                            "bio": bio,
                            "posicionamento": posicionamento,
                            "tom_voz": tom_voz,
                            "marcas_sonho": "",
                            "marcas_no_fit": "",
                            "obs": obs,
                            "seguidores": "0",
                            "alcance": "0",
                            "impressoes": "0",
                            "stories": "0",
                            "engajamento": "0%",
                            "crescimento": "0%",
                            "tags": [nicho] if nicho else [],
                        }
                        st.session_state.selected_creator = nome
                        st.session_state.show_new_creator = False
                        st.rerun()

    left, right = st.columns([1.05, 3.4], gap="large")
    names = get_creator_names()

    if not names:
        st.warning("Nenhum influenciador cadastrado.")
        st.stop()

    if st.session_state.selected_creator not in names:
        st.session_state.selected_creator = names[0]

    with left:
        st.markdown("### Influenciadores")
        query = st.text_input("Buscar influenciador", placeholder="Buscar influenciador...", label_visibility="collapsed").lower()
        shown = [n for n in names if query in n.lower() or query in st.session_state.creators[n].get("handle", "").lower()]

        for name in shown:
            data = st.session_state.creators[name]
            is_selected = name == st.session_state.selected_creator
            label = f"{data.get('initials', 'CR')}  |  {name}  |  {data.get('handle', '')}"
            if is_selected:
                st.markdown(f"**Selecionado:** {name}")
            if st.button(label, key=f"select_{name}", use_container_width=True):
                st.session_state.selected_creator = name
                st.rerun()
            st.caption(data.get("status", "Ativo"))

        st.caption(f"{len(st.session_state.creators)} influenciadores cadastrados")

    selected = st.session_state.selected_creator
    creator = st.session_state.creators[selected]

    with right:
        pc1, pc2 = st.columns([4, 1.3])
        with pc1:
            st.markdown(
                f'<div class="profile-box"><div style="display:flex;align-items:center;gap:22px;"><div class="avatar">{creator.get("initials","CR")}</div><div><div style="font-size:30px;font-weight:900;color:#17002E;">{selected}</div><div style="color:#6F2DE2;font-weight:800;">{creator.get("handle","")}</div><div class="muted">{creator.get("nicho","")}</div><div class="muted" style="margin-top:8px;">📍 {creator.get("cidade","")}</div></div></div></div>',
                unsafe_allow_html=True
            )
        with pc2:
            st.markdown("**Responsável**")
            st.write(creator.get("responsavel", "Jean"))
            st.markdown("**Status**")
            render_status(creator.get("status", "Ativo"))

        a1, a2, a3 = st.columns([1, 1, 4])
        with a1:
            if st.button("Editar dados", use_container_width=True):
                st.session_state.editing_creator = selected
        with a2:
            if st.button("Excluir", use_container_width=True):
                st.session_state.deleting_creator = selected

        if st.session_state.deleting_creator == selected:
            st.error(f"Tem certeza que deseja excluir {selected}?")
            d1, d2, d3 = st.columns([1, 1, 4])
            with d1:
                if st.button("Sim, excluir", use_container_width=True):
                    del st.session_state.creators[selected]
                    st.session_state.deleting_creator = None
                    if st.session_state.creators:
                        st.session_state.selected_creator = next(iter(st.session_state.creators))
                    st.rerun()
            with d2:
                if st.button("Cancelar", use_container_width=True):
                    st.session_state.deleting_creator = None
                    st.rerun()

        if st.session_state.editing_creator == selected:
            with st.expander("Editar dados do influenciador", expanded=True):
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
                        updated = {
                            **creator,
                            "nome": enome,
                            "nome_artistico": enomeart,
                            "initials": initials_from_name(enome),
                            "handle": ehandle,
                            "email": eemail,
                            "telefone": etel,
                            "cidade": ecid,
                            "nicho": enicho,
                            "aniversario": eani,
                            "cpf_cnpj": ecpf,
                            "status": estatus,
                            "pix": epix,
                            "banco": ebanco,
                            "agencia": eag,
                            "conta": econta,
                            "endereco": eend,
                            "bio": ebio,
                            "posicionamento": epos,
                            "tom_voz": etom,
                            "marcas_sonho": ems,
                            "marcas_no_fit": enf,
                            "obs": eobs,
                            "responsavel": "Jean",
                        }
                        if enome != selected:
                            del st.session_state.creators[selected]
                            st.session_state.creators[enome] = updated
                            st.session_state.selected_creator = enome
                        else:
                            st.session_state.creators[selected] = updated
                        st.session_state.editing_creator = None
                        st.rerun()
                    if cancel:
                        st.session_state.editing_creator = None
                        st.rerun()

        tabs = st.tabs(["Dados gerais", "Posicionamento", "Métricas", "Histórico", "Arquivos"])
        with tabs[0]:
            ca, cb, cc = st.columns(3)
            with ca:
                st.markdown("### Contato")
                st.write(f"**Nome completo:** {creator.get('nome','')}")
                st.write(f"**Nome artístico:** {creator.get('nome_artistico','')}")
                st.write(f"**Instagram:** {creator.get('handle','')}")
                st.write(f"**E-mail:** {creator.get('email','')}")
                st.write(f"**Telefone:** {creator.get('telefone','')}")
            with cb:
                st.markdown("### Dados pessoais")
                st.write(f"**Cidade:** {creator.get('cidade','')}")
                st.write(f"**Endereço:** {creator.get('endereco','')}")
                st.write(f"**Aniversário:** {creator.get('aniversario','')}")
                st.write(f"**CPF/CNPJ:** {creator.get('cpf_cnpj','')}")
                st.write(f"**Responsável:** {creator.get('responsavel','Jean')}")
            with cc:
                st.markdown("### Dados bancários")
                st.write(f"**Pix:** {creator.get('pix','')}")
                st.write(f"**Banco:** {creator.get('banco','')}")
                st.write(f"**Agência:** {creator.get('agencia','')}")
                st.write(f"**Conta:** {creator.get('conta','')}")
        with tabs[1]:
            st.markdown("### Posicionamento")
            st.write(f"**Nicho:** {creator.get('nicho','')}")
            st.write(f"**Bio estratégica:** {creator.get('bio','')}")
            st.write(f"**Posicionamento:** {creator.get('posicionamento','')}")
            st.write(f"**Tom de voz:** {creator.get('tom_voz','')}")
            st.write(f"**Marcas dos sonhos:** {creator.get('marcas_sonho','')}")
            st.write(f"**Marcas no-fit:** {creator.get('marcas_no_fit','')}")
            st.write(f"**Observações internas:** {creator.get('obs','')}")
            st.markdown("".join([f'<span class="pill">{t}</span>' for t in creator.get("tags", [])]), unsafe_allow_html=True)
        with tabs[2]:
            st.markdown("### Métricas principais")
            m1, m2, m3, m4, m5, m6 = st.columns(6)
            m1.metric("Seguidores", creator.get("seguidores", "0"), creator.get("crescimento", "0%"))
            m2.metric("Alcance", creator.get("alcance", "0"))
            m3.metric("Impressões", creator.get("impressoes", "0"))
            m4.metric("Stories", creator.get("stories", "0"))
            m5.metric("Engajamento", creator.get("engajamento", "0%"))
            m6.metric("Crescimento", creator.get("crescimento", "0%"))
            st.markdown("### Histórico mensal")
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
    col1, col2 = st.columns([1, 2])
    with col1:
        st.selectbox("Influenciador", get_creator_names())
        st.selectbox("Objetivo do mês", ["Crescimento", "Monetização", "Posicionamento", "Autoridade", "Relacionamento com marcas", "Awareness"])
        st.multiselect("Pilares editoriais", ["Lifestyle", "Beleza", "Skincare", "Humor", "Moda", "Viagem", "Fitness", "Gastronomia"], default=["Lifestyle"])
        st.checkbox("Reunião realizada")
        st.checkbox("Planejamento aprovado")
        st.checkbox("Creator alinhado")
        st.checkbox("Execução iniciada")
    with col2:
        st.markdown("### Plano do mês")
        st.text_area("Estratégia do mês", "Descrever a estratégia geral do creator para o mês.")
        st.text_area("Conteúdos orgânicos sugeridos", "Ideia 1\nIdeia 2\nIdeia 3")
        st.text_area("Collabs sugeridas", "Creator X — objetivo\nCreator Y — objetivo")
        st.text_area("Marcas alvo", "Marca 1 — motivo fit\nMarca 2 — abordagem")
        st.text_area("Datas importantes", "Eventos, sazonalidades e datas relevantes.")
    st.markdown("### Planejamentos em andamento")
    st.dataframe(st.session_state.planning, use_container_width=True, hide_index=True)

elif menu == "Oportunidades":
    st.markdown('<div class="page-title">Oportunidades</div>', unsafe_allow_html=True)
    st.markdown('<div class="page-subtitle">Pipeline comercial da assessoria por creator.</div>', unsafe_allow_html=True)
    with st.expander("+ Nova oportunidade"):
        with st.form("new_opportunity"):
            c1, c2, c3 = st.columns(3)
            with c1:
                op_creator = st.selectbox("Creator", get_creator_names())
                op_marca = st.text_input("Marca")
                op_status = st.selectbox("Status", ["Lead recebido", "Abordagem", "Negociação", "Contrato", "Fechado", "Perdido", "Pago"])
            with c2:
                op_valor = st.text_input("Valor")
                op_fee = st.text_input("Fee Zoy")
                op_data = st.text_input("Data")
            with c3:
                op_obs = st.text_area("Observações")
            if st.form_submit_button("Salvar oportunidade"):
                st.session_state.opportunities.append({
                    "Creator": op_creator,
                    "Marca": op_marca,
                    "Valor": op_valor,
                    "Fee Zoy": op_fee,
                    "Status": op_status,
                    "Data": op_data,
                    "Observações": op_obs,
                })
                st.rerun()
    statuses = ["Lead recebido", "Abordagem", "Negociação", "Contrato", "Fechado", "Pago"]
    cols = st.columns(len(statuses))
    for col, status in zip(cols, statuses):
        with col:
            st.markdown(f"### {status}")
            filtered = [o for o in st.session_state.opportunities if o["Status"] == status]
            if not filtered:
                st.caption("Sem oportunidades")
            for opp in filtered:
                st.markdown(f"**{opp['Marca']}**")
                st.caption(opp["Creator"])
                st.write(opp["Valor"])
                st.caption(f"Fee Zoy: {opp['Fee Zoy']}")
                st.markdown("---")
    st.markdown("### Base completa")
    st.dataframe(pd.DataFrame(st.session_state.opportunities), use_container_width=True, hide_index=True)

elif menu == "Documentos":
    st.markdown('<div class="page-title">Documentos</div>', unsafe_allow_html=True)
    st.markdown('<div class="page-subtitle">Central de arquivos dos influenciadores.</div>', unsafe_allow_html=True)
    st.selectbox("Influenciador", get_creator_names())
    st.markdown("### Uploads")
    st.file_uploader("Mídia kit", type=["pdf", "pptx", "docx"])
    st.file_uploader("Contrato", type=["pdf", "docx"])
    st.file_uploader("Documentos pessoais", type=["pdf", "jpg", "png"])
    st.file_uploader("Comprovante bancário", type=["pdf", "jpg", "png"])
    st.file_uploader("Notas fiscais", type=["pdf", "xml"])
    st.info("Na próxima etapa conectamos esses arquivos ao Google Drive ou banco de dados.")
