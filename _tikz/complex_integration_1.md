---
layout: tikzimage
title: This is a test title
tags: ml tikz
image: complex_integration_1.png
date: 2020-07-14
---

header information here

```tex
%%% This diagram was made for my homework of Mathematical 
%%% Physics at Drexel University during my Masters education
%%% The homework assignment can be found here at
%%% http://physics.drexel.edu/~pgautam/courses/
\begin{tikzpicture}
    [
    decoration={
      markings,
      mark=at position 1cm with {\arrow[line width=1pt]{>}},
      mark=at position .3 with {\arrow[line width=1pt]{>}},
      mark=at position .6 with {\arrow[line width=1pt]{>}},
      mark=at position 0.8 with {\arrow[line width=1pt]{>}},
      mark=at position -5mm with {\arrow[line width=1pt]{>}},
    },
    contourline/.style={line width=1.0pt},
    axisline/.style={->,line width=0.3pt},
    ]
    \tikzmath{\R=3;\r=0.5;\X=1.1*\R;\Y=1.1*\R;}
    \draw [axisline] (-\X,0) -- (\X,0)  node [below right] {Re($z$)};
    \draw [axisline] (0,1.2*\r) -- (0,-\Y)  node[left] {Im($z$)};
    \node at (0,0) {$\times$};
    \draw [contourline, postaction=decorate]
        (\r,0) node [below, font=\scriptsize] {$\epsilon$} -- 
        (\R,0) node [above] {$R$} 
        arc (0:-180:\R) node [above] {$-R$} -- 
        (-\r,0) node [below, font=\scriptsize] {$-\epsilon$} 
        arc (180:0:\r);
    \node at (\r,1.1*\r) {$\Gamma_{\varepsilon}$};
    \node at (1.15*\R*0.7,-1.15*\R*0.7) {$\Gamma_{R}$}; % 0.7 = sin(45) = cos(45)
\end{tikzpicture}


```
