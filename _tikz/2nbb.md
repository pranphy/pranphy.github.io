---
layout: tikzimage
title: This is a test title
tags: ml tikz
image: 2nbb.png
date: 2020-07-14
---

header information here

```tex
\begin{tikzpicture}
  \begin{feynman}
    \vertex (a);
    \vertex [below left=2cm and 0.4cm of a] (b);
    \vertex [above left=2cm and 0.4cm of a] (c);
    \vertex [above right=of a] (d);
    \vertex [above left=1cm and 0.4cm of d] (e);
    \vertex [above right=1cm and 0.4cm of d] (f);
    \diagram*{
        (b)--[fermion,edge label={$n^0$}] (a) --[fermion,edge label={$p^{+}$}] (c),
        (a) --[boson,edge label'={\small $W^{-}$}] (d),
        (d) --[fermion,edge label={$e^{-}$}] (e),
        (f) --[fermion,edge label'={\tiny $\bar{\nu}$}] (d)
    };
    \vertex [right=3.5cm of a] (aa);
    \vertex [below right=2cm and 0.4cm of aa] (ab);
    \vertex [above right=2cm and 0.4cm of aa] (ac);
    \vertex [above left=of aa] (ad);
    \vertex [above left=1cm and 0.4cm of ad] (ae);
    \vertex [above right=1cm and 0.4cm of ad] (af);
    \diagram*{
        (ab)--[fermion,edge label'={$n^0$}] (aa) --[fermion, edge label'={$p^{+}$}] (ac),
        (aa) --[boson,edge label={\small $W^{-}$}] (ad),
        (ae) --[fermion,edge label={\tiny $\bar{\nu}$}] (ad),
        (ad) --[fermion,edge label'={ $e^{-}$}] (af)
    };
  \end{feynman}
\end{tikzpicture}

```
