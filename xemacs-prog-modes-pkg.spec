%define 	srcname	prog-modes
Summary:	XEmacs modes for various programming languages
Summary(pl):	XEmacsowe tryby do rozmaitych jêzyków programowania
Name:		xemacs-%{srcname}-pkg
Version:	1.53
Release:	1
License:	GPL
Group:		Applications/Editors/Emacs
Source0:	ftp://ftp.xemacs.org/xemacs/packages/%{srcname}-%{version}-pkg.tar.gz
URL:		http://www.xemacs.org/
BuildArch:	noarch
Conflicts:	xemacs-sumo
Requires:	xemacs
Requires:	xemacs-mail-lib-pkg
Requires:	xemacs-devel-pkg
Requires:	xemacs-base-pkg
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
XEmacs modes for various programming languages: Perl, Python, SQL,
AWK, TCL and many more.

%description -l pl
XEmacsowe tryby do kilkunastu rozmaitych jêzyków programowania, m.in.
do: Perla, Pythona, SQLa, AWKa i TCLa.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/xemacs-packages

cp -a * $RPM_BUILD_ROOT%{_datadir}/xemacs-packages

gzip -9nf lisp/prog-modes/ChangeLog

# remove .el file if corresponding .elc file exists
find $RPM_BUILD_ROOT -type f -name "*.el" | while read i; do test ! -f ${i}c || rm -f $i; done

%clean
rm -fr $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc lisp/prog-modes/ChangeLog.gz
%dir %{_datadir}/xemacs-packages/lisp/*
%{_datadir}/xemacs-packages/lisp/*/*.el*
