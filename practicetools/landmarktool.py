"""
Landmark Tool by Melodi (WIP)
"""
# Explanation:
# imports maya commands
from maya import cmds

# function for creating landmarks
def create_landmark(colors):
    #user selects faces

    selection = cmds.ls(sl=True, flatten=True)

    # error handling due to lack of selection
    if not selection:
        raise RuntimeError("Error: Nothing is selected")

    # error handling due to lack of faces in selection
    if not cmds.filterExpand(sm=34):
        raise RuntimeError("Error: There is a lack of faces selected")

    # error handling due to wrong colors
    for color in colors:
        if color < 0.0 or color > 1.0:
            raise RuntimeError("Error: Colors should be between 0.0 and 1.0 ")


    
    #selects selection

    cmds.select(selection)
    

    #creates landmark shader as a shader node, with lambert material

    landmark_shader = cmds.shadingNode("lambert", asShader=True)


    #assigns shader to the selected faces
    cmds.hyperShade(assign=landmark_shader)


    #sets the colors for the landmark shader to RGB values

    cmds.setAttr(

    f"{landmark_shader}.color",

    colors[0], colors[1], colors[2],

    type="double3")
