%define 	srcname	prog-modes
Summary:	XEmacs modes for various programming languages
Summary(pl.UTF-8):	XEmacsowe tryby do rozmaitych języków programowania
Name:		xemacs-%{srcname}-pkg
Version:	1.91
Release:	3
License:	GPL
Group:		Applications/Editors/Emacs
Source0:	http://ftp.xemacs.org/xemacs/packages/%{srcname}-%{version}-pkg.tar.gz
# Source0-md5:	b0203d7e022fdf730845ffbceaf41bf0
URL:		http://www.xemacs.org/
BuildArch:	noarch
Conflicts:	xemacs-sumo
Requires:	xemacs
Requires:	xemacs-mail-lib-pkg
Requires:	xemacs-devel-pkg
Requires:	xemacs-base-pkg
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
XEmacs modes for various programming languages: Perl, SQL,
AWK, Tcl and many more.

%description -l pl.UTF-8
XEmacsowe tryby do kilkunastu rozmaitych języków programowania, m.in.
do: Perla, SQL-a, AWK-a i Tcl-a.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/xemacs-packages

cp -a * $RPM_BUILD_ROOT%{_datadir}/xemacs-packages

# remove .el file if corresponding .elc file exists
find $RPM_BUILD_ROOT -type f -name "*.el" | while read i; do test ! -f ${i}c || rm -f $i; done

%clean
rm -fr $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc lisp/prog-modes/ChangeLog
%dir %{_datadir}/xemacs-packages/lisp/*
%{_datadir}/xemacs-packages/lisp/*/*.el*
