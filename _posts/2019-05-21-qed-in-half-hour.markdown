---
layout: post
title: QED in half hour
tags: QED LaTeX Field-Theory
categories: physics
date: 2019-05-20 15:09:00
description: a brief look into QED and its working in under half an hour.
---

## Classical Electrodynamics
In the early days of the encounter with Electricity and magnetism, these were studied seperately as independent phenomenon in nature. With more studies, it was evident that Electricity and magnetism were intimately related. Maxwell painstakingly combined  the known laws of electricity and magnetism into a set of four beautiful first order differential equations and showed the intimate connection. 


* TOC
{:toc}

$$
\begin{align*}
    \nabla \cdot   \vec{B}  &= 0\nonumber 
\end{align*}
$$ 

$$
\begin{align*}
    \nabla \cdot \vec{E}   &= \frac{\rho}{\epsilon_0} \nonumber 
\end{align*}
$$

$$
\begin{align*}
    \nabla \times  \vec{E} - \frac{\partial \vec{B}}{ \partial t} &= 0 \nonumber
\end{align*}
$$

$$
\begin{align*}
    \nabla \times  \vec{B} - \frac{\partial \vec{E}}{\partial t} &= \vec{J} \nonumber
\end{align*}
$$

$$
\begin{align*}
    \vec{F} = q(\vec{v}\times \vec{B} + \vec{E}) \nonumber
\end{align*}
$$

In classical electrodynamics the four maxwells' equation together with the Lorentz force law form the complete set of equation required to understand all electromagnetic phenomenon.

Our goal in this class is to combine all of these into a single equation.

## Lagrangian
All of classical mechanics can be traced back to Newton's laws and Universal gravitational force equation. This approch involves Forces and acclerations of particles. And equally equivalent approach is to make use of principle of least action. In principle, to every system in nature we can find a lagrangian and the particle interaction and trajectory are given by the exteremities of the action, which is the integral of lagrangian.

$$
\begin{align*}
    \partial S = \partial \int L dt  = 0
\end{align*}
$$

Classically, the lagrangian is a function of all the particle positions $q$ and their time derivatives.

$$
\begin{align*}
    L = f(q_i,\dot{q}_i) \nonumber
\end{align*}
$$


where $i$ runs through the number of particles in a system. The principle of least action with the use of calculus of variation give rise to the well known Euler Lagrange's equation
$$ 
\begin{align} \label{eq:Euleq_classical}
    \frac{ \partial }{\partial t}  \left( \frac{\partial L}{\partial \dot{q_i}} \right)  = \frac{\partial \mathcal{L}}{\partial q}
\end{align}
$$

One of the simplest non trivial system well studied in classical mechanics is simple harmonic oscillator. The lagrangian for this system is 

$$
\begin{align*}
    L = \frac{p^{2}}{2m} - \frac{1}{2}kx^{2}
\end{align*}
$$

This with the use of euler lagrange euqation  we get.

$$
\begin{align*}
    m\ddot{x} = -kx \nonumber
\end{align*}
$$

which is the well known Hook's law equation for a spring system.  
If we know the lagrangian for a spring system we can, in principle, figure out everything there is to know about the system. Its position, velocity, amplitude, frequency, the oscillating mass are all in principle calculable from  the lagrangian. This concept of lagrangian in classical system can be extended to a broad category of systems. 

## Lagrangian Density
The classical approach of Lagrangian and principle of least of action can be directly carried over to Qauntum mechanical system with a few problems addressed. The first problem evidently is the different treatment of time prameter than the spatial parameter. As we know quite well from Special Relativity that nature is fundamentally four dimenstional with 3 space parameter along with the time giving the four dimensions.



To take our idea of classical fields to quantum fields we start with a lagrangian similar to the one for spring. Extending from the lagrangian for a spring mass system, we can imagine a scalar $\phi$ which  is a function of spacetime coordinates. Locally if we approximate the fluctation of this scalar field with harmonic potential, we can write teh approximate  potential energy as

$$
\begin{align*}
    U = \sum_i \left( \frac{1}{2}k_i \phi_i^{2} + \frac{1}{2} k_c \left[ (\phi_i - \phi_{i-1})^{2} + \Delta x^{2} \right]  \right)  \nonumber
