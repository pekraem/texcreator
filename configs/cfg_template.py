# -*- coding: utf-8 -*-

### configuration for LaTex Creator

## import some stuff
import os
import sys

# local imports
filedir = os.path.dirname(os.path.realpath(__file__))
basedir = os.path.dirname(filedir)
sys.path.append(basedir)

# LaTex code
import usepackage
import command
import hypersetup
import tocSettings
import biblio
import color
import texTools


## configs
language_engl   = True

documentclass   = "beamer"
fontSize        = 18
templatepath    = basedir+"/output/templates"
packages        = usepackage.defaultPackages(templatepath)
tocSettings     = [] #tocSettings.defaultTOC()
biblio          = [] #biblio.biblio()

title = {   "image"     : "nologo",
            "logo"      : "nologo",
            "title"     : "some plots",
            "subtitle"  : "",
            "author"    : "Peter Kraemer",
        }
titleFrame      = True

color           = color.KITColor()
cmds            = command.usefulCommands()
hypersetup      = hypersetup.hypersetup()

style           = "2Plot"
# style options are (at the moment):
    # "1Plot"       : creates slides with only 1 plot on each frame
    # "2Plot"       : creates slides with 2 plots on each frame (l1[p1]*l1[p2]...ln[p(n-1)]*ln[pn]))
    # "2Plot2List"  : creates slides with 2 plots on each frame (l1[p1]+l2[p1]...l1[pn]*l2[pn])

# some python magic for correct stringhandling...
for x in title:
    title[x] = "{"+title[x]+"}"


## paths
path    = "/home/pkraemer/Documents/STXS_Plots/002_Stage0_firstPlots/"
p1      = "controlPlots/plots"
p2      = "controlPlots_Log/plots"

# sourcePathList is the List with the important source paths, the others are only to build it
sourcePathList = [path+p1, path+p2]

# path to the directory where the outputfiles are created
outPath = basedir + "/output/"
outFileName = "slides.tex"


## functions to return configs to texcreator class
def getDocumentClass():
    doc = ["\\documentclass[{}pt]{}".format(fontSize,"{"+documentclass+"}")]
    return doc

def getPackages():
    return packages

def getTOCSettings():
    return tocSettings

def getBiblio():
    return biblio

def getColor():
    return color

def getCommands():
    return cmds

def getHypersetup():
    return hypersetup

def getTitle():
    title_str = '''
\\titleimage{image}
\\titlelogo{logo}
\\title{title}
\\subtitle{subtitle}
\\author{author}
'''.format(**title)
    return [title_str]

def getSources():
    return sourcePathList

def getOutPath():
    return outPath

def getOutFile():
    return outFileName

def getOutput():
    return outPath+outFileName

def getLanguage():
    return language_engl

def getInputDirs():
    return sourcePathList

def getStyle():
    return style

def getTitleFrame():
    return titleFrame

# create and return frames with all plots given as input
def getFrames():
    listOfPlotLists = texTools.getPlotsFromPaths(sourcePathList)
    # check how the plots shall be included and do so
    if style=="1Plot":
        inclGraphList = texTools.simpleInclude(listOfPlotLists)
    elif style=="2Plot2List":
        inclGraphList = texTools.include2PlotsFrom2Lists(listOfPlotLists)
    elif style=="2Plot":
        inclGraphList = texTools.include2Plots(listOfPlotLists)

    # maybe include captions here later
    # inclGraphList = texTools.addCaptions(inclGraphList)

    # build beamer frames
    frames = texTools.createBeamerFrames(inclGraphList)
    return frames()
