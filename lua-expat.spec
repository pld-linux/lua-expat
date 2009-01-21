Summary:	LuaExpat is a SAX XML parser based on the Expat library
Summary(hu.UTF-8):	LuaExpat egy SAX XML elemző az Expat könyvtárra épülve
Name:		lua-expat
Version:	1.1
Release:	0.1
License:	BSD-like
Group:		Development/Languages
Source0:	http://luaforge.net/frs/download.php/2469/luaexpat-%{version}.tar.gz
URL:		http://luaforge.net/projects/luaexpat/
BuildRequires:	expat-devel
BuildRequires:	lua51-devel
BuildRequires:	sed >= 4.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
LuaExpat is a SAX XML parser based on the Expat library.

%description -l hu.UTF-8
LuaExpat egy SAX XML elemző az Expat könyvtárra épülve.

%prep
%setup -q -n luaexpat-%{version}
%{__sed} -i "s@usr/local@usr@g ; s@5\.0@5.1@ ; s@^LUA_INC.*@LUA_INC= %{_includedir}/lua51@ ; \
	s@LUA_VERSION_NUM= 500@LUA_VERSION_NUM= 501@" config

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_datadir},%{_libdir}}/lua/5.1
install src/lxp.so* $RPM_BUILD_ROOT%{_libdir}/lua/5.1
install -d $RPM_BUILD_ROOT%{_datadir}/lua/5.1/lxp
install src/lxp/lom.lua $RPM_BUILD_ROOT%{_datadir}/lua/5.1/lxp
curdir=$(pwd)
cd $RPM_BUILD_ROOT%{_libdir}/lua/5.1
ln -sf lxp.so.1.1.0 lxp.so
cd $curdir

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README doc/us/*
%attr(755,root,root) %{_libdir}/lua/5.1/lxp*.so*
%dir %{_datadir}/lua/5.1/lxp
%{_datadir}/lua/5.1/lxp/*.lua
