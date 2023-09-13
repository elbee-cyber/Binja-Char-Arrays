# Inspiration
Make the current community plugin better.

# Software Description

# Software Procedure
1. Identify potential stack variables
2. Load user settings
3. Go through checks and save confidence scores
4. Render based on user settings

# Software Design
### Data structures

likely_vars (list)
size_table (dict) (var_name:size)

# Identify (S1)
My old plugin is lacking in all areas and not very efficient. The problem is it only saves void types to analyze, and the analyzing process only does the following checks to determine if the type is a char array.
- See if the variable is an argument in any calling function
It does this by listing function.callees and checking for the variable name in its tokens.
This misses many successful cases and this simple check in of itself does not inspire a lot of confidence.


Identification here will be changed to only identify potential variables and not actually analyze them, this will be done in later, segmented checks, which check for different characteristics.

A variable will be added to the identificaiton list if it is of any type and has a size larger than one byte.

# User settings (2)
A UI menu that allows the user to disable/enable heuristic checks, edit verbosity (disable pop-ups), display comments based on confidence and set a threshold for type replacement based on confidence. Default settings should be reasonable. Load user settings for further program execution. Update size table.

# Analyzing and Heuristic Checks (3)
The checks include, in order of confidence of detection:
- [x] Use in string functions
- [x] String literals (Not needed, binja will render using builtin strcpy for the literal, covered by above test)
	- [x] https://fh6q6ixevu.joplinusercontent.com/shares/2kw52rS0BoQVTgdtOV8VmS
- [ ] Access by index
	- [ ] Win4 can be used to test
- [ ] Use in stdio functions with file streams
- [ ] Use in functions with file descriptors
- [ ] Size is bigger than type's max size
- [ ] Null terminator
- [ ] Is void

A positive case will likely result in multiple heuristic checks passing

Checks will be executed in order until all checks have been executed or a var's confidence exceeds 100%. Whichever comes first. Heuristic checks will be made on all vars_identified. Progress bar based on var being checked out of possible_vars

# Render (4)
Add possible_vars into likely_vars based on confidence settings. Update binaryview. Execute user settings. Display pop up with information.

## Afterwards
- System to catch failed tests
- Test on lots of binaries, document results
- Create and push release
- Notify Vector35
- Blog post
