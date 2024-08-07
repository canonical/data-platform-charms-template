# Copyright 2024 Canonical Ltd.
# See LICENSE file for licensing details.
"""Basic unit tests for data charm."""

import unittest

from ops.testing import Harness

from charm import DataCharm


class TestCharm(unittest.TestCase):
    """Basic unit tests for data charm."""

    def setUp(self, *unused):
        """Set up the charm for each unit test."""
        self.harness = Harness(DataCharm)
        self.addCleanup(self.harness.cleanup)
        self.harness.begin()

    def test_charm(self):
        """TODO: Implement this test."""
