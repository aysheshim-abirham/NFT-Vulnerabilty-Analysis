from mythril.analysis import solver
from mythril.plugin.interface import MythrilPlugin
from mythril.analysis.report import Issue
from mythril.analysis.swc_data import UNPROTECTED_SELFDESTRUCT
from mythril.exceptions import UnsatError
from mythril.analysis.module.base import DetectionModule, EntryPoint
from mythril.laser.ethereum.state.global_state import GlobalState
from mythril.laser.ethereum.transaction.symbolic import ACTORS
from mythril.laser.smt.bool import And
from mythril.laser.smt import Extract, symbol_factory
from mythril.laser.ethereum.transaction.transaction_models import (
    ContractCreationTransaction,
)
from mythril.laser.ethereum.transaction.symbolic import ACTORS

import logging
from copy import copy
from typing import List
log = logging.getLogger(__name__)

class NFTOwnershipDetector(DetectionModule, MythrilPlugin):
 """This module checks for NFT ownership vulnerabilities"""
 # The following fields add some metadata to the plugin
 author = "Krishna Kushal"
 plugin_license = "MIT"
 plugin_type = "Detection Module"
 plugin_version = "0.0.1 "
 plugin_description = \
   "This is a reference implementation of detection module plugin which finds NFT ownership takeover vulnerabilities."
   default_enabled = True
   
   
   def __init__(self):
        super().__init__()
        self._cache_address = {}

    def reset_module(self):
        """
        Resets the module
        :return:
        """
        super().reset_module()

    def _execute(self, state: GlobalState) -> None:
        """
        :param state:
        :return:
        """
        
        //Usecase
        // Transfer NFT ownership from seller to buyer
        // Check if seller wallet address is valid
        // Check if buyer wallet address is valid
        // Check buyer wallet balance
        // Check if balance greater than purhase price
        // Check for unique transaction ID
        // Transfer funds from buyer to seller
        // Check if seller wallet is credited with funds matching purchase price and matching transaction ID
        // If transaction is successful change ownership of NFT from seller wallet address to buyer wallet address
        
        issues = []

        for k in state.nodes:
            node = state.nodes[k]

            # Check if the node calls a transfer function (e.g., `transferFrom`)
            if "transferFrom" in node.function_name:
                # Check for an Ether transfer before the NFT transfer
                eth_sent = node.state.get_constraints(
                    ["call.value", ">", 0]
                )

                if eth_sent:
                    transaction_sequence = solver.get_transaction_sequence(
                        node, node.constraints
                    )

                    try:
                        model = solver.get_model(node.constraints)
                    except UnsatError:
                        continue

                    # Create a report if a vulnerability is detected
                    issue = Issue(
                        contract=node.function.contract_name,
                        function_name=node.function_name,
                        address=node.address,
                        swc_id=TRANSFER_AFTER_FUND_TRANSFER,
                        title="NFT Ownership Transfer After Funds Transfer",
                        severity="Medium",
                        description="An NFT ownership transfer occurs after a funds transfer.",
                        debug="Transaction Sequence: {}".format(transaction_sequence),
                    )

                    issues.append(issue)

        return issues