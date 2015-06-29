#!/usr/bin/env python
USAGE = '''
Start a new webapp project.

Install Spring CLI from here: http://docs.spring.io/spring-boot/docs/current/reference/htmlsingle/#getting-started-installing-the-cli
'''

import argparse
import distutils.spawn
import os
import sys
import subprocess


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('project_name', help="The name of the project to kick off")
    parser.add_argument('-n', '--dry-run', action='store_true', default=False, help="Dry run")
    return parser.parse_args()

def _check_tool(toolname):
    executable = distutils.spawn.find_executable(toolname)
    return bool(executable)

def main():
    options = parse_args()

    print "Initializing project {}".format(options.project_name)
    if os.path.exists(options.project_name):
        print "Project directory '{}' already exists. Delete or provide a different project name to continue. Exiting"
        sys.exit(2)
    print "Checking that all necessary tools are installed"

    tools = ['yo', 'node', 'npm', 'java', 'gradle', 'spring']
    missing_tools = []
    for tool in tools:
        present = _check_tool(tool)
        if not present:
            missing_tools.append(tool)

    if len(missing_tools) > 0:
        print "Missing the following tools: {}".format(missing_tools)
        print "Exiting"
        sys.exit(1)

    print "All tools installed. Initializing project"
    commands = [
        'mkdir {}'.format(options.project_name),
        'cd {name} && mkdir {name}-ui && cd {name}-ui && yo react-webpack'.format(name=options.project_name),
        'cd {name} && spring init --build=gradle --dependencies=web,websocket,integration,aop,actuator,cloud-config,remote-shell {name}-rest'.format(name=options.project_name),
        'cd {name} && git init && touch README.md && git add . && git commit -m "Initial commit"'.format(name=options.project_name)
    ]

    for command in commands:
        if options.dry_run:
            print command
        else:
            retval = subprocess.call(command, shell=True)
            if retval != 0:
                print "Command failed, aborting"
                sys.exit(retval)

    
if __name__ == '__main__':
    main()
