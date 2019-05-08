print "Commands imported!"

def usefulCommands():
    cmds = ["% Define some commands\n% arrows\n",
            "\\newcommand{\\rar}{\\ensuremath{\\rightarrow}\\xspace}\n",
            "\\newcommand{\\Rar}{\\ensuremath{\\Rightarrow}\\xspace}\n\n",
            "% particle physics\n",
            "\\newcommand{\\ttbar}{t$\\overline{\\text{t}}$\\xspace }\n",
            "\\newcommand{\\boldttbar}{\\textbf{t}$\\overline{\\textbf{t}}$\\xspace}\n",
            "\\newcommand{\\ttbarH}{t$\overline{\\text{t}}$H\\xspace }\n",
            "\\newcommand{\\boldttbarH}{\\textbf{t}$\\overline{\\textbf{t}}$\\textbf{H}\\xspace}\n",
            "\\newcommand{\\bbbar}{b$\\overline{\\text{b}}$\\xspace }\n",
            "\\newcommand{\\pT}{${p_{T}}$\\xspace}\n",
            "\\newcommand{\\Htobb}{H$\\to $ \\bbbar}\n",
            "\\def\\nitem{\\begin{itemize}}\n",
            "\\def\\xitem{\\end{itemize}}\n",
            "\\newcommand{\\beq}{\\begin{equation}}\n",
            "\\newcommand{\\eeq}{\\end{equation}}\n\n\n"]
    return cmds
