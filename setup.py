from setuptools import setup, find_packages

setup(
    name='pear_flowering',
    version='0.2.0',
    description='pear-flowering date prediction using DVR, mDVR, CD model',
    url='https://github.com/riverallzero/pear_flowering',
    author='riverallzero',
    author_email='riverallzero.k@gmail.com',
    packages=find_packages(),
    install_requires=['pandas', 'numpy', 'requests']
)
