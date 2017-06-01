# -*- coding: utf-8 -*-
# DO NOT EDIT THIS FILE
# This file was automatically generated by Natron PyPlug exporter version 10.

# Hand-written code should be added in a separate file named EdgeBlurExt.py
# See http://natron.readthedocs.org/en/master/groups.html#adding-hand-written-code-callbacks-etc
# Note that Viewers are never exported

import NatronEngine
import sys

# Try to import the extensions file where callbacks and hand-written code should be located.
try:
    from EdgeBlurExt import *
except ImportError:
    pass

def getPluginID():
    return "fr.inria.EdgeBlur"

def getLabel():
    return "EdgeBlur"

def getVersion():
    return 1

def getGrouping():
    return "Filter"

def getPluginDescription():
    return "Blur the image where there are edges in the alpha/matte channel."

def createInstance(app,group):
    # Create all nodes in the group

    # Create the parameters of the group node the same way we did for all internal nodes
    lastNode = group

    # Create the user parameters
    lastNode.controlsPage = lastNode.createPageParam("controlsPage", "Controls")
    param = lastNode.createBooleanParam("Blur1NatronOfxParamProcessR", "R")
    param.setDefaultValue(True)
    param.restoreDefaultValue()

    # Add the param to the page
    lastNode.controlsPage.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setAnimationEnabled(False)
    lastNode.Blur1NatronOfxParamProcessR = param
    del param

    param = lastNode.createBooleanParam("Blur1NatronOfxParamProcessG", "G")
    param.setDefaultValue(True)
    param.restoreDefaultValue()

    # Add the param to the page
    lastNode.controlsPage.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(False)
    param.setAnimationEnabled(False)
    lastNode.Blur1NatronOfxParamProcessG = param
    del param

    param = lastNode.createBooleanParam("Blur1NatronOfxParamProcessB", "B")
    param.setDefaultValue(True)
    param.restoreDefaultValue()

    # Add the param to the page
    lastNode.controlsPage.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(False)
    param.setAnimationEnabled(False)
    lastNode.Blur1NatronOfxParamProcessB = param
    del param

    param = lastNode.createBooleanParam("Blur1NatronOfxParamProcessA", "A")
    param.setDefaultValue(True)
    param.restoreDefaultValue()

    # Add the param to the page
    lastNode.controlsPage.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(False)
    param.setAnimationEnabled(False)
    lastNode.Blur1NatronOfxParamProcessA = param
    del param

    param = lastNode.createBooleanParam("externalMatte", "External Matte")

    # Add the param to the page
    lastNode.controlsPage.addParam(param)

    # Set param properties
    param.setHelp("Use the edges from the Matte input instead of the alpha channel of the source image.")
    param.setAddNewLine(True)
    param.setAnimationEnabled(True)
    lastNode.externalMatte = param
    del param

    param = lastNode.createDoubleParam("size", "Size")
    param.setMinimum(0, 0)
    param.setDisplayMinimum(0, 0)
    param.setDisplayMaximum(100, 0)
    param.setDefaultValue(3, 0)
    param.restoreDefaultValue(0)

    # Add the param to the page
    lastNode.controlsPage.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setAnimationEnabled(True)
    lastNode.size = param
    del param

    param = lastNode.createChoiceParam("filter", "Filter")
    param.setDefaultValue(4)
    param.restoreDefaultValue()

    # Add the param to the page
    lastNode.controlsPage.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setAnimationEnabled(False)
    lastNode.filter = param
    del param

    param = lastNode.createBooleanParam("cropToFormat", "Crop To Format")
    param.setDefaultValue(True)
    param.restoreDefaultValue()

    # Add the param to the page
    lastNode.controlsPage.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(False)
    param.setAnimationEnabled(False)
    lastNode.cropToFormat = param
    del param

    param = lastNode.createDoubleParam("edgeMult", "Edge Mult")
    param.setMinimum(0, 0)
    param.setMaximum(2147483647, 0)
    param.setDisplayMinimum(0.1, 0)
    param.setDisplayMaximum(10, 0)
    param.setDefaultValue(2, 0)
    param.restoreDefaultValue(0)

    # Add the param to the page
    lastNode.controlsPage.addParam(param)

    # Set param properties
    param.setHelp("Sharpness of the borders of the blur area.")
    param.setAddNewLine(True)
    param.setAnimationEnabled(True)
    lastNode.edgeMult = param
    del param

    param = lastNode.createBooleanParam("Merge1maskInvert", "Invert Mask")

    # Add the param to the page
    lastNode.controlsPage.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setAnimationEnabled(False)
    lastNode.Merge1maskInvert = param
    del param

    param = lastNode.createDoubleParam("Blur1mix", "Mix")
    param.setMinimum(0, 0)
    param.setMaximum(1, 0)
    param.setDisplayMinimum(0, 0)
    param.setDisplayMaximum(1, 0)
    param.setDefaultValue(1, 0)
    param.restoreDefaultValue(0)

    # Add the param to the page
    lastNode.controlsPage.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setAnimationEnabled(True)
    lastNode.Blur1mix = param
    del param

    # Refresh the GUI with the newly created parameters
    lastNode.setPagesOrder(['controlsPage', 'Node', 'Settings'])
    lastNode.refreshUserParamsGUI()
    del lastNode

    # Start of node "EdgeDetect1"
    lastNode = app.createNode("eu.cimg.EdgeDetect", 4, group)
    lastNode.setScriptName("EdgeDetect1")
    lastNode.setLabel("EdgeDetect1")
    lastNode.setPosition(908, 181)
    lastNode.setSize(80, 34)
    lastNode.setColor(0.8, 0.5, 0.3)
    groupEdgeDetect1 = lastNode

    param = lastNode.getParam("NatronOfxParamProcessR")
    if param is not None:
        param.setValue(False)
        del param

    param = lastNode.getParam("NatronOfxParamProcessG")
    if param is not None:
        param.setValue(False)
        del param

    param = lastNode.getParam("NatronOfxParamProcessB")
    if param is not None:
        param.setValue(False)
        del param

    param = lastNode.getParam("NatronOfxParamProcessA")
    if param is not None:
        param.setValue(True)
        del param

    param = lastNode.getParam("multiChannel")
    if param is not None:
        param.set("Separate")
        del param

    param = lastNode.getParam("blurSize")
    if param is not None:
        param.setValue(3, 0)
        del param

    del lastNode
    # End of node "EdgeDetect1"

    # Start of node "Gamma1"
    lastNode = app.createNode("net.sf.openfx.GammaPlugin", 2, group)
    lastNode.setScriptName("Gamma1")
    lastNode.setLabel("Gamma1")
    lastNode.setPosition(895, 285)
    lastNode.setSize(104, 34)
    lastNode.setColor(0.48, 0.66, 1)
    groupGamma1 = lastNode

    param = lastNode.getParam("NatronOfxParamProcessR")
    if param is not None:
        param.setValue(False)
        del param

    param = lastNode.getParam("NatronOfxParamProcessG")
    if param is not None:
        param.setValue(False)
        del param

    param = lastNode.getParam("NatronOfxParamProcessB")
    if param is not None:
        param.setValue(False)
        del param

    param = lastNode.getParam("NatronOfxParamProcessA")
    if param is not None:
        param.setValue(True)
        del param

    param = lastNode.getParam("value")
    if param is not None:
        param.setValue(2, 0)
        param.setValue(2, 1)
        param.setValue(2, 2)
        param.setValue(2, 3)
        del param

    del lastNode
    # End of node "Gamma1"

    # Start of node "Blur1"
    lastNode = app.createNode("net.sf.cimg.CImgBlur", 4, group)
    lastNode.setScriptName("Blur1")
    lastNode.setLabel("Blur1")
    lastNode.setPosition(676, 349)
    lastNode.setSize(104, 34)
    lastNode.setColor(0.8, 0.5, 0.3)
    groupBlur1 = lastNode

    param = lastNode.getParam("size")
    if param is not None:
        param.setValue(3, 0)
        param.setValue(3, 1)
        del param

    param = lastNode.getParam("enableMask_Mask")
    if param is not None:
        param.setValue(True)
        del param

    del lastNode
    # End of node "Blur1"

    # Start of node "Shuffle1"
    lastNode = app.createNode("net.sf.openfx.ShufflePlugin", 2, group)
    lastNode.setScriptName("Shuffle1")
    lastNode.setLabel("Shuffle1")
    lastNode.setPosition(768, 104)
    lastNode.setSize(104, 34)
    lastNode.setColor(0.6, 0.24, 0.39)
    groupShuffle1 = lastNode

    param = lastNode.getParam("outputComponents")
    if param is not None:
        param.set("Alpha")
        del param

    del lastNode
    # End of node "Shuffle1"

    # Start of node "Dot1"
    lastNode = app.createNode("fr.inria.built-in.Dot", 1, group)
    lastNode.setScriptName("Dot1")
    lastNode.setLabel("Dot1")
    lastNode.setPosition(721, 114)
    lastNode.setSize(15, 15)
    lastNode.setColor(0.7, 0.7, 0.7)
    groupDot1 = lastNode

    del lastNode
    # End of node "Dot1"

    # Start of node "Source"
    lastNode = app.createNode("fr.inria.built-in.Input", 1, group)
    lastNode.setScriptName("Source")
    lastNode.setLabel("Source")
    lastNode.setPosition(676, 50)
    lastNode.setSize(104, 34)
    lastNode.setColor(0.3, 0.5, 0.2)
    groupSource = lastNode

    del lastNode
    # End of node "Source"

    # Start of node "Output1"
    lastNode = app.createNode("fr.inria.built-in.Output", 1, group)
    lastNode.setLabel("Output1")
    lastNode.setPosition(676, 430)
    lastNode.setSize(104, 34)
    lastNode.setColor(0.7, 0.7, 0.7)
    groupOutput1 = lastNode

    del lastNode
    # End of node "Output1"

    # Start of node "Mask"
    lastNode = app.createNode("fr.inria.built-in.Input", 1, group)
    lastNode.setScriptName("Mask")
    lastNode.setLabel("Mask")
    lastNode.setPosition(1084, 349)
    lastNode.setSize(104, 34)
    lastNode.setColor(0.3, 0.5, 0.2)
    groupMask = lastNode

    param = lastNode.getParam("optional")
    if param is not None:
        param.setValue(True)
        del param

    param = lastNode.getParam("isMask")
    if param is not None:
        param.setValue(True)
        del param

    del lastNode
    # End of node "Mask"

    # Start of node "Merge1"
    lastNode = app.createNode("net.sf.openfx.MergePlugin", 1, group)
    lastNode.setScriptName("Merge1")
    lastNode.setLabel("Merge1")
    lastNode.setPosition(895, 341)
    lastNode.setSize(104, 56)
    lastNode.setColor(0.3, 0.37, 0.776)
    groupMerge1 = lastNode

    param = lastNode.getParam("NatronOfxParamStringSublabelName")
    if param is not None:
        param.setValue("copy")
        del param

    param = lastNode.getParam("operation")
    if param is not None:
        param.set("copy")
        del param

    param = lastNode.getParam("bbox")
    if param is not None:
        param.set("A")
        del param

    param = lastNode.getParam("userTextArea")
    if param is not None:
        param.setValue("<Natron>(copy)</Natron>")
        del param

    del lastNode
    # End of node "Merge1"

    # Start of node "Switch1"
    lastNode = app.createNode("net.sf.openfx.switchPlugin", 1, group)
    lastNode.setScriptName("Switch1")
    lastNode.setLabel("Switch1")
    lastNode.setPosition(896, 104)
    lastNode.setSize(104, 34)
    lastNode.setColor(0.3, 0.37, 0.776)
    groupSwitch1 = lastNode

    param = lastNode.getParam("which")
    if param is not None:
        param.setValue(0, 0)
        del param

    del lastNode
    # End of node "Switch1"

    # Start of node "Matte"
    lastNode = app.createNode("fr.inria.built-in.Input", 1, group)
    lastNode.setScriptName("Matte")
    lastNode.setLabel("Matte")
    lastNode.setPosition(896, 51)
    lastNode.setSize(104, 34)
    lastNode.setColor(0.3, 0.5, 0.2)
    groupMatte = lastNode

    param = lastNode.getParam("optional")
    if param is not None:
        param.setValue(True)
        del param

    param = lastNode.getParam("isMask")
    if param is not None:
        param.setValue(True)
        del param

    del lastNode
    # End of node "Matte"

    # Now that all nodes are created we can connect them together, restore expressions
    groupEdgeDetect1.connectInput(0, groupSwitch1)
    groupGamma1.connectInput(0, groupEdgeDetect1)
    groupBlur1.connectInput(0, groupDot1)
    groupBlur1.connectInput(1, groupMerge1)
    groupShuffle1.connectInput(1, groupDot1)
    groupDot1.connectInput(0, groupSource)
    groupOutput1.connectInput(0, groupBlur1)
    groupMerge1.connectInput(1, groupGamma1)
    groupMerge1.connectInput(2, groupMask)
    groupSwitch1.connectInput(0, groupShuffle1)
    groupSwitch1.connectInput(1, groupMatte)

    param = groupEdgeDetect1.getParam("filter")
    group.getParam("filter").setAsAlias(param)
    del param
    param = groupEdgeDetect1.getParam("blurSize")
    group.getParam("size").setAsAlias(param)
    del param
    param = groupGamma1.getParam("value")
    param.setExpression("thisGroup.edgeMult.get()", False, 0)
    param.setExpression("thisGroup.edgeMult.get()", False, 1)
    param.setExpression("thisGroup.edgeMult.get()", False, 2)
    param.setExpression("thisGroup.edgeMult.get()", False, 3)
    del param
    param = groupBlur1.getParam("NatronOfxParamProcessR")
    group.getParam("Blur1NatronOfxParamProcessR").setAsAlias(param)
    del param
    param = groupBlur1.getParam("NatronOfxParamProcessG")
    group.getParam("Blur1NatronOfxParamProcessG").setAsAlias(param)
    del param
    param = groupBlur1.getParam("NatronOfxParamProcessB")
    group.getParam("Blur1NatronOfxParamProcessB").setAsAlias(param)
    del param
    param = groupBlur1.getParam("NatronOfxParamProcessA")
    group.getParam("Blur1NatronOfxParamProcessA").setAsAlias(param)
    del param
    param = groupBlur1.getParam("size")
    param.slaveTo(groupEdgeDetect1.getParam("blurSize"), 0, 0)
    param.slaveTo(groupEdgeDetect1.getParam("blurSize"), 1, 0)
    del param
    param = groupBlur1.getParam("cropToFormat")
    group.getParam("cropToFormat").setAsAlias(param)
    del param
    param = groupBlur1.getParam("mix")
    group.getParam("Blur1mix").setAsAlias(param)
    del param
    param = groupMerge1.getParam("maskInvert")
    group.getParam("Merge1maskInvert").setAsAlias(param)
    del param
    param = groupSwitch1.getParam("which")
    param.setExpression("thisGroup.externalMatte.get()", False, 0)
    del param

    try:
        extModule = sys.modules["EdgeBlurExt"]
    except KeyError:
        extModule = None
    if extModule is not None and hasattr(extModule ,"createInstanceExt") and hasattr(extModule.createInstanceExt,"__call__"):
        extModule.createInstanceExt(app,group)
