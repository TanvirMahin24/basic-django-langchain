# LangChain AI Assistant API

A Django REST API that integrates **LangChain** with **Google Gemini** to provide an AI-powered chat assistant. Send a message and receive intelligent responses powered by Gemini 2.5 Flash.

## Features

- **AI Chat Endpoint**: POST messages and get AI-generated responses
- **LangChain + Google Gemini**: Uses LangChain for orchestration and Google's Gemini 2.5 Flash model
- **Simple REST API**: JSON-based request/response format

## Prerequisites

- Python 3.10+
- [Google AI API Key](https://aistudio.google.com/apikey) (free tier available)

## Quick Start

### 1. Clone and Setup

```bash
# Navigate to project
cd Session-Project

# Create and activate virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### 2. Configure Environment

Create a `.env` file in the `langchain_project` directory:

```bash
cd langchain_project
echo "GOOGLE_API_KEY=your_api_key_here" > .env
```

> Get your API key from [Google AI Studio](https://aistudio.google.com/apikey)

### 3. Run the Server

```bash
# From langchain_project directory
python manage.py runserver
```

The API will be available at `http://127.0.0.1:8000/`

## API Usage

### POST `/api/ask`

Send a message to the AI assistant and receive a response.

**Request:**

```bash
curl -X POST http://127.0.0.1:8000/api/ask \
  -H "Content-Type: application/json" \
  -d '{"message": "Hello, what can you help me with?"}'
```

**Request Body:**

| Field    | Type   | Required | Description        |
|----------|--------|----------|--------------------|
| `message`| string | Yes      | The user's message |

**Success Response (200):**

```json
{
  "response": "I'm a helpful AI assistant. I can help you with...",
  "message": "Hello, what can you help me with?"
}
```

**Error Responses:**

- `400` - Missing message: `{"error": "Message is required"}`
- `500` - Server/API error: `{"error": "error description"}`

## Project Structure

```
Session-Project/
├── langchain_project/          # Django project
│   ├── api/                    # API app
│   │   ├── views.py            # Ask endpoint logic
│   │   └── urls.py
│   ├── langchain_project/      # Django settings
│   │   └── settings.py
│   ├── manage.py
│   └── .env                    # API keys (create from .env.example)
├── venv/                       # Virtual environment
├── requirements.txt
└── README.md
```

## Resource Links

### Documentation

- [Django Documentation](https://docs.djangoproject.com/) - Web framework
- [LangChain Documentation](https://python.langchain.com/docs/) - LLM orchestration
- [LangChain Google GenAI](https://python.langchain.com/docs/integrations/chat/google_generative_ai) - Google Gemini integration
- [Google AI Gemini API](https://ai.google.dev/gemini-api/docs) - Gemini model docs

### API Keys & Setup

- [Google AI Studio](https://aistudio.google.com/) - Get API key & try Gemini
- [Google AI API Key](https://aistudio.google.com/apikey) - Create API key

### Related Libraries

- [langchain-google-genai (PyPI)](https://pypi.org/project/langchain-google-genai/)
- [python-dotenv (PyPI)](https://pypi.org/project/python-dotenv/)

## License

MIT
