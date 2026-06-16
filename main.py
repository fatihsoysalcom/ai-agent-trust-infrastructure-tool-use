import math

def is_prime_tool(number: int) -> bool:
    """
    A reliable, deterministic tool to check if a number is prime.
    This represents a trusted external component or function in the trust infrastructure.
    """
    if number < 2:
        return False
    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            return False
    return True

def simulate_llm_agent_thought(query: str, number: int) -> dict:
    """
    Simulates an LLM agent's initial thought process. It might provide a general idea
    but also recognizes when a definitive, trustworthy answer requires a specialized tool.
    """
    if "prime number" in query.lower() or "asal sayı" in query.lower() or "asal mı" in query.lower():
        # The LLM identifies a task requiring precise calculation and suggests a tool.
        return {
            "thought": f"The query is about prime numbers. While I can discuss properties of prime numbers, for a definitive check on {number}, a specialized mathematical tool would be more reliable.",
            "action_required": "use_prime_checker_tool",
            "tool_input": number
        }
    else:
        return {
            "thought": f"I can answer general questions about '{query}'. For specific calculations, I might need to use other tools.",
            "action_required": "none",
            "tool_input": None
        }

def ai_agent_decision_process(query: str, number_to_check: int):
    """
    The AI agent's main decision process, incorporating a trust infrastructure.
    It uses the LLM for initial understanding and then delegates to a trusted tool
    for verifiable answers when necessary, enhancing reliability.
    """
    print(f"Agent received query: '{query}' for number {number_to_check}")

    # Step 1: Get initial thought/plan from the simulated LLM
    llm_output = simulate_llm_agent_thought(query, number_to_check)
    print(f"\nLLM's thought: {llm_output['thought']}")

    # Step 2: Implement trust infrastructure - check if a tool is needed based on LLM's suggestion
    if llm_output["action_required"] == "use_prime_checker_tool":
        print("\nTrust infrastructure activated: LLM suggests using a reliable tool for verification.")
        tool_input = llm_output["tool_input"]
        is_prime = is_prime_tool(tool_input) # Call the trusted tool for a verifiable answer
        print(f"Tool '{is_prime_tool.__name__}' executed with input {tool_input}.")
        if is_prime:
            final_answer = f"According to the trusted mathematical tool, {tool_input} IS a prime number."
        else:
            final_answer = f"According to the trusted mathematical tool, {tool_input} IS NOT a prime number."
    else:
        final_answer = f"LLM provided a general response: {llm_output['thought']}"

    print(f"\nAgent's final, verified response: {final_answer}")
    return final_answer

if __name__ == "__main__":
    print("--- Scenario 1: Checking a prime number (trust infrastructure used) ---")
    ai_agent_decision_process("Is 17 a prime number?", 17)

    print("\n" + "="*70 + "\n")

    print("--- Scenario 2: Checking a non-prime number (trust infrastructure used) ---")
    ai_agent_decision_process("Check if 21 is prime.", 21)

    print("\n" + "="*70 + "\n")

    print("--- Scenario 3: General query (LLM handles directly, no tool needed) ---")
    ai_agent_decision_process("What is the capital of France?", 0) # Number doesn't matter here
