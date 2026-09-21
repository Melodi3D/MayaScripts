# Melodi Extra Credit Script #2
# World Offset Grp Script

# Imports Maya Commands
import maya.cmds as cmds

# Grabs selection
selection = cmds.ls(orderedSelection=True)

# Stores selection under a variable for controls
cv_selection = selection[0]

# Makes a offset grp named world_offset_grp
world_offset_grp = cmds.group(empty=True, name=cv_selection + "_world_offset_grp")

# Match offset grp to control
cmds.matchTransform(world_offset_grp, cv_selection)

# Freezes transforms on grp before parenting
cmds.makeIdentity(world_offset_grp, apply=True, translate=True, rotate=True, scale=True)

# Parent controls under offset group
cmds.parent(cv_selection, world_offset_grp)

# Freezes transforms on grp before parenting
cmds.makeIdentity(cv_selection, apply=True, translate=True, rotate=True, scale=True)
