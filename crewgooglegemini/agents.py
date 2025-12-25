from crewai import Agent
from dotenv import load_dotenv
from tools import tool

load_dotenv()

MODEL = "gemini/gemini-flash-latest"  # Using litellm format with provider prefix

news_researcher = Agent(
    role="Senior Researcher",
    goal="Uncover groundbreaking technologies in {topic}",
    verbose=True,
    memory=True,
    backstory="Driven by curiosity, you explore cutting-edge innovation.",
    tools=[tool],
    llm=MODEL,
    allow_delegation=True
)

news_writer = Agent(
    role="Writer",
    goal="Narrate compelling tech stories about {topic}",
    verbose=True,
    memory=False,
    backstory="You turn complex tech into engaging stories.",
    tools=[],
    llm=MODEL,
    allow_delegation=False
)
