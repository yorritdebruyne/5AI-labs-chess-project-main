from fiveaichess.agents.example_agent import ExampleAgent
from fiveaichess.utilities.example_utility import ExampleUtility
from fiveaichess.engines.uci_engine import UCIEngine

if __name__ == "__main__":
    # create your utility
    utility = ExampleUtility()
    # create your agent
    agent = ExampleAgent(utility, 5.0)
    # create the engine
    engine = UCIEngine(agent)
    
    # run the engine (will loop until the game is done or exited)
    engine.run()
