import pickle
import json

class Solution:
    # two fairly obvious options:
    # 1. JSON
    # 2. pickle
    def encode(self, strs: List[str]) -> str:
        data = json.dumps(strs)
        return data

    def decode(self, s: str) -> List[str]:
        data = json.loads(s)
        return data