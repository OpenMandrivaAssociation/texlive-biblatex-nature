# revision 23952
# category Package
# catalog-ctan /macros/latex/contrib/biblatex-contrib/biblatex-nature
# catalog-date 2011-09-14 17:59:09 +0200
# catalog-license lppl
# catalog-version 1.2
Name:		texlive-biblatex-nature
Version:	1.2
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
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
The bundle offers styles that allow authors to use biblatex
when preparing papers for submission to the journal Nature.

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
%{_texmfdistdir}/bibtex/bib/biblatex-nature/biblatex-nature.bib
%{_texmfdistdir}/tex/latex/biblatex-nature/nature.bbx
%{_texmfdistdir}/tex/latex/biblatex-nature/nature.cbx
%doc %{_texmfdistdir}/doc/latex/biblatex-nature/README
%doc %{_texmfdistdir}/doc/latex/biblatex-nature/biblatex-nature.pdf
%doc %{_texmfdistdir}/doc/latex/biblatex-nature/biblatex-nature.tex
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar bibtex tex doc %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
