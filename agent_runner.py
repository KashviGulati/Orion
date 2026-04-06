# agent_runner.py

from agent_setup import agent

def autonomous_check():
    prompt = """
    Check:
    1. If I'm overspending
    2. If new relevant jobs exist
    Send alerts if needed
    """

    response = agent.run(prompt)
    return response