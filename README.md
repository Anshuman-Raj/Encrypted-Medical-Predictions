# Encrypted-Medical-Predictions
In the current times, there are plenty of data available that is private, having this large pool of data and not being able to use data science techniques on this is a problem. 
To use this private data without violating the privacy of any user we can use homomorphic encryption. 
It is a way of encryption with which we can operate on the data without actually knowing the data or the result of it. 
Only the users will know the result of the processing of their data. 
This will allow users to use powerful data processing tools without being afraid of the threat of data being exposed to a third party. 
To demonstrate this method I'm using medical data to show the results and implementations of homomorphic encryption.

The whole project can be broadly divided into 3 sections:
  1. Designing of the machine learning model (Decision Tree in this case) to be used in 2 parts: i) on the server ii)Decryption part on the client-side.
  2. Encrypting the user data and sending it to the server for processing along with the public key that is used for the encryption.
  3. Decrypting the conditions with the private key on the client-side and matching it with the results given by the server.
  
 How it works:
 
 Firstly, data of the user is taken in (13 attributes in total), then it gets encrypted and is sent to the AWS S3 bucket.
 From there the server takes the data and processes it, by encrypting the 'critical values' of all the attributes with the public key and substracting that encrypted critical values from the encrypted data received. Since Paillier's homomorphic encryption method allows the addition between encrypted values,
 it can be used to keep the data encrypted on the server while it is processed.
 
 After processing this data is sent back to the client side, along with all the possible conditions and results. So, to check if data is higher than the critical value, 
 we simply have to take that processed encrypted data, decrypt it and see if it is greater than 0 or not.
 
 So, using this method, conditions are matched with the corresponding results given by the server.
 
 Project-specific details:
 Interface: It takes the data then calls, 'clientside_enc_dec.py' to encrypt it and send it to the S3 bucket. 
            _(This project has deployed its server on AWS Lambda but, you can run the server separately on any device)_
            Then 'serverwork.py' is called to do the server-side processing and put the encrypted results in an S3 bucket
            After this process ends, 'clientwork.py' decrypts the result and sends it to a file from where the interface picks it up and displays it on screen.
            Right after displaying the results, all the additional files are deleted.

extract_data.py: This is an auxiliary file that helps other files to upload and download data from the s3 bucket.

des_t.py: It is the decision tree that is used to create a tree and split it into two sections and print out the code for those 2 sections.
 
 Conclusion and Future Scope:
 
 Using this method, data gets processed on a third-party server and only the user who sent the data can know the result of the processed data.
 
 This project can further be extended using different fully homomorphic schemes and can the accommodate uses of neural networks.
