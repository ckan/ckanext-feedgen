from __future__ import annotations

import ckan.plugins as p
import ckan.plugins.toolkit as tk


@tk.blanket.blueprints
@tk.blanket.config_declarations
class FeedgenPlugin(p.SingletonPlugin):
    pass
