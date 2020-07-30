---
layout: tikzimage
title: This is a test title
tags: ml tikz
image: neutrino_mass_hierarchy.png
date: 2020-07-14
---

header information here

```tex
\tikzset{
    dimen/.style={<->,>=latex,thin,every rectangle node/.style={fill=white,midway}},
    symmetry/.style={dashed,thin},
    munu/.style={draw,fill,rectangle,color=red!80,text=black,minimum height=1mm,font=\scriptsize},
    taunu/.style={draw,fill,rectangle,color=green,text=black,minimum height=1mm,font=\scriptsize},
    enu/.style={draw,fill,rectangle,color=blue!60,text=black,minimum height=1mm,font=\scriptsize},
    muone/.pic = {
        \node[opacity=0] (bummy) {};
        \node[munu,minimum width=7mm, right=1mm of bummy] (twomu) {};
        \node[taunu,minimum width=6mm,right=0mm of twomu] (twotau) {};
        \node[enu,minimum width=7mm,right=0mm of twotau] (twoe) {};
        \node{ \tikzpictext};
    },
    mutwo/.pic = {
        \node[opacity=0] (eummy) {};
        \node[munu,minimum width=12mm,right=1mm of eummy] (threemu) {};
        \node[taunu,minimum width=4mm,right=0mm of threemu] (threetau) {};
        \node[enu,minimum width=4mm,right=0mm of threetau] (threee) {};
        \node{ \tikzpictext};
    },
    muthree/.pic = {
        \node[opacity=0] (dummy) {};
        \node[munu,minimum height=2mm,minimum width=2mm,right=1mm of dummy] (onemu) {};
        \node[taunu,minimum width=8mm,right=0mm of onemu] (onetau) {};
        \node[enu,minimum width=10mm,right=0mm of onetau] (onee) {};
        \node{\tikzpictext};
    },
}
\begin{tikzpicture}
    \draw[->,thick] (-1,0) -- node [sloped, above] {$m^2$} (-1,3) ;
    \pic ["$\nu_3$"] (normuone)   at (0,3) {muone};
    \pic ["$\nu_1$"] (normutwo)   at (0,1) {mutwo};
    \pic ["$\nu_2$"] (normuthree) at (0,0) {muthree};
    \pic ["$\nu_2$"] (invmutwo)   at (5,3) {mutwo};
    \pic ["$\nu_1$"] (invmuone)   at (5,2) {muone};
    \pic ["$\nu_3$"] (invmuthree) at (5,0) {muthree};
    \draw[dimen] (1,.2) --(1,0.8) node [right=2mm] {$\Delta m^2_{\text{sol}}$};
    \draw[dimen] (1,1.2) --(1,2.8) node [right=2mm]{$\Delta m^2_{\text{atm}}$};
    \draw[dimen] (6,.2) --(6,1.8) node [right=2mm] {$\Delta m^2_{\text{atm}}$};
    \draw[dimen] (6,2.2) --(6,2.8) node [right=2mm]{$\Delta m^2_{\text{sol}}$};
    \node[munu] (mulab)   at  (3.6,1) [label=below:$\nu_\mu$] {}; %}{$\nu_\mu$};
    \node[taunu] (taulab) at  (3.6,2) [label=below:$\nu_\tau$] {};
    \node[enu] (elab)     at  (3.6,3) [label=below:$\nu_e$] {};
    \node (norhie) at (1.2,4) {Normal Hierarchy};
    \node (invhie) at (6.5,4) {Inverted Hierarchy};
\end{tikzpicture}



```
