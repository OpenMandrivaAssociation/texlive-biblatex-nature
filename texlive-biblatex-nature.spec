# revision 27234
# category Package
# catalog-ctan /macros/latex/contrib/biblatex-contrib/biblatex-nature
# catalog-date 2012-06-08 18:13:51 +0200
# catalog-license lppl
# catalog-version 1.2b
Name:		texlive-biblatex-nature
Version:	1.2b
Release:	1
Summary:	Biblatex support for Nature
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/biblatex-contrib/biblatex-nature
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/biblatex-nature.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/biblatex-nature.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The bundle offers styles that allow authors to use biblatex
when preparing papers for submission to the journal Nature.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/biblatex-nature/nature.bbx
%{_texmfdistdir}/tex/latex/biblatex-nature/nature.cbx
%doc %{_texmfdistdir}/doc/latex/biblatex-nature/README
%doc %{_texmfdistdir}/doc/latex/biblatex-nature/biblatex-nature.bib
%doc %{_texmfdistdir}/doc/latex/biblatex-nature/biblatex-nature.pdf
%doc %{_texmfdistdir}/doc/latex/biblatex-nature/biblatex-nature.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
