import sys
from flow_agents.crew import flow_agents
from dotenv import load_dotenv
from fastapi import FastAPI
from flow_agents.api.routes import router

load_dotenv()

def run(a, b):
    """
    Run the crew.
    """
    inputs = {
        'topic': f'{a}',
        'platform': f'{b}'
    }
    flow_agents().crew().kickoff(inputs=inputs)

# def train():
#     """
#     Train the crew for a given number of iterations.
#     """
#     inputs = {
#         'topic': 'sample_value',
#         'platform': 'sample_value'
#     }
#     try:
#         flow_agents().crew().train(n_iterations=int(sys.argv[1]), filename=sys.argv[2], inputs=inputs)

#     except Exception as e:
#         raise Exception(f"An error occurred while training the crew: {e}")

# def replay():
#     """
#     Replay the crew execution from a specific task.
#     """
#     try:
#         flow_agents().crew().replay(task_id=sys.argv[1])

#     except Exception as e:
#         raise Exception(f"An error occurred while replaying the crew: {e}")

# def test():
#     """
#     Test the crew execution and returns the results.
#     """
#     inputs = {
#         'topic': 'sample_value',
#         'platform': 'sample_value'
#     }
#     try:
#         flow_agents().crew().test(n_iterations=int(sys.argv[1]), openai_model_name=sys.argv[2], inputs=inputs)

#     except Exception as e:
#         raise Exception(f"An error occurred while testing the crew: {e}")

def start_flow(a, b, c):

    command = c
    if command == "run":
        run(a, b)
    # elif command == "train":
    #     train()
    # elif command == "replay":
    #     replay()
    # elif command == "test":
    #     test()
    else:
        print(f"Unknown command: {command}")
        sys.exit(1)

# Prefixo para as rotas da API
app = FastAPI()
app.include_router(router, prefix="/ms_flow_agents_influencers")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=1000)