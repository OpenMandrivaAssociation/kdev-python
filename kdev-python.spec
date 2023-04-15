Summary:	Python plugin for kdevelop
Name:		kdev-python
Version:	23.03.90
Release:	1
License:	GPLv2+
Group:		Development/Other
Url:		http://www.kdevelop.org
Source0:	http://download.kde.org/%([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un)stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:	kdevplatform-devel >= %{EVRD}
BuildRequires:	kdevelop-pg-qt-devel >= 0.9.82
BuildRequires:	pkgconfig(python3)
BuildRequires:	pkgconfig(Qt5Core)
BuildRequires:	pkgconfig(Qt5Widgets)
BuildRequires:	pkgconfig(Qt5Test)
BuildRequires:	pkgconfig(Qt5WebKitWidgets)
BuildRequires:	cmake(KF5Archive)
BuildRequires:	cmake(KF5ThreadWeaver)
BuildRequires:	cmake(KF5TextEditor)
BuildRequires:	cmake(KF5I18n)
BuildRequires:	cmake(KF5ItemModels)
BuildRequires:	cmake(KF5KCMUtils)
BuildRequires:	cmake(KDevelop)
Requires:	kdevelop >= %{EVRD}

%description
This plugin adds python language support (including classview 
and code-completion) to KDevelop.

%files -f kdevpython.lang
%{_datadir}/qlogging-categories5/kdevpythonsupport.categories
%{_libdir}/libkdevpythoncompletion.so
%{_libdir}/libkdevpythonduchain.so
%{_libdir}/libkdevpythonparser.so
%{_libdir}/qt5/plugins/kdevplatform/*/*.so
%{_datadir}/kdevappwizard/templates/*.tar.bz2
%{_datadir}/kdevpythonsupport
%{_datadir}/metainfo/*.xml
#--------------------------------------------------------------------

%prep
%autosetup -p1
%cmake_kde5 -DBSDTAR=1 -DBUILD_TESTING=OFF

%build
%ninja_build -C build

%install
%ninja_install -C build

%find_lang kdevpython
