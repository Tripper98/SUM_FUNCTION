import setuptools

setuptools.setup(
    name='sumtripper',
    version='0.0.1',
    author='A.D Tripper',
    author_email='adnanedriouche98@gmail.com',
    description='Testing installation of Package',
    long_description="Just testin packaging for sum function",
    long_description_content_type="text/markdown",
    url='https://github.com/Tripper98/SUM_FUNCTION',
    packages=['src\sumtripper'],
    install_requires=['h5py', 'typing-extensions', 'wheel'],
)