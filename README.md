# Encrypted-Medical-Predictions
In the current times, there are plenty of data available that is private, having this large pool of data and not being able to use data science techniques on this is a problem. 
To use this private data without violating the privacy of any user we can use homomorphic encryption. 
It is a way of encryption with which we can operate on the data without actually knowing the data or the result of it. 
Only the users will know the result of the processing of their data. 
This will allow users to use powerful data processing tools without being afraid of the threat of data being exposed to a third party. 
To demonstrate this method I'm using medical data to show the results and implementations of homomorphic encryption.

The whole project can be broadly divided into 3 section:
  1. Designing of the machine learning model (Decision Tree in this case) to be used in 2 parts: i) on the server ii)Decryption part on the client-side.
  2. Encrypting the user data and sending it to the server for processing along with the public key that is used for the encryption.
  3. Decrypting the conditions with the private key on the client-side and matching it with the results given by the server.
  
 How it works:
 
 Firstly, data of the user is taken in (13 attributes in total), then it gets encrypted and is sent to the AWS S3 bucket.
 From there the server takes the data and processes it, by encryting the 'critical-values' of all the attributes with the publick key and 
 substracting that encrypted critical values from the encrypted data recieved. Since, Paillier's homomorphic encryption method allows the addition between encrypted values,
 it can be used to keep the data encrypted on the server while it is processed.
 
 After processing this data is sent back to the client-side, along with all the possible conditions and results. So, to check if data is higher than critical value, 
 we simply have to take that processed encrypted data, decrypt it and see if it is greater than than 0 or not.
 
 So, using this method, condition are matched with the corrosponding results given by server.
 
 Conclusion and Future Scope:
 
 Using this method, data gets processed on a third party server and only the user who sent the data can know the result of the processed data.
 
 THis project can further be extended using different fully homomorphic schemes and can the accomodate uses of neural network.