\end{align*}
$$

The kinetic energy term looks something line

$$
\begin{align*}
    T = \frac{1}{2} m \dot{\phi}^{2} \nonumber
\end{align*}
$$

Using this with our familar expression $L = T-V$ we get. In the limit as $\Delta x \to 0$ enables us to write  write a simple lagrangian with scalar fields as

$$
\begin{align*}
    L = \int dx \left( \frac{1}{2}\mu \dot{\phi}^{2} - \frac{1}{2}T \left( \frac{\partial \phi}{ \partial x}  \right) ^{2} - \frac{1}{2} \sigma \phi^{2} \right) \nonumber
\end{align*}
$$

From this we can write the Action which is the integral of the Lagrangian as, 

$$
\begin{align*}
    S = \int dt dx \left(  \frac{1}{2} \dot{\phi}^{2} - \frac{1}{2} \frac{T}{\mu} \left( \frac{\partial \phi}{\partial x}  \right) ^{2} - \frac{1}{2} \frac{\sigma}{\mu} \phi ^{2} \right) \nonumber
\end{align*}
$$

In full glory of three dimension it can be rewritten as

$$
\begin{align*}
    S = \int dt d^3x \left(  \frac{1}{2} \dot{\phi}^{2} - \frac{1}{2} \frac{T}{\mu} \left(  \nabla^{2}\phi  \right)^{2}- \frac{1}{2} \frac{\sigma}{\mu} \phi ^{2} \right) \nonumber
\end{align*}
$$

Introducing a new term $\mathcal{L}$ as the lagrangian density and $dt d^3x = d^4x$ we can write this as

$$
\begin{align*}
    S = \int d^4x \mathcal{L}\nonumber
\end{align*}
$$

here $T$ is tension in string $\mu$ is the mass per unit length. Sigma is propoprtional to restoring force.
With the constants scaled we can rewrite this as
In three dimension this has simple extension as

$$
\begin{align*}
    \mathcal{L} = \left(  \frac{1}{2} \dot{\phi}^{2} - \frac{1}{2} \left(  \nabla^{2}\phi  \right)^{2}- \frac{1}{2} m^{2} \phi ^{2} \right) \nonumber
\end{align*}
$$

Introducing the term $\partial_\mu \phi \partial^\mu \phi  = (\frac{\partial^2}{t^2} - \nabla^{2})\phi$

$$
\begin{align*}
    \mathcal{L} = \frac{1}{2} \partial^\mu \phi \partial_\mu \phi     - \frac{1}{2} m^{2} \phi ^{2}\nonumber
\end{align*}
$$

Minimizing the action gives the Euler lagranges equations in the similar fashion

$$
\begin{align*}
    \partial_\mu \left(  \frac{\partial \mathcal{L}}{\partial (\partial_\mu \phi)} \right) = \frac{\partial \mathcal{L}}{\partial \phi} \nonumber
\end{align*}
$$

which are unsruprisingly similar the the Eq. \ref{eq:Euleq_classical} for classical mechanics.

The lagrangian and the Euler lagranges equation in hand we can find everything thaere is to know about the system that the lagrangian represents. The differential equations that we get from the application of the Euler-Lagrange's equation is all we need to know.
\section {Gauge Transformation}
Now that we know that the lagrangian represents systems, we can play around with lagrangian and see what the solution leads. What if we made a lagrangian involving not only one field but two independent fields we could write the lagrangian with two fields similar to free fields as

$$
\begin{align*}
    \mathcal{L} = \frac{1}{2} \partial_\mu \phi_1 \partial^\mu \phi_1 - \frac{1}{2} m_1^{2}\phi_1^{2} +
     \frac{1}{2} \partial_\mu \phi_2 \partial^\mu \phi_2 - \frac{1}{2}m_2^{2}\phi_2^{2} \nonumber
\end{align*}
$$

There is a way we can represent two independent parameter as a single parameter in maths. We can use a complex number or a two component vector. This lagrangian can be made simpler by substitution

