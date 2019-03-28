from setuptools import setup, find_packages

setup(
    name='sample-library-for-cdp-builds',
    description="Short description",
    long_description=open('README.md').read(),
    version='0.5',
    packages=find_packages(),
    author='User A, User B',
    author_email='user.a@nolar.info, user.b@nolar.info',
    maintainer='User C, User D',
    maintainer_email='user.c@nolar.info, user.d@nolar.info',
)
