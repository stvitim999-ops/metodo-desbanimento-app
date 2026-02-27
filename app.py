import streamlit as st
import time

# Configurações de Design
st.set_page_config(page_title="UNBAN VIP - BLUE", page_icon="💎")

st.markdown("""
    <style>
    .stApp { background-color: #000000; }
    h1, h2, h3, p, span { color: #FFFFFF !important; }
    
    /* Botão Azul Bebê Bonito */
    div.stButton > button {
        background-color: #89CFF0 !important;
        color: #000000 !important;
        border-radius: 20px !important;
        border: none !important;
        font-weight: bold !important;
        height: 50px !important;
        width: 100% !important;
    }
    
    /* Inputs Pretos com borda Azul */
    input {
        background-color: #1a1a1a !important;
        color: #89CFF0 !important;
        border: 1px solid #89CFF0 !important;
    }
    </style>
    """, unsafe_allow_box=True)

st.title("💎 UNBAN VIP: GARENA")
st.write("---")

# Campos
id_player = st.text_input("DIGITE O ID DA CONTA", placeholder="Ex: 12345678")
motivo = st.selectbox("MOTIVO DO BAN", ["Regedit", "Software Terceiro", "Blacklist", "Outros"])

if st.button("🚀 DESBANIR EM 60 SEGUNDOS"):
    if id_player:
        bar = st.progress(0)
        status = st.empty()
        
        for i in range(1, 101):
            time.sleep(0.3) # Total de 30 segundos de injeção
            bar.progress(i)
            if i == 20: status.write("🔍 Conectando ao Banco de Dados...")
            if i == 50: status.write("💉 Injetando Script Azul Bebê...")
            if i == 80: status.write("🔓 Quebrando Filtros Garena...")
        
        st.snow()
        st.success(f"✅ ID {id_player} DESBANIDO COM SUCESSO!")
        
        st.markdown(f"""
        <div style="border: 2px solid #89CFF0; padding: 15px; border-radius: 10px;">
        <h3 style="color: #89CFF0;">PRÓXIMOS PASSOS:</h3>
        1. Limpe o Cache do Free Fire.<br>
        2. Reinicie o Celular.<br>
        3. Entre na conta em menos de 1 minuto.
        </div>
        """, unsafe_allow_box=True)
    else:
        st.error("Digite um ID!")
