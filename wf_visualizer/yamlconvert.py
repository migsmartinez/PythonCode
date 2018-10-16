import yaml
#TODO user input for yaml file
#TODO class for yamlconvert
#TODO Split into models/mistral and models/orquesta
#TODO unit testing

with open('link.yaml', 'r') as stream:
    data = yaml.load(stream)

#TODO Constructor taking in yaml file and converting it to python object
class YamlConvert:
    def __extract_workflows(self, yaml_data):
        '''
        Extracts workflow name(s) from the yaml_data object
        
        :param object yaml_data: python object loaded from yaml file
        '''
        if 'workflows' in list(yaml_data.keys()):
            print(yaml_data['workflows'])
        else:
            keys = list(yaml_data.keys())[1:]
            return keys
     
    def __extract_tasks(self, workflow_name):
        '''
        Extracts the tasks of a given workflow
        '''
        raise NotImplementedError
        
print(extract_actions(data))

class Action:
    '''
    Represents a yaml file under the /actions folder
    '''
    def __init__(self, name, runner_type):
        self.name = name
        
class Workflow:
    '''
    Represents a yaml file under the /actions/workflows folder
    '''
    def __init__(self, name, description, type, input, vars, tasks):
        self.name = name
    
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
