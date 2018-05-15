from __future__ import print_function
import os
import subprocess
import argparse


WORKING_REPO = "/insert/working_repo/path/here/"
REVIEW_REPO = "/insert/review/repo/"
PATCH_NAME = "copy_commit_patch"
EXPORT_ARG_LIST = ["hg", "export", "-o", REVIEW_REPO+PATCH_NAME]


def export_import():
   arguments = args()
   print("Check if paths exists")
   assert os.path.isdir(WORKING_REPO), "Working Repo Path Does Not Exist"
   assert os.path.isdir(REVIEW_REPO), "Review Repo Path Does Not Exist"

   print("Exporting changes from Working Repo to patch")
   if arguments.c is not None:
       EXPORT_ARG_LIST.extend(("-r", str(arguments.c)))
   elif arguments.r is not None:
       rev_range = "{}:{}".format(arguments.r[0], arguments.r[1])
       EXPORT_ARG_LIST.extend(("-r", rev_range))
   subprocess.check_output(EXPORT_ARG_LIST, cwd=WORKING_REPO)

   print("Applying Patch to Review Repo")
   subprocess.check_output(["hg", "import", PATCH_NAME], cwd=REVIEW_REPO)

   print("Deleting patchfile")
   os.remove(REVIEW_REPO+PATCH_NAME)


def args():
   prog_desc = "A script to copy changesets from a Working Repo to a Code Review Repo."
   help_c = "Single changeset revision number to copy. Ex) 10466"
   help_r = "Range of changeset revision numbers to copy over. Ex) 10453 10458"
   parser = argparse.ArgumentParser(description=prog_desc)
   group = parser.add_mutually_exclusive_group()
   group.add_argument('-c', type=int, help=help_c)
   group.add_argument('-r', type=int, nargs=2, help=help_r)
   return parser.parse_args()


if __name__ == "__main__":
   export_import()
