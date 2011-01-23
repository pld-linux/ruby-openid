
%define gitrev 8e979da
%define gitauthor openid
%define gitname ruby-openid

Summary:	OpenID library for Ruby
Name:		ruby-openid
Version:	2.1.8
Release:	1
License:	Apache
Group:		Development/Libraries
Source0:	http://download.github.com/%{gitauthor}-%{gitname}-%{gitrev}.tar.gz
# Source0-md5:	dea26c5dbe0435ecb845bdcaed825d08
#Patch0:	%{name}-nogems.patch
URL:		http://github.com/openid/ruby-openid
BuildRequires:	rpmbuild(macros) >= 1.277
BuildRequires:	ruby
BuildRequires:	ruby-modules
BuildRequires:	setup.rb >= 3.4.1
%{?ruby_mod_ver_requires_eq}
#BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Grit gives you object oriented read/write access to Git repositories via Ruby.
The main goals are stability and performance. To this end, some of the
interactions with Git repositories are done by shelling out to the system's
`git` command, and other interactions are done with pure Ruby reimplementations
of core Git functionality. This choice, however, is transparent to end users,
and you need not know which method is being used.

%prep
%setup -q -n %{gitauthor}-%{gitname}-%{gitrev}
#%patch0 -p1
cp %{_datadir}/setup.rb .
ruby setup.rb config \
	--installdirs=std
ruby setup.rb setup

%install
rm -rf $RPM_BUILD_ROOT

ruby setup.rb install \
	--prefix=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{ruby_rubylibdir}/openid.rb
%{ruby_rubylibdir}/openid
%{ruby_rubylibdir}/hmac
