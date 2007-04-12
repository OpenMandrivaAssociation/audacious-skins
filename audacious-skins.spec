%define name audacious-skins
%define version 1.0.0
%define release %mkrel 5

Name: 		%{name}
Summary: 	Additional skins for Audacious
Version: 	%{version}
Release: 	%{release}
License: 	GPL
URL: 		http://www.xmms.org/
Source: 	audacious-skins.tar.bz2
Group: 		Sound
Requires: 	audacious unzip
Buildroot: 	%{_tmppath}/%{name}-%{version}
BuildArch:	noarch
Provides:	beep-media-player-skins
Obsoletes:	beep-media-player-skins

%description
Skins for Audacious. When you install this package the skins
will instantly become available from inside Audacious.
Browse them in the appearance category in the Audacious
preferences.
%prep

%install
rm -rf $RPM_BUILD_ROOT 
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/audacious

bzip2 -cd %{SOURCE0} | tar xf - -C $RPM_BUILD_ROOT/%{_datadir}/audacious

cat > README << EOF
This package is a collection of skins for audacious.
Most of them come from http://www.xmms.org
If you would like even more of them you can visit sites like:
  http://www.skinz.org
  http://www.customize.org
EOF

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-, root, root)
%doc README
%{_datadir}/audacious/Skins/*


