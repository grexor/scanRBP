# scanRBP, https://github.com/grexor/scanRBP

from setuptools import setup
from setuptools import find_packages

with open("README.md", "r") as fh:
    long_desc = fh.read()
    long_desc = "\n".join(long_desc.split("\n")[1:])

setup(
    name='scanRBP',
    version = open("scanRBP/version", "rt").readlines()[0].replace("\n", "").replace("\r", ""),
    packages=find_packages(),
    description='scanRBP: RNA-protein binding toolkit',
    long_description = long_desc,
    long_description_content_type = "text/markdown",
    classifiers=[
        'Programming Language :: Python :: 3',
    ],
    zip_safe=False,
    author='Gregor Rot',
    scripts=["scanRBP/scanRBP"],
    author_email='gregor.rot@gmail.com',
    url='https://github.com/grexor/scanRBP',
    keywords=['scanRBP', 'bioinformatics', 'RBP', 'RNA-protein binding', 'toolkit'],
    include_package_data=True,
    package_data={
        'scanRBP': ['version'],
    },
    install_requires=["biopython"],
)
