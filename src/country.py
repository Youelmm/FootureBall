class Country:
    current_id = 0

    def __init__(self, name):
        # Unique ID
        self.id = Country.current_id
        Country.current_id += 1

        self.name = name
