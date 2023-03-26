import os
import unittest
from _thread import *
import time
import WorkloadBuilder
import asyncio



class TestStringMethods(unittest.TestCase):

    def test_single_node(self):
        start_new_thread(WorkloadBuilder.buildAndRunPingServer, ())
        hasResult = WorkloadBuilder.buildAndRunClient()
        self.assertTrue(hasResult)

    def test_multiple_nodes(self):
        start_new_thread(WorkloadBuilder.buildAndRunPingServerMultiple, (10,))
        sol,res = WorkloadBuilder.buildAndRunMultipleClients(10)

        self.assertEqual(len(sol),len(res))




if __name__ == '__main__':
    unittest.main()

