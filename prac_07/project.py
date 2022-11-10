class Project:
    def __init__(self, name="", date="", priority=0, cost=0.0, completion=0):
        self.name = name
        self.date = date
        self.priority = priority
        self.cost = cost
        self.completion = completion

    def __str__(self):
        return f"{self.name}, start: {self.date}, priority {self.priority}, estimate: ${self.cost}, completion: %{self.completion} "
