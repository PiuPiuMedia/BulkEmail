from setuptools import setup

with open("README.md", 'r') as f:
    long_description = f.read()

setup(
   name='BulkEmail',
   version='1.0',
   description='Bulk Email Automation',
   license="MIT",
   long_description=long_description,
   author='Anton',
   author_email='piupiu.aff@gmail.com',
   url="https://github.com/PiuPiuMedia/BulkEmail",
   #packages=['BulkEmail'],
   #install_requires=['smtplib', 'ssl'], #external packages as dependencies
)
