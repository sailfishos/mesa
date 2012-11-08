# 
# Do NOT Edit the Auto-generated Part!
# Generated by: spectacle version 0.25
# 

Name:       mesa-llvmpipe

# >> macros
# << macros

Summary:    Mesa graphics libraries built for LLVMpipe
Version:    8.0.5
Release:    0
Group:      System/Libraries
License:    MIT
URL:        http://www.mesa3d.org/
Source0:    ftp://ftp.freedesktop.org/pub/mesa/%{version}/MesaLib-%{version}.tar.bz2
Source1:    mesa-llvmpipe-rpmlintrc
Source100:  mesa-llvmpipe.yaml
Patch0:     mesa-7.11-git-notimestamping.patch
Patch1:     0001-wayland-drm-Implement-wl_buffer.damage-in-old-versio.patch
Patch2:     0001-st-egl-Also-remove-wl_buffer_damage-in-wayland-backe.patch
Patch3:     0001-st-egl-Update-to-the-new-wl_shm_pool-interface.patch
Patch4:     0001-Stop-using-wl-buffer-damage.patch
Patch5:     mesa-8.0.3-llvm3.1.patch
BuildRequires:  pkgconfig(glproto)
BuildRequires:  pkgconfig(dri2proto) >= 1.1
BuildRequires:  pkgconfig(xproto)
BuildRequires:  pkgconfig(libdrm)
BuildRequires:  pkgconfig(xxf86vm)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xfixes)
BuildRequires:  pkgconfig(xdamage)
BuildRequires:  pkgconfig(xi)
BuildRequires:  pkgconfig(xmu)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(talloc)
BuildRequires:  pkgconfig(libudev) >= 160
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-server)
BuildRequires:  pkgconfig autoconf automake
BuildRequires:  expat-devel >= 2.0
BuildRequires:  python
BuildRequires:  libxml2-python
BuildRequires:  bison
BuildRequires:  flex
BuildRequires:  makedepend
BuildRequires:  llvm-devel

%description
Mesa is an open-source implementation of the OpenGL specification  -
a system for rendering interactive 3D graphics.


%package libglapi
Summary:    Mesa shared gl api library
Group:      System/Libraries
Requires:   %{name} = %{version}-%{release}
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig

%description libglapi
Mesa shared gl api library.

%package libGLESv1
Summary:    Mesa libGLESv1 runtime libraries
Group:      System/Libraries
Requires:   %{name} = %{version}-%{release}
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig
Provides:   libGLESv1 = %{version}-%{release}

%description libGLESv1
Mesa libGLESv1 runtime library.

%package libGLESv2
Summary:    Mesa libGLESv2 runtime libraries
Group:      System/Libraries
Requires:   %{name} = %{version}-%{release}
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig
Provides:   libGLESv2 = %{version}-%{release}

%description libGLESv2
Mesa libGLESv2 runtime library.

%package libGLESv2-compat
Summary:    Mesa libGLESv2 runtime compatibility library
Group:      System/Libraries
Requires:   %{name} = %{version}-%{release}
Requires:   libGLESv2.so.2
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig
Provides:   libGLESv2.so

%description libGLESv2-compat
Mesa libGLESv2 runtime compatibility library.

%package libEGL
Summary:    Mesa libEGL runtime libraries and DRI drivers
Group:      System/Libraries
Requires:   %{name} = %{version}-%{release}
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig
Provides:   libEGL = %{version}-%{release}

%description libEGL
Mesa libEGL runtime library.

%package libEGL-compat
Summary:    Mesa libEGL runtime compatibility library
Group:      System/Libraries
Requires:   %{name} = %{version}-%{release}
Requires:   libEGL.so.1
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig
Provides:   libEGL.so

%description libEGL-compat
Mesa libEGL runtime compatibility library.

%package libglapi-devel
Summary:    Mesa libglapi development package
Group:      System/Libraries
Requires:   %{name} = %{version}-%{release}
Requires:   mesa-llvmpipe-libglapi = %{version}-%{release}
Provides:   libglapi-devel

%description libglapi-devel
Mesa libglapi development package.

%package libGLESv1-devel
Summary:    Mesa libGLESv1 development package
Group:      Development/Libraries
Requires:   %{name} = %{version}-%{release}
Requires:   mesa-llvmpipe-libGLESv1 = %{version}-%{release}
Provides:   libGLESv1-devel

%description libGLESv1-devel
Mesa libGLESv1 development packages

%package libGLESv2-devel
Summary:    Mesa libGLESv2 development package
Group:      Development/Libraries
Requires:   %{name} = %{version}-%{release}
Requires:   mesa-llvmpipe-libGLESv2 = %{version}-%{release}
Provides:   libGLESv2-devel
Obsoletes:   mesa-llvmpipe-libGLESv2-compat

%description libGLESv2-devel
Mesa libGLESv2 development packages

