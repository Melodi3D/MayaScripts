"""
Landmark Tool by Melodi (WIP)
"""

from maya import cmds

def create_landmark(colors):
    #user selects faces

    selection = cmds.ls(sl=True, flatten=True)


    #selects selection

    cmds.select(selection)


    #creates landmark shader with lambert material

    landmark_shader = cmds.shadingNode(“lambert”, asShader=True)


    #assigns shader 

    cmds.hyperShade(assign=landmark_shader)





    #creates landmark shader colors

    cmds.setAttr(

    f”{landmark_shader}.color”,

    colors[0], colors[1], colors[2],

    type=“double3”)
