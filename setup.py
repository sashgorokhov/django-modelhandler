from distutils.core import setup

with open('README.rst') as readme:
    with open('HISTORY.rst') as history:
        long_description = readme.read() + '\n\n' + history.read()

setup(
    install_requires=['django'],
    name='django-modelhandler',
    version='1.0.0',
    packages=['modelhandler'],
    url='https://github.com/sashgorokhov/django-modelhandler',
    download_url='https://github.com/sashgorokhov/django-modelhandler/archive/master.zip',
    keywords=['django', 'logging', 'handler'],
    classifiers=[],
    long_description=long_description,
    license='MIT License',
    author='sashgorokhov',
    author_email='sashgorokhov@gmail.com',
    description="A python logging handler that saves logs into django model. That's it.",
)