%package libEGL-devel
Summary:    Mesa libEGL development package
Group:      Development/Libraries
Requires:   %{name} = %{version}-%{release}
Requires:   mesa-llvmpipe-libEGL = %{version}-%{release}
Provides:   libEGL-devel
Obsoletes:   mesa-llvmpipe-libEGL-compat

%description libEGL-devel
Mesa libEGL development packages

%package libGL
Summary:    Mesa libGL runtime libraries and DRI drivers
Group:      System/Libraries
Requires:   %{name} = %{version}-%{release}
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig
Provides:   libGL = %{version}-%{release}

%description libGL
Mesa libGL runtime library.

%package libGL-devel
Summary:    Mesa libGL development package
Group:      Development/Libraries
Requires:   %{name} = %{version}-%{release}
Requires:   mesa-llvmpipe-libGL = %{version}-%{release}
Requires:   libX11-devel
Provides:   libGL-devel

%description libGL-devel
Mesa libGL development packages

%package libGLU-devel
Summary:    Mesa libGLU development package
Group:      Development/Libraries
Requires:   %{name} = %{version}-%{release}
Requires:   mesa-llvmpipe-libGLU = %{version}-%{release}
Requires:   libGL-devel
Provides:   libGLU-devel

%description libGLU-devel
Mesa libGLU development packages

%package libGLU
Summary:    Mesa libGLU runtime library
Group:      System/Libraries
Requires:   %{name} = %{version}-%{release}
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig

%description libGLU
Mesa libGLU runtime libraries

%package dri-drivers-devel
Summary:    Mesa-based DRI development files
Group:      Development/Libraries
Requires:   %{name} = %{version}-%{release}

%description dri-drivers-devel
Mesa-based DRI driver development files.

%package dri-swrast-driver
Summary:    Mesa-based DRI drivers
Group:      Graphics/Display and Graphics Adaptation
Requires:   %{name} = %{version}-%{release}
Provides:   mesa-llvmpipe-dri-drivers = %{version}-%{release}

%description dri-swrast-driver
Mesa-based swrast DRI driver.

%package libwayland-egl-devel
Summary:    Mesa libwayland-egl development package
Group:      Development/Libraries
Requires:   %{name} = %{version}-%{release}
Requires:   mesa-llvmpipe-libwayland-egl = %{version}-%{release}
Provides:   libwayland-egl-devel

%description libwayland-egl-devel
Mesa libwayland-egl development packages

%package libwayland-egl
Summary:    Mesa libwayland-egl runtime library
Group:      System/Libraries
Requires:   %{name} = %{version}-%{release}
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig

%description libwayland-egl
Mesa libwayland-egl runtime libraries


%prep
%setup -q -n Mesa-%{version} -b1

# mesa-7.11-git-notimestamping.patch
%patch0 -p1
# 0001-wayland-drm-Implement-wl_buffer.damage-in-old-versio.patch
%patch1 -p1
# 0001-st-egl-Also-remove-wl_buffer_damage-in-wayland-backe.patch
%patch2 -p1
# 0001-st-egl-Update-to-the-new-wl_shm_pool-interface.patch
%patch3 -p1
# 0001-Stop-using-wl-buffer-damage.patch
%patch4 -p1
# mesa-8.0.3-llvm3.1.patch
%patch5 -p1
# >> setup
# << setup

%build
# >> build pre

# << build pre

%reconfigure --disable-static \
    --with-x \
    --enable-gallium-llvm \
    --with-dri-drivers=swrast \
    --with-state-trackers=egl \
    --enable-glew=no \
    --enable-glw=no \
    --enable-glut=no \
    --enable-gles1=yes \
    --enable-gles2=yes \
    --enable-egl=yes \
    --enable-gallium-egl \
    --enable-osmesa=no \
    --with-gallium-drivers=swrast \
    --with-egl-platforms=x11,fbdev,wayland \
    --enable-glx-tls \
    --enable-glx=yes \
    --enable-dri

make %{?jobs:-j%jobs}

# >> build post
# << build post

%install
rm -rf %{buildroot}
# >> install pre
# << install pre
%make_install

# >> install post

# strip out undesirable headers
pushd $RPM_BUILD_ROOT%{_includedir}/GL
rm [a-fh-np-wyz]*.h
rm osmesa.h
popd

#remove egl_glx.so, which is broken
#pushd $RPM_BUILD_ROOT%{_libdir}
#rm -f egl/egl_glx.so
#popd

# << install post


%post libglapi -p /sbin/ldconfig

%postun libglapi -p /sbin/ldconfig

%post libGLESv1 -p /sbin/ldconfig

%postun libGLESv1 -p /sbin/ldconfig

%post libGLESv2 -p /sbin/ldconfig

%postun libGLESv2 -p /sbin/ldconfig

%post libGLESv2-compat -p /sbin/ldconfig

%postun libGLESv2-compat -p /sbin/ldconfig

%post libEGL -p /sbin/ldconfig

%postun libEGL -p /sbin/ldconfig

%post libEGL-compat -p /sbin/ldconfig

%postun libEGL-compat -p /sbin/ldconfig

%post libGL -p /sbin/ldconfig

