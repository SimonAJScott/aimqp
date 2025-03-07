from pynput.keyboard import Key
from enum import Enum


class Keys(Enum):
    """
    Enum class to map in-game actions to specific keyboard keys.
    Can be extended to add more actions and keys as needed.
    """

    LEFT = Key.left  # LEFT action corresponds to the left arrow key
    RIGHT = Key.right  # RIGHT action corresponds to the right arrow key
    JUMP = Key.space  # JUMP action corresponds to the spacebar key
    DASH = Key.shift  # DASH action corresponds to the shift key
    DOWN = Key.down  # DOWN action corresponds to the down arrow key

    def get_key(self):
        """
        Return the actual key value corresponding to the enum.
        This allows for direct usage in functions like 'keyboard.press' and 'keyboard.release'.

        :return: The corresponding key constant from the pynput 'Key' class.
        """
        return self.value
