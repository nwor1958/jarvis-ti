#importar streamlit e genai e antrhopic
#Configurações iniciais e chaves (no topo) --> configurar no secrets
#Iniciar clientes
#Definição do Prompt do Sistema
#Escolha modelo - lateral
#Criação lista de mensagens na sessão
#Título do chatbot
#Exibição do histórico de conversas na tela
#chamada a LLM
#chamada a API do Gemini ou Claude
#Exibição resposta da IA
#Salvar API na pasta secrets 
#Requirements.txt

import os
import io
import base64
import streamlit as st
from dotenv import load_dotenv
from google import genai
from google.genai import types
from anthropic import Anthropic
from PIL import Image
load_dotenv()

st.set_page_config(page_title="Assistente TI - Portfólio", page_icon="💻", layout="wide")

try:
    GEMINI_KEY = st.secrets["GEMINI_API_KEY"]
    ANTHROPIC_KEY = st.secrets["ANTHROPIC_API_KEY"]
except Exception:
    GEMINI_KEY = os.getenv("GEMINI_API_KEY", "")
    ANTHROPIC_KEY = os.getenv("ANTHROPIC_API_KEY", "")

cliente_gemini = genai.Client(api_key=GEMINI_KEY) if GEMINI_KEY else None  
cliente_claude = Anthropic(api_key=ANTHROPIC_KEY) if ANTHROPIC_KEY else None


PROMPT_SISTEMA = """
You are Jarvis-TI, an elite software architecture, systems engineering, and bioinformatics AI assistant designed for technical portfolio demonstration and high-level problem solving.

**CORE EXPERTISE:
1. Software Architecture & Design Patterns (Microservices, Clean Architecture, Distributed Systems, Event-Driven).
2. Advanced AI & LLM Systems (RAG, Vector Embeddings, MCP - Model Context Protocol, token optimization).
3. Databases & Data Engineering (Relational, NoSQL, Vector DBs, and specialized Bioinformatics databases like GenBank, FASTA/FASTQ storage structures, and genomic data pipelines).
4. Protocols & Networking (HTTP/2, gRPC, WebSockets, SSE, IPFS, and peer-to-peer data overlays).

**OPERATIONAL GUIDELINES:
- Provide rigorous, production-grade technical answers with clean code snippets (Python, TypeScript, Java).
- When discussing architecture, prioritize scalability, maintainability, and security.
- Reference appropriate network protocols or data structures when handling heavy files or real-time streams.
- If a query involves bioinformatics or complex data processing, suggest optimized memory structures or indexing strategies.
- Maintain a professional, objective, and deeply technical tone. Avoid superficial placeholders; write functional patterns.
"""
def imagem_para_base64(imagem_pil):
    buffer = io.BytesIO()
    imagem_pil.save(buffer, format="PNG")
    return base64.b64encode(buffer.getvalue()).decode("utf-8")

with st.sidebar:
    st.header("⚙️ Configurações do Agente")
    modelo_escolhido = st.selectbox(
        "Escolha o Provedor de LLM:",
        ["Google Gemini (gemini-flash-latest)", "Anthropic Claude (3.5 Sonnet)"]
    )
    st.markdown("---")
    st.markdown("**Projeto de Portfólio:** Assistente de TI & Arquitetura de Software")
    st.markdown("Focado em microsserviços, bioinformática e padrões de engenharia.")
    if "Claude" in modelo_escolhido and not ANTHROPIC_KEY:
        st.warning("⚠️ Chave da API do Claude não encontrada. Por favor, configure o arquivo .env para testá-lo.")

if "mensagem_lista" not in st.session_state:
    st.session_state["mensagem_lista"] = []

st.title("💻 Assistente de TI & Arquitetura de Software")

for mensagem in st.session_state["mensagem_lista"]:
    with st.chat_message(mensagem["role"]):
        if mensagem.get("image"):
            st.image(mensagem["image"], width=350)
        st.write(mensagem["content"])

entrada_usuario = st.chat_input(
    "Digite sua mensagem ténica ou anexe uma imagem...",
    accept_file=True,
    file_type=["png", "jpg", "jpeg", "webp"]
)

if entrada_usuario:
    texto_usuario = entrada_usuario.text or "Analise esta imagem técnica"
    arquivos = entrada_usuario.files
    imagem_pil = Image.open(arquivos[0]) if arquivos else None
    with st.chat_message("user"):
        if imagem_pil: 
            st.image(imagem_pil, width=350)
        st.write(texto_usuario)
    st.session_state["mensagem_lista"].append({"role": "user", "content": texto_usuario, "image": imagem_pil})
    
    resposta_assistente = ""

    try:
        if "Gemini" in modelo_escolhido:
            if not GEMINI_KEY:
                resposta_assistente = "Erro: A chave de API do Gemini não foi configurada."
            else: 
                historico_texto = "\n".join(
                    [f"{m['role']}: {m['content']}" for m in st.session_state["mensagem_lista"][:-1]]
                )
                prompt_atual = f"Histórico anterior:\n{historico_texto}\n\nPergunta atual: {texto_usuario}" if historico_texto else texto_usuario
                conteudos = [imagem_pil, prompt_atual] if imagem_pil else [prompt_atual]
                resposta_modelo = cliente_gemini.models.generate_content(
                    model = "gemini-3.5-flash",
                    contents=conteudos,
                    config=types.GenerateContentConfig(
                        system_instruction=PROMPT_SISTEMA
                    )
                )
                resposta_assistente = resposta_modelo.text

        elif "Claude" in modelo_escolhido:
            if not ANTHROPIC_KEY:
                resposta_assistente = (
                    "💡 **Modo Demonstrativo de Arquitetura:** "
                    "O código está estruturado para integrar o **Anthropic Claude**, "
                    "mas a chave de API não foi inserida no momento (sem créditos ativos). "
                    "Assim que você adicionar créditos na Anthropic, basta preencher a variável "
                    "no `.env` e ele funcionará instantaneamente!"
                )
            else:
                mensagem_claude = [
                    {"role": m["role"], "content": m["content"]}
                    for m in st.session_state["mensagem_lista"][:-1]
                ]
                if imagem_pil: 
                    conteudo_atual = [
                        {
                            "type": "image",
                            "source": {
                                "type": "base64",
                                "media_type": "image/png", 
                                "data": imagem_para_base64(imagem_pil)
                            }
                        },
                        {"type": "text", "text": texto_usuario}
                    ]
                else: 
                    conteudo_atual = texto_usuario
                mensagem_claude.append({"role": "user", "content": conteudo_atual})
                resposta_modelo = cliente_claude.messages.create(
                    model="claude-3-5-sonnet-20241022",
                    max_tokens=1500,
                    system=PROMPT_SISTEMA,
                    messages=mensagem_claude
                )
                resposta_assistente = resposta_modelo.content[0].text

    except Exception as e:
        resposta_assistente = f"Ocorreu um erro de conexão com a API escolhida: {str(e)}"

    st.chat_message("assistant").write(resposta_assistente)
    st.session_state["mensagem_lista"].append({"role": "assistant", "content": resposta_assistente})