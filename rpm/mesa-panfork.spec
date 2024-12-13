Name:       mesa

Summary:    Mesa graphics libraries
Version:    23.0.0
Release:    0
License:    MIT
URL:        http://www.mesa3d.org/
Source0:    %{name}-%{version}.tar.bz2
Patch1:     disable-avx-support.diff
Patch2:     0001-meson-fix-filename-printed-when-generating-devenv-fi.patch
Patch3:     0002-meson-megadriver-fix-install-message-to-match-the-re.patch
Patch4:     0003-meson-megadriver-stop-removing-the-master-.so-file.patch
Patch5:     0004-meson-megadriver-replace-hardlinks-with-symlinks.patch

BuildRequires:  pkgconfig(libdrm)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-egl)
BuildRequires:  pkgconfig(wayland-protocols)
BuildRequires:  pkgconfig(wayland-server)
BuildRequires:  pkgconfig(zlib) >= 1.2.3
BuildRequires:  pkgconfig meson
BuildRequires:  expat-devel >= 2.0
BuildRequires:  python3-devel
BuildRequires:  python3-mako
BuildRequires:  bison
BuildRequires:  flex
BuildRequires:  llvm-devel
BuildRequires:  gettext
BuildRequires:  clang-devel
BuildRequires:  libzstd-devel
BuildRequires:  kernel-headers

%description
Mesa is an open-source implementation of the OpenGL specification  -
a system for rendering interactive 3D graphics.


%package libgbm
Summary:    Generic buffer management API
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig
Provides:   libgbm = %{version}-%{release}

%description libgbm
Generic buffer management API

%package libgbm-devel
Summary:    Mesa libgbm development package
Requires:   %{name}-libgbm = %{version}-%{release}
Provides:   libgbm-devel

%description libgbm-devel
Mesa libgbm development package.

%package libglapi
Summary:    Mesa shared gl api library
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig

%description libglapi
Mesa shared gl api library.

%package libGLESv1
Summary:    Mesa libGLESv1 runtime libraries
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig
Provides:   libGLESv1 = %{version}-%{release}

%description libGLESv1
Mesa libGLESv1 runtime library.

%package libGLESv2
Summary:    Mesa libGLESv2 runtime libraries
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig
Provides:   libGLESv2 = %{version}-%{release}

%description libGLESv2
Mesa libGLESv2 runtime library.

%package libEGL
Summary:    Mesa libEGL runtime libraries and DRI drivers
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig
Provides:   libEGL = %{version}-%{release}

%description libEGL
Mesa libEGL runtime library.

%package libglapi-devel
Summary:    Mesa libglapi development package
Requires:   %{name}-libglapi = %{version}-%{release}
Provides:   libglapi-devel

%description libglapi-devel
Mesa libglapi development package.

%package libGLESv1-devel
Summary:    Mesa libGLESv1 development package
Requires:   %{name}-libGLESv1 = %{version}-%{release}
Provides:   libGLESv1-devel

%description libGLESv1-devel
Mesa libGLESv1 development packages

%package libGLESv2-devel
Summary:    Mesa libGLESv2 development package
Requires:   %{name}-libGLESv2 = %{version}-%{release}
Provides:   libGLESv2-devel

%description libGLESv2-devel
Mesa libGLESv2 development packages

%package libEGL-devel
Summary:    Mesa libEGL development package
Requires:   %{name}-libEGL = %{version}-%{release}
Provides:   libEGL-devel

%description libEGL-devel
Mesa libEGL development packages

%package libGL-devel
Summary:    Mesa libGL development package
Requires:   %{name}-libGL = %{version}-%{release}
Provides:   libGL-devel

%description libGL-devel
Mesa libGL development packages

%package dri-drivers
Summary:    Mesa-based DRI drivers
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig
Provides:   mesa-dri-drivers = %{version}-%{release}

%description dri-drivers
Mesa-based dri drivers.

%package dri-drivers-devel
Summary:    Mesa-based DRI development files

%description dri-drivers-devel
Mesa-based DRI driver development files.

%prep
%autosetup -p1 -n %{name}-%{version}/mesa
# Compilation fix: https://gitlab.freedesktop.org/mesa/mesa/-/issues/6505
sed -i -e "s/'instcombine'/'instcombine', 'passes'/" meson.build

