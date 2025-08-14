"""
Mergers module for post-processing and structuring extracted data.
"""

from .ministry_merger import merge_ministers
from .ministry_amendment_merger import group_by_change_type
from .ministry_amendment_table import merge_gazette_responses
from .person_merger import merge_person

__all__ = [
    "merge_ministers",
    "group_by_change_type", 
    "merge_gazette_responses",
    "merge_person"
]
