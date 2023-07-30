from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as f:
    __long_description__ = f.read()

with open("requirements.txt", "r", encoding="utf-8") as f:
    __requirements__ = f.read()

__name__ = 'huynhngocuyen'
__version__ = '0.1'
__author__ = 'huynhngocuyen'
__author_email__ = 'ttniv01457@gmail.com'
__short_description__ = 'This Module Is Obfuscate Your Code.'
__url__ = 'https://github.com/addi00000/pycloak'
__license__ = 'AGPL-3.0'

setup(
    name=__name__,
    version=__version__,
    author=__author__,
    author_email=__author_email__,
    description=__short_description__,
    long_description=__long_description__,
    long_description_content_type="text/markdown",
    url=__url__,
    license=__license__,
    packages=find_packages(),
    python_requires='>=3.6',
    install_requires=[__requirements__],
    entry_points={
        'console_scripts': [
            'huynhngocuyen = huynhngocuyen.main:main',
        ],
    },
)