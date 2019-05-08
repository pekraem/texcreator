def biblio():
    bib = ['''% bibliography
\\usepackage[style=numeric, backend=biber, sorting=ynt]{biblatex}
\\addbibresource{bibliography.bib}
\\beamertemplatenavigationsymbolsempty''']
    return bib

#TODO
# write bibliofunction with parameters
