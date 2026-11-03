# 💻 Jarvis-TI: AI Assistant for Software Architecture & Bioinformatics

Um assistente de inteligência artificial de alta performance desenvolvido em Python e Streamlit, focado em apoiar estudantes e profissionais de tecnologia em tarefas de engenharia de software, arquitetura de sistemas, design de banco de dados e bioinformática.

## 🚀 Tecnologias Utilizadas
- **Linguagem:** Python 3.10+
- **Interface:** Streamlit (UI interativa baseada em chat)
- **Provedores de LLM:** Google GenAI SDK (`gemini-flash-latest`) & Anthropic Claude API (`claude-3-5-sonnet`)
- **Segurança:** `python-dotenv` para gerenciamento seguro de variáveis de ambiente (`.env`)

## ⚙️ Arquitetura e Diferenciais
- **Padrão Multi-LLM:** O backend possui uma camada de abstração que permite alternar em tempo real entre diferentes provedores de inteligência artificial na barra lateral.
- **System Prompt Especializado:** Configurado com diretrizes rígidas de engenharia, priorizando código limpo, padrões de projeto (Design Patterns) e otimização de estruturas de dados.
- **Tratamento de Exceções Resiliente:** Gerenciamento elegante de estados e chaves de API ausentes para demonstração em portfólio.
