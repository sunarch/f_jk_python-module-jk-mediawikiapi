################################################################################
################################################################################
###
###  This file is automatically generated. Do not change this file! Changes
###  will get overwritten! Change the source file for "setup.py" instead.
###  This is either 'packageinfo.json' or 'packageinfo.jsonc'
###
################################################################################
################################################################################


from setuptools import setup

def readme():
	with open("README.md", "r", encoding="UTF-8-sig") as f:
		return f.read()

setup(
	author = "Jürgen Knauth",
	author_email = "pubsrc@binary-overflow.de",
	classifiers = [
		"Development Status :: 3 - Alpha",
		"License :: OSI Approved :: Apache Software License",
	],
	description = "This python module provides access to a MediaWiki wiki via its API.",
	download_url = "https://github.com/jkpubsrc/python-module-jk-mediawikiapi/tarball/0.2020.3.24",
	include_package_data = False,
	install_requires = [
		"jk_furl",
		"jk_typing",
		"jk_json",
		"jk_version",
		"beautifulsoup4",
	],
	keywords = [
		"mediawiki",
		"mediawiki-api",
	],
	license = "Apache 2.0",
	name = "jk_mediawikiapi",
	packages = [
		"jk_mediawikiapi",
	],
	url = "https://github.com/jkpubsrc/python-module-jk-mediawikiapi",
	version = "0.2020.3.24",
	zip_safe = False,
	long_description = readme(),
	long_description_content_type="text/markdown",
)
