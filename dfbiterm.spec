Summary:	Terminal emulator for DirectFB
Summary(pl):	Emulator terminala dla DirectFB
Name:		dfbiterm
Version:	0.1
Release:	3
License:	GPL v2
Group:		Applications/Graphics
Source0:	http://republika.pl/rkd/%{name}-%{version}.tar.bz2
#Source0-md5:	0477c55c67815a89542ee60c861e8453
Patch0:		%{name}-new.patch
Patch1:		%{name}-bold.patch
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
%patch0 -p1
%patch1 -p1

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
