# Intel vulkan support needs libclc
#ifarch %{ix86} x86_64
#global platform_vulkan ,intel
#endif
%global vulkan_drivers swrast%{?platform_vulkan}

Name:       mesa-llvmpipe

Summary:    Mesa graphics libraries built for LLVMpipe
Version:    26.0.8
Release:    0
License:    MIT
URL:        https://github.com/sailfishos/mesa
Source0:    %{name}-%{version}.tar.bz2
Patch1:     disable-avx-support.diff

BuildRequires:  pkgconfig(libdrm)
BuildRequires:  pkgconfig(libelf)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-egl)
BuildRequires:  pkgconfig(wayland-protocols)
BuildRequires:  pkgconfig(wayland-server)
BuildRequires:  pkgconfig(zlib) >= 1.2.3
BuildRequires:  pkgconfig meson
BuildRequires:  expat-devel >= 2.0
BuildRequires:  python3-devel
BuildRequires:  python3-mako
BuildRequires:  python3-yaml
BuildRequires:  bison
BuildRequires:  flex
BuildRequires:  llvm-devel
BuildRequires:  gettext
BuildRequires:  glslang

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

%package libGLESv1-devel
Summary:    Mesa libGLESv1 development package
Requires:   mesa-llvmpipe-libGLESv1 = %{version}-%{release}
Provides:   libGLESv1-devel

%description libGLESv1-devel
Mesa libGLESv1 development packages

%package libGLESv2-devel
Summary:    Mesa libGLESv2 development package
Requires:   mesa-llvmpipe-libGLESv2 = %{version}-%{release}
Provides:   libGLESv2-devel

%description libGLESv2-devel
Mesa libGLESv2 development packages

%package libEGL-devel
Summary:    Mesa libEGL development package
Requires:   mesa-llvmpipe-libEGL = %{version}-%{release}
Provides:   libEGL-devel

%description libEGL-devel
Mesa libEGL development packages

%package libGL-devel
Summary:    Mesa libGL development package
Requires:   mesa-llvmpipe-libGL = %{version}-%{release}
Provides:   libGL-devel

%description libGL-devel
Mesa libGL development packages

%package dri-drivers-devel
Summary:    Mesa-based DRI development files

%description dri-drivers-devel
Mesa-based DRI driver development files.

%package dri-swrast-driver
Summary:    Mesa-based DRI drivers
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig
Provides:   mesa-llvmpipe-dri-drivers = %{version}-%{release}

%description dri-swrast-driver
Mesa-based swrast DRI driver.

%package vulkan-drivers
Summary:    Mesa vulkan drivers
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig
Requires:   vulkan
Provides:   vulkan-drivers

%description vulkan-drivers
Mesa vulkan drivers.

%prep
%autosetup -p1 -n %{name}-%{version}/mesa

%build
%meson \
    -Dandroid-libbacktrace=disabled \
    -Dcpp_rtti=false \
    -Ddisplay-info=disabled \
    -Degl=enabled \
    -Dgallium-drivers=llvmpipe,softpipe \
    -Dgallium-mediafoundation=disabled \
    -Dgallium-va=disabled \
    -Dgles1=enabled \
    -Dgles2=enabled \
    -Dglvnd=disabled \
    -Dglx=disabled \
    -Dintel-rt=disabled \
    -Dlibunwind=disabled \
    -Dllvm=enabled \
    -Dlmsensors=disabled \
    -Dmicrosoft-clc=disabled \
    -Dplatforms=wayland \
    -Dshared-llvm=disabled \
    -Dspirv-tools=disabled \
    -Dvalgrind=disabled \
    -Dvulkan-drivers=%{?vulkan_drivers} \
    -Dvulkan-layers=device-select \
    -Dxlib-lease=disabled \
    -Dzstd=disabled

%meson_build

%install
%meson_install

%post libgbm -p /sbin/ldconfig

%postun libgbm -p /sbin/ldconfig

%post libGLESv1 -p /sbin/ldconfig

%postun libGLESv1 -p /sbin/ldconfig

%post libGLESv2 -p /sbin/ldconfig

%postun libGLESv2 -p /sbin/ldconfig

%post libEGL -p /sbin/ldconfig

%postun libEGL -p /sbin/ldconfig

%post dri-swrast-driver -p /sbin/ldconfig

%postun dri-swrast-driver -p /sbin/ldconfig

%files
%license docs/license.rst

%files libgbm
%{_libdir}/libgbm.so.*

%files libgbm-devel
%{_includedir}/gbm.h
%{_includedir}/gbm_backend_abi.h
%{_libdir}/libgbm.so
%{_libdir}/gbm/dri_gbm.so
%{_libdir}/pkgconfig/gbm.pc

%files libGLESv1
%{_libdir}/libGLESv1_CM.so.*

%files libGLESv2
%{_libdir}/libGLESv2.so.*

%files libEGL
%{_libdir}/libEGL.so.*

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

%files vulkan-drivers
%{_libdir}/libVkLayer_MESA_device_select.so
%{_datadir}/vulkan/implicit_layer.d/VkLayer_MESA_device_select.json
%{_libdir}/libvulkan_lvp.so
%{_datadir}/vulkan/icd.d/lvp_icd.*.json
#ifarch %{ix86} x86_64
#{_libdir}/libvulkan_intel.so
#{_datadir}/vulkan/icd.d/intel_icd.*.json
#endif

%files dri-drivers-devel
%{_libdir}/pkgconfig/dri.pc

%files dri-swrast-driver
%dir %{_datadir}/drirc.d
%{_datadir}/drirc.d/00-mesa-defaults.conf
%{_libdir}/libgallium-*.so
