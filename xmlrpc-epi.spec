# TODO:
# - write real summarys and %%descriptions
# - fix group for -progs subpackage
Summary:	XML-RPC EPI library
Name:		xmlrpc-epi
Version:	0.50
Release:	0.1
License:	BSD
Group:		Libraries
Source0:	http://prdownloads.sourceforge.net/xmlrpc-epi/%{name}-%{version}.tar.gz
Patch0:		%{name}-system-expat.patch
URL:		http://xmlrpc-epi.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	expat-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_includedir	%{_prefix}/include/%{name}

%description

%package devel
Summary:	Header files etc to develop XML-RPC applications
Group:		Development/Libraries
Requires:	%{name} = %{version}

%description devel

%package static
Summary:	Static XML-RPC EPI libraries
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}

%description static

%package progs
Summary:	XML-RPC sample programs
Group:		Applications/Text
Requires:	%{name} = %{version}

%description progs

%prep
%setup -q
%patch0 -p1

%build
rm -f missing
libtoolize --copy --force
aclocal
autoconf
mv COPYING COPYING.orig
automake -a -c -f
mv COPYING.orig COPYING
%configure \
	--program-prefix=xmlrpc-epi-
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT 

#don't remove COPYING from package, license require this.
gzip -9nf AUTHORS ChangeLog NEWS README COPYING

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%files devel
%defattr(644,root,root,755)
%doc *.gz 
%attr(755,root,root) %{_libdir}/lib*.so
%attr(755,root,root) %{_libdir}/lib*.la
%{_includedir}

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a

%files progs
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
