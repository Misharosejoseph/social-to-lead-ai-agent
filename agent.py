class Agent:
    def __init__(self):
        self.state = {
            "intent": None,
            "step": None,
            "name": None,
            "email": None,
            "platform": None
        }

    def handle_input(self, user_input):

        # If already collecting details → don't reclassify intent
        if self.state["step"] == "ask_name":
            self.state["name"] = user_input
            self.state["step"] = "ask_email"
            return f"Thanks {user_input}! Please provide your email."

        elif self.state["step"] == "ask_email":
            self.state["email"] = user_input
            self.state["step"] = "ask_platform"
            return "Got it! Which platform do you create content on?"

        elif self.state["step"] == "ask_platform":
            self.state["platform"] = user_input

            # FINAL STEP → call tool
            mock_lead_capture(
                self.state["name"],
                self.state["email"],
                self.state["platform"]
            )

            self.state["step"] = None
            return "Thanks! We've captured your details."

        # NORMAL FLOW
        intent = classify_intent(user_input)
        self.state["intent"] = intent

        if intent == "greeting":
            return "Hi! How can I help you today?"

        elif intent == "pricing":
            pricing = get_pricing_info()
            return f"Basic: {pricing['basic']['price']}, Pro: {pricing['pro']['price']}"

        elif intent == "high_intent":
            self.state["step"] = "ask_name"
            return "Great! Can I have your name?"

        return "Can you please clarify your question?"