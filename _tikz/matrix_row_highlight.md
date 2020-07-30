---
layout: tikzimage
title: This is a test title
tags: ml tikz
image: matrix_row_highlight.png
date: 2020-07-14
---

header information here

```tex
\begin{tikzpicture}
    \matrix (m) [matrix of math nodes,
        ampersand replacement=\&,
         left delimiter = (,
         right delimiter = ),
         nodes={minimum size=2em}]
         {
        1   \&   3   \&   -8\\
        2   \&   0   \&   1 \\
        -7  \&   9   \&   1 \\
    };
    \matrix  [matrix of math nodes,
        right =60pt of m-2-3.east,
        ampersand replacement=\&,
         left delimiter = (,
         right delimiter = ),
         nodes={minimum size=2em}] (j)
         {
        5   \&   4   \&   -8\\
        3   \&   0   \&   9 \\
        -2  \&   3   \&   1 \\
    };
    \begin{pgfonlayer}{background}
        \draw[rounded corners, dotted, fill=green!20!white]
            (m-1-2.north west) rectangle (m-3-2.south east);
    \end{pgfonlayer}
    \begin{pgfonlayer}{background}
        \draw[rounded corners, dotted, fill=green!20!white]
            (j-2-1.north west) rectangle (j-2-3.south east);
    \end{pgfonlayer}
    \draw[->,thick,red] (m-2-2.east) to [out=0,in=270] (j-2-2.south);
    \node[draw=orange,cloud,double,fill=orange!30,cloud puffs=19, aspect=1.7,above right=1pt of j.north]{Final};
    %\draw[cloud, above=30pt of m,fill=red,opacity=0.4] {Hello there}; 
    
\end{tikzpicture}

```
