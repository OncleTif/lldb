import lldb

def init(debugger, command, result, internal_dict):
    debugger.HandleCommand('breakpoint set -name main')
    debugger.HandleCommand('run')

def __lldb_init_module(debugger, dict):
	debugger.HandleCommand('command script add -f init.init init')
