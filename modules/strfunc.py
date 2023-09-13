from binaryninja import *

def search(bv,function,var_table):
	passed = []
	for c in function.call_sites:
		try:
			symbol = bv.get_symbol_at(c.mlil.operands[1].constant)
			if symbol and (symbol.type == SymbolType.ImportedFunctionSymbol or symbol.type == SymbolType.ImportAddressSymbol):
				if "str" in symbol.full_name:
					for reg in c.mlil.operands[2]:
						if reg.operation == MediumLevelILOperation.MLIL_VAR_SSA or reg.operation == MediumLevelILOperation.MLIL_VAR and type(reg.value) == StackFrameOffsetRegisterValue:
							stack_var = function.get_stack_var_at_frame_offset(reg.value.value,c.address)
							if stack_var.name not in passed:
								passed.append(stack_var.name)
								var_table[stack_var.name] += 1
							else:
								continue
		except Exception as e:
			log_info(e)
			continue
	return var_table
