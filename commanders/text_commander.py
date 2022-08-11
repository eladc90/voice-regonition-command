from .app_command import App_command


class text_commander(App_command):
    def __init__(self, app_status=True, app_key='text'):
        super().__init__(app_status, app_key)
        self.command_dict = {
            'to file': self._write_to_file
        }

                
    def _write_to_file(self, command):
        with open('text_file', 'w') as fd:
            fd.write(command)