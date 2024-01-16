# -*- coding: utf-8 -*-
"""
    Created on Tue Jan 10  22:51:42 2024
    Title   :   Task Manager Program
    @author :   Aritr Ranjan Chowdhury 
"""
#%%

class Task (object):
    '''
    Simple Task class to track a single task information.
    TITLE, DESCRIPTION, SUB_DESCRIPTION and STATUS attributes are there
    TITLE is the unique for all task
    '''
    def __init__(self, title, description='', status='incomplete'):
        super().__init__()
        self.title = title 
        self.description = description
        self.status = status
    @property
    def title(self):         # Getter Property of Title 
        return self.__title
    @property
    def description (self):       # Getter Property of Description 
        if not self.__description:
            return "NOT SET"
        return self.__description
    @property
    def status(self):         # Getter Property of status
        if self._has_completed:
            return 'complete'
        elif not self._has_completed:
            return 'incomplete'  
    @title.setter
    def title(self,title):
        if not title:
            raise Exception("Task must need a Title")
        self.__title = title
    @description.setter
    def description (self, description):     # Setter Property of Price 
        if type(description) is str:
            self.__description = description
        else : raise Exception("Invalid Type")
    @status.setter     # Setter Property of status
    def status(self, status:str):
        if status=='complete':
            self._has_completed = True
        elif status=='incomplete':
            self._has_completed = False  
        else: raise Exception("Status must be 'complete' or 'icomplete'.")
    def __str__(self):      # Display or Print function overloading 
        return f'''Task (
    title = {self.title}
    description = {self.description}
    status = {self.status}  )'''
    def make_as_complete(self):
        self._has_completed = True
    def to_s(self):
        print(f'''Task (  title = {self.title}
        description = {self.description}
        status = {self.status}  )''')
# %% 
class TaskList(list):
    """TaskList class represents a collection of tasks.
Tracks all task normal task and Priority task also"""
    def __init__(self,*args):
        super().__init__(args)
    def find_task(self,title=None,priority=None,status=None):
        """Find a single task by name or find multiple task using statuss or priority"""
        if title:
            for task in self:
                if task.title == title:
                    return task
        elif priority:  
            
            return self.__class__(*[task for task in self
                if type(task) is PriorityTask and task.priority == priority])
       
        elif status:
            return self.__class__(*[task for task in self
                if task.status == status])
    def add_task(self, title, description='', status='incomplete'):
        """Method overloading to add tasks with a description nad status. 
Take input as title,description,status and create Task with blank description """
        if self.find_task(title):
            raise Exception("Duplicate task title is not alowed ")
        new_task = Task(title, description, status)
        self.append(new_task)

    def remove_task(self, title):
        """Method to remove a task by its title."""
        try:
            self.remove(self.find_task(title))
        except:
            raise Exception("Task Not Found")
        
    def remove_task(self, task:Task):
        """Method to remove a task by its Task object. """
        self.remove(task)                

    def add_priority_task(self, title, description='',priority=None,status='incomplete'):
        """Method overloading to add tasks with a description nad status. 
Take input as title,description,status and create Task with blank description """
        if self.find_task(title):
            raise Exception("Duplicate task title is not alowed ")        
        priority_task = PriorityTask(title, description,priority,status)
        self.append(priority_task)
    def view_all_tasks(self):
            '''Display all task available in task in a form of a table'''
            print( 'Priority Task List :\n' + '-'*130 +
                '\n %-25s \t %-50s \t %-10s \t %-5s \n'%('Title','Description','Priority', 'Status')+'-'*130 )
            for task in self:
                if type(task) is PriorityTask:
                    print("%-25s \t %-50s \t %-10s \t %-5s "
                        %(task.title,task.description,task.priority,task.status))
            print('\n\nNormal Task List :\n' + '-'*130 +
                '\n %-25s \t %-50s \t %-5s \n'%('Title','Description', 'Status')+'-'*130 )
            for task in self:
                if type(task) is Task:
                    print("%-25s \t %-50s \t %-5s "
                        %(task.title,task.description,task.status))   
    def mark_task_complete(self,title):
        '''complete a selected task'''
        self.find_task(title).make_as_complete()
    def find_priority_task(self,title):
        '''find task only by priority'''
        for task in self:
            if type(task) == PriorityTask and task.title == title:
                return task
class PriorityTask(Task):
    def __init__(self, title, description='', priority='low',status='incomplete' ):
        """PriorityTask class inherits from Task."""
        super().__init__(title, description, status)
        self.priority = priority
    @property
    def priority(self):
        return self.__priority
    @priority.setter
    def priority(self,priority):
        if priority not in ['low','medium','high']:
            raise Exception("Not a valid Priority Type. Priority must be [low, medium, high].")
        self.__priority = priority
    def to_s(self):
        print(f'''Task (  title = {self.title}
        description = {self.description}
        priority = {self.priority}
        status = {self.status}  )''')
