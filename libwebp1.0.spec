%define major 7
%define libname %mklibname webp %{major}
%define devname %mklibname -d webp

Summary:	Old version of the WebP library
Name:		libwebp1.0
Version:	1.0.3
Release:	2
Group:		Development/C
# Additional IPR is licensed as well. See PATENTS file for details
License:	BSD
Url:		https://webmproject.org/
# https://chromium.googlesource.com/webm/libwebp/
# Take the last commit from the right branch --
# https://chromium.googlesource.com/webm/libwebp/+/%{version}
Source0:	https://chromium.googlesource.com/webm/libwebp/+archive/%{version}.tar.gz
Patch0:		libwebp-0.6.1-install-extras-lib.patch
BuildRequires:	libtool
BuildRequires:	swig
BuildRequires:	jpeg-devel
BuildRequires:	pkgconfig(libpng)

%description
WebP is an image format that does lossy compression of digital
photographic images. WebP consists of a codec based on VP8, and a
container based on RIFF. Webmasters, web developers and browser
developers can use WebP to compress, archive and distribute digital
images more efficiently.

#----------------------------------------------------------------------------

%package -n	%{libname}
Group:		Development/C
Summary:	Library for the WebP format (Old version)

%description -n %{libname}
WebP is an image format that does lossy compression of digital
photographic images. WebP consists of a codec based on VP8, and a
container based on RIFF. Webmasters, web developers and browser
developers can use WebP to compress, archive and distribute digital
images more efficiently.

%files -n %{libname}
%{_libdir}/libwebp.so.%{major}*

%libpackage webpmux 3
%libpackage webpdemux 2
%libpackage webpdecoder 3
%libpackage webpextras 0

#----------------------------------------------------------------------------

%prep
%autosetup -p1 -c libwebp-%{version}
./autogen.sh

%build
%ifarch aarch64
export CFLAGS="%{optflags} -frename-registers"
%endif
%configure --disable-static \
	--enable-libwebpmux \
	--enable-libwebpdemux \
	--enable-libwebpdecoder \
	--enable-libwebpextras
%make_build

%install
%make_install

# No -devel stuff or tools for compat libraries -- we get them
# from the current version (libwebp package)
rm -rf %{buildroot}%{_includedir} \
	%{buildroot}%{_libdir}/*.so \
	%{buildroot}%{_bindir} \
	%{buildroot}%{_libdir}/pkgconfig \
	%{buildroot}%{_datadir}
