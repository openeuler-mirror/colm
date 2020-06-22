#%global debug_package %{nil}

Name:    colm
Version: 0.14.1
Release: 1
Summary: Colm is a programming language designed for the analysis and transformation of computer languages
License: MIT and LGPLv2+
URL:	 http://www.colm.net/open-source/%{name}
Source0: https://www.colm.net/files/colm/%{name}-%{version}.tar.gz

BuildRequires: 	gcc autoconf automake asciidoc make 

%description
Colm is a programming language designed for the analysis and transformation of computer languages. Colm is influenced primarily by TXL. It is in the family of program transformation languages.

%package devel
Summary: devel package for colm
Requires: %{name} = %{version}-%{release}
%description devel
Colm is a programming language designed for the analysis and transformation of computer languages. Colm is influenced primarily by TXL. It is in the family of program transformation languages.


%prep
%setup -q -n %{name}-%{version}/

%build
%configure
%make_build

%install
%make_install
rm -rf %{buildroot}/%{_libdir}/*.la
rm -rf %{buildroot}/%{_libdir}/*.a
install -d %{buildroot}/usr/share/%{name}
mv %{buildroot}/usr/share/*.lm %{buildroot}/usr/share/%{name}
mv %{buildroot}/usr/share/runtests %{buildroot}/usr/share/%{name}

%pre
%preun
%post
%postun

%check

%files
%license COPYING 
%doc README 
%{_bindir}/*
%{_libdir}/libcolm-%{version}.so
%{_libdir}/libfsm.so.*


%files devel
%{_includedir}/*
%{_libdir}/libcolm.so
%{_libdir}/libfsm.so
%{_docdir}/%{name}/*
/usr/share/%{name}/*

%changelog
* Sun Mar 29 2020 Wei Xiong <myeuler@163.com>
- Package init

