def classify_intent(user_input):
    user_input = user_input.lower()

    if any(word in user_input for word in ["hi", "hello", "hey"]):
        return "greeting"

    elif any(word in user_input for word in ["price", "cost", "plan"]):
        return "pricing"

    elif any(word in user_input for word in ["buy", "subscribe", "sign up", "try"]):
        return "high_intent"

    return "general"