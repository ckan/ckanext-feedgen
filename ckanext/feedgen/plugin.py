from __future__ import annotations

import ckan.plugins as p
import ckan.plugins.toolkit as tk


@tk.blanket.blu
class FeedgenPlugin(plugins.SingletonPlugin):
    plugins.implements(plugins.IConfigurer)


    # IConfigurer

    def update_config(self, config_):
        toolkit.add_template_directory(config_, "templates")
        toolkit.add_public_directory(config_, "public")
        toolkit.add_resource("assets", "feedgen")
