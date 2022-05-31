from .application_services import Application_Service
from .directories_services import Directories_Service
import json

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
            elif(dest == 'kernel'):
                self.directories = Directories_Service(cmd)
                self.applications = Application_Service(cmd)

    def return_states(self):
        response = {'kernel_state':self.kernel, 'gui_state':self.gui, 'directories_state':self.directories.service_state, 'applications_state':self.applications.service_state}
        return response

    def manage_directories(self, name):
        response = json.loads((self.directories.manage_directory(name)).decode())
        return response

    def manage_applications(self, pid):
        response = json.loads((self.applications.manage_app(pid)).decode())
        return response

    def manage_kernel(self):
        response = {'kernel_state':0, 'gui_state':0, 'directories_state':self.directories.service_state, 'applications_state':self.applications.service_state}
        print(response)
        return response