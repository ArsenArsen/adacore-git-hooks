def test_push_bad_revert_commit(testcase):
    """Try pushing trunk..."""
    p = testcase.run("git push origin trunk".split())
    testcase.assertNotEqual(p.status, 0, p.image)
    testcase.assertRunOutputEqual(p, """\
remote: *** Commit df3a09266b6685060fb1e11268922b491e3e5cd8 looks like it was intended as a revert.
remote: ***
remote: *** When reverting, you should leave the 'This reverts commit'
remote: *** line unaltered.
remote: error: hook declined to update refs/heads/trunk
To ../bare/repo.git/
 ! [remote rejected] trunk -> trunk (hook declined)
error: failed to push some refs to '../bare/repo.git/'
""")


def test_push_good_revert_commit(testcase):
    """Try pushing trunk..."""
    p = testcase.run("git push origin trunk-good:trunk".split())
    testcase.assertEqual(p.status, 0, p.image)
    testcase.assertRunOutputEqual(p, """\
remote: DEBUG: Content-Type: text/plain; charset="utf-8"
remote: MIME-Version: 1.0
remote: Content-Transfer-Encoding: quoted-printable
remote: From: Test Suite <testsuite@gcc.gnu.org>
remote: To: true
remote: Subject: [repo/trunk] Revert "rs6000: Disassemble opaque modes using subregs to allow optimizations"
remote: X-Act-Checkin: repo
remote: X-Git-Author: Surya Kumari Jangala <jskumari@linux.ibm.com>
remote: X-Git-Refname: refs/heads/trunk
remote: X-Git-Oldrev: dc366d741ae38b1dfb105a67176c1de93cf1ed55
remote: X-Git-Newrev: 12ec343fa812ffa793dd0f41ecb47d2d06109673
remote:
remote: https://gcc.gnu.org/g:12ec343fa812ffa793dd0f41ecb47d2d06109673
remote:
remote: commit 12ec343fa812ffa793dd0f41ecb47d2d06109673
remote: Author: Surya Kumari Jangala <jskumari@linux.ibm.com>
remote: Date:   Sat Apr 11 12:19:45 2026 -0500
remote:
remote:     Revert "rs6000: Disassemble opaque modes using subregs to allow optimizations"
remote:
remote:     This reverts commit 69a2c243dd2cf9f77150c0eb86dfbc0931876bc1.
remote:
remote:     This will resolve the issue reported in PR124804.
remote:
remote: Diff:
remote: ---
remote:
remote: hooks/post-update: line 5: exec: git-update-server-info: not found
To ../bare/repo.git/
   dc366d7..12ec343  trunk-good -> trunk
""")
