from __future__ import absolute_import
from __future__ import print_function
from __future__ import unicode_literals


# TODO: maybe `git ls-remote git://github.com/pre-commit/pre-commit-hooks` to
# determine the latest revision?  This adds ~200ms from my tests (and is
# significantly faster than https:// or http://).  For now, periodically
# manually updating the revision is fine.
SAMPLE_CONFIG = '''\
# See http://pre-commit.com for more information
# See http://pre-commit.com/hooks.html for more hooks
-   repo: https://github.com/pre-commit/pre-commit-hooks
    sha: v0.9.1
    hooks:
    -   id: trailing-whitespace
    -   id: end-of-file-fixer
    -   id: check-yaml
    -   id: check-added-large-files
'''


def sample_config():
    print(SAMPLE_CONFIG, end='')
    return 0
