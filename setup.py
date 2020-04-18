import setuptools
import glob
import platform
if platform.system().startswith("CYGWIN") and platform.machine()=="x86_64":
  pass
else:
  raise OSError("juman-cygwin64 only for 64-bit Cygwin")

setuptools.setup(
  name="juman-cygwin64",
  version="0.6.0",
  packages=setuptools.find_packages(),
  data_files=[
    ("local/bin",glob.glob("bin/*")),
    ("local/libexec/juman",glob.glob("libexec/juman/*")),
    ("local/lib",glob.glob("lib/*")),
    ("local/etc",glob.glob("etc/*")),
    ("local/include",glob.glob("include/*")),
    ("local/share/juman/dic",glob.glob("share/juman/dic/*")),
    ("local/share/juman/autodic",glob.glob("share/juman/autodic/*")),
    ("local/share/juman/wikipediadic",glob.glob("share/juman/wikipediadic/*")),
    ("local/share/juman/doc",glob.glob("share/juman/doc/*"))
  ]
)
