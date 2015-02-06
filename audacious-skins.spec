%define name audacious-skins
%define version 1.0.0
%define release 9

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




%changelog
* Thu Dec 09 2010 Oden Eriksson <oeriksson@mandriva.com> 1.0.0-8mdv2011.0
+ Revision: 616631
- the mass rebuild of 2010.0 packages

* Tue Sep 01 2009 Thierry Vignaud <tv@mandriva.org> 1.0.0-7mdv2010.0
+ Revision: 423983
- rebuild

* Thu Jun 19 2008 Thierry Vignaud <tv@mandriva.org> 1.0.0-6mdv2009.0
+ Revision: 226196
- rebuild

* Wed Jan 02 2008 Olivier Blin <oblin@mandriva.com> 1.0.0-5mdv2008.1
+ Revision: 140690
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Thu Feb 01 2007 Nicolas Lécureuil <neoclust@mandriva.org> 1.0.0-5mdv2007.0
+ Revision: 115824
- Rebuild to have good release
- Import audacious-skins

* Fri Dec 16 2005 Eskild Hustvedt <eskild@mandriva.org> 1.0.0-4mdk
- Fixed description (thanks to Tim Sawchuck for complaining :P)

* Fri Dec 16 2005 Eskild Hustvedt <eskild@mandriva.org> 1.0.0-3mdk
- Renamed from beep-media-player-skins

* Tue Mar 29 2005 Eskild Hustvedt <eskild@mandrake.org> 1.0.0-2mdk
- %%mkrel

* Fri Mar 04 2005 Eskild Hustvedt <eskild@mandrake.org> 1.0.0-1mdk
- Initial Mandrakelinux package
	o Spec and source taken from xmms-skins

