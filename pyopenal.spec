%define	name	pyopenal
%define	oname	PyOpenAL
%define version 0.1.6
%define release 1
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


