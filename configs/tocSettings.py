print "tocSettings imported!"

def defaultTOC():
    TOC = ['''% settings for making the table of contents less ugly
\\setbeamertemplate{section in toc}{\\inserttocsectionnumber\\ \\ ~\\inserttocsection
\\setbeamertemplate{subsection in toc}{\\qquad\\inserttocsectionnumber.\\inserttocsubsectionnumber\\ \\ ~\\inserttocsubsection\\\\ }''']
    return TOC
