# -*- coding=utf-8 -*-

from pretty_console.modules.output import console

class Listener:

    ROBOT_LISTENER_API_VERSION = 2

    def __init__(self) -> None:
        return

    def start_suite(self, name, attributes):
        console.print_suite_info(name, attributes)


    def end_suite(self, name, attributes):
        print('\n')
        console.print_suite_info(name, attributes)


    def start_test(self,name, attributes):
        print('\n')
        console.print_test_case_info(name, attributes)


    def end_test(self,name, attributes):
        print('\n')
        console.print_test_case_info(name, attributes)


    def start_keyword(self, name, attributes):
        if attributes['status'] == "NOT RUN":
            return

        if name != "BuiltIn.Log To Console":
            return
        console.print_log_to_console_info()
    

    def end_keyword(self, name, attributes):
        if attributes['status'] == "NOT RUN":
            return

        if name == "BuiltIn.Log To Console":
            print('\n')
            console.print_log_to_console_info()

        console.print_test_keyword_info(name, attributes)


    def library_import(self, name, attributes):
        console.print_import_library(name, attributes)


    def resource_import(self, name, attributes):
        console.print_import_resource(name, attributes)


    def variables_import(self, name, attributes):
        console.print_import_variables(name, attributes)
    

    def log_message(self, message):
        try:
            mensaje = message["message"]
            expression = eval(mensaje)
        except:
            expression = message
        
        console.print_log_message(expression)


