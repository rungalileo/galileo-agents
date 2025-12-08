"""Content crew agents."""
from crewai import Agent

from prompts import EDITOR_BACKSTORY, EDITOR_GOAL, WRITER_BACKSTORY, WRITER_GOAL


def create_writer_agent(llm) -> Agent:
    return Agent(
        role="Content Writer",
        goal=WRITER_GOAL,
        backstory=WRITER_BACKSTORY,
        llm=llm,
        verbose=True,
    )


def create_editor_agent(llm) -> Agent:
    return Agent(
        role="Content Editor",
        goal=EDITOR_GOAL,
        backstory=EDITOR_BACKSTORY,
        llm=llm,
        verbose=True,
    )
