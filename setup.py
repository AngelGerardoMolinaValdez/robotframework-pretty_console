# -*- coding=utf-8 -*-

from setuptools import setup, find_packages

setup(
    name="robotframework-prettyconsole",
    version="1.0.0",
    
    author="Angel Gerardo Molina Valdez",
    maintainer="Angel Gerardo Molina Valdez",
    author_email="angelgerardomolinavaldez@gmail.com",
    maintainer_email="angelgerardomolinavaldez@gmail.com",

    url="https://github.com/AngelGerardoMolinaValdez/robotframework-pretty_console.git",

    python_requires=">=3.7",
    zip_safe=False,
    platforms="Windows",

    package_dir={"" : "src"},
    package_data={"pretty_console": []},
    packages= find_packages("src"),

    entry_points = {
        "console_scripts" : [
            "probot=pretty_console.main:prettify",
            "prettyrobot=pretty_console.main:prettify",
            "pretty_robot=pretty_console.main:prettify",
            "pr=pretty_console.main:prettify",


            "cprobot=pretty_console.main:color_prettify",
            "colorprettyrobot=pretty_console.main:color_prettify",
            "color_pretty_robot=pretty_console.main:color_prettify",
            "cpr=pretty_console.main:color_prettify"


        ]
    }

)