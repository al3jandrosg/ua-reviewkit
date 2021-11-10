#!/usr/bin/env python3
"""
Parse results from a sonobuoy run.

Run with: {} status (failed|passed|skipped)
"""
import sys
import yaml


def __filter_tests(status="skipped"):
  return filter(lambda x: x['status'] == status, [
      x for x in yaml.safe_load(sys.stdin.read())['items'][0]['items'][0]['items']])


def main():
    if not len(sys.argv) > 1:
        print(__doc__.format(sys.argv[0]))
        sys.exit(-1)
    status=sys.argv[1]
    print("List of tests with {} status:".format(status))
    for test in __filter_tests(status=status):
        print(test['name'])


if __name__ == "__main__":
    main()
