# Galileo Agents

AI agent examples instrumented with Traceloop (OpenLLMetry), exporting traces to Galileo.

## Agents

| Framework | Agent | Span Types |
|-----------|-------|------------|
| LangGraph | Weather | `agent`, `workflow`, `llm`, `tool` |
| LangGraph | Calculator | `agent`, `workflow`, `llm`, `tool` |
| LangGraph | RAG | `agent`, `workflow`, `llm`, `tool`, `retriever` |
| CrewAI | Content | `agent`, `llm`, `tool` |
| CrewAI | Research | `agent`, `llm`, `tool`, `retriever` |

## Setup

```bash
# Install uv
curl -LsSf https://astral.sh/uv/install.sh | sh

# Install dependencies
uv sync --all-extras

# Configure environment
cp env.example .env
# Edit .env with your API keys
```

## Run

```bash
# LangGraph
uv run agents-langgraph/weather/agent.py
uv run agents-langgraph/calculator/agent.py
uv run agents-langgraph/rag/agent.py

# CrewAI
uv run agents-crewai/content/crew.py
uv run agents-crewai/research/crew.py

# Custom queries
uv run agents-langgraph/weather/agent.py "What's the forecast for NYC?"
```

## Environment Variables

| Variable | Description |
|----------|-------------|
| `GALILEO_API_KEY` | Galileo API key |
| `TRACELOOP_BASE_URL` | Traceloop endpoint (default: https://api.galileo.ai/otel) |
| `TRACELOOP_HEADERS` | Traceloop headers: `Galileo-API-Key=${GALILEO_API_KEY},X-Use-Otel-New=true` |
| `OPENAI_API_KEY` | OpenAI API key |

## Telemetry

All agents use Traceloop for automatic instrumentation. Traceloop reads `TRACELOOP_BASE_URL` and `TRACELOOP_HEADERS` from environment variables and automatically appends `/v1/traces` to the base URL.

Project and logstream are specified via resource attributes (hardcoded in each agent):

```python
from traceloop.sdk import Traceloop

Traceloop.init(
    app_name="weather-agent",
    resource_attributes={
        "galileo.project.name": "galileo-agents",
        "galileo.logstream.name": "weather-agent",
    },
)
```

Traceloop automatically instruments LangGraph workflows and CrewAI crews, generating spans for agents, tools, LLM calls, and retrievers.
