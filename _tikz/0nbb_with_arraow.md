---
layout: tikzimage
title: This is a test title
tags: ml tikz
image: 0nbb_with_arraow.png
date: 2020-07-14
---

header information here

```tex
\begin{tikzpicture}
  \begin{feynman}
    \vertex (b);
    \vertex [below=of b] (c);
    \vertex [below left=1cm and 1.4cm of c] (d);
    \vertex [above left=.8cm and 1.4cm of b] (a);
    \vertex [left=of a] (i1) {\tiny $d$};
    \vertex [left=of d] (i2) {\tiny $d$};
    \vertex [right = 2cm of b] (f2) {\tiny $e^{-}$};
    \vertex [right = 2cm of c] (f3) {\tiny $e^{-}$};
    \vertex [below = 2cm of f3] (f4) {\tiny $u$};

    \vertex [above = 2cm of f2] (f1) {\tiny $u$};

    \vertex [above=0.25cm of i1] (f6) {\tiny $d$}; % d quark outgoing
    \vertex [above=0.25cm of f1] (i3) {\tiny $d$}; % d quark ingoing

    \vertex [above=0.25cm of i3] (f7) {\tiny $u$}; % u quark outgoing
    \vertex [above=0.25cm of f6] (i4) {\tiny $u$}; % u quark ingoing

    % copy quarks for bottom

    \vertex [below=0.25cm of i2] (f8) {\tiny $d$}; % d quark outgoing
    \vertex [below=0.25cm of f4] (i5) {\tiny $d$}; % d quark ingoing

    \vertex [below=0.25cm of i5] (f9) {\tiny $u$}; % u quark outgoing
    \vertex [below=0.25cm of f8] (i6) {\tiny $u$}; % u quark ingoing

    \newcommand\tmpda{0.9cm}
    \newcommand\tmpdb{-1.7cm}
    \diagram* {
        (a) -- [boson, edge label'= {\tiny $W^{-}$}] (b) 
            -- [anti majorana, insertion=0.5, edge label' = {\tiny $\nu_{\scriptsize M}$} ] (c) 
            -- [boson, edge label'={\tiny $W^{-}$}] (d),
        (i1) -- [with arrow=\tmpda] (a),
        (i2) -- [with arrow=\tmpda] (d),
        (a) -- [with arrow=\tmpdb] (f1),
        (b) -- [fermion] (f2),
        (c) -- [fermion] (f3),
        (d) -- [with arrow=\tmpdb] (f4),
        (f6) -- [with arrow=\tmpda, with arrow=\tmpdb, out=0, in=200] (i3),
        (i4) -- [with arrow=\tmpda, with arrow=\tmpdb, out=0, in=200] (f7),
        (f8) -- [with arrow=\tmpda, with arrow=\tmpdb, out=0, in=160] (i5),
        (i6) -- [with arrow=\tmpda, with arrow=\tmpdb, out=0, in=160] (f9),
    };

    \draw [decoration = {brace} , decorate] (i1.south west) -- (i4.north west) node [pos = 0.5 , left = 0.065cm] {\small $n$};

    \draw [decoration = {brace} , decorate] (f7.north east) -- (f1.south east) node [pos = 0.5 , right = 0.125cm] {\small p};

    %J\draw [decoration = {brace} , decorate] (i6.south west) -- (i2.north west) node [pos = 0.5 , left = 0.125cm] {\small n};

    %\draw [decoration = {brace} , decorate] (f4.north east) -- (f9.south east) node [pos = 0.5 , right = 0.125cm] {\small p};
  \end{feynman}
\end{tikzpicture}

```
