title: Small o bound for the tail of distribution with finite expectation.
date: 2020-02-28
layout: post
tags: probability, real-analysis
status: published

Let $X \ge 0$ be a random variable with finite mean, i.e., $\mathbb E{X} < \infty$.
By Markov inequality, we have
$$
\mathbb P(X \ge n) \le \frac{\mathbb E X}{n} = O(n^{-1}).
$$
However,  $\mathbb E{X} < \infty$ actually implies that
$$
\mathbb P(X \ge n) = o(n^{-1}).
$$
This can be very helpful in some cases.

The proof is by contradiction. Assume that
$$
\liminf_{n \to \infty} n \mathbb P(x \ge n) = c > 0.
$$
This means there exists a sequence $a_k \uparrow \infty$ such that
\begin{equation}\label{XYSMV}
    \mathbb P(X \ge a_{k}) \ge \frac{c}{a_{k}}.
\end{equation}
Thus
\begin{align}
    \mathbb E X
    &
    = \int_{0}^{\infty} \mathbb P (X \ge x) \; \mathrm d x
    \\
    &
    = 
    \sum_{k \ge 1} 
    \int_{a_{k-1}}^{a_k} \mathbb P (X \ge x) \; \mathrm d x
    \\
    &
    \ge
    \sum_{k \ge 1} 
    \int_{a_{k-1}}^{a_k} \mathbb P (X \ge a_{k}) \; \mathrm d x
    \\
    &
    \ge
    \sum_{k \ge 1} 
    \frac{c}{a_{k}} (a_{k}-a_{k-1})
    \\
    &
    \ge
    c
    \sum_{k \ge 2} 
    1-\frac{a_{k-1}}{a_{k}}
\end{align}
Let $x_{k} = 1-\frac{a_{k}}{a_{k+1}}$. Then
\begin{equation}\label{ILIUG}
    \prod_{k = 1}^{n} (1-x_{k}) = \frac{a_{1}}{a_{n+1}} \to 0
\end{equation}
as $n \to \infty$.
This imples $\sum_{k \ge i}x_{k} = \infty$, a contradiction.
