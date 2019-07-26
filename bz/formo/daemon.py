# Copyright 2019 Nicholas Kroeker
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

from typing import Dict
from typing import List
from typing import Optional
from typing import Union
import asyncio
import asyncio.subprocess
import collections
import json
import pathlib
import tarfile
import tempfile
import shutil


Path_T = Union[str, pathlib.Path]
JsonValue_T = Union[str, int, float, bool, None]


class Configurator:
    """Utility class for augmenting Bluzelle configuration files.

    This is intended to be used directly, and then renders out your settings
    either as JSON or a CLI argument list.

    >>> my_config = Configurator()
    >>> my_config.listener_port = 50001
    >>> my_config.log_to_stdout = True
    >>> my_config.private_key_file = "./private-key.pem"
    >>> with open('bluzelle.json', 'w') as f:
    ...     f.write(my_config.resolve_json())

    """

    DEFAULT_CONFIG = {
        "stack": "beekeeper-local",
        "debug_logging": True,
        "log_to_stdout": True,
    }

    def __init__(self) -> None:
        self._overrides: Dict[str, JsonValue_T] = {}

    def __setattr__(self, name: str, value: JsonValue_T):
        """Include or override the config as specified."""
        self._overrides[name] = value

    def set_config(self, config_name: str, config_value: JsonValue_T) -> None:
        """Include or override the config as specified."""
        self._overrides[config_name] = config_value

    def resolve_json(self) -> str:
        """Returns the resolved config by first applying defaults."""
        return json.dumps(
            dict(collections.ChainMap(self._overrides, self.DEFAULT_CONFIG))
        )

    def resolve_options(self) -> List[str]:
        """Returns CLI parameter string used to set the configs."""
        raise NotImplementedError


class Bee:
    """Representation of a running swarm/daemon process."""

    _process: asyncio.subprocess.Process

    CONFIG_PATH = pathlib.PurePath("bluzelle.json")

    def __init__(self, exec_path: Path_T, data_dir: Optional[Path_T] = None) -> None:

        # TODO: Provide way to attach logger object to stdout/stderr?

        self._base_dir = pathlib.Path(data_dir)
        self._data_dir = data_dir if data_dir is not None else tempfile.mkdtemp()

    def _write_state_files(self) -> None:
        """Writes out various files needed for the process to function."""
        with open() as f:
            pass
        raise NotImplementedError

    @property
    def log(self) -> str:
        """Fetches all log contents recorded by this process."""
        raise NotImplementedError

    @property
    def port(self) -> str:
        """The port that this process is working on."""
        raise NotImplementedError

    @property
    def is_running(self) -> bool:
        """Returns whether or not the process is running."""
        raise NotImplementedError

    def ws_ping(self) -> bool:
        """Returns wether or not the process responds to a WebSocket ping."""
        raise NotImplementedError

    async def start(self, port, **opts) -> asyncio.subprocess.Process:
        p = await asyncio.create_subprocess_exec(
            "./swarm", stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE
        )
        return p

    def kill(self, timeout: float = 10.0, signal: Optional[int] = None) -> None:
        """Kills the process, and waits for it to terminate

        If the underlying OS supports signals and the `signal` argument is
        given, then that signal will be sent to the process.

        Args:
            timeout: Default 10.0s. The time to wait for the process to die.
            signal: Optional. If given, this signal is sent to the process.

        Raises:
            formo.exceptions.TimeoutError: If the process does not die
                within the given/default timeout.
        """

    def generate_debug_archive(self) -> pathlib.Path:
        """Get a blob of archived data useful for debugging.

        The following information will be included:
            - Daemon logs
            - Daemon binary
            - Daemon coredump (if possible to trigger & fetch)

        If any issue is encountered in gathering any of the pieces, the
        resulting archive will still contain the successful pieces.

        The generated archive will live in temporary storage and thus will
        likely not be available upon restart of the host machine.

        Returns:
            A path to the generated archive.
        """
        raise NotImplementedError


class BeeHive:

    bees: List[Bee]
