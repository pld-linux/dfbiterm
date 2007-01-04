Summary:	Terminal emulator for DirectFB
Summary(pl):	Emulator terminala dla DirectFB
Name:		dfbiterm
Version:	0.3
Release:	1
License:	GPL v2
Group:		Applications/Graphics
Source0:	http://republika.pl/rkd/%{name}-%{version}.tar.bz2
#Source0-md5:	c3df6a76ada315ebe1418c0292d1e82a
BuildRequires:	DirectFB-devel
BuildRequires:	libiterm-devel >= 0.5-4
Requires:	libiterm >= 0.5-4
Requires:	DirectFB-font-ft2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
dfbiterm is a terminal application for DirectFB.
It is capable to display 256 colors like xterm or rxvt.

%description -l pl
dfbiterm to emulator terminala dla DirectFB.
Potrafi wy¶wietliæ 256 kolorów, tak jak xterm czy rxvt.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README przeczytajto.txt
%attr(755,root,root) %{_bindir}/*
