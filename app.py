import streamlit as st

# Configuração visual da página
st.set_page_config(page_title="Método de Desbanimento", page_icon="🛡️")

# Cabeçalho Estratégico
st.title("🛡️ Sistema de Recuperação Estratégica")
st.markdown("---")

st.info("""
**Protocolo de Recuperação:** Este sistema automatiza a estruturação de recursos técnicos, 
substituindo termos emocionais por argumentos de conformidade para priorizar a análise humana.
""")

# interface de Diagnóstico
col1, col2 = st.columns(2)
with col1:
    plataforma = st.selectbox("Plataforma Alvo", ["Instagram", "Garena / Free Fire", "Google", "WhatsApp", "Facebook"])
    motivo_ban = st.selectbox("Natureza da Penalidade", ["Software de Terceiros", "Atividade Incomum", "Diretrizes", "Spam"])

with col2:
    tempo_ban = st.selectbox("Tempo da Suspensão", ["Recente", "Intermediário", "Antigo"])
    investimento = st.radio("Houve investimento financeiro?", ["Sim", "Não"])

# Campo de Entrada do Usuário
st.subheader("📝 Relato do Ocorrido")
texto_original = st.text_area("Descreva o que aconteceu (o sistema fará o ajuste técnico):", 
                              placeholder="Ex: Tomei ban por usar regedit, achei injusto, por favor me ajuda.")

# Botão de Processamento
if st.button("Gerar Recurso Blindado"):
    if texto_original:
        # Lógica de substituição do seu método (Filtro Anti-Bot)
        dicionario_estrategico = {
            "injusto": "falso positivo técnico",
            "injustiça": "inconsistência na detecção",
            "por favor": "solicito revisão manual",
            "me ajuda": "requer análise de conformidade",
            "imploro": "solicito parecer técnico",
            "fiz nada": "não identifico violações diretas nos logs",
            "erro de vocês": "divergência sistêmica",
            "quero minha conta": "restabelecimento do acesso"
        }
        
        texto_ajustado = texto_original.lower()
        for erro, termo_certo in dicionario_estrategico.items():
            texto_ajustado = texto_ajustado.replace(erro, termo_certo)

        # Exibição do Resultado Final
        st.success("✅ Recurso Estratégico Gerado!")
        
        template_final = f"""
**Assunto: Solicitação de Revisão Técnica - [INSERIR SEU ID/USER]**

Prezada Equipe de Suporte da {plataforma},

Venho por meio desta solicitar a reavaliação da suspensão aplicada à minha conta. 
Com base no Protocolo de Conformidade, identifiquei uma possível {texto_ajustado}. 

Considerando o histórico de {'investimento e ' if investimento == "Sim" else ''}fidelidade à plataforma, 
solicito que este ticket seja encaminhado para uma análise humana dedicada.

Atenciosamente,
[Seu Nome Completo]
        """
        
        st.code(template_final, language="text")
        st.warning("⚠️ **Dica do Método:** Não envie mensagens repetitivas. Use os canais oficiais como o [Suporte da Garena](https://ffsuporte.garena.com) ou o [Centro de Ajuda do Instagram](https://help.instagram.com).")
    else:
        st.error("Por favor, preencha o relato antes de gerar.")

st.markdown("---")
st.caption("Método de Desbanimento - Foco em Análise Técnica vs. Script Automatizado.")
