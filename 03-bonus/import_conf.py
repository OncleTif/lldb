import lldb
import os.path

def import_conf(debugger, command, result, internal_dict):
    s = str(debugger.GetSelectedTarget()) + ".config"
    if os.path.isfile(s):
        debugger.HandleCommand('script print "\033[32m[Loading ' + s + ']\033[0m"')
        debugger.HandleCommand("command source " + s);
        return
    if os.path.isfile("commandes"):
        debugger.HandleCommand('script print "\033[32m[Loading \"commandes\"]\033[0m"')
        debugger.HandleCommand("command source commandes");
        return

def __lldb_init_module(debugger, dict):
    debugger.HandleCommand('command script add -f import_conf.import_conf import -h "This command detect a <file>.config file or commandes file and execute its commands');
