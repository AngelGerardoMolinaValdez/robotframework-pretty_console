# -*- coding:utf-8 -*-

import os
from pretty_console.data import info
import colorama

def print_suite_info(name, attributes):
    if not attributes["suites"]:
        print_test_suite_info(name, attributes)
        return

    print_dir_suite_info(name, attributes)
    


def print_test_suite_info(name, attributes):

    if info.color:
        decorator = colorama.Back.MAGENTA + "::" + colorama.Style.RESET_ALL

        try:
            if attributes['status'] == "PASS":
                status = colorama.Back.GREEN + attributes['status'] + colorama.Style.RESET_ALL
            else:
                status = colorama.Back.RED + attributes['status'] + colorama.Style.RESET_ALL
        except:
            pass
    else:
        decorator = "::"
        try:
            status = attributes['status']
        except:
            pass



    try:
        time = attributes['endtime']
        name_time = 'endtime'
    except:
        time = attributes['starttime']
        name_time = 'starttime'

    print(decorator, attributes['id'], decorator, name, decorator, time)
    print(decorator, "doc       ", decorator.ljust(10), attributes['doc'])
    print(decorator, "metadata  ", decorator.ljust(10), attributes['metadata'])
    print(decorator, "tests     ", decorator.ljust(10), attributes['tests'])
    print(decorator, "source    ", decorator.ljust(10), attributes['source'])
    try:
        print(decorator, "status    ", decorator.ljust(10), status)
        print(decorator, "message   ", decorator.ljust(10), attributes['message'])
        print(decorator, "statistics", decorator.ljust(10), attributes['statistics'])
    except:
        pass
    print('\n')
    

def print_dir_suite_info(name, attributes):

    if info.color:
        decorator = colorama.Back.BLUE + "::" + colorama.Style.RESET_ALL
    else:
        decorator = "::"
    try:
        time = attributes['endtime']
    except:
        time = attributes['starttime']


    print(decorator, attributes['id'], decorator, name, decorator, time)
    print(decorator, "suites ", decorator.ljust(10), attributes['suites'])
    print(decorator, "source ", decorator.ljust(10), attributes['source'])
    print('\n')


def print_test_case_info(name, attributes):

    if info.color:
        decorator = colorama.Back.CYAN + "::" + colorama.Style.RESET_ALL

        try:
            if attributes['status'] == "PASS":
                status = colorama.Back.GREEN + attributes['status'] + colorama.Style.RESET_ALL
            else:
                status = colorama.Back.RED + attributes['status'] + colorama.Style.RESET_ALL
        except:
            pass

    else:
        decorator = "::"
        try:
            status = attributes['status']
        except:
            pass

    try:
        time = attributes['endtime']
    except:
        time = attributes['starttime']


    print(
    decorator, attributes['id'], 
    decorator, attributes['longname'], 
    decorator, time
    )

    print(decorator, " doc     ", decorator.ljust(5), attributes['doc'])
    print(decorator, " tags    ", decorator.ljust(5), attributes['tags'])
    print(decorator, " lineno  ", decorator.ljust(5), attributes['lineno'])
    print(decorator, " source  ", decorator.ljust(5), attributes['source'])
    try:
        print(decorator, " template", decorator.ljust(5), attributes['template'])
    except:
        pass
    try:
        print(decorator, " status  ", decorator.ljust(5), status)
        print(decorator, " message ", decorator.ljust(5), attributes['message'])
    except:
        pass
    print('\n')


def print_test_keyword_info(name, attributes):
    if info.color:
        if attributes['status'] == "PASS":
            status_color = colorama.Back.GREEN
        else:
            status_color = colorama.Back.RED

        decorator = status_color + "::" + colorama.Style.RESET_ALL

    else:
        decorator = "::"

    try:
        time = attributes['endtime']
    except:
        time = attributes['starttime']

    print(
        decorator, os.path.basename(attributes['source']), 
        decorator, attributes['lineno'],
        decorator, attributes['type'],
        decorator, name,
        decorator, time,
        decorator, attributes['status'],
        "\n"
    )
    

def print_log_to_console_info():
    if info.color:
        decorator = colorama.Back.YELLOW + "::" + colorama.Style.RESET_ALL
    else:
        decorator = "::"
    print(decorator, "Robot Framework Output", decorator, "\n")

def print_log_message(message):
    print("log ::", message['message'], '\n')

def print_import_resource(name, attributes):
    if info.color:
        decorator = colorama.Back.YELLOW + "::" + colorama.Style.RESET_ALL
    else:
        decorator = "::"
    print("Resource",decorator,  name, "\n")

def print_import_library(name, attributes):
    if info.color:
        decorator = colorama.Back.YELLOW + "::" + colorama.Style.RESET_ALL
    else:
        decorator = "::"

    print("Library",decorator,  name, decorator, attributes['args'],"\n")
    
def print_import_variables(name, attributes):
    if info.color:
        decorator = colorama.Back.YELLOW + "::" + colorama.Style.RESET_ALL
    else:
        decorator = "::"

    print("Variables", decorator, name, "\n")
    

def print_log_message(message):
    if info.color:
        decorator = colorama.Back.BLUE + "::" + colorama.Style.RESET_ALL
    
    else:
        decorator = "::"

    print(decorator, message['message'], '\n')
    
