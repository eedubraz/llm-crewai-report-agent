from crewai import Agent
from tools import tool
import os
from dotenv import load_dotenv
load_dotenv()

from langchain_google_genai import ChatGoogleGenerativeAI

## call the gemini models
llm=ChatGoogleGenerativeAI(model="gemini-1.5-flash",
                           verbose=True,
                           temperature=0.5,
                           google_api_key=os.getenv('GOOGLE_API_KEY'))

## Creating a senior researcher agent with memory and verbose mode
news_researcher = Agent(
    role="Senior Researcher",
    goal='Unccover ground breaking technologies in {topic}',
    llm=llm,
    tools=[tool],
    memory=True,
    verbose=True,
    backstory=(
        "You are a senior researcher at a leading technology company."
        "You are tasked with uncovering ground breaking technologies in the field of {topic}."
        "You have access to a wide range of resources, including the internet, scientific databases, and internal company data."
        "You are also able to collaborate with other researchers and experts in the field."
        "Your goal is to identify promising new technologies that could have a significant impact on the company's business."
    ),
    allow_delegation=True
)

## Creating a writer agent with custom tools responsible in writing news blog
news_writer = Agent(
    role="Writer",
    goal='Narrate compelling tech stories about {topic}',
    llm=llm,
    tools=[tool],
    memory=True,
    verbose=True,
    backstory=(
        "You are a writer for a technology blog."
        "You are tasked with writing compelling tech stories about {topic}."
        "Your goal is to create engaging and informative content that will attract a large audience."
    ),
    allow_delegation=False
)
