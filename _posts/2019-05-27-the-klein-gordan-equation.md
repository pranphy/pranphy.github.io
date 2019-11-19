---
layout: post
date: 2019-05-27 16:34:41
title: The Klein-Gordan equation
author: Prakash
tags: Schrodinger Klein-Gordan Lorentz-Invariance
categories: Physics
description: an introduction to the Dirac equation
---

# Schr&ouml;dinger's Equation
Two of the greatest triumphs in Physics in the first three decades of 20<sup>th</sup> century are, i) Einstein's Theory of Relativity", both special and general, and  ii) Quantum Mechanics. While both of them are very successful, there is still some friction between them.  Special Theory of Relativity taught us that space and time (which we thought were independent), in fact, were just components of more fundamental 4-dimensional spacetime. There are various ways we can formulate quantum mechanics, in any case, Schr&ouml;dinger's equation can be thought of as of central importance to the theory.  The Schr&ouml;dinger's equation is

* TOC
{:toc}

$$
\begin{align*} 
    H \ket{\psi} = i\hbar \pdv{ }{t} \ket{\psi}
\end{align*}
$$


In the position basis $x$ we can write the above equation as 


$$
\begin{align*}
    H \psi(x) = i\hbar \pdv{ }{t} \psi(x)
\end{align*}
$$

Where $\psi(x)$ is the projection of the wavevector onto the position basis vectors. For a free particle without any spin and mass $m$ we can write the classical Hamiltonian as


$$
\begin{align*}
    H = \frac{p^{2}}{2m} 
\end{align*}
$$

Promoting the observables, which in this case is just the momentum $p$ and energy $H$, to operators we write in Quantum Mechanics the Hamiltonian operator as

$$
\begin{align*}
    \hat{H} = \frac{\hat{p}^{2}}{2m} 
\end{align*}
$$

The momentum operator $\hat{p}$ in position basis can be easily written as

$$
\begin{align*}
    \hat{p} = - i\hbar \nabla
\end{align*}
$$

So the Schr&ouml;dinger's equation for a free particle  now transforms to

$$
\begin{align*}
    i \hbar \pdv{ }{t}  \psi(x) = - \frac{\hbar^{2}}{2m} \nabla^{2} \psi(x)
\end{align*}
$$

# Lorentz Invariance
The obvious problem in this equation is that it treats time as special from rest of the spatial coordinates, for the time derivative appearing in the above equation is is first order but the spatial derivative is second order. For this reason it is evidently not Lorentz invariant which implies it doesn't satisfy special theory of relativity which is the fundamental law of nature. We could try to incorporate Lorentz invariance by writing the Hamiltonian as

$$
\hat{H} = \sqrt{\hat{p}^2c^2 + m^2 c^4} 
$$

which comes from the Energy relation in special relativity. Thus the Schr&ouml;dinger's equation becomes 

$$
\sqrt{ -\hbar^2 \nabla^2 c^2 + m^2 c^4} \psi(x) = i\hbar \pdv{}{t} \psi(x)
$$

At lest in this form the degree of spacial derivative and the time derivative are equal. But this expression, which potentially is Lorentz invariant, is not very helpful. Because, in principle we could solve this differential equation, but the square root sign still poses a problem to us. 


# Klein Gordan Equation
If we could get rid of the square root sign, our job somehow would be more easier. What if we operate both sides by the Hamiltonian operator again?


$$
\begin{align*}
\left(-\hbar^2 \nabla^2 c^2 + m^2 c^4\right) \psi(x) = -\hbar^2 \pdv[2]{}{t} \psi(x)
\end{align*}
$$

A simple rearrangement of this expression gives the following expression.


$$
\begin{align*}
\hbar^2 \left( \frac{1}{c^{2}}\pdv[2]{ }{t}  -\nabla^2  + \left( \frac{mc}{\hbar} \right)^{2}\right) \psi(x) = 0
\end{align*}
$$

The partial derivative expression $ \frac{1}{c^2}\pdv[2]{ }{t}  - \nabla^2  $ is usually written as

$$
\begin{align*}
    \square \equiv  \frac{1}{c^{2}}\pdv[2]{ }{t}  - \nabla^2 
\end{align*}
$$

So the above expression becomes

$$
\begin{align} \label{eq:KleinGordanPrem}
\hbar^2 \left( \square + \left( \frac{mc}{\hbar} \right)^{2}\right) \psi(x) = 0
\end{align}
$$

Equation. \eqref{eq:KleinGordanPrem} is called the Klein-Gordan equation. For sake of brevity we usually work in the units of $\hbar =1 =c $, which are called the natural units. In this system of units, the Klein Gordan equation becomes 

$$
\begin{align*}
   \left( \square + m^{2} \right)  \psi(x)  = 0
\end{align*}
$$

This beautiful second order differential equation is called the glorious Klein Gordan equation. This describes a free spinless particle with mass $m$. Since there is no preference of time over the spatial coordinates, this si potentially Lorentz invariant, (we can prove that this is indeed Lorentz invariant). But this has introduced another serious problem. The serious problem and its resolution is discussed in [this post]({% post_url  2019-05-21-qed-in-half-hour %}).
