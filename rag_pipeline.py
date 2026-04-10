import json

def load_knowledge():
    with open("knowledge_base.json") as f:
        return json.load(f)

def get_pricing_info():
    kb = load_knowledge()
    return kb["pricing"]