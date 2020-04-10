title: RandomTree.jl -- Simulation on large random trees with Julia
date: 2019-05-13
layout: post
tags:  probability, programming, experimental-math
status: published

I have been working on a software package
[`RandomTree.jl`](https://github.com/newptcai/RandomTree.jl) that could effectively generate pretty
large ($10^8$ nodes) random trees, in particular Conditional Galton-Watson trees.  The package is
written in Julia, a language designed for high-performance-computation. It is high-level language
that is as easy to use as Python, but also has performance in the same order of C (if you use it
correctly).

I have experimented to implement this package with Python + [Cython](https://cython.org/) and Python
+ [Numba](http://numba.pydata.org/). Both are quite impressive in terms of efficiency. But writing
  Cython code is so much like working in C that you lose the reason to use Python in the first
  place. While numba keeps things close to Python, unfortunately it is pretty [slow at generating
  exponential random variables](https://github.com/numba/numba/issues/4051). Eventually I settled
  down in Julia and I have to say it's perhaps the best language to use for simulations and
  computations if you do not want to use C or CPP. It is definitely worth the time to learn it if
  you care about efficiency of your code.

{% notebook notebook/2019-05-13-RandomTree.jl.ipynb %}
