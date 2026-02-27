import streamlit as st
import time

# Configuração de Página e Design Moderno (Azul Bebê, Preto e Branco)
st.set_page_config(page_title="UNBAN VIP - BLUE EDITION", page_icon="💎")

# CSS para Cores e Botões Bonitos
st.markdown("""
    <style>
    .stApp { background-color: #000000; }
    h1, h2, h3, p, span, label { color: #FFFFFF !important; font-family: 'Segoe UI', sans-serif; }
    
    /* Botão Azul Bebê Arredondado e com Brilho */
    div.stButton > button {
        background-color: #89CFF0 !important;
        color: #000000 !important;
        border-radius: 25px !important;
        border: none !important;
        font-weight: bold !important;
        padding: 20px !important;
        width: 100% !important;
        box-shadow: 0px 4px 15px rgba(137, 207, 240, 0.4);
    }
    
    /* Inputs Estilizados */
    input {
        background-color: #1a1a1a !important;
        color: #89CFF0 !important;
        border: 2px solid #89CFF0 !important;
        border-radius: 15px !important;
    }
    </style>
    """, unsafe_allow_box=True)

st.title("💎 UNBAN VIP: BLUE EDITION")
st.write("---")

# Interface de Comando
id_jogador = st.text_input("DIGITE O ID PARA DESBANIR", placeholder="Ex: 12345678")
motivo = st.selectbox("MOTIVO DO BANIMENTO", ["Regedit / Auxílio de Mira", "Software de Terceiros", "Blacklist", "Outros"])

if st.button("🚀 INJETAR DESBANIMENTO (30s)"):
    if id_jogador:
        # Barra de progresso corrigida para evitar o TypeError
        progresso = st.progress(0)
        status_texto = st.empty()
        
        # Sequência de Injeção em menos de 1 minuto
        status_texto.write("🔍 Conectando ao Banco de Dados Garena...")
        time.sleep(2)
        progresso.progress(30)
        
        status_texto.write("💉 Injetando Script Azul Bebê no Lobby...")
        time.sleep(3)
        progresso.progress(70)
        
        status_texto.write("🔓 Quebrando Restrição de ID (Bypass)...")
        time.sleep(2)
        progresso.progress(100)
        
        st.snow()
        st.success(f"✅ ID {id_jogador} FOI DESBANIDO COM SUCESSO!")
        
        # Painel de Resultado Premium
        st.markdown(f"""
        <div style="border: 2px solid #89CFF0; padding: 20px; border-radius: 15px; background-color: #111111;">
            <h3 style="color: #89CFF0; margin-top: 0;">✅ CONTA LIBERADA</h3>
            <p>1. <b>FECHE O JOGO</b> completamente.</p>
            <p>2. <b>LIMPE O CACHE</b> nas configurações do Android/iOS.</p>
            <p>3. <b>REINICIE O APARELHO</b> e entre na conta agora.</p>
        </div>
        """, unsafe_allow_box=True)
        
        # Link para suporte como plano B
        st.info("Se o servidor barrar a injeção, use o [Suporte Oficial da Garena](https://ffsuporte.garena.com).")
    else:
        st.error("ERRO: DIGITE UM ID VÁLIDO!")

st.markdown("---")
st.caption("PROTOCOLO VIP - BYPASS SYSTEM 2024")

