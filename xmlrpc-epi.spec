# TODO:
# - fix group for -progs subpackage
Summary:	XML-RPC EPI library - an implementation of the xmlrpc protocol
Summary(pl):	Biblioteka XML-RPC EPI - implementacja protoko³u xmlrpc
Name:		xmlrpc-epi
Version:	0.51
Release:	1
License:	BSD
Group:		Libraries
Source0:	http://dl.sourceforge.net/xmlrpc-epi/%{name}-%{version}.tar.gz
# Source0-md5:	51c5f062365f82ff1c26c2763e7f0654
Patch0:		%{name}-system-expat.patch
URL:		http://xmlrpc-epi.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	expat-devel
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_includedir	%{_prefix}/include/%{name}

%description
xmlrpc-epi is an implementation of the xmlrpc protocol in C. It
provides an easy to use API for developers to serialize RPC requests
to and from XML. It doesn't include a transport layer, such as
HTTP. The API is primarily based upon proprietary code written for
internal usage at Epinions.com, and was later modified to incorporate
concepts from the xmlrpc protocol. It passed the xmlrpc validation
test suite in December 2000.

%description -l pl
xmlrpc-epi to implementacja protoko³u xmlrpc napisana w C. Daje proste
w u¿yciu API dla programistów do serializacji ¿±dañ RPC do i z XML-a.
Nie zawiera warstwy transportowej typu HTTP. API bazuje g³ównie na
w³asno¶ciowym kodzie napisanym do u¿ytku wewnêtrznego na Epinions.com
i zosta³o pó¼niej zmodyfikowane, aby w³±czyæ idee protoko³u xmlrpc.
API to przesz³o test sprawdzaj±cy poprawno¶æ implementacji w grudniu
2000.

%package devel
Summary:	Header files etc to develop XML-RPC applications
Summary(pl):	Pliki nag³ówkowe do tworzenia aplikacji XML-RPC
Group:		Development/Libraries
Requires:	%{name} = %{version}

%description devel
Header files etc needed to develop XML-RPC applications.

%description devel -l pl
Pliki nag³ówkowe potrzebne do tworzenia aplikacji u¿ywaj±cych XML-RPC.

%package static
Summary:	Static XML-RPC EPI libraries
Summary(pl):	Biblioteki statyczne XML-RPC EPI
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
Static XML-RPC EPI libraries.

%description static -l pl
Biblioteki statyczne XML-RPC EPI.

%package progs
Summary:	XML-RPC sample programs
Summary(pl):	Programy przyk³adowe XML-RPC
Group:		Applications/Text
Requires:	%{name} = %{version}

%description progs
Sample programs for XML-RPC EPI library.

%description progs -l pl
Programy przyk³adowe do biblioteki XML-RPC EPI.

%prep
%setup -q
%patch0 -p1

%build
rm -f missing
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--program-prefix=xmlrpc-epi-
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%files devel
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog NEWS README
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a

%files progs
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
