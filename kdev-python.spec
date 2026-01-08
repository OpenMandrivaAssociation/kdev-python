Summary:	Python plugin for kdevelop
Name:		kdev-python
Version:	25.12.1
Release:	1
License:	GPLv2+
Group:		Development/Other
Url:		https://www.kdevelop.org
Source0:	http://download.kde.org/%([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un)stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:	kdevplatform-devel >= %{EVRD}
BuildRequires:	kdevelop-pg-qt-devel >= 0.9.82
BuildRequires:	pkgconfig(python3)
BuildRequires:	pkgconfig(Qt6Core)
BuildRequires:	pkgconfig(Qt6Widgets)
BuildRequires:	pkgconfig(Qt6Test)
BuildRequires:	pkgconfig(Qt6WebEngineWidgets)
BuildRequires:	cmake(KF6Archive)
BuildRequires:	cmake(KF6ThreadWeaver)
BuildRequires:	cmake(KF6TextEditor)
BuildRequires:	cmake(KF6I18n)
BuildRequires:	cmake(KF6ItemModels)
BuildRequires:	cmake(KF6KCMUtils)
BuildRequires:	cmake(KDevelop)
Requires:	kdevelop >= %{EVRD}
BuildSystem:	cmake
BuildOption:	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON
BuildOption:	-DBSDTAR:BOOL=ON
BuildOption:	-DBUILD_TESTING:BOOL=OFF

%patchlist
kdev-python-python-3.14.patch

%description
This plugin adds python language support (including classview 
and code-completion) to KDevelop.

%files -f %{name}.lang
%{_datadir}/qlogging-categories6/kdevpythonsupport.categories
%{_libdir}/libkdevpythoncompletion.so
%{_libdir}/libkdevpythonduchain.so
%{_libdir}/libkdevpythonparser.so
%{_qtdir}/plugins/kdevplatform/*/*.so
%{_datadir}/kdevappwizard/templates/*.tar.bz2
%{_datadir}/kdevpythonsupport
%{_datadir}/metainfo/*.xml
