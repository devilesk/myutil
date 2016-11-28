import os
import setuptools

module_path = os.path.join(os.path.dirname(__file__), 'myutil.py')
version_line = [line for line in open(module_path)
                if line.startswith('__version__')][0]

__version__ = version_line.split('__version__ = ')[-1][1:][:-2]

setuptools.setup(
    name="myutil",
    version=__version__,
    url="https://github.com/devilesk/myutil",

    author="devilesk",
    author_email="devilesk@gmail.com",

    description="My python util library.",
    long_description=open('README.rst').read(),

    py_modules=['myutil'],
    zip_safe=False,
    platforms='any',

    install_requires=[],

    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
    ],
)
