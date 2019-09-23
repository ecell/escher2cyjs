from setuptools import setup

__version__ = '0.0.1'

with open("README.md") as f:
    long_description = f.read()

setup(
    name='escher2cyjs',
    version=__version__,
    url='https://github.com/ecell/escher2cyjs',
    license='MIT',
    py_modules=['escher2cyjs'],
    python_requires='>=3.6',
    author='Kozo Nishida',
    author_email='knishida@riken.jp',
    install_requires=['requests'],
    description='Convert Escher map JSON to Cytoscape.js JSON (.cyjs)',
    long_description=long_description,
    long_description_content_type='text/markdown',
    classifiers=['License :: OSI Approved :: MIT License',]
)
