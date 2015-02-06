%define	name	pyopenal
%define	oname	PyOpenAL
%define version 0.1.6
%define release 3
%{expand:%%define py_ver %(python -V 2>&1| awk '{print $2}'|cut -d. -f1-2)}

Name:		%{name}
Version:	%{version}
Release:	%mkrel %{release}
License:	GPL
Url:		http://home.gna.org/oomadness/en/pyopenal/
Source0:	http://download.gna.org/pyopenal/%{oname}-%{version}.tar.bz2
Group:		Development/Python
Summary:	OpenAL port to Python
BuildRequires:	python-devel openal-devel freealut-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
OpenAL port to Python.

%prep
%setup -q -n %{oname}-%{version}

%build
%{__python} setup.py build

%install
%{__rm} -rf $RPM_BUILD_ROOT
%{__python} setup.py install --root=$RPM_BUILD_ROOT

%clean
%{__rm} -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README CHANGES AUTHORS
%{_libdir}/python%{py_ver}/site-packages/%{name}
%{_libdir}/python%{py_ver}/site-packages/_openal.so
%{_libdir}/python%{py_ver}/site-packages/*.egg-info




%changelog
* Tue Sep 15 2009 Thierry Vignaud <tv@mandriva.org> 0.1.6-2mdv2010.0
+ Revision: 442000
- rebuild

* Fri Dec 21 2007 Olivier Blin <oblin@mandriva.com> 0.1.6-1mdv2008.1
+ Revision: 136445
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Sat Dec 09 2006 Emmanuel Andry <eandry@mandriva.org> 0.1.6-1mdv2007.0
+ Revision: 94099
- New version 0.1.6
  buildrequires freealut-devel
- Import pyopenal

* Wed Aug 24 2005 Per Øyvind Karlsen <pkarlsen@mandriva.com> 0.1.5-1mdk
- 0.1.5
- %%mkrel

* Sun Dec 05 2004 Michael Scherer <misc@mandrake.org> 0.1.4-2mdk
- Rebuild for new python

* Fri Jul 09 2004 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 0.1.4-1mdk
- 0.1.4
- drop P0 (merged upstream)

* Mon Mar 08 2004 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 0.1.3-2mdk
- fix build with newer openal snapshots(P0)

* Wed Mar 03 2004 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 0.1.3-1mdk
- 0.1.3
- py_ver macro
- fix buildrequires (lib64..)
- updated url

