# revision 15878
# category Package
# catalog-ctan /language/tibetan/pecha
# catalog-date 2006-10-13 13:00:52 +0200
# catalog-license gpl
# catalog-version 0.1
Name:		texlive-pecha
Version:	0.1
Release:	1
Summary:	Print Tibetan text in the classic pecha layout style
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/language/tibetan/pecha
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pecha.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pecha.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
The pecha class provides an environment for writing Tibetan on
LaTeX2e in the traditional Tibetan Pecha layout used for
spiritual or philosophical texts, using the cTib4TeX package by
Oliver Corff. It provides features like headers in different
languages, page numbering in Tibetan and more.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
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
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
