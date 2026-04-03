from __future__ import annotations

from typing_extensions import override

import ckan.plugins as p
import ckan.plugins.toolkit as tk
from ckan.common import CKANConfig


@tk.blanket.blueprints
@tk.blanket.config_declarations
class FeedgenPlugin(p.IConfigurer, p.SingletonPlugin):
    @override
    def update_config(self, config: CKANConfig) -> None:
        tk.add_template_directory(config, "templates")
