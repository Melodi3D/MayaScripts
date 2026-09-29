# Match Script Extra Credit by Melodi

import maya.cmds as cmds

# Select driver and driven

selection = cmds.ls(orderedSelection=True)

# Index, Driver Driven

driver = selection[0]

driven = selection[1]

# Hint: You can make your parent constraint a variable

constraint = cmds.parentConstraint(driver, driven, maintainOffset=False)

# Extra Credit Section (Delete Parent Constraint)

cmds.delete(constraint)

# Alternatively, cmds.delete(driven, cn=True) can delete constraints connected to the driven object

# While cmds.delete(constraint) deletes the specific constraint created.
