Name:		texlive-seuthesix
Version:	40088
Release:	2
Summary:	LaTeX class for theses at Southeast University, Nanjing, China
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/seuthesix
License:	gpl3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/seuthesix.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/seuthesix.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/seuthesix.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This project provides a LaTeX document class as well as a
bibliography style file for typesetting theses at the Southeast
University, Nanjing, China. It is based on the seuthesis
package which, according to the author of seuthesix, is buggy
and has not been maintained for some time.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/seuthesix
%{_texmfdistdir}/tex/latex/seuthesix
%{_texmfdistdir}/bibtex/bst/seuthesix
%doc %{_texmfdistdir}/doc/latex/seuthesix

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
