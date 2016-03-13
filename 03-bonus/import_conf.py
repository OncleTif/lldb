import lldb
import os.path

def import_conf(debugger, command, result, internal_dict):
    s = str(debugger.GetSelectedTarget()) + ".config"
    if os.path.isfile(s):
        debugger.HandleCommand("command source " + s)
        return
    if os.path.isfile("commandes"):
		with open("commandes") as f:
			for line in f:
				print line
				debugger.HandleCommand(str(line))
		return

def __lldb_init_module(debugger, dict):
    debugger.HandleCommand('command script add -f import_conf.import_conf import -h "This command detect a <file>.config file or commandes file and execute its commands');
