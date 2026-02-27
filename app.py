import streamlit as st
import time

# Configuração da Página e Design Premium
st.set_page_config(page_title="UNBAN VIP - BLUE EDITION", page_icon="💎", layout="centered")

# CSS Personalizado: Cores Azul Bebê, Preto e Branco
st.markdown("""
    <style>
    .main { background-color: #000000; }
    .stApp { background-image: radial-gradient(circle, #1a1a1a 0%, #000000 100%); }
    
    /* Títulos e Textos */
    h1, h2, h3, p { color: #FFFFFF !important; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; }
    
    /* Botão Estilizado Azul Bebê */
    div.stButton > button:first-child {
        background-color: #89CFF0;
        color: #000000;
        border: none;
        border-radius: 12px;
        padding: 15px 30px;
        font-size: 1.2rem;
        font-weight: bold;
        transition: all 0.3s ease;
        box-shadow: 0px 0px 15px rgba(137, 207, 240, 0.4);
    }
    div.stButton > button:first-child:hover {
        background-color: #FFFFFF;
        box-shadow: 0px 0px 25px rgba(137, 207, 240, 0.8);
        transform: scale(1.02);
    }

    /* Inputs e Selects */
    .stTextInput>div>div>input, .stSelectbox>div>div>div {
        background-color: #111111 !important;
        color: #89CFF0 !important;
        border: 1px solid #89CFF0 !important;
        border-radius: 10px;
    }
    
    /* Container de Status */
    .stStatusWidget { background-color: #111111; border: 1px solid #FFFFFF; }
    </style>
    """, unsafe_allow_box=True)

# Interface Principal
st.title("💎 UNBAN VIP: BLUE EDITION")
st.write("---")

# Layout de Colunas
col1, col2 = st.columns(2)
with col1:
    id_alvo = st.text_input("ID DO JOGADOR", placeholder="Ex: 987654321")
with col2:
    servidor = st.selectbox("SERVIDOR", ["Brasil (BR)", "LATAM", "Global"])

st.write("") # Espaçador

# Botão de Ação
if st.button("🚀 INJETAR DESBANIMENTO (60s)"):
    if id_alvo:
        # Sequência de Injeção Ultra Rápida
        with st.status("🛠️ PROCESSANDO BYPASS...", expanded=True) as status:
            st.write("🔍 Conectando ao Banco de Dados Garena...")
            time.sleep(1.5)
            st.write("💉 Injetando Script de Limpeza de Device ID...")
            time.sleep(2)
            st.write("🔓 Quebrando Filtros de Lobby (MM01)...")
            time.sleep(1.5)
            st.write("✅ Finalizando Sincronização de ID...")
            time.sleep(1)
            status.update(label="🚀 PROCESSO CONCLUÍDO!", state="complete", expanded=False)
        
        # Efeito Visual de Sucesso
        st.snow() # Efeito de neve combina com Azul Bebê
        st.success(f"**CONTA {id_alvo} LIBERADA COM SUCESSO!**")
        
        # Painel de Próximos Passos
        st.markdown(f"""
        <div style="background-color: #111111; padding: 20px; border-radius: 15px; border-left: 5px solid #89CFF0;">
            <h3 style="color: #89CFF0; margin-top: 0;">✅ CONTA PRONTA PARA O LOBBY</h3>
            <p>1. <b>LIMPE O CACHE:</b> Vá em Configurações > Apps > Free Fire > Limpar Cache.</p>
            <p>2. <b>REINICIE:</b> Desligue e ligue o celular para resetar o ID do dispositivo.</p>
            <p>3. <b>LOGIN:</b> Abra o jogo. Se o ban persistir, o sistema exige <b>Revisão Técnica</b>.</p>
        </div>
        """, unsafe_allow_box=True)
        
        # Método de Contingência (Plano B)
        with st.expander("⚠️ BAN PERSISTIU? USE O MÉTODO ESTRATÉGICO"):
            st.write("Caso a Garena bloqueie a injeção manual, use este ticket no [Suporte Oficial](https://ffsuporte.garena.com):")
            st.code(f"Solicito revisão manual imediata do ID {id_alvo} por erro de sincronização de logs pós-atualização.")
            
    else:
        st.error("ERRO: DIGITE UM ID VÁLIDO!")

# Rodapé
st.write("---")
st.caption("DESENVOLVIDO POR: MÉTODO DE DESBANIMENTO VIP 2024")
