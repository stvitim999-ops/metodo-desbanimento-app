import streamlit as st

st.set_page_config(page_title="FF Recupera - Método Estratégico", page_icon="🎮")

st.title("🛡️ Recuperação de Conta Free Fire")
st.subheader("Método Estratégico Anti-Ban")

st.info("Este sistema gera recursos técnicos para a Garena, focados em revisão manual de ID suspenso por software de terceiros ou regedit.")

# Campos de ID e Diagnóstico
id_jogador = st.text_input("ID do Jogador (Ex: 12345678)", placeholder="Digite seu ID da conta")
motivo_ff = st.selectbox("Qual o motivo do Ban?", ["Uso de Software não oficial (Regedit/Mod)", "Atividade Suspeita", "Reembolso Indevido", "Outros"])
tempo_ban = st.selectbox("Há quanto tempo foi o banimento?", ["Menos de 3 meses", "Mais de 6 meses", "Ban antigo (1 ano+)"])

# Processador de Texto do Método
texto_usuario = st.text_area("Descreva o que aconteceu (o app vai limpar o lado emocional):")

if st.button("Gerar Recurso para Garena"):
    if texto_usuario and id_jogador:
        # Substituições técnicas do seu método
        recurso = texto_usuario.lower().replace("injusto", "falso positivo").replace("por favor", "solicito análise manual").replace("regedit", "arquivo de otimização de terceiros")
        
        st.success("✅ Recurso de Free Fire Gerado!")
        
        template_garena = f"""
        **Assunto: Solicitação de Revisão de Suspensão - ID: {id_jogador}**

        Prezada Equipe de Suporte Garena,

        Venho solicitar a verificação técnica da suspensão aplicada ao ID {id_jogador}. 
        Identifiquei que a detecção pode ter ocorrido por {recurso}.

        Como jogador ativo e ciente das Regras de Conduta, solicito que o caso seja revisado por um analista humano para verificar a possibilidade de remoção da restrição ou conversão em suspensão temporária.

        Atenciosamente,
        [Seu Nome]
        """
        st.code(template_garena)
        st.warning("Envie este texto pelo [Suporte Oficial da Garena](https://ffsuporte.garena.com).")
    else:
        st.error("Preencha seu ID e o relato para continuar.")