# %% 
# Sample usage
default_task_list = TaskList( # Creating some dummy task as default 
    Task(title="Finish Presentation", description="Prepare slides for the team meeting"), 
    Task(title="Grocery Shopping", description="Buy fruits, vegetables, and milk"), 
    Task(title="Write Report", description="Summarize findings from the research"), 
    Task(title="Exercise", description="30 minutes of jogging or yoga"), 
    Task(title="Read Book", description="Complete chapters 5 to 8"), 
    Task(title="Call Mom", description="Check in and chat about the weekend"),
    Task(title="Pay Bills", description="Electricity and internet bills due this week"),
    Task(title="Organize Desk", description="Sort papers and declutter workspace"),
    Task(title="Watch Tutorial", description="Learn about new programming language features"),
    Task(title="Plan Vacation", description="Research destinations and hotel options"),
    PriorityTask(title="Finish Project Proposal", description="Complete the proposal for upcoming project", priority="high"),
    PriorityTask(title="Review Code Changes", description="Check and approve recent code modifications", priority="medium"),
    PriorityTask(title="Organize Team Meeting", description="Plan agenda and schedule for the weekly meeting", priority="low"),
    PriorityTask(title="Prepare Presentation Slides", description="Create slides for the client presentation", priority="medium"),
    PriorityTask(title="Resolve Critical Bug", description="Fix urgent bug affecting the system", priority="high"),
)
#%%

def assignment_solution():
    '''solvin the question that are given in the problems'''
    task_list = TaskList()
    task_list.add_task("Do homework")
    task_list.add_task("Go to the gym", "Cardio workout")
    task_list.add_priority_task("Buy groceries", "Milk and eggs", "high")
    # task_list.list_tasks
    task_list.view_all_tasks()
    task_list.mark_task_complete("Go to the gym")
    print(task_list.find_task("Do homework"))
    print(task_list.find_priority_task("Buy groceries"))



# %%
def print_ui():
    '''Printing Function of Basic UI '''
    print('\n\n'+'-'*50+'\nMENU :\n' +'-'*50+'''
 1) Add Task                2) Add Priority Task
 3) Add Default Tasks       4) View All Tasks
 5) Remove Task             6) Complete Task
 7) Serach Task             8) Assignment Solution   
 9) Exit\n'''+'-'*50)

def search_task_ui():
    print(
        ''' Search by 
1) Title        2) Status       3) Priority ''')    

def main():
    task_list = TaskList() # Creating Empty task list
    while True:
        print_ui()
        # Choice Validation
        try:
            choice = int(input('Choice : '))
        except: 
            print("Choice must be integer. ")
            continue
        #  switch-case structure based on user's choice
        if choice == 1:     # for adding Tasks
            title = input('Enter Title :')
            description = input('Enter description [None] :')
            status = input('Enter Status [Incomplete] :')
            if status not in ['incomplete','complete']: status = 'incomplete'
            try:
                task_list.add_task(title,description,status)
            except Exception as e:
                print(e)
        elif choice == 2:
            title = input('Enter Title :')
            description = input('Enter description [None] :')
            priority = input('Enter description [low] :')
            if not priority : priority = 'low'
            status = input('Enter Status [Incomplete] :')
            if status not in ['incomplete','complete']: status = 'incomplete'
            
            try:
                task_list.add_priority_task(title,description,priority,status)
            except Exception as e:
                print(e)

        elif choice == 3:   # for adding default tasks
            task_list = TaskList(*default_task_list) # Copy from the DEFAULT_task_LIST
        elif choice == 4:   # for viewing all tasks
            task_list.view_all_tasks()
        elif choice == 5:   # for removing a task
            name = input("Enter name of the task :")
            try: 
                task_list.remove_task(name)
            except Exception as e:
                print(e)
        elif choice == 6:   # for editing quantity
            name = input("Enter name of the task :")
            try:
               task_list.mark_task_complete(name)
            except Exception as e: 
                print(e)
           
        elif choice == 7:
            search_task_ui()
            try:
                choice = int(input("Enter Choice :"))
            except:
                print('wrong Choice')
                continue
            if choice <0 or choice >3:
                print('wrong Choice')
                continue
            if choice == 1:
                title = input('Enter title : ')
                task_list.find_task(title=title).to_s()
            elif choice == 2:
                status = input('Enter status : ')
                task_list.find_task(status=status).view_all_tasks()
            elif choice == 3:
                priority = input('Enter priority : ')
                task_list.find_task(priority=priority).view_all_tasks()
        elif choice == 8:   # for assignment solution
            assignment_solution()
        elif choice == 9:
            print("Exiting the program...")
            break
        else:
            print("Invalid choice. Please select a valid option.")



#%%
if __name__ == '__main__':
    main()