import unittest

from vaults.experiment import (
    PlannedTransaction,
    PlannedUTXO,
    ScriptTemplate,
)

class AbstractPlanningTests(unittest.TestCase):
    def test_planned_transaction(self):
        planned_transaction1 = PlannedTransaction(name="name goes here")
        planned_transaction2 = PlannedTransaction(name="")
        planned_transaction3 = PlannedTransaction(name=None)
        del planned_transaction3
        del planned_transaction2
        del planned_transaction1

    def test_planned_transaction_counter(self):
        counter_start = int(PlannedTransaction.__counter__)
        planned_transaction1 = PlannedTransaction(name="name goes here")
        planned_transaction2 = PlannedTransaction(name="")
        planned_transaction3 = PlannedTransaction(name=None)
        counter_end = int(PlannedTransaction.__counter__)

        self.assertEqual(counter_end - counter_start, 3)
        del planned_transaction3
        del planned_transaction2
        del planned_transaction1
        self.assertEqual(counter_end - counter_start, 3)

    def test_planned_utxo(self):
        utxo1 = PlannedUTXO(name="some UTXO", transaction=None, script_template=ScriptTemplate)
        utxo2 = PlannedUTXO(name="second UTXO", transaction=None)
        utxo3 = PlannedUTXO(name="another UTXO")
        del utxo3
        del utxo2
        del utxo1

    def test_planned_utxo_counter(self):
        counter_start = int(PlannedUTXO.__counter__)
        utxo1 = PlannedUTXO(name="some UTXO")
        counter_end = int(PlannedUTXO.__counter__)

        self.assertEqual(counter_end - counter_start, 1)
        del utxo1
        self.assertEqual(counter_end - counter_start, 1)

    def test_planned_transaction_cpfp_hook_utxo(self):
        planned_transaction = PlannedTransaction(name="name goes here")
        self.assertEqual(len(planned_transaction.output_utxos), 1)
        self.assertEqual(planned_transaction.output_utxos[0].name, "CPFP hook")