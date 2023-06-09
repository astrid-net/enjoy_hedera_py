from hedera import PrivateKey
from hedera import FileId, FileContentsQuery
import os
from hedera import (
    Client,
    Hbar,
    PrivateKey,
    AccountCreateTransaction,
    AccountId,
    AccountBalanceQuery,
    FileCreateTransaction,
    FileContentsQuery,
    Client
    )

def fetchAccountBalance(accountId):
    OPERATOR_ID = AccountId.fromString('Get yours on Hedera Portal')
    OPERATOR_KEY = PrivateKey.fromString('Get yours on Hedera Portal')
    client = Client.forTestnet()
    client.setOperator(OPERATOR_ID, OPERATOR_KEY)

    #
    acc_id = AccountId.fromString(accountId)
    balance = AccountBalanceQuery().setAccountId(acc_id).execute(client).hbars.toString()
