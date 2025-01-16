from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import WebsiteSearchTool
from crewai_tools import ScrapeWebsiteTool
from crewai_tools import YoutubeVideoSearchTool
from dotenv import load_dotenv

load_dotenv()

@CrewBase
class flow_agents():
    """flow_agents crew"""

    @agent
    def trend_youtube(self) -> Agent:
        return Agent(
            config=self.agents_config['trend_youtube'],
            tools=[YoutubeVideoSearchTool()],
            llm="azure/gpt-4o",	
        )

    @agent
    def trend_researcher(self) -> Agent:
        return Agent(
            config=self.agents_config['trend_researcher'],
            tools=[WebsiteSearchTool()],
            llm="azure/gpt-4o-mini",
        )

    @agent
    def content_analyst(self) -> Agent:
        return Agent(
            config=self.agents_config['content_analyst'],
            tools=[ScrapeWebsiteTool()],
            llm="azure/gpt-4o-mini",
        )

    @agent
    def content_creator(self) -> Agent:
        return Agent(
            config=self.agents_config['content_creator'],
            tools=[],
            llm="azure/gpt-4o-mini",
        )

    @agent
    def seo_specialist(self) -> Agent:
        return Agent(
            config=self.agents_config['seo_specialist'],
            tools=[],
            llm="azure/gpt-4o-mini",
        )


    @task
    def youtube_trends_task(self) -> Task:
        return Task(
            config=self.tasks_config['youtube_trends_task'],
            tools=[YoutubeVideoSearchTool()],
        )
    
    @task
    def research_trends_task(self) -> Task:
        return Task(
            config=self.tasks_config['research_trends_task'],
            tools=[WebsiteSearchTool()],
        )

    @task
    def analyze_content_task(self) -> Task:
        return Task(
            config=self.tasks_config['analyze_content_task'],
            tools=[ScrapeWebsiteTool()],
        )

    @task
    def create_content_task(self) -> Task:
        return Task(
            config=self.tasks_config['create_content_task'],
            
        )

    @task
    def optimize_content_task(self) -> Task:
        return Task(
            config=self.tasks_config['optimize_content_task'],
            
        )

    @crew
    def crew(self) -> Crew:
        """Creates the flow_agents crew"""
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True,
            #embedder={"type": "azure", "model": "text-embedding-ada-002"},
        )
