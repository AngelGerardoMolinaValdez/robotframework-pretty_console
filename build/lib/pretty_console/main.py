# -*- coding: utf-8 -*-

import robot
import os
import sys
import colorama
from pretty_console.data import info


class PrettyRobotConsole:
    
    def _set_path_project(self):
        project_basedir: str = os.path.dirname(__file__)
        self.project_basedir = project_basedir
        

    def _get_args_execution(self) -> list[str]: 
        args : list = list(sys.argv)[1:]
        path_listener = os.path.join(self.project_basedir, "modules", "robotframework", "Listener.py")
        args.insert(0, "--quiet")
        args.insert(1, "--listener")
        args.insert(2, path_listener)
        return args

    def prettify(self, color = False) -> None:
        if color:
            info.color = True

        self._set_path_project()
        args = self._get_args_execution()
        robot.run_cli(args, exit=False)
        

    

def prettify():
    PrettyRobotConsole().prettify()

def color_prettify():
    colorama.init(autoreset=True)
    PrettyRobotConsole().prettify(True)
