# vim:fileencoding=utf-8:noet

# Copyright (c) 2020 Matheus Castello
# MicroHobby licenses this file to you under the MIT license.
# See the LICENSE file in the project root for more information.

from __future__ import (unicode_literals, division, absolute_import, print_function)

from powerline.segments import Segment, with_docstring
from powerline.theme import requires_segment_info, requires_filesystem_watcher

import os
import random

@requires_filesystem_watcher
@requires_segment_info
class CustomSegment(Segment):
  divider_highlight_group = None

  def __call__(self, pl, segment_info, create_watcher):
    last_pipe_status = (
      segment_info['args'].last_pipe_status
      or (segment_info['args'].last_exit_code,)
    )

    # get the current branch
    gitbranch = os.popen("cd {} && git rev-parse --abbrev-ref HEAD"
                          .format(segment_info['getcwd']())).read().rstrip()

    error_emoji_list = ["😖", "😵", "🥴", "😭", "😱", "😡", "🤬", "🙃", "🤔",
                        "🙄", "🥺", "😫", "💀", "💩", "😰"]

    # Houstoun we have a problem
    if any(last_pipe_status):
        return [
			{
        # No problem at all if we show a emoji
				'contents': "{}".format(random.choice(error_emoji_list)
                                if (gitbranch == "")
                                else  u'\uE0A0 '+gitbranch),
				'highlight_groups': ['myfail'],
				'draw_inner_divider': True
			}
			#for status in last_pipe_status
		]
    else:
        return [{
        # is all ok we are cool as f¨*&
        'contents': "{}".format("😎" if (gitbranch == "")
                                else u'\uE0A0 '+gitbranch),
        'highlight_groups': ['critical:success'],
        }]

hello = with_docstring(CustomSegment(),
          '''Return sad random emojis in case of command errors''')

@requires_filesystem_watcher
@requires_segment_info
class Docker(Segment):
  divider_highlight_group = None

  def __call__(self, pl, segment_info, create_watcher):
    
    # count docker images and how many containers are running now
    dpsc = os.popen("docker images -q | wc -l").read().rstrip()
    runs = os.popen("docker ps -q | wc -l").read().rstrip()

    if int(runs) > 0:
      ret = "🐳 :: 📦 {} :: ▶ {} ".format(dpsc, runs)
    else:
      ret = "🐳 :: 📦 {}".format(dpsc)

    return [{
    'contents': ret,
    'highlight_groups': ['session'],
    }]

docker = with_docstring(Docker(),
          '''Return a segment with Docker info''')

@requires_segment_info
class Pwd(Segment):
  divider_highlight_group = None

  def __call__(self, pl, segment_info, use_shortened_path=True, **kwargs):

    try:
      pwd = segment_info['getcwd']()
    except KeyError:
      pwd = "Key Error"

    return [{
    'contents': "👉 {}".format(pwd),
    'highlight_groups': ['session'],
    }]

pwd = with_docstring(Pwd(), '''Return a string with the current path''')

@requires_filesystem_watcher
@requires_segment_info
class End(Segment):
  divider_highlight_group = None

  def __call__(self, pl, segment_info, create_watcher):
    last_pipe_status = (
      segment_info['args'].last_pipe_status
      or (segment_info['args'].last_exit_code,)
    )

    if any(last_pipe_status):
      return [{
      'contents': ">",
      'highlight_groups': ['myfail'],
      }
      ]
    else:
      return [{
      'contents': ">",
      'highlight_groups': ['session'],
      }]

end = with_docstring(End(),
        '''Return a pipe segment that change color in case of errors''')

@requires_filesystem_watcher
@requires_segment_info
class Git(Segment):
  divider_highlight_group = None

  def __call__(self, pl, segment_info, create_watcher):
    
    gitret = os.popen("cd {} && git status -s -uno | wc -l"
                        .format(segment_info['getcwd']())).read().rstrip()

    if gitret != '0':
      return [{
      'contents': "📑 :: {} ".format(gitret),
      'highlight_groups': ['session'],
      }]
    else:
      return [{
      'contents': ".",
      'highlight_groups': ['session'],
      }]

git = with_docstring(Git(),
        '''Return git branch and count how many files modified on repo''')
