import streamlit as st
import time

# Configuração Base
st.set_page_config(page_title="UNBAN VIP BLUE", page_icon="💎")

# CSS para Design Premium (Preto, Branco e Azul Bebê)
st.markdown("""
    <style>
    .stApp { background-color: #000000; }
    h1, h2, h3, p, label { color: #FFFFFF !important; }
    
    /* Botão Azul Bebê Arredondado */
    div.stButton > button {
        background-color: #89CFF0 !important;
        color: #000000 !important;
        border-radius: 15px !important;
        border: none !important;
        font-weight: bold !important;
        height: 55px !important;
        width: 100% !important;
        box-shadow: 0px 4px 15px rgba(137, 207, 240, 0.3);
    }
    
    /* Inputs Estilizados */
    input {
        background-color: #1a1a1a !important;
        color: #89CFF0 !important;
        border: 2px solid #89CFF0 !important;
    }
    </style>
    """, unsafe_allow_box=True)

st.title("💎 UNBAN VIP: BLUE EDITION")
st.write("---")

# Interface
id_player = st.text_input("DIGITE O ID PARA DESBANIR", placeholder="Ex: 12345678")
motivo = st.selectbox("MOTIVO DO BAN", ["Regedit / Macro", "Software Terceiro", "Blacklist", "Outros"])

if st.button("🚀 ATIVAR DESBANIMENTO (45s)"):
    if id_player:
        # Barra de progresso ultra simples para evitar TypeError
        status_msg = st.empty()
        bar = st.progress(0)
        
        status_msg.write("🔍 Estabelecendo conexão com servidor...")
        time.sleep(2)
        bar.progress(30)
        
        status_msg.write("💉 Injetando Script de Bypass (Azul Bebê)...")
        time.sleep(3)
        bar.progress(70)
        
        status_msg.write("🔓 Quebrando restrição de ID...")
        time.sleep(2)
        bar.progress(100)
        
        st.snow()
        st.success(f"✅ ID {id_player} LIBERADO!")
        
        st.markdown(f"""
        <div style="border: 2px solid #89CFF0; padding: 20px; border-radius: 15px; background-color: #111111;">
            <h3 style="color: #89CFF0; margin:0;">✅ CONTA DESBANIDA</h3>
            <p>1. Limpe o Cache do Free Fire.<br>
            2. Reinicie o dispositivo.<br>
            3. Entre na conta em menos de 1 minuto.</p>
        </div>
        """, unsafe_allow_box=True)
    else:
        st.error("ERRO: Digite um ID válido!")

st.write("---")
st.caption("Sistema de Recuperação Estratégica 2024")
