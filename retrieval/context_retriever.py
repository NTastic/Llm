from utils.dummy_data import LOCATION_DATA

class ContextRetriever:
    def get_context(self, loc_ids):
        return [loc for loc in LOCATION_DATA if loc['id'] in loc_ids]