%define		luaver 5.3
%define		real_name luaexpat

%define		luasuffix %(echo %{luaver} | tr -d .)
%if "%{luaver}" == "5.1"
%define		luaincludedir %{_includedir}/lua51
%else
%define		luaincludedir %{_includedir}/lua%{luaver}
%endif
%define		lualibdir %{_libdir}/lua/%{luaver}
%define		luapkgdir %{_datadir}/lua/%{luaver}

Summary:	LuaExpat is a SAX XML parser based on the Expat library
Summary(hu.UTF-8):	LuaExpat egy SAX XML elemző az Expat könyvtárra épülve
Name:		lua%{luasuffix}-expat
Version:	1.3.0
Release:	1
License:	BSD-like
Group:		Development/Languages
Source0:	http://matthewwild.co.uk/projects/luaexpat/%{real_name}-%{version}.tar.gz
# Source0-md5:	3c20b5795e7107f847f8da844fbfe2da
Patch0:		makefile.patch
URL:		http://luaforge.net/projects/luaexpat/
BuildRequires:	expat-devel
BuildRequires:	lua%{luasuffix}-devel
BuildRequires:	sed >= 4.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
LuaExpat is a SAX XML parser based on the Expat library.

%description -l hu.UTF-8
LuaExpat egy SAX XML elemző az Expat könyvtárra épülve.

%prep
%setup -q -n %{real_name}-%{version}
%patch0 -p1

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags}" \
	LDFLAGS="%{rpmldflags}" \
	LUA_V="%{luaver}" \
	LUA_INC="-I%{luaincludedir}" \
	LUA_LDIR="%{luapkgdir}" \
	LUA_CDIR="%{lualibdir}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{luapkgdir},%{lualibdir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags}" \
	LDFLAGS="%{rpmldflags}" \
	LUA_V="%{luaver}" \
	LUA_INC="-I%{luaincludedir}" \
	LUA_LDIR="%{luapkgdir}" \
	LUA_CDIR="%{lualibdir}"

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README doc/us/*
%attr(755,root,root) %{lualibdir}/lxp*.so*
%dir %{luapkgdir}/lxp
%{luapkgdir}/lxp/*.lua