%build
%meson \
    -Dcpp_rtti=false \
    -Ddri3=disabled \
    -Degl=enabled \
    -Dgallium-drivers=swrast,panfrost \
    -Dgallium-opencl=disabled \
    -Dgallium-va=disabled \
    -Dgallium-vdpau=disabled \
    -Dgallium-xa=disabled \
    -Dgles1=enabled \
    -Dgles2=enabled \
    -Dglvnd=false \
    -Dglx=disabled \
    -Dintel-clc=auto \
    -Dlibunwind=disabled \
    -Dllvm=enabled \
    -Dlmsensors=disabled \
    -Dmicrosoft-clc=disabled \
    -Dosmesa=false \
    -Dplatforms=wayland \
    -Dshared-llvm=disabled \
    -Dvalgrind=disabled \
    -Dvulkan-drivers= \
    -Dvulkan-layers=device-select \
    -Dxlib-lease=disabled \
    -Dzstd=disabled

%meson_build

%install
%meson_install

# Remove empty file created by build
rm -rf %{buildroot}/%{_libdir}/dri/kms_swrast_dri.so

%post libgbm -p /sbin/ldconfig

%postun libgbm -p /sbin/ldconfig

%post libglapi -p /sbin/ldconfig

%postun libglapi -p /sbin/ldconfig

%post libGLESv1 -p /sbin/ldconfig

%postun libGLESv1 -p /sbin/ldconfig

%post libGLESv2 -p /sbin/ldconfig

%postun libGLESv2 -p /sbin/ldconfig

%post libEGL -p /sbin/ldconfig

%postun libEGL -p /sbin/ldconfig

%post dri-drivers -p /sbin/ldconfig

%postun dri-drivers -p /sbin/ldconfig

%files
%license docs/license.rst

%files libgbm
%{_libdir}/libgbm.so.*

%files libgbm-devel
/usr/include/gbm.h
%{_libdir}/libgbm.so
%{_libdir}/pkgconfig/gbm.pc

%files libglapi
%{_libdir}/libglapi.so.0
%{_libdir}/libglapi.so.0.*

%files libGLESv1
%{_libdir}/libGLESv1_CM.so.*

%files libGLESv2
%{_libdir}/libGLESv2.so.*

%files libEGL
%{_libdir}/libEGL.so.*

%files libglapi-devel
%{_libdir}/libglapi.so

%files libGLESv1-devel
%{_libdir}/libGLESv1_CM.so
%{_includedir}/GLES/egl.h
%{_includedir}/GLES/gl.h
%{_includedir}/GLES/glext.h
%{_includedir}/GLES/glplatform.h
%{_libdir}/pkgconfig/glesv1_cm.pc

%files libGLESv2-devel
%{_libdir}/libGLESv2.so
%{_includedir}/GLES2/gl2.h
%{_includedir}/GLES2/gl2ext.h
%{_includedir}/GLES2/gl2platform.h
%{_includedir}/GLES3/gl3.h
%{_includedir}/GLES3/gl31.h
%{_includedir}/GLES3/gl32.h
%{_includedir}/GLES3/gl3ext.h
%{_includedir}/GLES3/gl3platform.h
%{_libdir}/pkgconfig/glesv2.pc

%files libEGL-devel
%{_libdir}/libEGL.so
%dir %{_includedir}/EGL
%{_includedir}/EGL/egl.h
%{_includedir}/EGL/eglext.h
%{_includedir}/EGL/eglext_angle.h
%{_includedir}/EGL/eglplatform.h
%{_includedir}/EGL/eglmesaext.h
%dir %{_includedir}/KHR
%{_includedir}/KHR/khrplatform.h
%{_libdir}/pkgconfig/egl.pc

%files libGL-devel
%{_includedir}/GL/gl.h
%{_includedir}/GL/glcorearb.h
%{_includedir}/GL/glext.h
%dir %{_includedir}/GL/internal
%{_includedir}/GL/internal/dri_interface.h

%files dri-drivers-devel
%{_libdir}/pkgconfig/dri.pc

%files dri-drivers
%dir %{_datadir}/drirc.d
%{_datadir}/drirc.d/00-mesa-defaults.conf
%{_libdir}/dri/*.so
