class Course:
    def __init__(self, title='', schedule='', description=''):
        self.title = title
        self.schedule = schedule
        self.description = description
        
    def __repr__(self):
        output = f'\nTitle: {self.title}\nSchedule: {self.schedule}\nDescription: {self.description}\n ------------------'
        return output
