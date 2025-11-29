# =======================================================
# 🏥 REACH-AI AGENTS PACKAGE
# =======================================================
# This file exposes the agent modules to the main app.
# It makes imports cleaner in app.py.

from . import monitor
from . import decision
from . import automation
from . import network
from . import learning
from . import result

# Define what gets imported if someone uses "from agents import *"
__all__ = [
    'monitor',
    'decision',
    'automation',
    'network',
    'learning',
    'result'
]