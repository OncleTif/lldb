import lldb
import os.path

def import_conf(debugger, command, result, internal_dict):
	s = str(debugger.GetSelectedTarget()) + ".config"
	if os.path.isfile(s):
		debugger.HandleCommand("command source " + s);
		return
	if os.path.isfile("commandes"):
		debugger.HandleCommand("command source commandes");
		return

def __lldb_init_module(debugger, dict):
	debugger.HandleCommand('command script add -f import_conf.import_conf import_config');
	debugger.HandleCommand('import_config');
