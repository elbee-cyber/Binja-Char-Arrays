from binaryninja import *
from .modules import settings
from .modules import strfunc
from .modules import accIndex
import logging

size_table = {}

logging.disable(logging.WARNING)

def analyze(bv,function):
	var_table = {}
	for v in function.stack_layout:
		if (v.last_seen_name[:4] == "var_" or v.last_seen_name[:3] == "buf") and type(v.type) != types.PointerType:
			var_table[v.last_seen_name] = 0

	if Settings().get_bool("chararr.Heuristics.strfunc"):
		var_table = strfunc.search(bv,function,var_table)

	if Settings().get_bool("chararr.Heuristics.indexAccess"):
		var_table = accIndex.search(bv,function,var_table)

	log_alert(var_table) # for debugging


PluginCommand.register_for_function("Analyze Char Arrays","Analyze binaryview for incorrectly declared character arrays.", analyze)
