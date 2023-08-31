# =========== Copyright 2023 @ CAMEL-AI.org. All Rights Reserved. ===========
# Licensed under the Apache License, Version 2.0 (the “License”);
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an “AS IS” BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# =========== Copyright 2023 @ CAMEL-AI.org. All Rights Reserved. ===========

from abc import ABC, abstractmethod
from typing import List, Optional

from camel.messages.base import BaseMessage


class BaseMemory(ABC):
    """
    Abstract base class representing the basic operations
    required for a memory system.
    """

    @abstractmethod
    def read(self,
             current_state: Optional[BaseMessage] = None) -> List[BaseMessage]:
        """
        Reads a message or messages from memory.

        Returns:
            Union[BaseMessage, List[BaseMessage]]: Retrieved message or list of
                messages.
        """
        ...

    @abstractmethod
    def write(self, msgs: List[BaseMessage]) -> None:
        """
        Writes a message to memory.

        Args:
            msg (BaseMessage): The message to be written.
        """
        ...

    @abstractmethod
    def clear(self) -> None:
        """
        Clears all messages from memory.
        """
        ...