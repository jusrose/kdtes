from setuptools import setup

with open("README.md", "r") as fo:
    ld = fo.read()
    
setup(
    long_description=ld,
    long_desription_content_type="text/markdown"
    name='kdtes',
    description='a way to encrypt ascii text for many purpuses',
    py_modules["kdtes"],
    package_dir={'':'src'},
    version='0.1.0'
  )