---
layout: tikzimage
title: This is a test title
tags: ml tikz
image: rn_222_decay_chain.png
date: 2020-07-14
---

header information here

```tex
\newcommand{\nucl}[2]{${}^{#2}{\text{#1}}$}
\begin{tikzpicture}[
    nucleus/.style={scale=.7,thick,draw,rectangle,minimum height=1cm,minimum width=2cm,align=flush center,fill=gray!10,rounded corners},
        decay/.style={thick,->,align=flush center,color=blue!80,font=\tiny}
    ]
    \node[nucleus] (Ra226) {\nucl{Ra}{224} \\1620 y};
    \node[nucleus,below=6mm of Ra226] (Rn222) {\nucl{Rn}{222} \\55.4 s};
    \node[nucleus,below=6mm of Rn222] (Po218) {\nucl{Po}{218} \\0.145 ns};
    \node[nucleus,below=6mm of Po218] (Pb214) {\nucl{Pb}{214} \\10.6 h};
    \node[nucleus,right=12mm of Rn222] (Bi214) {\nucl{Bi}{214} \\ 60.5 m};
    \node[nucleus,below=6mm of Bi214] (Po214) {\nucl{Po}{214} \\ 3.05 m};
    \node[nucleus,below=6mm of Po214] (Pb210) {\nucl{Pb}{210} \\ 60.5 m};
    \node[nucleus,right=36mm of Rn222] (Bi210) {\nucl{Bi}{210} \\ 60.5 m};
    \node[nucleus,below=6mm of Bi210] (Po210) {\nucl{Po}{210} \\ 3.05 m};
    \node[nucleus,below=6mm of Po210] (Pb216) {\nucl{Pb}{216} \\ 3.05 m};
    \draw[decay] (Ra226) -- node [right] { $\alpha$ \\ 5520keV}  (Rn222);
    \draw[decay] (Rn222) -- node [right] { $\alpha$ \\ 5520keV}  (Po218);
    \draw[decay] (Po218) -- node [right] { $\alpha$ \\ 5520keV}  (Pb214);
    \draw[decay] (Bi214) -- node [right] { $\alpha$ \\ 5520keV}  (Po214);
    \draw[decay] (Po214) -- node [right] { $\alpha$ \\ 5520keV}  (Pb210);
    \draw[decay] (Bi210) -- node [right] { $\alpha$ \\ 5520keV}  (Po210);
    \draw[decay] (Po210) -- node [right] { $\alpha$ \\ 5520keV}  (Pb216);
    \draw[decay] (Pb214.east) -- node [sloped, below left] {$\beta$ \\ 570keV} (Bi214.west);
    \draw[decay] (Pb210.east) -- node [sloped, below left] {$\beta$\\ 570keV}  (Bi210.west);
\end{tikzpicture}

```
