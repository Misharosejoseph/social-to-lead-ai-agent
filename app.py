from agent import Agent

agent = Agent()

while True:
    user_input = input("User: ")

    if user_input.lower() == "exit":
        break

    response = agent.handle_input(user_input)
    print("Agent:", response)