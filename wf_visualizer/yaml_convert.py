import yaml
from models import workflow, action
#TODO user input for yaml file
#TODO class for yamlconvert
#TODO Split into models/mistral and models/orquesta
#TODO unit testing

# with open('link.yaml', 'r') as stream:
#     data = yaml.load(stream)

#TODO Constructor taking in yaml file and converting it to python object
class YamlConvert:
    def __init__(self, yaml_file):
        '''
        :param str yaml file to process
        '''
        with open(yaml_file, 'r') as stream:
            self.yaml_data = yaml.load(stream)
        self.workflows = self.__extract_workflows()

    def __extract_workflows(self):
        '''
        Extracts workflow name(s) from the yaml_data object
        
        :param yaml_data: python object loaded from yaml file
        '''
        keys = list(self.yaml_data.keys())
        workflow_list = []
        #create workflow objects based on keys in yaml data
        if 'workflows' in keys:
            workflow_list = [workflow.Workflow(name=key) for key in keys ]
        else:            
            wf_names = [key for key in keys if key != 'version' and key != 'description']
            for wf in wf_names:
                workflow_list.append(workflow.Workflow(name=wf))
        
        #extract the workflow metadata
        metadata_keys = ['description', 'type', 'input', 'vars']
        for i, wf in enumerate(workflow_list):
            for key in metadata_keys:
                setattr(wf, key, self.yaml_data[wf.name][key])
            wf.tasks = self.__extract_tasks(wf.name)
            workflow_list[i] = wf

        #extract tasks from the workflow
        return workflow_list
     
    def __extract_tasks(self, workflow_name):
        '''
        Extracts the tasks of a given workflow
        '''
        return list(self.yaml_data[workflow_name]['tasks'].keys())
        
converter = YamlConvert('link.yaml')
print(converter.workflows)
for wf in converter.workflows:
    print (wf.name, wf.description, wf.tasks)

