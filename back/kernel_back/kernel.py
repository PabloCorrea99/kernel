import os
import subprocess
import sys
from pathlib import Path

class Kernel:
    def __init__(self) -> None:
        pass
    
    def initializer(self):
        if sys.argv[1] == '-start':
            cmd_kernel = f'python {Path(__file__).resolve(strict=True).parent}/manage.py runserver'
            subprocess.call(f'start {cmd_kernel}', shell=True)
            cmd_gui = f'cd {Path(__file__).resolve(strict=True).parent.parent.parent}/front/kernel_front/ && npm start'
            print(cmd_gui)
            os.system(cmd_gui)
        elif sys.argv[1] == '-shutdown':
            self.shutdown()

    def shutdown():
        print('apagando')

kernel = Kernel()
kernel.initializer()