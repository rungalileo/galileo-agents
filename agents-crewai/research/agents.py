"""Research crew agents."""
from crewai import Agent

from prompts import ANALYST_BACKSTORY, ANALYST_GOAL, RESEARCHER_BACKSTORY, RESEARCHER_GOAL


def create_researcher_agent(llm, tools=None) -> Agent:
    return Agent(
        role="Researcher",
        goal=RESEARCHER_GOAL,
        backstory=RESEARCHER_BACKSTORY,
        llm=llm,
        tools=tools or [],
        verbose=True,
    )


def create_analyst_agent(llm, tools=None) -> Agent:
    return Agent(
        role="Analyst",
        goal=ANALYST_GOAL,
        backstory=ANALYST_BACKSTORY,
        llm=llm,
        tools=tools or [],
        verbose=True,
    )
