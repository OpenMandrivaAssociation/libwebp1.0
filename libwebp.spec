%define major 4

%define	libname %mklibname webp %major
%define	devellibname %mklibname -d webp

Name:		libwebp
Version:	0.2.1
Release:	1
Group:		Development/C
URL:		http://webmproject.org/
Summary:	Library and tools for the WebP graphics format
# Additional IPR is licensed as well. See PATENTS file for details
License:	BSD
Source0:	http://webp.googlecode.com/files/%{name}-%{version}.tar.gz
BuildRequires:	jpeg-devel libpng-devel libtool swig

%description
WebP is an image format that does lossy compression of digital
photographic images. WebP consists of a codec based on VP8, and a
container based on RIFF. Webmasters, web developers and browser
developers can use WebP to compress, archive and distribute digital
images more efficiently.

%package tools
Group:		Development/Other
Summary:	The WebP command line tools

%description tools
WebP is an image format that does lossy compression of digital
photographic images. WebP consists of a codec based on VP8, and a
container based on RIFF. Webmasters, web developers and browser
developers can use WebP to compress, archive and distribute digital
images more efficiently.

%package -n	%{libname}
Group:		Development/C
Summary:	Library for the WebP format
Provides:	webp-devel = %{version}-%{release}

%description -n %{libname}
WebP is an image format that does lossy compression of digital
photographic images. WebP consists of a codec based on VP8, and a
container based on RIFF. Webmasters, web developers and browser
developers can use WebP to compress, archive and distribute digital
images more efficiently.

%package -n	%{devellibname}
Group:		Development/C
Summary:	Development files for libwebp, a library for the WebP format
Requires:	%{libname} = %{version}-%{release}

%description -n %{devellibname}
WebP is an image format that does lossy compression of digital
photographic images. WebP consists of a codec based on VP8, and a
container based on RIFF. Webmasters, web developers and browser
developers can use WebP to compress, archive and distribute digital
images more efficiently.

%prep
%setup -q
find . -perm 0640 | xargs chmod 0644

%build
mkdir -p m4
./autogen.sh
%configure2_5x --disable-static 
#--enable-experimental-libwebpmux
%make

%install
%makeinstall_std
find "%{buildroot}/%{_libdir}" -type f -name "*.la" -delete

%files tools
%{_bindir}/*
%{_mandir}/man*/*

%files -n %{libname}
%doc README PATENTS COPYING NEWS AUTHORS
%{_libdir}/%{name}*.so.%{major}*

%files -n %{devellibname}
%{_libdir}/%{name}*.so
%{_includedir}/*
%{_libdir}/pkgconfig/*
