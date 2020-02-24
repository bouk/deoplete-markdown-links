import re

import subprocess
from os.path import dirname, join
from deoplete.base.source import Base
from deoplete.util import Nvim, UserContext, Candidates

class Source(Base):

    def __init__(self, vim: Nvim) -> None:
        super().__init__(vim)

        self.name = 'markdown_links'
        self.mark = '[ML]'
        self.rank = 1000
        self.matchers = ['matcher_full_fuzzy']
        self.filetypes = ['markdown']
        self.min_pattern_length = 0
        self.matcher_key = 'name'
        self.__pattern = re.compile(r'\[\[[^\]]*(?!\]\])$')

    def get_complete_position(self, context: UserContext) -> int:
        match = self.__pattern.search(context['input'])
        return match.start() + 2 if match is not None else -1

    def gather_candidates(self, context: UserContext) -> Candidates:
        directory = dirname(join(context['cwd'], context['bufname']))
        result = subprocess.run(["rg", "--files", "-t", "md"], cwd=directory, capture_output=True, encoding='utf-8')
        words = result.stdout.split('\n')
        result = [{'word': x + ']]', 'name': x, 'abbr': x} for x in words if len(x) > 0]
        return result
