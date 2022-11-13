Name:		texlive-pecha
Version:	15878
Release:	1
Summary:	Print Tibetan text in the classic pecha layout style
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/language/tibetan/pecha
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pecha.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pecha.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The pecha class provides an environment for writing Tibetan on
LaTeX2e in the traditional Tibetan Pecha layout used for
spiritual or philosophical texts, using the cTib4TeX package by
Oliver Corff. It provides features like headers in different
languages, page numbering in Tibetan and more.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/pecha/ctibmantra.sty
%{_texmfdistdir}/tex/latex/pecha/pecha.cls
%doc %{_texmfdistdir}/doc/latex/pecha/CHANGES
%doc %{_texmfdistdir}/doc/latex/pecha/COPYING
%doc %{_texmfdistdir}/doc/latex/pecha/README
%doc %{_texmfdistdir}/doc/latex/pecha/example.pdf
%doc %{_texmfdistdir}/doc/latex/pecha/example.tex
%doc %{_texmfdistdir}/doc/latex/pecha/pecha_docu.pdf
%doc %{_texmfdistdir}/doc/latex/pecha/pecha_docu.tex

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
