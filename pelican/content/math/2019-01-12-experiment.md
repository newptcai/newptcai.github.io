---
title: The joy of experimental mathematics
date: 2019-01-12
layout: post
tags: probability, integration, Mathematica
status: published
---

I came across [an interesting identity](https://math.stackexchange.com/q/3070440/1618) on math.stackexchange.com.
<!-- END_SUMMARY -->
$$
\int_{0}^{1}((1-x^r)^{1/r}-x)^{2 n}\,\mathrm dx=\frac{1}{2 n+1}
$$
for all $n \in \mathbb N$ and $r > 0$.
Someone has found this [very smart proof](https://math.stackexchange.com/a/3070493/1618) for it.

I will give a much less smart proof, but perhaps equally joyful one. When I see something like this,
I always try it with a few fix numbers with Mathematica.  Let
$$
f(n)=\int \left(\left(1-x^r\right)^{1/r}-x\right)^{2 n} \, \mathrm dx
$$
then,
$$
f(1)
=
x \, _2F_1\left(-\frac{2}{r},\frac{1}{r};1+\frac{1}{r};x^r\right)-x^2 \, _2F_1\left(-\frac{1}{r},\frac{2}{r};1+\frac{2}{r};x^r\right)+\frac{x^3}{3},
$$
\begin{align}
f(2)
=
& x \, _2F_1\left(-\frac{4}{r},\frac{1}{r};1+\frac{1}{r};x^r\right)-x^4 \, _2F_1\left(-\frac{1}{r},\frac{4}{r};1+\frac{4}{r};x^r\right) \\
& +2 x^3 \, _2F_1\left(-\frac{2}{r},\frac{3}{r};1+\frac{3}{r};x^r\right)-2 x^2 \, _2F_1\left(-\frac{3}{r},\frac{2}{r};1+\frac{2}{r};x^r\right)+\frac{x^5}{5}
,
\end{align}
and
\begin{align}
f(3)
=
&
x \, _2F_1\left(-\frac{6}{r},\frac{1}{r};1+\frac{1}{r};x^r\right)-x^6 \, _2F_1\left(-\frac{1}{r},\frac{6}{r};1+\frac{6}{r};x^r\right)
\\
&
+3 x^5 \, _2F_1\left(-\frac{2}{r},\frac{5}{r};1+\frac{5}{r};x^r\right)-5 x^4 \, _2F_1\left(-\frac{3}{r},\frac{4}{r};1+\frac{4}{r};x^r\right)
\\
&
+5 x^3 \, _2F_1\left(-\frac{4}{r},\frac{3}{r};1+\frac{3}{r};x^r\right)-3 x^2 \, _2F_1\left(-\frac{5}{r},\frac{2}{r};1+\frac{2}{r};x^r\right)+\frac{x^7}{7}
\end{align}
where $_2F_1$ is the hypergeometric function.

Do you see the patterns? Looks like a binomial expansion, right? It turns out, if we do a binomail
expansion
$$
\left(\left(1-x^r\right)^{1/r}-x\right)^{2 n}
=
\underset{j=1}{\overset{2 n+1}{\sum }} 
\left(
\begin{array}{c}
 2 n \\
 j-1 \\
\end{array}
\right) 
(-x)^{j-1}
\left(\left(1-x^r\right)^{1/r}\right)^{-j+2 n+1}
$$
Then it is easy to verify with Mathematica that
$$
\left(
\begin{array}{c}
 2 n \\
 j-1 \\
\end{array}
\right) 
(-x)^{j-1}
\left(\left(1-x^r\right)^{1/r}\right)^{-j+2 n+1}
=
\frac{\mathrm d}{\mathrm d x}\left(
\frac{1}{2 n+1}
(-1)^{j+1} x^j \binom{2 n+1}{j} \, _2F_1\left(\frac{j}{r},-\frac{-j+2 n+1}{r};\frac{j}{r}+1;x^r\right)
\right)
$$
Therefore, we have
$$
\int((1-x^r)^{1/r}-x)^{2 n} \mathrm dx
=
\sum _{j=1}^{2 n+1} \frac{1}{2 n+1} (-1)^{j+1} x^j \binom{2 n+1}{j} \, _2F_1\left(\frac{j}{r},-\frac{-j+2 n+1}{r};\frac{j}{r}+1;x^r\right).
$$
When $j=2n+1$, the summand in the right hand equals $\frac{x^{2 n+1}}{2 n+1}$. This is the term
which gives us $\frac 1 {2n+1}$. Everything else vanishes in the original definite integral.

The moral of this story is perhaps with the help of computers, it is much easier to find patterns
and often seeing the pattern is enough to give the proof. Moreover, the moment when you see the
pattern is quite joyful, as much as the moment that you come up with a proof.
