
%define		_theme		login-scan-fusion

Summary:	login-scan 'fusion' KDM theme
Summary(pl.UTF-8):	Motyw KDM login-scan 'fusion'
Name:		kdm-theme-%{_theme}
Version:	0.3.1
Release:	2
License:	GPL
Group:		X11/Amusements
Source0:	http://www.rokkford.de/loginscanfusion/%{_theme}-0-3-1.tar.gz
# Source0-md5:	8864027a6f865fa324cec7676c13e9d7
URL:		http://www.kde-look.org/content/show.php?content=26718
Requires:	kdebase-desktop >= 9:3.2.0
Requires:	kdm >= 9:3.4.0
Obsoletes:	kdm-theme-login-scan-integrated
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
login-scan 'fusion' KDM Theme.

%description -l pl.UTF-8
Motyw KDM login-scan 'fusion'.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/apps/kdm/themes/%{_theme}

install %{_theme}/*.{desktop,png,xml} $RPM_BUILD_ROOT%{_datadir}/apps/kdm/themes/%{_theme}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
#doc %{_theme}/README
%{_datadir}/apps/kdm/themes/%{_theme}
