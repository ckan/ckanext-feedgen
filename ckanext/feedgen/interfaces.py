from __future__ import annotations

from typing import TYPE_CHECKING, Any

from ckan.plugins import Interface

from .types import PFeedFactory

if TYPE_CHECKING:
    from .views import CKANFeed


class IFeed(Interface):
    """For extending the default Atom feeds."""

    def get_feed_class(self) -> PFeedFactory:
        """Allows plugins to provide a custom class to generate feed items.

        :returns: feed class
        :rtype: type

        The feed item generator's constructor is called as follows::

            feed_class(
                feed_title,        # Mandatory
                feed_link,         # Mandatory
                feed_description,  # Mandatory
                language,          # Optional, always set to 'en'
                author_name,       # Optional
                author_link,       # Optional
                feed_guid,         # Optional
                feed_url,          # Optional
                previous_page,     # Optional, url of previous page of feed
                next_page,         # Optional, url of next page of feed
                first_page,        # Optional, url of first page of feed
                last_page,         # Optional, url of last page of feed
            )

        """
        return CKANFeed

    def get_item_additional_fields(self, dataset_dict: dict[str, Any]) -> dict[str, Any]:
        """Allows plugins to set additional fields on a feed item.

        :param dataset_dict: the dataset metadata
        :type dataset_dict: dictionary
        :returns: the fields to set
        :rtype: dictionary
        """
        return {}
