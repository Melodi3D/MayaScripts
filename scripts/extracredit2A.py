# Melodi Extra Credit Script #2
# Control Object Offset Grp

# Importing Maya Commands
import maya.cmds as cmds

# Grabs selection
selection = cmds.ls(orderedSelection=True)

# Stores selection under control variable
control = selection[0]

# Makes an Offset grp
offset_grp = cmds.group(empty=True, name=control + "_offset_grp")

# Matches offset grp to the control
cmds.matchTransform(offset_grp, control)

# Matches offset grp to the control
cmds.parent(control, offset_grp)
