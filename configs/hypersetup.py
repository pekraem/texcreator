# -*- coding: utf-8 -*-

print "hypersetup imported!"

def hypersetup():
    hset = ['''\\hypersetup{
    bookmarks=true,         % show bookmarks bar?
    unicode=false,          % non-Latin characters in Acrobat’s bookmarks
    pdftoolbar=true,        % show Acrobat’s toolbar?
    pdfmenubar=true,        % show Acrobat’s menu?
    pdffitwindow=false,     % window fit to page when opened
    pdfstartview={FitH},    % fits the width of the page to the window
    pdftitle={My title},    % title
    pdfauthor={Author},     % author
    pdfsubject={Subject},   % subject of the document
    pdfcreator={Creator},   % creator of the document
    pdfproducer={Producer}, % producer of the document
    pdfkeywords={keyword1, key2, key3}, % list of keywords
    pdfnewwindow=true,      % links in new PDF window
    colorlinks=true,       % false: boxed links; true: colored links
    linkcolor=KIT-Rot,          % color of internal links (change box color with linkbordercolor)
    citecolor=KIT-MaiGruen,        % color of links to bibliography
    filecolor=KIT-Lila,      % color of file links
    urlcolor=KIT-Blau,         % color of external links
    final=true
}''']
    return hset
