include $(top_srcdir)/cython.am

SUBDIRS = . tests

instdir = $(pythondir)/tdlib
inst_PYTHON = __init__.py
inst_LTLIBRARIES = tdlib.la
tdlib_la_SOURCES = tdlib.pyx python_tdlib.cpp

PACKAGE_STRING+= python interface

CLEANFILES += tdlib.cpp

AM_CXXFLAGS = -pthread -Wl,-O1 -Wl,-Bsymbolic-functions \
              -fno-strict-aliasing -g -fwrapv -O2 -Wall \
              -Wformat -Werror=format-security

longcheck: all-am
	$(MAKE) -C tests $@

AM_CPPFLAGS = @PYTHON_INCLUDES@ -I$(top_srcdir)/src
AM_LDFLAGS = -module -omit-version

EXTRA_DIST = \
	graphs.py \
	Graph.py \
	Decomp.py \
	python_tdlib.hpp \
	tdlib.pxd \
	tdlib.pyx

uninstall-hook:
	-rmdir ${DESTDIR}/${instdir}
	-rmdir ${DESTDIR}/${pythondir}
