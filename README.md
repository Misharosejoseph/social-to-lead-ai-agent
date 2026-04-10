Social-to-Lead Agentic Workflow (Inflx Assignment)
📌 Overview

This project implements a Conversational AI Agent for a fictional SaaS product AutoStream, designed to convert user interactions into qualified leads.

The agent goes beyond a simple chatbot by:

Understanding user intent
Retrieving accurate information using a knowledge base (RAG)
Identifying high-intent users
Capturing leads through structured interaction
🧠 Features
1. Intent Detection

The agent classifies user input into:

Greeting
Pricing/Product Inquiry
High-Intent Lead

This enables dynamic conversation flow and personalized responses.

2. RAG-Based Knowledge Retrieval

The system uses a local knowledge base (knowledge_base.json) containing:

Pricing plans (Basic & Pro)
Features and policies

The agent retrieves relevant information and generates accurate responses, simulating a Retrieval-Augmented Generation (RAG) workflow.

3. Multi-Step Lead Capture (Tool Execution)

When a high-intent user is detected, the agent:

Asks for Name
Collects Email
Asks for Platform (YouTube, Instagram, etc.)

After collecting all details, a mock function is triggered:

mock_lead_capture(name, email, platform)

This simulates backend lead storage.

4. State Management

The agent maintains conversation state across multiple turns using a structured state dictionary:

Tracks intent
Tracks conversation step (name → email → platform)
Stores user details

This ensures a smooth and realistic conversational experience.

⚙️ Tech Stack
Python 3.9+
Rule-based Intent Classification
JSON-based Knowledge Base
Modular Agent Architecture
(Extendable to LangChain / LangGraph)
