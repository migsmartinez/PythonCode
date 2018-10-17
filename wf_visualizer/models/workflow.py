class Workflow:
    '''
    Represents a yaml file under the /actions/workflows folder
    '''
    def __init__(self, name, description=None, wf_type=None, input=None, vars=None, tasks=[]):
        self.name = name
        self.description = description
        self.wf_type = wf_type
        self.input = input
        self.vars = vars
        self.tasks = tasks
