---
layout: tikzimage
title: This is a test title
tags: ml tikz
image: complex_integration_3.png
date: 2020-07-14
---

header information here

```tex
\begin{tikzpicture}
  [
    decoration={ %
      markings,
      mark=at position 1cm with {\arrow[line width=1pt]{>}},
      %mark=at position 2cm with {\arrow[line width=1pt]{>}},
      mark=at position .3 with {\arrow[line width=1pt]{>}},
      mark=at position .6 with {\arrow[line width=1pt]{>}},
      mark=at position 0.8 with {\arrow[line width=1pt]{>}},
      mark=at position -5mm with {\arrow[line width=1pt]{>}},
    },
    contourline/.style={line width=1.0pt},
    axisline/.style={->,line width=0.3pt},
  ]
  \draw [axisline] (-4,0) -- (4,0) coordinate (xaxis) node [below,thick] {Re($z$)};
  \draw [axisline] (0,-0.6) -- (0,3.3) coordinate (yaxis) node [left,thick] {Im($z$)};
  \node at (0,0) {$\times$};
  \draw [contourline, postaction=decorate] 
      (.5,0) node [below, font=\scriptsize] {$\epsilon$} -- 
      (3,0) node [below] {$R$} 
      arc (0:180:3) node [below] {$-R$} -- 
      (-.5,0) node [below, font=\scriptsize] {$-\epsilon$} 
      arc (180:0:.5);
  \node at (0.5,0.6) {$\Gamma_{\varepsilon}$};
  \node at (2,2.6) {$\Gamma_{R}$};
\end{tikzpicture}

```
