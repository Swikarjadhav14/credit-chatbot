STEPS : 

In terminal , 

1. python -m venv .venv
2. .venv\Scripts\activate
3. pip install -r requirements.txt
4. set HF_TOKEN="__________"
5. uvicorn app:app --reload


flowchart TD
    %% Interfaces
    subgraph Interfaces
        WebUI[Web UI (index.html)\nText + Voice]
        OtherChannels[Other Channels\nMobile / WhatsApp / IVR]
    end

    %% Backend
    subgraph Backend[FastAPI Backend\nGenAI Credit Card Assistant]
        ChatAPI[/POST /api/chat\nConversation Orchestrator/]
        Retriever[FAQ Retriever\nEmbeddings + faqs.yaml]
        LLM[LLM Planner & Answer Generator]
        Tools[Tools Layer\n(get_summary, block_card,\npay_bill, list_transactions)]
    end

    %% Data & Services
    subgraph DataAndServices[Data & External Services]
        FAQ[(Knowledge Base\nfaqs.yaml)]
        UserState[(User State\nMock card data in memory)]
        HF[Hugging Face Inference API\nEmbeddings + LLM]
    end

    %% Flows
    WebUI -->|JSON: user_id, channel, messages[]| ChatAPI
    OtherChannels -->|JSON: user_id, channel, messages[]| ChatAPI

    ChatAPI -->|query embedding + similarity| Retriever
    Retriever -->|top FAQ + score| ChatAPI

    ChatAPI -->|plan: answer vs action\n+ use KB snippet| LLM
    LLM -->|plan JSON| ChatAPI

    ChatAPI -->|action + parameters| Tools
    Tools -->|tool result| ChatAPI

    ChatAPI -->|reply JSON\n(reply, tool_calls, source)| WebUI
    ChatAPI -->|reply JSON\n(reply, tool_calls, source)| OtherChannels

    Retriever -->|embed FAQs + queries| HF
    LLM -->|chat / completions| HF

    Retriever --> FAQ
    Tools --> UserState
