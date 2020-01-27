Name:       mesa-llvmpipe

Summary:    Mesa graphics libraries built for LLVMpipe
Version:    19.3.2
Release:    0
Group:      System/Libraries
License:    MIT
URL:        http://www.mesa3d.org/
Source0:    %{name}-%{version}.tar.bz2
Patch1:     disable-avx-support.diff

BuildRequires:  pkgconfig(libdrm)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(talloc)
BuildRequires:  pkgconfig(libudev) >= 160
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-egl)
BuildRequires:  pkgconfig(wayland-protocols)
BuildRequires:  pkgconfig(wayland-server)
BuildRequires:  pkgconfig meson
BuildRequires:  expat-devel >= 2.0
BuildRequires:  python3-devel
BuildRequires:  python3-mako
BuildRequires:  libxml2-python
BuildRequires:  bison
BuildRequires:  flex
BuildRequires:  llvm-devel
BuildRequires:  gettext

%description
Mesa is an open-source implementation of the OpenGL specification  -
a system for rendering interactive 3D graphics.


%package libgbm
Summary:    Generic buffer management API
Group:      System/Libraries
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig
Provides:   libgbm = %{version}-%{release}

%description libgbm
Generic buffer management API

%package libgbm-devel
Summary:    Mesa libgbm development package
Group:      System/Libraries
Requires:   %{name}-libgbm = %{version}-%{release}
Provides:   libgbm-devel

%description libgbm-devel
Mesa libgbm development package.

%package libglapi
Summary:    Mesa shared gl api library
Group:      System/Libraries
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig

%description libglapi
Mesa shared gl api library.

%package libGLESv1
Summary:    Mesa libGLESv1 runtime libraries
Group:      System/Libraries
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig
Provides:   libGLESv1 = %{version}-%{release}

%description libGLESv1
Mesa libGLESv1 runtime library.

%package libGLESv2
Summary:    Mesa libGLESv2 runtime libraries
Group:      System/Libraries
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig
Provides:   libGLESv2 = %{version}-%{release}

%description libGLESv2
Mesa libGLESv2 runtime library.

%package libEGL
Summary:    Mesa libEGL runtime libraries and DRI drivers
Group:      System/Libraries
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig
Provides:   libEGL = %{version}-%{release}

%description libEGL
Mesa libEGL runtime library.

%package libglapi-devel
Summary:    Mesa libglapi development package
Group:      System/Libraries
Requires:   mesa-llvmpipe-libglapi = %{version}-%{release}
Provides:   libglapi-devel

%description libglapi-devel
Mesa libglapi development package.

%package libGLESv1-devel
Summary:    Mesa libGLESv1 development package
Group:      Development/Libraries
Requires:   mesa-llvmpipe-libGLESv1 = %{version}-%{release}
Provides:   libGLESv1-devel

%description libGLESv1-devel
Mesa libGLESv1 development packages

%package libGLESv2-devel
Summary:    Mesa libGLESv2 development package
Group:      Development/Libraries
Requires:   mesa-llvmpipe-libGLESv2 = %{version}-%{release}
Provides:   libGLESv2-devel

%description libGLESv2-devel
Mesa libGLESv2 development packages

%package libEGL-devel
Summary:    Mesa libEGL development package
Group:      Development/Libraries
Requires:   mesa-llvmpipe-libEGL = %{version}-%{release}
Provides:   libEGL-devel

%description libEGL-devel
Mesa libEGL development packages

%package libGL-devel
Summary:    Mesa libGL development package
Group:      Development/Libraries
Requires:   mesa-llvmpipe-libGL = %{version}-%{release}
Provides:   libGL-devel

%description libGL-devel
Mesa libGL development packages

%package dri-drivers-devel
Summary:    Mesa-based DRI development files
Group:      Development/Libraries

%description dri-drivers-devel
Mesa-based DRI driver development files.

%package dri-swrast-driver
Summary:    Mesa-based DRI drivers
Group:      Graphics/Display and Graphics Adaptation
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig
Provides:   mesa-llvmpipe-dri-drivers = %{version}-%{release}

%description dri-swrast-driver
Mesa-based swrast DRI driver.

%prep
%setup -q -n %{name}-%{version}/mesa

%patch1 -p1

%build
%meson -Ddri-drivers= \
    -Dosmesa=none \
    -Ddri3=false \
    -Dllvm=true \
    -Dshared-llvm=false \
    -Dgallium-drivers=swrast \
    -Dvulkan-drivers= \
    -Dplatforms=drm,wayland \
    -Dglx=disabled \
    -Degl=true \
    -Dgles1=true \
    -Dgles2=true

%meson_build

%install
%meson_install

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

%post dri-swrast-driver -p /sbin/ldconfig

%postun dri-swrast-driver -p /sbin/ldconfig

%files libgbm
%defattr(-,root,root,-)
%{_libdir}/libgbm.so.*

%files libgbm-devel
%defattr(-,root,root,-)
/usr/include/gbm.h
%{_libdir}/libgbm.so
%{_libdir}/pkgconfig/gbm.pc

%files libglapi
%defattr(-,root,root,-)
%{_libdir}/libglapi.so.0
%{_libdir}/libglapi.so.0.*

%files libGLESv1
%defattr(-,root,root,-)
%{_libdir}/libGLESv1_CM.so.*

%files libGLESv2
%defattr(-,root,root,-)
%{_libdir}/libGLESv2.so.*

%files libEGL
%defattr(-,root,root,-)
%{_libdir}/libEGL.so.*

%files libglapi-devel
%defattr(-,root,root,-)
%{_libdir}/libglapi.so

%files libGLESv1-devel
%defattr(-,root,root,-)
%{_libdir}/libGLESv1_CM.so
%{_includedir}/GLES/egl.h
%{_includedir}/GLES/gl.h
%{_includedir}/GLES/glext.h
%{_includedir}/GLES/glplatform.h
%{_libdir}/pkgconfig/glesv1_cm.pc

%files libGLESv2-devel
%defattr(-,root,root,-)
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
%defattr(-,root,root,-)
%{_libdir}/libEGL.so
%dir %{_includedir}/EGL
%{_includedir}/EGL/egl.h
%{_includedir}/EGL/eglext.h
%{_includedir}/EGL/eglextchromium.h
%{_includedir}/EGL/eglplatform.h
%{_includedir}/EGL/eglmesaext.h
%dir %{_includedir}/KHR
%{_includedir}/KHR/khrplatform.h
%{_libdir}/pkgconfig/egl.pc

%files libGL-devel
%defattr(-,root,root,-)
%{_includedir}/GL/gl.h
%{_includedir}/GL/glcorearb.h
%{_includedir}/GL/glext.h
%dir %{_includedir}/GL/internal
%{_includedir}/GL/internal/dri_interface.h

%files dri-drivers-devel
%defattr(-,root,root,-)
%{_libdir}/pkgconfig/dri.pc

%files dri-swrast-driver
%defattr(-,root,root,-)
%dir %{_datadir}/drirc.d
%{_datadir}/drirc.d/00-mesa-defaults.conf
%{_libdir}/dri/swrast_dri.so
%{_libdir}/dri/kms_swrast_dri.so
