### Tools for running the texCreator

## import some stuff
import os


##some functions

# searches all files of type 'filetype' in each path in pathList and returns a list of lists with filenames
def getPlotFromPaths(pathList, filetype=".png"):
    listOfPlotLists = []
    for path in pathList:
        if not os.path.isdir(path):
            print "{} does not exist!\n".format(path)
        else:
            plotList = []
            for filename in os.listdir(path):
                if not path.endswith("/"): path+="/"
                if filename.endswith(filetype):
                    plotList.append(str(path+filename))
            plotList.sort()
            listOfPlotLists.append(plotList)
    return listOfPlotLists

# creates a list with every plot as an own LaTex include statement
def simpleInclude(listOfPlotLists, width=0.9):
    inclGraphList = []
    for plotList in listOfPlotLists:
        for plot in plotList:
            inclGraphList.append(str("\\includegraphics[width={}\\textwidth]{}\\\\".format(width,str("{"+plot+"}"))))
#    print inclGraphList
    return inclGraphList

def include2Plots(listOfPlotLists, width=0.49):
    completeList=[]
    inclGraphList=[]
    indexList=[]
    i=0
    for l in listOfPlotLists:
        completeList+=l
    while (len(indexList)!=len(completeList)/2):
        i+=1
        indexList.append([i-1,i])
        i+=1
    for d in indexList:
        inclGraphList.append(str("\\includegraphics[width={}\\textwidth]{}\n\t\\includegraphics[width={}\\textwidth]{}\\\\".format(width,str("{"+completeList[d[0]]+"}"),width,str("{"+completeList[d[1]]+"}"))))
    if len(completeList)%2!=0:
        inclGraphList.append(str("\\includegraphics[width={}\\textwidth]{}\\\\".format(width,str("{"+completeList[-1]+"}"))))
    return inclGraphList
    
# creates a list with LaTex include statements with 2 plots besides from 2 different lists.
# e.g. normal and logarithmic plot besides
def include2PlotsFrom2Lists(listOfPlotLists, w1=0.49, w2=0.49, i=0, j=1):
    inclGraphList = []
    orderedList = []
    while len(orderedList)<len(listOfPlotLists[i]):
        for p1 in listOfPlotLists[i]:
            for p2 in listOfPlotLists[j]:
                #if p1.split("/")[-1]==p2.split("/")[-1]:
                    orderedList.append(p2)
    for p1, p2 in zip(listOfPlotLists[i],orderedList):
        inclGraphList.append(str("\\includegraphics[width={}\\textwidth]{}\n\t\\includegraphics[width={}\\textwidth]{}\\\\".format(w1,str("{"+p1+"}"),w2,str("{"+p2+"}"))))
    return inclGraphList

def createBeamerFrames(inclGraphList):
    frameList = []
    for incl in inclGraphList:
        frameList.append("\\begin{frame}\n\\begin{center}\n\t"+incl+"\n\\end{center}\n\\end{frame}\n\n")
    return frameList

def getFrames(sourcePathList,style):
    listOfPlotLists = getPlotFromPaths(sourcePathList)
    # check how the plots shall be included and do so
    if style=="1Plot":
        inclGraphList = simpleInclude(listOfPlotLists)
    elif style=="2Plot2List":
        inclGraphList = include2PlotsFrom2Lists(listOfPlotLists)
    elif style=="2Plot":
        inclGraphList = include2Plots(listOfPlotLists)

    # maybe include captions here later
    # inclGraphList = texTools.addCaptions(inclGraphList)

    # build beamer frames
    frames = createBeamerFrames(inclGraphList)
    return frames

