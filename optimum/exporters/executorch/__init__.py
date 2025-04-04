# Copyright 2025 The HuggingFace Team. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from typing import TYPE_CHECKING

from transformers.utils import _LazyModule


_import_structure = {
    "convert": [
        "export_to_executorch",
    ],
    "recipe_registry": [
        "discover_recipes",
        "register_recipe",
    ],
    "task_registry": [
        "discover_tasks",
        "register_task",
    ],
    "tasks": [
        "causal_lm",
        "seq2seq_lm",
    ],
    "recipes": [
        "xnnpack",
    ],
    "utils": [
        "save_config_to_constant_methods",
    ],
    "integrations": [
        "Seq2SeqLMExportableModule",
    ],
    "__main__": ["main_export"],
}

if TYPE_CHECKING:
    from .__main__ import main_export
    from .convert import export_to_executorch
else:
    import sys

    sys.modules[__name__] = _LazyModule(
        __name__,
        globals()["__file__"],
        _import_structure,
        module_spec=__spec__,
    )
