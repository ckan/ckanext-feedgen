[![Tests](https://github.com/CKAN/ckanext-feedgen/workflows/Tests/badge.svg?branch=main)](https://github.com/CKAN/ckanext-feedgen/actions)

# ckanext-feedgen

Atom feed generator for CKAN. This extension provides paginated Atom feeds for
datasets, allowing users and applications to subscribe to dataset updates
filtered by tags, groups, organizations, or custom search queries.

## Features

- **General feed** — `/feeds/dataset.atom` shows all recently updated datasets
- **Custom search feed** — `/feeds/custom.atom` supports `q`, `fq`, `sort`, and `filters` parameters
- **Tag feeds** — `/feeds/tag/<id>.atom` for datasets with a specific tag
- **Group feeds** — `/feeds/group/<id>.atom` for datasets in a specific group
- **Organization feeds** — `/feeds/organization/<id>.atom` for datasets owned by a specific organization
- **Pagination** — Feeds include first, last, previous, and next links
- **JSON enclosures** — Each feed entry includes a link to the CKAN `package_show` API
- **Extensible** — Plugins can customize feed generation via the `IFeed` interface

Feed links are automatically added to group and organization pages.

## Requirements

This extension is compatible with CKAN 2.12 and later.

Compatibility with core CKAN versions:

| CKAN version     | Compatible? |
|------------------|-------------|
| 2.11 and earlier | no          |
| 2.12             | yes         |


## Installation

To install ckanext-feedgen:

1. Activate your CKAN virtual environment, for example:

   ```sh
   . /usr/lib/ckan/default/bin/activate
   ```


2. Clone the source and install it on the virtualenv

   ```sh
   git clone https://github.com/CKAN/ckanext-feedgen.git
   cd ckanext-feedgen
   pip install -e .
   pip install -r requirements.txt
   ```

3. Add `feedgen` to the `ckan.plugins` setting in your CKAN
   config file (by default the config file is located at
   `/etc/ckan/default/ckan.ini`).

4. Restart CKAN. For example if you've deployed CKAN with Apache on Ubuntu:

   ```sh
   sudo service apache2 reload
   ```


## Config settings

The following configuration options are available:

```ini
# Feed author name (optional, falls back to ckan.site_id)
ckan.feeds.author_name = My CKAN Site

# Feed author link (optional, falls back to ckan.site_url)
ckan.feeds.author_link = https://example.com

# Publisher domain for tagURIs (optional, falls back to ckan.site_url)
ckan.feeds.authority_name = https://example.com

# Date string for tagURI generation (optional, e.g. 2012-03-22)
ckan.feeds.date = 2012-03-22

# Number of items per feed page (optional, default: 20)
ckan.feeds.limit = 50
```

## Developer installation

To install ckanext-feedgen for development, activate your CKAN virtualenv and
do:

```sh
git clone https://github.com/CKAN/ckanext-feedgen.git
cd ckanext-feedgen
pip install -e .
pip install -r dev-requirements.txt
```

## Tests

To run the tests, do:

```sh
pytest --ckan-ini=test.ini
```

## Extending

Other plugins can customize feed behavior by implementing the `IFeed` interface:

```python
from ckanext.feedgen.interfaces import IFeed
from ckan.plugins import implements


class MyFeedPlugin(p.SingletonPlugin):
    implements(IFeed)

    def get_feed_class(self):
        # Return a custom feed generator class
        return MyCustomFeed

    def get_item_additional_fields(self, dataset_dict):
        # Return additional fields to add to each feed item
        return {
            'contributor': dataset_dict.get('maintainer'),
        }
```

## Releasing a new version of ckanext-feedgen

If ckanext-feedgen should be available on PyPI you can follow these steps to publish a new version:

1. Update the version number in the `pyproject.toml` file. See [PEP 440](http://legacy.python.org/dev/peps/pep-0440/#public-version-identifiers) for how to choose version numbers.

1. Tag the new release of the project on GitHub with the version number from
   the `pyproject.toml` file. For example if the version number is
   v0.0.1 then do:
   ```sh
   git tag v0.0.1
   git push --tags
   ```

## License

[AGPL](https://www.gnu.org/licenses/agpl-3.0.en.html)
