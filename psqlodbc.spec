Summary:	psqlodbc
Summary(pl):	psqlodbc
Name:		psqlodbc
Version:	7.2.5
Release:	1
License:	BSD
Group:		Libraries
Source0:	ftp://ftp.us.postgresql.org/odbc/versions/src/%{name}-%{version}.tar.gz
URL:		http://gborg.postgresql.org/project/%{name}/projdisplay.php
BuildRequires:	postgresql-devel
BuildRequires:	unixODBC-devel
Requires:	postgresql-libs
Requires:	unixODBC
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
psqlodbc

%description -l pl
psqlodbc

%prep
%setup -q

%build
%configure \
    --with-unixodbc
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/*.so
%{_libdir}/*.la
%{_datadir}/%{name}/*
