#define gitdate 20130117

Summary:Gnome integration for i3
Name: i3-gnome
Version: 4.0
Release: 0chadv1%{?dist}
License: GPL
Group: System Environment/Libraries
URL: http://i3wm.org
BuildArch:noarch
Requires: gnome-session i3 gdm-control

%description
Gnome integration for the i3 window manager

%prep

%build

%install
install -D -m 755 %{_sourcedir}/bin/i3-gnome $RPM_BUILD_ROOT%{_bindir}/i3-gnome 
install -D -m 644 %{_sourcedir}/share/xsessions/i3-gnome.desktop $RPM_BUILD_ROOT/usr/share/xsessions/i3-gnome.desktop 
install -D -m 644 %{_sourcedir}/share/gnome-session/sessions/i3-gnome.session $RPM_BUILD_ROOT/usr/share/gnome-session/sessions/i3-gnome.session
install -D -m 644 %{_sourcedir}/share/applications/i3-gnome.desktop $RPM_BUILD_ROOT/usr/share/applications/i3-gnome.desktop 

%post -p /usr/bin/update-desktop-database -q
%postun -p /usr/bin/update-desktop-database -q

%files
%defattr(-,root,root,-)
%{_bindir}/i3-gnome
/usr/share/applications/i3-gnome.desktop
/usr/share/gnome-session/sessions/i3-gnome.session
/usr/share/xsessions/i3-gnome.desktop

%changelog
* Fri Mar 08 2013 Chad Versace <chad@chad-versace.us> 4.0-0chadv1
- Copy from https://aur.archlinux.org/packages/i3-gnome/ .
