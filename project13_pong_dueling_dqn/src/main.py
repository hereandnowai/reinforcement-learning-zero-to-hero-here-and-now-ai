from agent import Agent
from environment import Env

def main():
    env = Env()
    agent = Agent(env)
    agent.train(episodes=1000)

if __name__ == "__main__":
    main()
