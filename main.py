from agents.root_agent import plan_trip

if __name__ == "__main__":
    destination = input("Enter destination: ")
    budget = input("Enter budget: ")

    result = plan_trip(destination, budget)

    print("\n===== TRAVEL PLAN =====\n")
    print(result)