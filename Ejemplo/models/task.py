class Task:
    def __init__(self, title, description='', completed=False):
        self.title = title
        self.description = description
        self.completed = completed

    def to_dict(self):
        return {
            'title': self.title,
            'description': self.description,
            'completed': self.completed
        }

    @classmethod
    def from_dict(cls, data):
        return cls(data['title'], data.get('description', ''), data.get('completed', False))
