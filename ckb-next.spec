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

# Required dependecies on the build step.
BuildRequires: qt5 qt5-qtbase-gui qt5-qtbase qt5-qtbase-devel
BuildRequires: quazip-qt5-devel dbusmenu-qt5 dbusmenu-qt5-devel
BuildRequires: quazip-qt5 xcb-util-wm-devel xcb-util-wm
BuildRequires: cmake pkgconfig qt5-qtx11extras-devel systemd-devel

#Prefix: $RPM_BUILD_ROOT
Provides: %{name}

# The release differentiate newer updates of the RPM itself.
# Symply starts at 1 and increment it when modifying the spec
# file and recreate the package.
Release: 1

Source1: %{name}.tar.gz
Source2: ckb-0.6.0-1.patch

ExclusiveArch: x86_64

ExclusiveOS: linux

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
# Create a git repo within the expanded tarball.
git init
git config user.email "r4u1974@gmail.com"
git config user.name "Raul Vilchez"
git add .
git commit -a -q -m "ckb-next-%{version} baseline."
# Apply all the patches on top.
git am %{patches}

###
### Pre. It runs scripts prior to installation. 
###

%pre
# Find out how many cores the system has, for make
if [[ -z "$JOBS" ]]; then
	JOBS=$(getconf _NPROCESSORS_ONLN 2>/dev/null)
fi

# Default to 2 jobs if something went wrong earlier
if [[ -z "$JOBS" ]]; then
    JOBS=2
fi

###
### Build section
###

%build
rm -rf $RPM_BUILD_ROOT
cmake -H. -Bbuild -DCMAKE_BUILD_TYPE=Release -DSAFE_INSTALL=ON -DSAFE_UNINSTALL=ON
cmake --build build --target linux -- -j "$JOBS"
###
### Install section
###

%install
rm -fr $RPM_BUILD_ROOT
sudo cmake --build build --target install

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
