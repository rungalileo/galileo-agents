"""Weather Agent - Answers weather questions using tools."""
import os
import sys

from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain_core.tools import tool
from langchain_openai import ChatOpenAI
from opentelemetry import trace
from opentelemetry.sdk.trace.export import BatchSpanProcessor, ConsoleSpanExporter
from traceloop.sdk import Traceloop

from prompt import WEATHER_AGENT_SYSTEM_PROMPT
from shared import logger
from tools import get_current_weather, get_forecast

load_dotenv()

Traceloop.init(
    app_name="weather-agent",
    resource_attributes={
        "galileo.project.name": "galileo-agents",
        "galileo.logstream.name": "weather-agent",
    },
    disable_batch=True,
)

# Add console exporter for debugging if enabled
if os.getenv("TRACELOOP_CONSOLE_EXPORTER_ENABLED", "false").lower() == "true":
    tracer_provider = trace.get_tracer_provider()
    if hasattr(tracer_provider, "add_span_processor"):
        console_processor = BatchSpanProcessor(ConsoleSpanExporter())
        tracer_provider.add_span_processor(console_processor)


@tool
def weather_tool(city: str) -> str:
    """Get current weather for a city."""
    result = get_current_weather(city)
    return f"Weather in {result['city']}: {result['temperature_f']}F, {result['conditions']}, {result['humidity']}% humidity"


@tool
def forecast_tool(city: str, days: int = 3) -> str:
    """Get multi-day weather forecast for a city."""
    result = get_forecast(city, days)
    lines = [f"Forecast for {result['city']}:"]
    for day in result["forecast"]:
        lines.append(f"  Day {day['day']}: High {day['high_f']}F, Low {day['low_f']}F, {day['conditions']}")
    return "\n".join(lines)


def create_weather_agent():
    llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)
    return create_agent(llm, [weather_tool, forecast_tool], system_prompt=WEATHER_AGENT_SYSTEM_PROMPT)


def main(query: str = "What's the weather like in San Francisco?"):
    logger.info(f"Weather Agent - Query: {query}")
    agent = create_weather_agent()
    result = agent.invoke({"messages": [("user", query)]})
    response = result["messages"][-1].content
    logger.info(f"Response: {response}")
    return response


if __name__ == "__main__":
    query = " ".join(sys.argv[1:]) if len(sys.argv) > 1 else "What's the weather like in San Francisco?"
    main(query)
