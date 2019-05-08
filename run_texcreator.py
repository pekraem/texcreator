### skript to create tex code with include plots

## import stuff
import os
import subprocess
import stat
import optparse
import sys

# local imports
filedir = os.path.dirname(os.path.realpath(__file__))
basedir = os.path.dirname(filedir)
sys.path.append(basedir)

import texcreator
import texTools


## parser configuration
usage = "usage=%prog [options]\n"
usage += "USE: python texcreator.py -c FILE -o FILE -p DIR -i DIR --addInput --compile"

parser = optparse.OptionParser(usage=usage)

parser.add_option("-c", "--configFile", dest="configPath", default="cfg_template",
        help="Path to the personal configuration file", metavar="configPath")

parser.add_option("-o", "--outputFile", dest="outputFile",
        help="Path to the .tex file, that will be created and compiled", metavar="outputFile")

parser.add_option("-i", "--inputDir", dest="inputDir",
        help="Path to the inputdirectory, all files (of certain type) will be included in texFile", metavar="inputDir")

parser.add_option("-p", "--outputPath", dest="outputPath",
        help="Path where .tex files are created and compiled", metavar="outputPath")

parser.add_option("--noCompile", dest="noCompile", action="store_true", default=False,
        help="no .pdf will be created, only the .tex", metavar="noCompile")

parser.add_option("--titleImage", dest="titleImage",
        help="Path to image that shall be used as title, default is no image", metavar="titleImage")

parser.add_option("--titleLogo", dest="titleLogo",
        help="Path to titleLogo, default is no logo", metavar="titleLogo")

parser.add_option("--addInput", dest="addInput",
        help="adds an additional path to the inputPathList", metavar="addInput")

(options, args) = parser.parse_args()


TC = texcreator.texCreator(options.configPath)
if options.outputPath:
    TC.workpath = options.outputPath
if options.outputFile:
    TC.outFile = TC.workpath + options.outputFile
if options.inputDir:
    TC.inputDirs = options.inputDir
if options.addInput:
    TC.inputDirs.append(options.addInput)
if options.noCompile:
    TC.noCompile = True
if options.titleImage:
    TC.titleImage = options.titleImage
if options.titleLogo:
    TC.titleLogo = options.titleLogo

TC.frames = texTools.getFrames(TC.inputDirs,TC.style)
TC.addLists()
TC.createTexFile()
if not TC.noCompile:
    TC.compileTex()