%postun libGL -p /sbin/ldconfig

%post libGLU -p /sbin/ldconfig

%postun libGLU -p /sbin/ldconfig

%post libwayland-egl -p /sbin/ldconfig

%postun libwayland-egl -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
# >> files
%{_libdir}/egl/egl_gallium.so
%{_libdir}/egl/st_GL.so
# << files

%files libglapi
%defattr(-,root,root,-)
# >> files libglapi
%{_libdir}/libglapi.so.0
%{_libdir}/libglapi.so.0.*
# << files libglapi

%files libGLESv1
%defattr(-,root,root,-)
# >> files libGLESv1
%{_libdir}/libGLESv1_CM.so.1
%{_libdir}/libGLESv1_CM.so.1.1.0
# << files libGLESv1

%files libGLESv2
%defattr(-,root,root,-)
# >> files libGLESv2
%{_libdir}/libGLESv2.so.2
%{_libdir}/libGLESv2.so.2.0.0
# << files libGLESv2

%files libGLESv2-compat
%defattr(-,root,root,-)
# >> files libGLESv2-compat
%{_libdir}/libGLESv2.so
# << files libGLESv2-compat

%files libEGL
%defattr(-,root,root,-)
# >> files libEGL
%{_libdir}/libEGL.so.1
%{_libdir}/libEGL.so.1.0
# << files libEGL

%files libEGL-compat
%defattr(-,root,root,-)
# >> files libEGL-compat
%{_libdir}/libEGL.so
# << files libEGL-compat

%files libglapi-devel
%defattr(-,root,root,-)
# >> files libglapi-devel
%{_libdir}/libglapi.so
# << files libglapi-devel

%files libGLESv1-devel
%defattr(-,root,root,-)
# >> files libGLESv1-devel
%{_libdir}/libGLESv1_CM.so
%{_includedir}/GLES/egl.h
%{_includedir}/GLES/gl.h
%{_includedir}/GLES/glext.h
%{_includedir}/GLES/glplatform.h
%{_libdir}/pkgconfig/glesv1_cm.pc
# << files libGLESv1-devel

%files libGLESv2-devel
%defattr(-,root,root,-)
# >> files libGLESv2-devel
%{_libdir}/libGLESv2.so
%{_includedir}/GLES2/gl2.h
%{_includedir}/GLES2/gl2ext.h
%{_includedir}/GLES2/gl2platform.h
%{_libdir}/pkgconfig/glesv2.pc
# << files libGLESv2-devel

%files libEGL-devel
%defattr(-,root,root,-)
# >> files libEGL-devel
%{_libdir}/libEGL.so
%dir %{_includedir}/EGL
%{_includedir}/EGL/egl.h
%{_includedir}/EGL/eglext.h
%{_includedir}/EGL/eglplatform.h
%{_includedir}/EGL/eglmesaext.h
%dir %{_includedir}/KHR
%{_includedir}/KHR/khrplatform.h
%{_libdir}/pkgconfig/egl.pc
# << files libEGL-devel

%files libGL
%defattr(-,root,root,-)
# >> files libGL
%{_libdir}/libGL.so.*
# << files libGL

%files libGL-devel
%defattr(-,root,root,-)
# >> files libGL-devel
%{_includedir}/GL/gl.h
%{_includedir}/GL/gl_mangle.h
%{_includedir}/GL/glext.h
%{_includedir}/GL/glx.h
%{_includedir}/GL/glx_mangle.h
%{_includedir}/GL/glxext.h
%dir %{_includedir}/GL/internal
%{_includedir}/GL/internal/dri_interface.h
%{_libdir}/libGL.so
%{_libdir}/pkgconfig/gl.pc
# << files libGL-devel

%files libGLU-devel
%defattr(-,root,root,-)
# >> files libGLU-devel
%{_libdir}/libGLU.so
%{_libdir}/pkgconfig/glu.pc
%{_includedir}/GL/glu.h
%{_includedir}/GL/glu_mangle.h
# << files libGLU-devel

%files libGLU
%defattr(-,root,root,-)
# >> files libGLU
%{_libdir}/libGLU.so.1
%{_libdir}/libGLU.so.1.3.*
# << files libGLU

%files dri-drivers-devel
%defattr(-,root,root,-)
# >> files dri-drivers-devel
%{_libdir}/pkgconfig/dri.pc
# << files dri-drivers-devel

%files dri-swrast-driver
%defattr(-,root,root,-)
# >> files dri-swrast-driver
%{_libdir}/dri/swrast_dri.so
# << files dri-swrast-driver

%files libwayland-egl-devel
%defattr(-,root,root,-)
# >> files libwayland-egl-devel
%{_libdir}/libwayland-egl.so
%{_libdir}/pkgconfig/wayland-egl.pc
# << files libwayland-egl-devel

%files libwayland-egl
%defattr(-,root,root,-)
# >> files libwayland-egl
%{_libdir}/libwayland-egl.so.1
%{_libdir}/libwayland-egl.so.1.*
# << files libwayland-egl
