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

def createFile():
    query = FileContentsQuery()

    OPERATOR_ID = AccountId.fromString('Get yours on Hedera Portal')
    OPERATOR_KEY = PrivateKey.fromString('Get yours on Hedera Portal')
    client = Client.forTestnet()
    client.setOperator(OPERATOR_ID, OPERATOR_KEY)
    
    f_content = 'This is my test for new file'
    tnx = FileCreateTransaction()
    resp = tnx.setKeys(OPERATOR_KEY.getPublicKey()).setContents(f_content).setMaxTransactionFee(Hbar(2)).execute(client)
    receipt = resp.getReceipt(client)

    #Create new file
    tx_id = receipt.transactionId.toString()
    
    #Get file ID
    fileId = receipt.fileId
    query = FileContentsQuery()

    #Retreive file content through its ID
    fileContent = query.setFileId(fileId).execute(client).toStringUtf8()
