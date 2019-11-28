---
layout: post
author : Prakash Gautam
Date   : 03-06-2019 19:08:25
title: The Dirac Equation
tags: Dirac Schrodinger LaTeX
categoreis: physics
description: very brief introduction to the Dirac equation
---

# Klein Gordan Equation

We have seen in [this post]({% post_url  2019-05-27-the-klein-gordan-equation %}) that Klein-Gordan equation describes a spinless particle with mass $m$. The Klein-Gordan equation formally is


$$
\begin{align*}
    \left( \square + m^{2} \right) \psi = 0
\end{align*}
$$

Unlike Schr&ouml;dinger's equation, this equation doesn't treat time differently from space derivatives. It can be shown that this in indeed Lorentz invariant. However, the problem with Klein-Gordan equation is that it violates the conservation of probability, which is a serious problem. We need a first order differential equation which would indeed conserve the probability.

# Dirac Equation

This dynamic equation also doesn't take into account the spin of particles, electron for example. Paul Dirac attempted to obtain a first order equation which would conserve probability and also take into consideration the spin of the particle. The first line of attack is  to start from Schr&ouml;dinger's equation and add an extra paramter in the wae function which would correspond to different spins. Taking a wave function solution 
 
 $$
 \begin{align*}
     \psi(x,a)
 \end{align*}
 $$

where the different values of $a$ would correspond to different spin of the particle.

we could try to factorize the equation as


$$
\begin{align*}
       \left( \delta p^\mu + \chi m \right) \left( p_\mu \alpha - \beta m \right)  =  \left(\square - m^{2} \right)  
\end{align*}
$$

Like we did in quantum harmonic oscillator. We could multiply through this expression and see what should we have for the coefficients $\alpha$ and $\beta$. Working out the product on the left side we get

$$
\begin{align*}
    \delta   p_{\mu} p^{\mu}  \alpha + \chi m p_\mu \alpha - \delta \beta m p^\mu  -\chi \beta m^{2} = \square - m^{2}
\end{align*}
$$


Since there are no cross terms in the RHS of the above expression we necessarily eed to have 

$$
\begin{align*}
    \alpha \beta - \beta \alpha  = 0
\end{align*}
$$

Such situation is referred to as being commuting and is usually written as 

$$
\begin{align*}
    \left[ A, B \right]  = AB - BA
\end{align*}
$$

Thus in this notation $\left[ \alpha, \beta \right]  = 0$ 


$$
\begin{align*}
     \left( i \gamma^\mu \partial_\mu - m  \right) \psi  = 0
\end{align*}
$$

As in tensor notation the expressions with a raised and a repeated lower index contract. Similarly the expression like $\gamma^\mu \partial_\mu$ contract and Feynman suggested a notation to use for these kinds of expression as

$$
\begin{align*}
    \gamma^\mu \partial_\mu \equiv \slashed{\partial}
\end{align*}
$$

whith the use of this notation we can write the dirac equation in the form.



$$
\begin{align*}
     \left( i \slashed{\partial} - m  \right) \psi  = 0
\end{align*}
$$

Which is our glorius Dirac equation, which describes the particle dynamics of particle with spin. 


[//]: # (this is some comment)
