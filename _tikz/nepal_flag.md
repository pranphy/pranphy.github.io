---
layout: tikzimage
title: This is a test title
tags: ml tikz
image: nepal_flag.png
date: 2020-07-14
---

header information here

```tex
%%D very rough nepal flag. Although the shape looks like nepal flag
%%D the measurements are not accurate. The constitution mentions the
%%D geometric construction in great detail. Sometimes I will have to
%%D follow the constitution to accurately draw the flat.
\tikzset{
    sunspike/.style={color=white,fill=white,decorate,decoration={zigzag,segment length=2mm,amplitude=1mm,pre length=-.1mm}},
    flagcolor/.style={color=blue,fill=red!90,line width=3mm}
}
\begin{tikzpicture}
    \draw[flagcolor] (4.5,0) -- (0,0) -- ++(90:6) -- ++(-35:5) -- ++(180:3) -- cycle ;
    \draw[sunspike] (1.2,1.5) circle (.5);
    \draw[
       fill=white,color=white,
       decoration={zigzag,segment length=1mm,amplitude=1mm,pre length=-.1mm}
    ] 
     (1.6,4.3) arc (0:-180:6mm) 
     arc (180:295:2mm) 
     decorate {arc (180:0:3mm) }
     arc (250:360:2.3mm) --cycle;
\end{tikzpicture}



```