$$
\begin{align*}
    \phi = \left( \frac{\phi_1  + \phi_2}{2} \right) + i \left( \frac{\phi_1 - \phi_2}{2} \right) \nonumber
\end{align*}
$$

With this substitutin we can write the final lagrangian as

$$
\begin{align*}
    \mathcal{L} =  \partial_\mu \phi \partial^\mu \phi^* - m^{2}\phi \phi^*
\end{align*}
$$

Although in our representation $\phi$ represent the fields fluctuating in spacetime. The observable fo the fields are given by the differntial equation applied on the lagrangina. If we make any alteration in the field without ever changing the value of lagrangian, the observable are still going to come out exactly as before. 

For instance if we alter the $\phi$ fields as

$$
\begin{align*}
    \phi \to e^{i\theta} \phi \nonumber
\end{align*}
$$

The above lagrangian is still going to be the same and so the observables are still going to be the same. Such a transformation in field are called the gauge transformation.

## QED Lagrangian
I am going to make a big jump here and say we already know lagrangian for charged particle with spin. Which is the dirac equation and I will state that.  

From hunderd of years of knowledge of Classical electrodynamics we know that the field in classical electrodynamics are the scalar potential and the vector potential. So if we are ever trying to write such a lorentz invariant theory of electrodynamics it has to involve lagrangian over vector fields. 

People tried to write a Lagrangian involving vector fields such that we obtained the dynamical equations of electrodynamics and it did not turn out to be the easiest task historically. 


Dirac had combined quantum mechanics and special relativity into a beautiful equation called the dirac equatio, which detail I am not goint to go into but simply state the dirac equation whih is

$$
\begin{align*}
    \left( i\gamma^\mu\partial_\mu -m \right) \psi = 0 \nonumber
\end{align*}
$$

The lagrangian for which can be conveniently written as

$$
\begin{align*}
    \mathcal{L} = \bar{\psi}\left( i\gamma^\mu\partial_\mu -m \right) \psi  \nonumber
\end{align*}
$$


This lagrangian also has a very beautiful global gauge symmetry in that if we make a transformation

$$
\begin{align*}
    \psi \to e^{-i\theta}\psi
\end{align*}
$$

The dirac lagrangian stays the same. We then wonder what would happen if we also tried to look for a lagrangian which not only had this global symmetry but also local gauge symmetry?

We might be tempted to make this gauge transformation  such that

$$
\begin{align*}
    \psi \to e^{-i q\theta(x)}\psi
\end{align*}
$$

where the gauge factor $\theta(x)$ is a function of position vector. The lagrangian as is won't be symmetric under this gauge. As a simple check with the derivative of $\psi$ is going to leave us with extra term like

$$
\begin{align*}
    -q\partial_\mu \theta(x) \nonumber
\end{align*}
$$

We could try adding to the field a new vector function $A_\mu$ such that under this this transformation 

$$
\begin{align*}
    A_\mu \to A_\mu + \partial_\mu \theta (x) \nonumber
\end{align*}
$$ 

we could try with a new field $\psi$ such that the new field is

$$
\begin{align*}
    \partial_\mu \psi \to (\partial_\mu + i q A_\mu )\psi \equiv D_\mu \psi \nonumber
\end{align*}
$$

Under such transformation though our lagrangian would be

$$
\begin{align*}
    \mathcal{L} = \bar{\psi} \left[ i \gamma^\mu \left( \partial_\mu + i qA_\mu \right) -m \right] \psi \equiv \bar{\psi} \left( i\gamma_\mu D_\mu -m \right)  \psi \nonumber
\end{align*}
$$


This is a possible lagrangian but we can still add further terms in the lagrangian without destroying the local gauge invariance.  

$$
\begin{align*}
    (\partial_\mu A_\nu - \partial_\nu A_\mu)^2  \nonumber
\end{align*}
$$

Thus our final lagrangian that has local gauge invariance is 

$$
\begin{align*}
    \mathcal{L} = \bar{\psi} \left[ i \gamma^\mu \left( \partial_\mu + i qA_\mu \right) -m \right] \psi +  (\partial_\mu A_\nu - \partial_\nu A_\mu)^2  \nonumber
\end{align*}
$$

The way it is usually writen is with a few terms rearranged. We introduce new variables 

