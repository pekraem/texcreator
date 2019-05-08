print "usepackages imported!"

def defaultPackages(templatepath):
    packages = ["\\usepackage[utf8]{inputenc}\n",
                "\\usepackage[T1]{fontenc}\n",
                "\\usepackage{microtype}\n",
                "\\usepackage{}\n".format("{"+templatepath+"/beamerthemekit}"),
                #"\\usepackage{}\n".format("{"+templatepath+"/beamerthemekitwide}"),
                "\\usepackage{amsmath}\n",
                "\\usepackage{amsfonts}\n",
                "\\usepackage{amssymb}\n",
                "\\usepackage{siunitx}\n\\sisetup{range-units = single, range-phrase = {-}, separate-uncertainty = true,multi-part-units=brackets, product-units=brackets, locale=US, detect-weight=true, binary-units=true}\n",
                "\\usepackage{color}\n",
                "\\usepackage{todonotes}\n",
                "\\presetkeys{todonotes}{inline}{}\n",
                "\\usepackage{booktabs}\n",
                "\\usepackage{listings}\n",
                "\\usepackage{parnotes}\n",
                "\\usepackage{xspace}\n",
                "\\usepackage{multirow}\n",
                "\\usepackage{hyperref}\n"]
    return packages

