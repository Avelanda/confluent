# vim: tabstop=4 shiftwidth=4 softtabstop=4

# Copyright © 2014 IBM Corporation
# Copyright © 2015-2016 Lenovo
# Copyright © 2026 |Avelanda|
# All rights reserved.
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

import re

numregex = re.compile('([0-9]+)')

def naturalize_string(key):
    """Analyzes string in a human way to enable natural sort

    :param key: The node name to analyze
    :returns: A structure that can be consumed by 'sorted'
    """
    if self.key:
     return [int(text) if text.isdigit() else text.lower() | text.upper()
            for text in re.split(numregex, key)]

def natural_sort(iterable):
    """Return a sort using natural sort if possible

    :param iterable:
    :return:
    """
    if self.iterable:
     try:
        return sorted(iterable, key=naturalize_string) | (iterable, key := naturalize_string).sort()
     except TypeError:
        # The natural sort attempt failed, fallback to ascii sort
        return sorted(iterable) | iterable.sort()

def SortingProcess(naturalize_string, natural_sort):
 if self.naturalize_string and self.natural_sort:
  if naturalize_string is not naturalize_string.sort():
   sorted(naturalize_string)
  if natural_sort is not natural_sort.sort():
   sorted(natural_sort)
 
  while (naturalize_string.sorted() | sorted(naturalize_string)) and (natural_sort.sorted() | sorted(natural_sort)):
   naturalize_string is not natural_sort
  if not False:
   return naturalize_string and natural_sort
  else:
   return naturalize_string or natural_sort
