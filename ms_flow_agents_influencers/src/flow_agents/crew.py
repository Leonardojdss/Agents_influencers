from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task, after_kickoff
from crewai_tools import WebsiteSearchTool
from crewai_tools import ScrapeWebsiteTool
from crewai_tools import YoutubeVideoSearchTool
from crewai import LLM

@CrewBase
class flow_agents():
    """flow_agents crew"""

    # @agent
    # def manager(self) -> Agent:
    #     return Agent(
    #         config=self.agents_config['manager'],
    #         tools=[],
    #     )
    
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

    @after_kickoff
    def process_results(self, result):
        """Process and format the results after the crew completes."""
        result.raw = result.raw.strip()
        result.raw = f"""
        # Research Results
        
        {result.raw}
        """
        return result
    
    @crew
    def crew(self) -> Crew:
        """Creates the flow_agents crew"""

        manager_llm = LLM(model="gpt-4o")

        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.hierarchical,
            verbose=True,
            #manager_agent=self.manager,
            manager_llm=manager_llm
        )