$$
\begin{align*}
    J^\mu = -A_\mu q \bar{\psi} \gamma^\mu \psi  \qquad 
    F_{\mu \nu} = \partial_\mu A_\mu - \partial_\nu A_\mu \nonumber
\end{align*}
$$

and the last terms can be conviniently written as

$$
\begin{align*}
    \left( \partial_\mu A_\nu - \partial_\nu A_\mu \right) ^{2} = F_{\mu \nu}F^{\mu \nu} \nonumber
\end{align*}
$$

With these new variables the final lagrangian written usually in the form is 

$$
\begin{align*}
    \mathcal{L} = \bar{\psi} \left[ i \gamma^\mu \partial_\mu - m \right] \psi - A_\mu J^\mu - \frac{1}{4} F_{\mu \nu} F^{\mu \nu} \nonumber
\end{align*}
$$

This is our glorius lagrangian. If we apply the Euler lagrange's equation to this lagrangian we will get the differential equations for the fields $\psi$  and $A$. 

## Solution to the Lagrangian 
Perhaps not a big surprise with our previous knowledge of maxwells equations form the classical mechanics we obtain the vector field $A_\mu$ as


$$
\begin{align*}
    A_\mu = \begin{pmatrix} \phi\\ A_x\\ A_y \\ A_z \end{pmatrix}  \nonumber
\end{align*}
$$

where $\phi$ is our scalar electric potential and $A_x,A_y,A_z$ are the components of usual vector magnetic potential.

Substuting the values fo $A_\mu$ is the expression  $F_{\mu \nu} = (\partial_\mu A_\nu  - \partial_\nu A_\mu)$ we get the components as

$$
\begin{align*}
    F_{\mu \nu} = 
    \begin{pmatrix}
        0 & -E_x & -E_y & -E_z \\
        E_x & 0 & -B_x & B_y \\
        E_y & B_z & 0 & -B_x \\
        E_z & -B_y & B_x & 0 \\
    \end{pmatrix} \nonumber
\end{align*}
$$

The way we have defined the variable $F_{\mu \nu}$ it is very straightforward to show that

$$
\begin{align*}
    \partial_\lambda F_{\mu \nu} + \partial_\mu F_{\nu \lambda} + \partial_\nu F_{\lambda \mu} = 0
\end{align*}
$$ 

Now that we have the components of the Bianchi identity we can evaluate the value of Bianchi identity which for example for $\mu = 0, \nu =1, \lambda=2$ gives

$$
\begin{align*}
    \frac{\partial E^x}{\partial y}
    \left( \nabla \times  \vec{E} \right)^z &= -\dot{B}^z
\end{align*}
$$

Combining all of these we get the famous faradays law

$$
\begin{align*}
    \nabla \times  \vec{E} = -\dot{\vec{B}}
\end{align*}
$$

The values of all other indices give the rest of the maxwells equation.%, including the bonus Lorentz force law.
The lorentz force law, contunity equation and all that good stuffs comes from the use of contunity equation involving stress energy tensor.

## Takeaway

The takeaway of all of these is the following. 

1. We asserted that we can find a lagrangian corresponding to every phenomenon in nature.
2. Starting with Dirac lagrangian, which has this beautiful global U(1) gauge symmetry, we wondered what if we demanded the lagrangian be symmetric under \emph{local} $U(1)$ gauge symmetry, and wrote such a algrangian.
3. Solving the lagrangian with the Euler Lagrange's equation, we found that the solution for  the compoennts of vector field were simpoly the electric potential and the magnetic vector potential.
4. The Bianchi identity gave us all of the Maxwell's eqation and the Lorentz force law.

We wonder further and demand that the lagrangian not only be globally symmetric but  $SU(2)$ gauge symmetric. Such a demand beautifully yields all of weak interaction. No prize for guessing, $SU(3)$ local gauge symmetry yields all of strong interaction.  
As a bonus the gravitational ``force" is described field equations

$$
\begin{align*}
    G_{\mu \nu} + \Lambda g_{\mu \nu} = 8\pi T_{\mu \nu}
\end{align*}
$$

for which we are still to come up with a gauge theory.
