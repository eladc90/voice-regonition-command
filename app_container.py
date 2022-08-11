import string


class App_container:
    """
    hold all app commanders, manage the apps and dispatch commands.   
    """
    
    def __init__(self):
        self.apps_dict = {}
        self.listen_app_list = []
        
        
    def dispatch_command(self, command):
        # TODO check if this is a better way
        # for key, val in self.apps_dict.items():
        #     if key in command:
        #         val.register_as_listener()
        
        for app in self.listen_app_list:
            app.execute_command(command)
        
        
    def register_app(self, app, key, status):
        self.apps_dict[key] = app
        if status is True:
            self.listen_app_list.append(app)
            
            
    def set_app_as_listener(self, key: string) -> bool:
        
        """
        check if the app is in the register to the app dict if it does 
        add to the listener list if not already exist in the list.
        
        
        Args:
            key (str): the key of the app

        Returns:
            bool
            - return False if unsuccessfully added to the listeners list (if app not register to container)
            - return True if successfully added
        """
        
        if key in self.apps_dict.keys():
            app = self.apps_dict[key]
        else:
            return False
        
        if not app in self.listen_app_list:
            self.listen_app_list.append(app)
        return True
    
    
    def remove_from_listener_list(self, app):
        try: 
            self.listen_app_list.remove(app)
        except ValueError as ex:
            print(ex)
        
        
    def print_status(self):
        print("the apps on listening list: ")
        for i in self.apps_dict:
            print(f'   - {i}')
            


