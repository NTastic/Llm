def generate_prompt(query, loc_context, conversation_history, dialogue_state):
    prompt = f"User Query: {query}\n\n"
    prompt += "Location Context:\n"
    
    for loc in loc_context:
        name = loc.get('displayName', 'Unknown Location')
        description = loc.get('adrFormatAddress', 'No address available')
        primary_type = loc.get('primaryTypeDisplayName', 'N/A')
        rating = loc.get('rating', 'N/A')
        
        prompt += f"- {name}: {description}\n"
        prompt += f"  Type: {primary_type}, Rating: {rating}\n"
        
        if loc.get('reviews'):
            top_review = loc['reviews'][0].get('text', 'No review available')
            prompt += f"  Sample Review: {top_review[:100]}...\n"
        
        prompt += "\n"
    
    prompt += "\nConversation History:\n"
    for turn in conversation_history[-3:]:  # Include last 3 turns
        prompt += f"User: {turn['user']}\nSystem: {turn['system']}\n"
    
    prompt += f"\nCurrent Dialogue State: {dialogue_state}\n\n"
    prompt += "Based on the user query, location context, conversation history, and current dialogue state, "
    prompt += "provide the top 10 most relevant location recommendations. For each recommendation, include the location name, "
    prompt += "a brief explanation of why it's recommended, and its price.\n"
    
    return prompt