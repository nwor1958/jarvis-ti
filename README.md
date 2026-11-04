# 💻 Jarvis-TI: AI Assistant for Software Architecture & Bioinformatics

[PT] Assistente de inteligência artificial de alta performance desenvolvido em Python e Streamlit, focado em apoiar estudantes e profissionais de tecnologia em engenharia de software, arquitetura de sistemas e bioinformática.
[EN] High-performance AI assistant built with Python and Streamlit, designed to support tech students and professionals in software engineering, systems architecture, and bioinformatics.

---

## 🇧🇷 Português

### 📌 Sobre o Projeto
O **Jarvis-TI** é um assistente conversacional inteligente que combina uma interface fluida em Streamlit com capacidades multi-provedor de Inteligência Artificial (Google Gemini e Anthropic Claude). O projeto foi arquitetado com foco em boas práticas de desenvolvimento, padrões de projeto (*Design Patterns*) e suporte a tarefas complexas de engenharia de sistemas e bioinformática.

### 🚀 Funcionalidades e Diferenciais
- **Padrão Multi-LLM:** Camada de abstração no backend que permite alternar dinamicamente entre diferentes provedores de IA na barra lateral.
- **System Prompt Especializado:** Diretrizes rígidas de engenharia configuradas para priorizar código limpo, robustez e otimização de estruturas de dados.
- **Tratamento de Exceções Resiliente:** Gerenciamento elegante de estados da sessão e verificação de chaves de API ausentes para alta resiliência.
- **Segurança Robusta:** Gestão segura de credenciais utilizando variáveis de ambiente locais (`.env`) e suporte nativo ao Streamlit Secrets para deploy em nuvem.

### 🛠️ Stack Tecnológica
- **Linguagem:** Python 3.10+
- **Interface:** Streamlit (UI interativa baseada em chat com `st.chat_message` e `st.session_state`)
- **Provedores de LLM:** Google GenAI SDK (`gemini-flash-latest`) & Anthropic Claude API (`claude-3-5-sonnet`)
- **Segurança & Configuração:** `python-dotenv`

---

## 🇺🇸 English

### 📌 About the Project
**Jarvis-TI** is a high-performance conversational AI assistant combining a fluid Streamlit interface with multi-provider AI capabilities (Google Gemini and Anthropic Claude). The project is engineered with a strong emphasis on clean code, design patterns, and support for complex systems engineering and bioinformatics tasks.

### 🚀 Key Features & Differentiators
- **Multi-LLM Architecture:** A backend abstraction layer allowing dynamic switching between different AI providers directly from the sidebar.
- **Specialized System Prompt:** Strict engineering guidelines tuned to prioritize clean code, robustness, and data structure optimization.
- **Resilient Exception Handling:** Elegant state management and graceful fallback for missing API keys to ensure high availability.
- **Enterprise-Grade Security:** Secure credential management leveraging local environment variables (`.env`) and native Streamlit Secrets for cloud deployments.

### 🛠️ Tech Stack
- **Language:** Python 3.10+
- **UI Framework:** Streamlit (Interactive chat UI using `st.chat_message` and `st.session_state`)
- **LLM Providers:** Google GenAI SDK (`gemini-flash-latest`) & Anthropic Claude API (`claude-3-5-sonnet`)
- **Security & Config:** `python-dotenv`

---

## 📁 Como Executar o Projeto / How to Run

1. **Clone o repositório / Clone the repo:**
   ```bash
   git clone [https://github.com/nwor1958/jarvis-ti.git](https://github.com/nwor1958/jarvis-ti.git)
   cd jarvis-ti
