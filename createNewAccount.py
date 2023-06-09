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

def generate_account():
 
    OPERATOR_ID = AccountId.fromString('Get yours on Hedera Portal')
    OPERATOR_KEY = PrivateKey.fromString('Get yours on Hedera Portal')
    client = Client.forTestnet()
    client.setOperator(OPERATOR_ID, OPERATOR_KEY)
    
    newKey = PrivateKey.generate()
    newPublicKey = newKey.getPublicKey()

    resp = (AccountCreateTransaction()
            .setKey(newPublicKey)
            .setInitialBalance(Hbar.fromTinybars(1000))
            .execute(client))

    receipt = resp.getReceipt(client)

    #
    tx_id = receipt.transactionId.toString()
    account_id = receipt.accountId.toString()
