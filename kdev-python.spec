%define kdevelop_ver 5.%(echo %{version} | cut -d. -f2,3)

Summary:	Python plugin for kdevelop
Name:		kdev-python
Version:	22.03.90
Release:	1
License:	GPLv2+
Group:		Development/Other
Url:		http://www.kdevelop.org
Source0:	http://download.kde.org/stable/kdevelop/%{kdevelop_ver}/src/%{name}-%{version}.tar.xz
BuildRequires:	kdevplatform-devel >= 4:%{version}
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
Requires:	kdevelop >= 4:%{kdevelop_ver}

%description
This plugin adds python language support (including classview 
and code-completion) to KDevelop.

%files -f kdevpython.lang
%{_datadir}/qlogging-categories5/kdevpythonsupport.categories
%{_libdir}/libkdevpythoncompletion.so
%{_libdir}/libkdevpythonduchain.so
%{_libdir}/libkdevpythonparser.so
%{_libdir}/qt5/plugins/kdevplatform/35/*.so
%{_datadir}/kdevappwizard/templates/*.tar.bz2
%{_datadir}/kdevpythonsupport
%{_datadir}/metainfo/*.xml
#--------------------------------------------------------------------

%prep
%setup -q

%build
%cmake_kde5 -DBSDTAR=1 -DBUILD_TESTING=OFF
%ninja

%install
%ninja_install -C build

%find_lang kdevpython

