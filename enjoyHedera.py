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

def generate_wallet():
 
    OPERATOR_ID = AccountId.fromString('0.0.13752044')
    OPERATOR_KEY = PrivateKey.fromString('302e020100300506032b657004220420aa2f73270c906f5a4ffafd8c42261b7b7fcfdb83d15bdcbacbad3bd140039302')
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

def fetchAccountBalance():
    
    OPERATOR_ID = AccountId.fromString('0.0.13752044')
    OPERATOR_KEY = PrivateKey.fromString('302e020100300506032b657004220420aa2f73270c906f5a4ffafd8c42261b7b7fcfdb83d15bdcbacbad3bd140039302')
    client = Client.forTestnet()
    client.setOperator(OPERATOR_ID, OPERATOR_KEY)

    #
    acc_id = AccountId.fromString(wallet_id)
    balance = AccountBalanceQuery().setAccountId(acc_id).execute(client).hbars.toString()
    

def createFile():
    fileId = 20
    query = FileContentsQuery()

    OPERATOR_ID = AccountId.fromString('0.0.13752044')
    OPERATOR_KEY = PrivateKey.fromString('302e020100300506032b657004220420aa2f73270c906f5a4ffafd8c42261b7b7fcfdb83d15bdcbacbad3bd140039302')
    client = Client.forTestnet()
    client.setOperator(OPERATOR_ID, OPERATOR_KEY)
    
    f_content = 'This is my test for new file'
    tnx = FileCreateTransaction()
    resp = tnx.setKeys(OPERATOR_KEY.getPublicKey()).setContents(f_content).setMaxTransactionFee(Hbar(2)).execute(client)
    receipt = resp.getReceipt(client)

    #
    tx_id = receipt.transactionId.toString()
    
    fileId = receipt.fileId
    query = FileContentsQuery()

    #
    fileContent = query.setFileId(fileId).execute(client).toStringUtf8()
    
createFile()
