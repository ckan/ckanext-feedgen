from __future__ import annotations

from typing import Any, Protocol


class PFeed(Protocol):
    def add_item(self: Any, **kwargs: Any) -> None: ...

    def writeString(self: Any, encoding: str) -> str: ...  # noqa: N802


class PFeedFactory(Protocol):
    """Contract for IFeed.get_feed_class."""

    def __call__(  # noqa: PLR0913
        self,
        feed_title: str,
        feed_link: str,
        feed_description: str,
        language: str | None,
        author_name: str | None,
        feed_guid: str | None,
        feed_url: str | None,
        previous_page: str | None,
        next_page: str | None,
        first_page: str | None,
        last_page: str | None,
    ) -> PFeed: ...
