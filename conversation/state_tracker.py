class StateTracker:
    def __init__(self):
        self.states = {}

    async def get_state(self, user_id):
        return self.states.get(user_id, {})

    async def update_state(self, user_id, new_state):
        self.states[user_id] = new_state