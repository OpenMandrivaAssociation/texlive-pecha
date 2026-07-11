%global tl_name pecha
%global tl_revision 15878

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.1
Release:	%{tl_revision}.1
Summary:	Print Tibetan text in the classic pecha layout style
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/language/tibetan/pecha
License:	gpl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/pecha.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/pecha.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The pecha class provides an environment for writing Tibetan on LaTeX2e
in the traditional Tibetan Pecha layout used for spiritual or
philosophical texts, using the cTib4TeX package by Oliver Corff. It
provides features like headers in different languages, page numbering in
Tibetan and more.

