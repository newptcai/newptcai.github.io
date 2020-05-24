title: Reinstall Julia
date: 2020-05-24
layout: post
tags:  programming, Julia
status: published

A couple of days ago, I found that I [could not install and compile
`ArbNumerics.jl`](https://github.com/JeffreySarnoff/ArbNumerics.jl/issues/41). The only options is to reinstall Julia. Fortunately, this is quite easy.

To be extra cautious, I started with a backup of the whole `~/.julia`. Start a terminal by typing

```shell
cp -r ~/.julia/ ~/Downloads/
```

Then I removed `~/.julia` without mercy 👿.
```shell
rm -rf ~/.julia/
```

This means all my previously installed Julia packages are now gone, but Julia itself (the binary and
core packages) are still there.

Most of my project has its own environment. In other words, there are two files `Project.toml` and
`Manifest.tomal` in the directory containing an environment. For example, to play with `Weave.jl`, I
have an environment in `~/Work/weave`. The content of `Project.toml` is quite simple,
which just indicates that this environment needs three dependencies `DSP`, `Plots` and `Weave`.

```toml
[deps]
DSP = "717857b8-e6f2-59f4-9121-6e50c889abd2"
Plots = "91a5bcdd-55d7-5caf-9e0b-520d859cae80"
Weave = "44d3d7a6-8a23-5bf8-98c5-b353f8df5ec9"
```

The content of `Manifest.toml` is a bit more complicated. The first few lines of it are like this.

```toml
# This file is machine-generated - editing it directly is not advised

[[AbstractFFTs]]
deps = ["LinearAlgebra"]
git-tree-sha1 = "051c95d6836228d120f5f4b984dd5aba1624f716"
uuid = "621f4979-c628-5d54-868e-fcf4e3e8185c"
version = "0.5.0"

[[Base64]]
uuid = "2a0f44e3-6c83-55bd-87e4-b1978d98bd5f"
```

What it does, is to indicate what exact packages are installed the last time I modified the
environment. 

These two files allow me to install all the packages needed to run this environment. I can simply to
launch Julia `REPL` in the directly where the environment is, `active` the environment, and run the command
`instantiate`.

```julia
(@v1.4) pkg> activate . # press ] to get the pkg prompt
 Activating environment at `~/Work/weave/Project.toml`

(weave) pkg> st
Status `~/Work/weave/Project.toml`
→ [717857b8] DSP v0.6.6
  [91a5bcdd] Plots v1.2.4
→ [44d3d7a6] Weave v0.9.4
┌ Warning: Some packages (indicated with a red arrow) are not downloaded, use `instantiate` to instantiate the current environment
└ @ Pkg.Display /buildworker/worker/package_linux64/build/usr/share/julia/stdlib/v1.4/Pkg/src/Display.jl:238

(weave) pkg> instantiate
   Updating registry at `~/.julia/registries/General`
   Updating git-repo `https://github.com/JuliaRegistries/General.git`
  Installed AbstractFFTs ──────────────── v0.5.0
  Installed Parsers ───────────────────── v1.0.3
  Installed Tables ────────────────────── v1.0.4
  Installed SpecialFunctions ──────────── v0.10.0
  Installed Weave ─────────────────────── v0.9.4
  Installed DataStructures ────────────── v0.17.15
  Installed Plots ─────────────────────── v1.2.4
  Installed DSP ───────────────────────── v0.6.6
  Installed IteratorInterfaceExtensions ─ v1.0.0
  Installed TableTraits ───────────────── v1.0.0
  Installed PlotUtils ─────────────────── v1.0.2
  Installed Mustache ──────────────────── v1.0.2
  Installed DataValueInterfaces ───────── v1.0.0
  Installed FFTW ──────────────────────── v1.2.1
  Installed IntelOpenMP_jll ───────────── v2018.0.3+0
  Installed Polynomials ───────────────── v0.8.0
  Installed IterTools ─────────────────── v1.3.0
  Installed FFTW_jll ──────────────────── v3.3.9+5
  Installed MKL_jll ───────────────────── v2019.0.117+2
  Installed YAML ──────────────────────── v0.4.0
   Building Plots → `~/.julia/packages/Plots/zOV0T/deps/build.log`
   Building FFTW ─→ `~/.julia/packages/FFTW/5DZuu/deps/build.log`
Downloading artifact: IntelOpenMP
######################################################################## 100.0%##O=#  #                               Downloading artifact: FFTW
######################################################################## 100.0%##O=#  #                          

```

To test, I load `Weave` into the `REPL`.

```julia
julia> using Weave
[ Info: Precompiling Weave [44d3d7a6-8a23-5bf8-98c5-b353f8df5ec9]
```

Everything seems to be fine. 😄

Now if you check, you will see a `~/.julia` has been recreated.

```julia
shell> ls ~/.julia # Press ; to get shell prompt
artifacts  compiled  conda  environments  logs	packages  prefs  registries
```

So one last thing is to do is to restore my `config` folder by.
```julia
shell> cp -r ~/Downloads/.julia/config/ ~/.julia
```
and remove the backup
```julia
shell> rm -rf ~/Downloads/.julia/config/
```
