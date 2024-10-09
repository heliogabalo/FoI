###
### Introduction section
###

%define major 0
%define minor 6
%define patch 0
%define version %{major}.%{minor}.%{patch}
%define packager 'Territorio Linux'
%define distribution CentOS
%define vendor 'K. DeSouza'

Summary: Open-source driver for Corsair keyboards and mice.

License: GPLv2

Group: System Environment/Daemons

Distribution: %{distribution}

# The icon directive names an icon file stored in the RPM.
#Icon: linux/icons/48x48/apps/ckb-next.png

Name: ckb-next

#Prefix: $RPM_BUILD_ROOT
Provides: %{name}

# The release differentiate newer updates of the RPM itself.
# Symply starts at 1 and increment it when modifying the spec
# file and recreate the package.
Release: 1

Source0: %{name}.tar.gz

Excludeos: arm

## The vendor directive names the company or organization
## behind an RPM package.
Vendor: %{vendor}

## The Packager directive provides an optional name an e-mail
## for the person who created the RPM. Territorio Linux.
Packager: %{packager}

URL: https://github.com/ckb-next/ckb-next/wiki

Version: %{version}

##########################################
# Build locations  #######################
##########################################
# The build directory is the location where RPM actually builds.
# Automatic processing by RPM system, ocurs when changes to a 
# directory as part of the whole process.
# 
# The buildroot directory, acts as staging area and it looks like
# a final installation path.
# The buildroot name refers to the root, /.
Buildroot: %{name}-%{version}

%description
	Open-source driver for Corsair keyboards and mice.

	Major features:
	- Control multiple devices independently
	- United States and European keyboard layouts
	- Customizable key bindings
	- Per-key lighting and animation
	- Reactive lighting
	- Multiple profiles/modes with hardware save function
	- Adjustable mouse DPI with ability to change DPI on
		button press.
	- This project is maintained by:
	- https://github.com/ckb-next/ckb-next/wiki

###
### Prepare section
###

%prep
%setup -n %{name}

###
### Build section
###

%build
./quickinstall

###
### Install section
###

%install
rm -fr $RPM_BUILD_ROOT

###
### Clean section
###
%clean
rm -fr $RPM_BUILD_ROOT

###
### Files section
###

## If you don't include the full path to a documentation file or
## files, the RPM system will create a special documentation
## directory for the package, usually /usr/share/doc or /usr/doc.
## 

%files
%doc README.md LICENSE CHANGELOG.md

defattr(-, $USERNAME, $USERNAME)















