%global tl_name seuthesix
%global tl_revision 40088

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.0.1
Release:	%{tl_revision}.1
Summary:	LaTeX class for theses at Southeast University, Nanjing, China
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/seuthesix
License:	gpl3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/seuthesix.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/seuthesix.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/seuthesix.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This project provides a LaTeX document class as well as a bibliography
style file for typesetting theses at the Southeast University, Nanjing,
China. It is based on the seuthesis package which, according to the
author of seuthesix, is buggy and has not been maintained for some time.

