import os
import json
import logging

import executor

_root_path = os.path.dirname(os.path.realpath(__file__))

executor.execute(_root_path)