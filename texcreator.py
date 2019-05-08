# -*- coding: utf-8 -*-

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
configdir = filedir+"/configs"
print configdir
sys.path.append(configdir)



## class texcreator

class texCreator:
    # some lists with different parts of the LaTex-file
    documentClass = []
    packages = []
    tocSettings = []
    biblio = []
    title = []
    color = []
    commands = []
    hypersetup = []
    language = []
    institude = ["\\iflanguage{english}{\\institute{Institute of Experimental Particle Physics (ETP)}}{\\institute{Institut für Experimentelle Teilchenphysik (ETP)}}"]
    begin = ["\\begin{document}\n\n\n"]
    titleFrame = []
    frames = []
    end = ["\\end{document}"]

    complete = []

    workpath = ""
    outFile = "slides.tex"
    inputDirs = []
    addInputDirs = []

    style = "1Plot"
    noCompile = False
    titleImage = "nologo"
    titleLogo = "nologo"


    # initializes a new class and sets options, that are defined in a config file
    def __init__(self, config):
        # import the config file
        cfg = __import__(config)

        self.documentClass = cfg.getDocumentClass()
        self.packages = cfg.getPackages()
        self.tocSettings = cfg.getTOCSettings()
        self.biblio = cfg.getBiblio()
        self.title = cfg.getTitle()
        self.color = cfg.getColor()
        self.commands = cfg.getCommands()
        self.hypersetup = cfg.getHypersetup()

        if cfg.getLanguage():
            self.language = ["\\selectlanguage{english}\n\n"]
            #self.begin.append("\\selectlanguage{english}")
        else:
            self.language = ["\\selectlanguage{ngerman}\n\n"]
            #self.begin.append("\\selectlanguage{ngerman}")

        if cfg.getTitleFrame():
            self.titleFrame = ["\\begin{frame}\n\\titlepage\n\\end{frame}\n"]

        self.inputDirs = cfg.getInputDirs()

        # get paths n stuff
        self.workpath = cfg.getOutPath()
        self.outFile = cfg.getOutput()
        self.style = cfg.getStyle()
        #self.titleImage = cfg.getTitleImage()
        #self.titleLogo = cfg.getTitleLogo()

    def addLists(self):
        for d in [self.documentClass,self.packages,self.tocSettings,self.biblio,self.title,self.color,self.commands,self.hypersetup,self.language,self.institude,self.begin,self.frames,self.end]:
            if type(d)==str:
                print d
        self.complete = self.documentClass+self.packages+self.tocSettings+self.biblio+self.title+self.color+self.commands+self.hypersetup+self.language+self.institude+self.begin+self.titleFrame+self.frames+self.end

    def createTexFile(self):
        self.writeAll(self.complete, self.outFile)

    def compileTex(self):
        scriptPath = self.workpath + "compileTex.sh"
        with open(scriptPath,"w") as shellscript:
            shellscript.write("#!/bin/bash\n")
            shellscript.write("pdflatex {}".format(self.outFile))
        st = os.stat(scriptPath)
        os.chmod(scriptPath, st.st_mode | stat.S_IEXEC)
        os.chdir(self.workpath)
        subprocess.call(scriptPath)

    def printAll(frameList):
        for s in frameList:
            print s

    def writeAll(self,frameList, outFile="slides.tex"):
        with open(outFile,"w") as texfile:
            for frame in frameList:
                texfile.write(frame)
        print "Created LaTex source file {} with all frames".format(outFile)
