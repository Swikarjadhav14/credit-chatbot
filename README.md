Here is a clean, simple README section that includes:

1. **Short project description**
2. **Basic architecture overview**
3. **Instructions to run**

All in plain Markdown (no emojis).

---

```markdown
# Credit Card Assistant – GenAI Chatbot

This project is an AI-powered credit card assistant built with FastAPI and Hugging Face models.  
It answers credit card related queries, retrieves information from a knowledge base, and triggers actions such as blocking a card or showing account details.

---

## How the System Works (Architecture Overview)

The system follows a three-step workflow:

1. **User Query Handling**
   - User messages are sent to the FastAPI backend.
   - Messages are stored as a short conversation history.

2. **Knowledge Retrieval + AI Reasoning**
   - The system embeds the user query and compares it to stored FAQs.
   - If a relevant FAQ is found, its answer is used.
   - Otherwise, a language model generates a response.
   - For certain inputs, the model decides to call an action/tool.

3. **Action Execution + Final Response**
   - Tools (mock functions) handle actions such as:
     - Blocking a card
     - Fetching account summary
   - The system generates a final text response.
   - Output is returned to the user or UI.

### Components

```

FastAPI Backend
│
├── Router (handles API requests)
├── LLM Client (planning + response generation)
├── Knowledge Base (FAQs stored in YAML)
├── Embeddings Retriever (semantic search)
└── Tools (mock APIs for card actions)

```

### Data Flow

```

User → API → Retriever → LLM → (Tool?) → Response

```

This design ensures accurate FAQ responses, controlled business logic, and the ability to automate tasks.

---

## Instructions to Run

### 1. Clone the repository
```

git clone [https://github.com/Swikarjadhav14/credit-card-bot.git](https://github.com/Swikarjadhav14/credit-card-bot.git)
cd credit-card-bot

```

### 2. Create and activate a virtual environment
```

python -m venv .venv

```

Windows:
```

.venv\Scripts\activate

```

Mac/Linux:
```

source .venv/bin/activate

```

### 3. Install dependencies
```

pip install -r requirements.txt

```

### 4. Create a `.env` file with your Hugging Face token
```

HF_TOKEN=your_token_here

```

### 5. Start the FastAPI server
```

uvicorn app:app --reload

```

Server will run at:
```

[http://127.0.0.1:8000](http://127.0.0.1:8000)

```

### 6. Open the UI
Open the file:
```

index.html

```
in your browser.

You can now chat with the assistant.

---

## Optional: Test API with Postman

POST request to:
```

[http://127.0.0.1:8000/api/chat](http://127.0.0.1:8000/api/chat)

````

Example body:
```json
{
  "user_id": "user_123",
  "channel": "web",
  "messages": [
    { "role": "user", "content": "Block my card" }
  ]
}
````

---

This README is intentionally brief and focuses on helping users understand how the system works and how to run it locally.
