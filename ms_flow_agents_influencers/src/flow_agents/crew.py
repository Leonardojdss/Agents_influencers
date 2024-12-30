from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import WebsiteSearchTool
from crewai_tools import ScrapeWebsiteTool
from crewai_tools import YoutubeVideoSearchTool

@CrewBase
class flow_agents():
    """flow_agents crew"""

    @agent
    def trend_youtube(self) -> Agent:
        return Agent(
            config=self.agents_config['trend_youtube'],
            tools=[YoutubeVideoSearchTool()],
        )

    @agent
    def trend_researcher(self) -> Agent:
        return Agent(
            config=self.agents_config['trend_researcher'],
            tools=[WebsiteSearchTool()],
        )

    @agent
    def content_analyst(self) -> Agent:
        return Agent(
            config=self.agents_config['content_analyst'],
            tools=[ScrapeWebsiteTool()],
        )

    @agent
    def content_creator(self) -> Agent:
        return Agent(
            config=self.agents_config['content_creator'],
            tools=[],
        )

    @agent
    def seo_specialist(self) -> Agent:
        return Agent(
            config=self.agents_config['seo_specialist'],
            tools=[],
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
            agents=self.agents, # Automatically created by the @agent decorator
            tasks=self.tasks, # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
        )
