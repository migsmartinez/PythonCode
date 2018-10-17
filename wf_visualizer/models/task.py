class Task:
    '''
    Represents a task under a workflow
    '''
    def __init__(self, name, action, input, publish, on_success, on_error, on_completed, retry):
        self.name = name
        self.action = action
        self.input = input
        self.publish = publish
        self.on_success = on_success
        self.on_error = on_error
        self.on_completed = on_completed
        self.retry = retry
