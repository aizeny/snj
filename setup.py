from setuptools import setup
from sphinx.setup_command import BuildDoc

name = 'spectraltree'
version = '0.1'
release = '0.1.0'
setup(
    name=name,
    version=version,
    description='Spectral neighbor joining',
    url='https://github.com/aizeny/snj',
    author='Ariel Jaffe, Noah Amsel, Yariv Aizenbud, Boaz Nadler, Joseph T. Chang, Yuval Kluger',
    author_email='yariv.aizenbud@yale.edu',
    license='GPLv3',
    packages=['spectraltree'],
    install_requires=[
        'dendropy',
        'numpy',
        'pandas',
        'python-igraph',
        'scipy',
        'scikit-learn',
        'seaborn',
        'sphinx',
        'sphinx-rtd-theme'
    ],
    include_package_data=True,
    zip_safe=False,
    test_suite="tests",
    cmdclass={'build_sphinx': BuildDoc},
    command_options={
        'build_sphinx': {
            'project': ('setup.py', name),
            'version': ('setup.py', version),
            'release': ('setup.py', release),
            'source_dir': ('setup.py', 'docs'),
            'build_dir': ('setup.py', 'docs/_build')}})
