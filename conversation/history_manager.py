class HistoryManager:
    def __init__(self):
        self.history = {}

    async def get_history(self, user_id, limit=5):
        return self.history.get(user_id, [])[-limit:]

    async def add_to_history(self, user_id, user_query, system_response):
        if user_id not in self.history:
            self.history[user_id] = []
        self.history[user_id].append({"user": user_query, "system": system_response})