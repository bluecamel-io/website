# ds_website

So to get the email to send we have to have the API key.  I'll share the google doc that has the api_key, username and password for SendGrid, that way you guys can fool around with stuff as well.

Once you have the api_key, run the following code in your environment

```python
echo "export SENDGRID_API_KEY='YOUR_API_KEY'" > sendgrid.env
echo "sendgrid.env" >> .gitignore
source ./sendgrid.env
```

then you can either 

` pip install sendgrid `

or you can 

`  conda install -c conda-forge sendgrid `

now you should be able to run on a local server and send emails.
