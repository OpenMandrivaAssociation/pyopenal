%define	oname	PyOpenAL

%{expand:%%define py_ver %(python -V 2>&1| awk '{print $2}'|cut -d. -f1-2)}

Name:		pyopenal
Version:	0.1.6
Release:	4
License:	GPL
Url:		https://home.gna.org/oomadness/en/pyopenal/
Source0:	http://download.gna.org/pyopenal/%{oname}-%{version}.tar.gz
Group:		Development/Python
Summary:	OpenAL port to Python
BuildRequires:	python-devel
BuildRequires:	openal-devel
BuildRequires:	freealut-devel

%description
OpenAL port to Python.

%prep
%setup -q -n %{oname}-%{version}

%build
python setup.py build

%install
python setup.py install --root=%{buildroot}

%clean

%files
%doc README CHANGES AUTHORS
%{_libdir}/python%{py_ver}/site-packages/%{name}
%{_libdir}/python%{py_ver}/site-packages/_openal.so
%{_libdir}/python%{py_ver}/site-packages/*.egg-info
