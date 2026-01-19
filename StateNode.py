from ast import Dict
from Enums import State
import copy

class StateNode:

    def __init__(self, state: State, callbackFuctions: Dict):
        self._state = state
        self._callbackFuctions = copy.deepcopy(callbackFuctions)

    @property
    def state(self)-> State:
        return self._state

    @property
    def callbackFuctions(self)-> Dict:
        return copy.deepcopy(self._callbackFuctions)

    @state.setter
    def state(self, state: State)-> None:

        if self._state == state: return

        self._state == state
        for function in self._callbackFuctions.values():
            function()

    @callbackFuctions.setter
    def callbackFuctions(self, callbackFuctions: Dict)-> None:
        self._callbackFuctions = copy.deepcopy(callbackFuctions)
    
