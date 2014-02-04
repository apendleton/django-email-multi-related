from setuptools import setup, find_packages
import os

f = open(os.path.join(os.path.dirname(__file__), 'README.md'))
readme = f.read()
f.close()

setup(
    name='emailmultirelated',
    version="0,1",
    description='Multi-part email sending with Django.',
    long_description=readme,
    author=' gzbender',
    author_email='apendleton@sunlightfoundation.com',
    url='https://github.com/apendleton/django-email-multi-related',
    packages=find_packages(),
    license='BSD License',
    platforms=["any"],
    py_modules=["emailmultirelated"],
    install_requires=['beautifulsoup4', 'lxml'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Environment :: Web Environment',
    ],
)
