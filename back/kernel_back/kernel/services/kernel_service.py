from .application_services import Application_Service
from .directories_services import Directories_Service

class Kernel_Service:
    def __init__(self, general_state, dest, cmd) -> None:
        if general_state == 0:
            self.kernel = 1
            self.gui = 1
            self.directories = Directories_Service(cmd)
            self.applications = Application_Service(cmd)
        elif general_state == 1:
            if(dest == 'GestorArc'):
                 self.directories = Directories_Service(cmd)
            elif(dest == 'APP'):
                self.applications = Application_Service(cmd)

    def return_states(self):
        response = {'kernel_state':self.kernel, 'gui_state':self.gui, 'directories_state':self.directories.service_state, 'applications_state':self.applications.service_state}
        return response

    def manage_directories(self, name):
        self.directories.manage_directory(name)