---
layout: tikzimage
title: This is a test title
tags: ml tikz
image: rn_220_decay_chain.png
date: 2020-07-14
---

header information here

```tex
\newcommand{\nucl}[2]{${}^{#2}{\text{#1}}$}
\begin{tikzpicture}[
    nucleus/.style={scale=.7,thick,draw,rectangle,minimum height=1cm,minimum width=2cm,align=flush center,fill=gray!10},
        decay/.style={thick,->,align=flush center,color=blue!80,font=\tiny}
    ]
    \node[nucleus] (Th228) {\nucl{Th}{228} \\ 1.91 yr};
    \node[nucleus,below=6mm of Th228] (Ra224) {\nucl{Ra}{224} \\3.66 d};
    \node[nucleus,below=6mm of Ra224] (Rn220) {\nucl{Rn}{220} \\55.4 s};
    \node[nucleus,below=6mm of Rn220] (Po216) {\nucl{Po}{216} \\0.145 ns};
    \node[nucleus,below=6mm of Po216] (Pb212) {\nucl{Pb}{212} \\10.6 h};
    \node[nucleus,right=12mm of Po216] (Bi212) {\nucl{Bi}{212} \\ 60.5 m};
    \node[nucleus,below=6mm of Bi212] (Tl208) {\nucl{Tl}{208} \\ 3.05 m};
    \node[nucleus,right=36mm of Rn220] (Po212) {\nucl{Po}{212} \\ 60.5 m};
    \node[nucleus,below=6mm of Po212] (Pb208) {\nucl{Pb}{208} \\ 3.05 m};
    \draw[decay] (Th228) -- node [right] { $\alpha$ \tiny 5520keV}  (Ra224);
    \draw[decay] (Ra224) -- node [right] { $\alpha$ \\ \tiny 5520keV}  (Rn220);
    \draw[decay] (Rn220) -- node [right] { $\alpha$ \\ \tiny 5520keV}  (Po216);
    \draw[decay] (Po216) -- node [right] { $\alpha$ \\ \tiny 5520keV}  (Pb212);
    \draw[decay] (Po212) -- node [right] { $\alpha$ \\ \tiny 5520keV}  (Pb208);
    \draw[decay] (Bi212) -- node [right] { $\alpha$ \\ \tiny 5520keV}  (Tl208);
    \draw[decay] (Pb212.east) -- node [below] { $\beta$ \\ \tiny 570keV}  (Bi212.west);
    \draw[decay] (Bi212.east) -- node [below] { $\beta$ \\ \tiny 570keV}  (Po212.west);
    \draw[decay] (Tl208.east) -- node [below] { $\beta$ \\ \tiny 570keV}  (Pb208.west);
\end{tikzpicture}

```
