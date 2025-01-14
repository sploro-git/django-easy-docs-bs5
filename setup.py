from setuptools import setup, find_packages

with open('README.md', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='django-easy-docs-bs5',
    version='2.0.0',
    packages=find_packages(exclude=['*.migrations', '*.migrations.*', 'migrations.*', 'migrations', 'docs', 'docs.*']),
    url='https://github.com/sploro-git/django-easy-docs-bs5',
    author='Ivan Pajares',
    description='A simple documentation app for Django, using Bootstrap 5.',
    download_url='https://pypi.org/project/django-easy-docs-bs5/',
    long_description=long_description,
    long_description_content_type='text/markdown',
    license='MIT',
    keywords=['django', 'documentation', 'docs', 'easy', 'simple'],
    author_email='ivan.pajares@sploro.eu',
    include_package_data=True,
    install_requires=[
        'Django>=4.0',
        'django-markdownx>=4.0.7',
        'django-simple-history>=3.4.0',
        'markdown>=3.5.1',
        'django-htmx>=1.17.2'
    ],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 3.2',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.9',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)
